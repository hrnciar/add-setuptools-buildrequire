%global npm_name svgo

%bcond_without tests

Name:           nodejs-%{npm_name}
Version:        2.3.0
Release:        2%{?dist}
Summary:        Nodejs-based tool for optimizing SVG vector graphics files

# The package itself is MIT; other licenses come from bundled dependencies. See
# %%{npm_name}-%%{version}-bundled-licenses.txt, audited-null-licenses.toml,
# and the package.json files of the bundled dependencies for details.
License:        MIT and BSD and ISC and CC0
%global forgeurl https://github.com/svg/%{npm_name}
%forgemeta
URL:            %{forgeurl}
Source0:        https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
# The test, documentation, and example files are not included in the NPM
# tarball. Instead of using a dl-tests.sh script source, we add the
# corresponding GitHub tarball as a second source. This results in some
# duplication in the source RPM, but it is a lot simpler!
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
# https://bugzilla.redhat.com/show_bug.cgi?id=1920223
Source5:        check-null-licenses
Source6:        audited-null-licenses.toml

ExclusiveArch:  %{nodejs_arches} noarch
BuildArch:      noarch

BuildRequires:  nodejs-devel
BuildRequires:  symlinks
BuildRequires:  help2man

# For check-null-licenses
BuildRequires:  python3
BuildRequires:  python3dist(toml)

Requires:       nodejs

# This package predates the new naming guidelines for NodeJS pacakges as of
# Fedora 34. Since it primarily provides the svgo CLI tool, it should be called
# svgo rather than nodejs-svgo. We might go through the packaging renaming
# process at some point; for now, we add a virtual Provides. See
#   https://docs.fedoraproject.org/en-US/packaging-guidelines/Node.js/
#     #_naming_guidelines
Provides:       %{npm_name} = %{version}-%{release}

%description
SVG Optimizer is a Nodejs-based tool for optimizing SVG vector graphics files.

Why?

SVG files, especially those exported from various editors, usually contain a
lot of redundant and useless information. This can include editor metadata,
comments, hidden elements, default or non-optimal values and other stuff that
can be safely removed or converted without affecting the SVG rendering result.


%prep
%setup -q -n package

# Copy in the tests, documentation, and examples from the GitHub tarball.
%setup -q -T -D -b 1 -n package
for dir in docs examples test
do
  cp -rp "../%{npm_name}-%{version}/${dir}" ./
done

cp %{SOURCE4} .
# Set up bundled runtime (prod) node modules.
tar -xzf %{SOURCE2}
mkdir -p node_modules
pushd node_modules
ln -s ../node_modules_prod/* .
! [ -e ../node_modules_prod/.bin ]
popd

# Remove pre-built browser JavaScript bundle
rm -rf dist

# Ensure script entry point is executable
chmod -v 0755 bin/%{npm_name}

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
help2man --no-info --output %{npm_name}.1 ./bin/%{npm_name}


%install
install -d %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -rp \
    package.json \
    bin \
    lib \
    plugins \
    node_modules node_modules_prod \
    %{buildroot}%{nodejs_sitelib}/%{npm_name}

install -d %{buildroot}%{_bindir}
# Create an absolute symlink in the buildroot, then convert it to a relative
# one that will still resolve after installation. Otherwise, to create a
# relative symlink, we would have to know how deeply nested %%nodejs_sitelib
# is, which breaks the abstraction of using a macro.
ln -sf %{buildroot}%{nodejs_sitelib}/%{npm_name}/bin/%{npm_name} \
    %{buildroot}%{_bindir}/%{npm_name}
symlinks -c -o %{buildroot}%{_bindir}/%{npm_name}

install -d %{buildroot}%{_mandir}/man1
install -t %{buildroot}%{_mandir}/man1 -p -m 0644 %{npm_name}.1


%check
%{python3} %{SOURCE5} --exceptions %{SOURCE6} --with prod node_modules_prod
%{python3} %{SOURCE5} --exceptions %{SOURCE6} --with dev node_modules_dev
%if %{with tests}
%nodejs_symlink_deps --check
%{__nodejs} -e 'require("./")'
# Set up bundled dev node_modules for testing. We must do this here, not in
# prep, so that they are not pulled into the installed RPM.
tar -xzf %{SOURCE3}
pushd node_modules
ln -s ../node_modules_dev/* .
ln -s ../node_modules_dev/.bin .
popd
NODE_ENV=test ./node_modules/.bin/c8 --reporter=html --reporter=text \
    ./node_modules/.bin/mocha test/*/_index.js
