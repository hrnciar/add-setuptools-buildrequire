%global npm_name topojson-client

Name:           %{npm_name}
Version:        3.1.0
Release:        2%{?dist}
Summary:        Manipulate TopoJSON and convert it to GeoJSON

# License of topojson-client is ISC; others come from bundled dependencies. See
# the license file %%{npm_name}-%%{version}-bundled-licenses.txt for a list of
# licenses in NPM format. Each bundled dependency has the license specified in
# the "license" key of its package.json file.
License:        ISC and MIT
%global forgeurl https://github.com/topojson/%{npm_name}
%forgemeta
URL:            %{forgeurl}
Source0:        https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
# The test files are not included in the NPM tarball. Instead of using a
# dl-tests.sh script source, we add the corresponding GitHub tarball as a
# second source. This results in some duplication in the source RPM, but it is
# a lot simpler!
#
# Note https://docs.fedoraproject.org/en-US/packaging-guidelines/Node.js/ says,
# “The canonical method for shipping most node modules is tarballs from the npm
# registry. […] This method should be preferred to using checkouts from git or
# automatically generated tarballs from GitHub.” (Otherwise, we might just use
# the GitHub tarball as the primary source.)
Source1:        %{forgesource}
# Created with (from nodejs-packaging RPM):
# nodejs-packaging-bundler %%{npm_name} %%{version}
Source2:        %{npm_name}-%{version}-nm-prod.tgz
Source3:        %{npm_name}-%{version}-nm-dev.tgz
Source4:        %{npm_name}-%{version}-bundled-licenses.txt
# Hand-written man pages
Source5:        topo2geo.1
Source6:        topomerge.1
Source7:        topoquantize.1
# https://bugzilla.redhat.com/show_bug.cgi?id=1920223
Source8:        check-null-licenses
Source9:        audited-null-licenses.toml

ExclusiveArch:  %{nodejs_arches} noarch
BuildArch:      noarch

BuildRequires:  nodejs-devel
BuildRequires:  /usr/bin/esbuild
BuildRequires:  symlinks

# For check-null-licenses
BuildRequires:  python3
BuildRequires:  python3dist(toml)

Requires:       nodejs

%description
This provides tools for manipulating TopoJSON, such as to merge shapes or
quantize coordinates, and for converting back to GeoJSON for rendering with
standard tools such as d3.geoPath.

topo2geo

  Converts one or more TopoJSON objects from an input topology to one or more
  GeoJSON features.

topomerge

  Merges polygons (or meshes lines) from the specified source TopoJSON geometry
  collection object, assigning to the target object.

topoquantize  

  Quantizes the coordinates of the input TopoJSON topology and delta-encodes
  the topology’s arcs.

See also topojson-server and topojson-simplify.


%prep
%setup -q -n package
# Copy in the tests from the GitHub tarball.
%setup -q -T -D -b 1 -n package
cp -rp ../%{npm_name}-%{version}/test ./

# Remove pre-compiled bundled JavaScript that was built with rollup. Fedora
# guidelines prevent us from using it.
rm -rf dist

cp -p %{SOURCE4} .
# Set up bundled runtime (prod) node modules.
tar -xzf %{SOURCE2}
mkdir -p node_modules
pushd node_modules
ln -s ../node_modules_prod/* .
if [ -e ../node_modules_prod/.bin ]
then
  ln -s ../node_modules_prod/.bin .
fi
popd

# Fix shebang lines in executables. For some reason, brp-mangle-shebangs does
# not seem to do this under %%nodejs_sitelib.
find . -type f -perm /0111 |
  while read -r fn
  do
    if head -n 1 "${fn}" | grep -E '^#!%{_bindir}/env[[:blank:]]+' >/dev/null
    then
      sed -r -i '1s/env +//' "${fn}"
    fi
  done


%build
# Under Fedora guidelines, we had to remove the pre-compiled bundled JavaScript
# sources. We have two options under the guidelines:
#
# 1. Patch everything to use ES6 modules directly. This is conceptually clean
#    but messy in practice.
# 2. Rebuild it ourselves. This is easy, and stays closest to upstream. Since
#    the rollup configuration is pretty trivial, and rollup is not in the prod
#    tarball, we choose to use esbuild instead of rollup. We also do not build
#    a minified bundle; that would be useful only for browsers.
#
# We choose to rebuild the bundle. We add a source map for better debugging,
# and we use CommonJS format instead of UMD since we do not need to support
# browsers. (Note that the tests would fail if we used iife format, for unknown
# reasons.)
mkdir -p dist
esbuild --bundle --platform=node --sourcemap \
    --outfile=dist/%{name}.js src/index.js


%install
install -d %{buildroot}%{nodejs_sitelib}/%{npm_name}
# Note that, per Fedora guidelines, we MUST install the original sources
# whether they are used or not.
cp -rp \
    package.json \
    bin \
    dist \
    src \
    node_modules node_modules_prod \
    %{buildroot}%{nodejs_sitelib}/%{npm_name}

install -d %{buildroot}%{_bindir}
# Create an absolute symlink in the buildroot, then convert it to a relative
# one that will still resolve after installation. Otherwise, to create a
# relative symlink, we would have to know how deeply nested %%nodejs_sitelib
# is, which breaks the abstraction of using a macro.
find %{buildroot}%{nodejs_sitelib}/%{npm_name}/bin/ -type f |
  while read -r target
  do
    link="%{buildroot}%{_bindir}/$(basename "${target}")"
    ln -sf "${target}" "${link}"
  done
symlinks -c -o %{buildroot}%{_bindir}/*

install -d %{buildroot}%{_mandir}/man1
install -t %{buildroot}%{_mandir}/man1 -p -m 0644 \
    %{SOURCE5} %{SOURCE6} %{SOURCE7}


%check
%{python3} %{SOURCE8} --exceptions %{SOURCE9} --with prod node_modules_prod
%{python3} %{SOURCE8} --exceptions %{SOURCE9} --with dev node_modules_dev
%nodejs_symlink_deps --check
%{__nodejs} -e 'require("./")'

# Set up bundled dev node_modules for testing. We must do this here, not in
# prep, so that they are not pulled into the installed RPM.
tar -xzf %{SOURCE3}
pushd node_modules
ln -s ../node_modules_dev/* .
popd
pwd
if [ -e node_modules_dev/.bin ]
then
  if [ ! -e node_modules/.bin ]
  then
    mkdir node_modules/.bin
  fi
  pushd node_modules/.bin
  ln -s ../../node_modules_dev/.bin/* .
  popd
fi
# See scripts.test in package.json. Note that we do not use rollup at all; we
# want to test the same bundle we use in production.
NODE_ENV=test find test -type f -name '*-test.js' \
    -exec ./node_modules/.bin/tape '{}' +


%files
%doc README.md
%license LICENSE %{npm_name}-%{version}-bundled-licenses.txt
%{nodejs_sitelib}/%{npm_name}
%{_bindir}/topo2geo
%{_bindir}/topomerge
%{_bindir}/topoquantize
%{_mandir}/man1/topo2geo.1*
%{_mandir}/man1/topomerge.1*
%{_mandir}/man1/topoquantize.1*


%changelog
* Fri Feb 05 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 3.1.0-2
- Add script to audit for dependencies with null licenses in %%check

* Sat Jan 23 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 3.1.0-1
- Initial package
