%global npm_name npm-name-cli

Name:           %{npm_name}
Version:        3.0.0
Release:        4%{?dist}
Summary:        Check whether a package or organization name is available on npm

# License of npm-name-cli is MIT; others come from bundled dependencies. See
# the license file %%{npm_name}-%%{version}-bundled-licenses.txt for a list of
# licenses in NPM format. Each bundled dependency has the license specified in
# the "license" key of its package.json file.
License:        MIT and ASL 2.0 and BSD and (BSD or MIT or ASL 2.0) and CC0 and CC-BY and ISC and (MIT or CC0) and MPLv2.0
URL:            https://github.com/sindresorhus/%{npm_name}
# The tests are not included in the NPM tarball. However, they all require
# Internet access, so we omit them entirely. This also means we require only
# the prod dependency bundle, not the dev one.
Source0:        https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
# Created with (from nodejs-packaging RPM):
# nodejs-packaging-bundler %%{npm_name} %%{version}
Source1:        %{npm_name}-%{version}-nm-prod.tgz
Source2:        %{npm_name}-%{version}-bundled-licenses.txt
# Hand-written man page
Source3:        npm-name.1
# https://bugzilla.redhat.com/show_bug.cgi?id=1920223
Source4:        check-null-licenses
Source5:        audited-null-licenses.toml

ExclusiveArch:  %{nodejs_arches} noarch
BuildArch:      noarch

BuildRequires:  nodejs-devel
BuildRequires:  symlinks

# For check-null-licenses script
BuildRequires:  python3
BuildRequires:  python3dist(toml)

Requires:       nodejs

%description
The npm-name command-line tool checks whether a package or organization name is
available on npm.

Why would I use npm-name rather than npm’s built-in search?

1. Nicer & simpler output
2. Squatter detection (https://github.com/sholladay/squatter)
3. Supports checking the availability of organization names
4. Performance


%prep
%setup -q -n package

cp %{SOURCE2} .
# Set up bundled runtime (prod) node modules.
tar -xzf %{SOURCE1}
mkdir -p node_modules
pushd node_modules
ln -s ../node_modules_prod/* .
ln -s ../node_modules_prod/.bin .
popd

# Fix shebang lines in executables. For some reason, brp-mangle-shebangs does
# not seem to do this under %%nodejs_sitelib.
find . -type f -perm /0111 |
  while read -r fn
  do
    if head -n 1 "${fn}" | grep -E '^#!%{_bindir}/env[[:blank:]]+' >/dev/null
    then
      # Script with banned env shebang; fix it
      sed -r -i '1s/env +//' "${fn}"
    elif ! head -n 1 "${fn}" | grep -E '^#!'
    then
      # Unexpected non-script executable file; fix the permissions
      chmod -v a-x "${fn}"
    fi
  done

# Remove dotfiles (hidden files) from bundled dependencies. As of 3.0.0-3,
# these include: (.editorconfig .eslintignore .eslintrc .eslintrc.json .gitkeep
# .istanbul.yml .jscs.json .npmignore .nvmrc .nycrc .testem.json .travis.yml
# .uglifyjsrc.json) and are all not needed at runtime. If a dependency appears
# with an important hidden file, we may need to exclude it from removal.
#
# Also remove zero-length files from bundled dependencies. As of 3.0.0-3, these
# are only in tests and examples for bundled dependencies, neither of which
# will be used by the installed package, so it is OK if these portions of the
# dependencies are broken by the removal.
find node_modules_prod -type f \( -name '.*' -o -size 0 \) -print -delete

# Remove hidden directories from bundled dependencies, except those known to be
# useful. If a dependency appears with an important hidden directory, we may
# need to exclude it from removal.
find node_modules_prod -depth -type d -name '.*' ! -name '.bin' \
    -printf '--> Remove hidden directory %p\n' -exec rm -rvf '{}' ';'


# Nothing to build


%install
install -d %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -rp \
    package.json \
    cli.js \
    node_modules node_modules_prod \
    %{buildroot}%{nodejs_sitelib}/%{npm_name}

install -d %{buildroot}%{_bindir}
# Create an absolute symlink in the buildroot, then convert it to a relative
# one that will still resolve after installation. Otherwise, to create a
# relative symlink, we would have to know how deeply nested %%nodejs_sitelib
# is, which breaks the abstraction of using a macro.
ln -sf %{buildroot}%{nodejs_sitelib}/%{npm_name}/cli.js \
    %{buildroot}%{_bindir}/npm-name
symlinks -c -o %{buildroot}%{_bindir}/npm-name

install -d %{buildroot}%{_mandir}/man1
install -t %{buildroot}%{_mandir}/man1 -p -m 0644 %{SOURCE3}


%check
# All upstream tests require Internet access, and package.json does not provide
# an importable/requirable library. Therefore we do not need to symlink any dev
# dependencies, or test require("./").

%{python3} %{SOURCE4} --exceptions %{SOURCE5} --with prod node_modules_prod


%files
%doc readme.md
%license license %{npm_name}-%{version}-bundled-licenses.txt
%{nodejs_sitelib}/%{npm_name}
%{_bindir}/npm-name
%{_mandir}/man1/npm-name.1*


%changelog
* Sat Mar 20 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 3.0.0-4
- Regenerate dependency bundle

* Tue Mar 16 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 3.0.0-3
- Remove hidden and zero-length files from prod dependency bundle
- Remove executable bit on non-script files
- Remove hidden directories from prod dependency bundle, except those known to
  be useful

* Wed Jan 27 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 3.0.0-2
- Add build-time check for missing licenses in dependency bundle

* Fri Jan 22 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 3.0.0-1
- Initial package