%else
%{_bindir}/echo -e "\e[101m -=#=- Tests disabled -=#=- \e[0m"
%endif


%files
%doc *.md docs/ examples/
%license LICENSE %{npm_name}-%{version}-bundled-licenses.txt
%{nodejs_sitelib}/%{npm_name}
%{_bindir}/%{npm_name}
%{_mandir}/man1/%{npm_name}.1*


%changelog
* Mon Mar 29 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 2.3.0-2
- Fix regression: missed correcting /usr/bin/env shebang in main script

* Mon Mar 29 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 2.3.0-1
- Update to 2.3.0

* Wed Mar 10 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 2.2.2-1
- Update to 2.2.2

* Sat Mar 06 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 2.2.1-1
- Update to 2.2.1

* Tue Mar 02 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 2.2.0-1
- Update to 2.2.0

* Wed Feb 24 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 2.1.0-1
- Update to 2.1.0

* Sun Feb 21 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 2.0.3-1
- Update to 2.0.3

* Sat Feb 20 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 2.0.2-1
- Update to 2.0.2

* Thu Feb 18 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 2.0.1-1
- Update to 2.0.1

* Thu Feb 18 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 2.0.0-1
- Update to 2.0.0

* Mon Jan 25 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 1.3.2-3
- Add a check for null license fields in dependencies

* Wed Jan 20 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 1.3.2-2
- Switch enable_tests global to a build conditional
- Add a more detailed description from upstream
- Assorted spec file tidying, and style adjustments to suit personal preference
- Convert absolute symlink to relative for executable
- Use the GitHub tarball as a second source, rather than creating
  tests/docs/examples tarballs from the git tag with a dl-tests.sh script
- Drop patch removing underscores in entity names; this test passes now
- Fix bundled prod dependencies not actually installed
- Do not install docs/ and examples/ under node_modules, only under _docdir
- Add virtual Provides for svgo
- Hold css-select dependency to '~2.0.0' to work around
  https://github.com/svg/svgo/issues/1315
- Fix or explicitly suppress (via an rpmlintrc file) all rpmlint output
- Add a man page, generated with help2man

* Thu Jan 14 2021 Troy Dawson <tdawson@redhat.com> - 1.3.2-1
- Update to 1.3.2
- Bundle runtime (prod) and testing (dev) dependencies

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-9
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Mar 10 2018 Tom Hughes <tom@compton.nu> - 0.7.2-3
- Relax npm(colors) dependency

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Sep 20 2017 Jared Smith <jsmith@fedoraproject.org> - 0.7.2-1
- Update to upstream 0.7.2 release

* Mon Jul 25 2016 Jared Smith <jsmith@fedoraproject.org> - 0.6.6-4
- Add .yml file

* Mon Jul 25 2016 Jared Smith <jsmith@fedoraproject.org> - 0.6.6-3
- Fix some dependency versions

* Sun Jul 24 2016 Jared Smith <jsmith@fedoraproject.org> - 0.6.6-2
- Fix tests so that the run correctly

* Sat Jul 23 2016 Jared Smith <jsmith@fedoraproject.org> - 0.6.6-1
- Update to upstream 0.6.6 release

* Sun Oct 25 2015 Jared Smith <jsmith@fedoraproject.org> - 0.5.6-1
- Initial packaging
