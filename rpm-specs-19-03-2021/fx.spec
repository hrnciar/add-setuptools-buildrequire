%global npm_name fx

Name:           %{npm_name}
Version:        20.0.2
Release:        2%{?dist}
Summary:        Command-line JSON processing tool

# License of fx is MIT; any others come from bundled dependencies. See the
# license file %%{npm_name}-%%{version}-bundled-licenses.txt for a list of
# licenses in NPM format. Each bundled dependency has the license specified in
# the "license" key of its package.json file.
#
# Additionally, node_modules_prod/@medv/blessed/usr/fonts/ is licensed under
# the SIL Open Font License 1.1 (OFL) even though the overall license of
# @medv/blessed is MIT; OFL is therefore not listed in the bundled licenses
# file.
License:        MIT and OFL
URL:            https://github.com/antonmedv/%{npm_name}
Source0:        https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
# The DOCS.md file, which is very useful, is not included in the NPM tarball.
#
# Note https://docs.fedoraproject.org/en-US/packaging-guidelines/Node.js/ says,
# “The canonical method for shipping most node modules is tarballs from the npm
# registry. […] This method should be preferred to using checkouts from git or
# automatically generated tarballs from GitHub.” (Otherwise, we might just use
# the GitHub tarball as the primary source.)
Source1:        https://raw.githubusercontent.com/antonmedv/%{npm_name}/%{version}/DOCS.md
# Created with (from nodejs-packaging RPM):
# nodejs-packaging-bundler %%{npm_name} %%{version}
Source2:        %{npm_name}-%{version}-nm-prod.tgz
Source3:        %{npm_name}-%{version}-nm-dev.tgz
Source4:        %{npm_name}-%{version}-bundled-licenses.txt
# Hand-written man page
Source5:        %{npm_name}.1
# https://bugzilla.redhat.com/show_bug.cgi?id=1920223
Source6:        check-null-licenses
Source7:        audited-null-licenses.toml

ExclusiveArch:  %{nodejs_arches} noarch
BuildArch:      noarch

BuildRequires:  nodejs-devel
BuildRequires:  symlinks

# For check-null-licenses
BuildRequires:  python3
BuildRequires:  python3dist(toml)

Requires:       nodejs

%description
Command-line JSON processing tool

Features:

  * Easy to use
  * Standalone binary
  * Interactive mode
  * Streaming support


%prep
%setup -q -n package
# Copy in the documentation file from GitHub; and copy in the bundled license
# list.
cp -p %{SOURCE1} %{SOURCE4} .
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


%install
install -d %{buildroot}%{nodejs_sitelib}/%{npm_name}
# Note that, per Fedora guidelines, we MUST install the original sources
# whether they are used or not.
cp -rp \
    package.json \
    *.js \
    node_modules node_modules_prod \
    %{buildroot}%{nodejs_sitelib}/%{npm_name}

install -d %{buildroot}%{_bindir}
# Create an absolute symlink in the buildroot, then convert it to a relative
# one that will still resolve after installation. Otherwise, to create a
# relative symlink, we would have to know how deeply nested %%nodejs_sitelib
# is, which breaks the abstraction of using a macro.
ln -s '%{buildroot}%{nodejs_sitelib}/%{npm_name}/index.js' \
    '%{buildroot}%{_bindir}/%{npm_name}'
symlinks -c -o %{buildroot}%{_bindir}/%{npm_name}

install -t %{buildroot}%{_mandir}/man1 -p -m 0644 -D %{SOURCE5}


%check
%{python3} %{SOURCE6} --exceptions %{SOURCE7} --with prod node_modules_prod
%{python3} %{SOURCE6} --exceptions %{SOURCE7} --with dev node_modules_dev
%nodejs_symlink_deps --check
# We do not call:
# %%{__nodejs} -e 'require("./")'
# because this package does not provide an importable module. See the lack of a
# "main" or "module" key in package.json.

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
# See scripts.test in package.json.
NODE_ENV=test ./node_modules/.bin/ava test.js


%files
%doc README.md
%doc DOCS.md
%license LICENSE %{npm_name}-%{version}-bundled-licenses.txt
%{nodejs_sitelib}/%{npm_name}
%{_bindir}/%{npm_name}
%{_mandir}/man1/%{npm_name}.1*


%changelog
* Tue Mar 16 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 20.0.2-2
- Do not convert Markdown docs to HTML

* Mon Feb 08 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 20.0.2-1
- Initial package
