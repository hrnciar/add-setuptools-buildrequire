Name:           jrnl
Version:        2.8
Release:        2%{?dist}
Summary:        A simple journal application for the command line

License:        GPLv3
URL:            https://%{name}.sh
%global forgeurl https://github.com/%{name}-org/%{name}/
Source0:        %{forgeurl}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

BuildRequires:  python3dist(pytest)

BuildRequires:  help2man

%description
%{name} is a simple journal application for the command line.

You can use it to easily create, search, and view journal entries. Journals are
stored as human-readable plain text, and can also be encrypted using AES
encryption.


%package doc
Summary:        Documentation for %{name}

BuildRequires:  mkdocs

%description doc
The %{name}-doc package contains detailed documentation for %{name}.


%prep
%autosetup -n %{name}-%{version}

# Loosen too-strict and fairly arbitrary upstream dependency version
# requirements as needed.
sed -r -i \
    -e 's/^(pyxdg = ">=0.)27(.0".*)$/\126\2/' \
    -e 's/^(tzlocal = ")>(2.0, <3.0".*)$/\1>=\2/' \
    pyproject.toml
%if 0%{?fedora} == 33
sed -r -i \
    -e 's/("poetry>=1.)1"/\10.10"/' \
    -e 's/^(parsedatetime = ">=2.)6(".*)$/\15\2/' \
    pyproject.toml
%endif

# Find non-executable files with shebang lines, and remove them
find %{name}/ -type f ! -perm /0111 |
  while read -r fn
  do
    if head "${fn}" | grep -E '^#!' >/dev/null
    then
      sed -r -i '1{/#!/d}' "${fn}"
    fi
  done
# Fix any remaining shebangs.
%py3_shebang_fix %{name}


%generate_buildrequires
%pyproject_buildrequires -r


%build
%pyproject_wheel

# https://github.com/jrnl-org/jrnl/issues/74
help2man --no-info '%{python3} -m %{name}' --output='%{name}.1'

mkdocs build


%install
%pyproject_install
%pyproject_save_files %{name}

install -D -t '%{buildroot}%{_mandir}/man1' -p -m 0644 '%{name}.1'


%check
%pytest


%files -f %{pyproject_files}
%license LICENSE.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*


%files doc
%license LICENSE.md
%doc CHANGELOG.md
%doc CODE_OF_CONDUCT.md
%doc CONTRIBUTING.md
%doc README.md
%doc site/


%changelog
* Sat Apr 10 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 2.8-2
- Drop workarounds for Fedora 32

* Wed Apr 07 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 2.8-1
- New upstream release 2.8 (with license change, MIT to GPLv3)
- Switch URL to HTTPS
- Use GitHub tarball instead of PyPI tarball to get documentation and tests
- Build with pyproject-rpm-macros (no setup.py)
- Adjust spec file whitespace to personal preference
- Update summary and description from upstream
- Add CHANGELOG.md, CODE_OF_CONDUCT.md, CONTRIBUTING.md
- Add a new -doc subpackage and build the HTML documentation
- Run the tests
- Generate and install a man page

* Wed Feb 10 2021 Fabian Affolter <mail@fabian-affolter.ch> - 2.7-1
- Update to latest upstream release 2.7 (#1907094)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Nov 28 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.5-1
- Update to latest upstream release 2.5 (#1875713)

* Fri Sep 04 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.4.5-2
- Fix requirement for dependency generator

* Sun Aug 23 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.4.5-1
- Update to latest upstream release 2.4.5 (#1875713)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.4-2
- Rebuilt for Python 3.9

* Fri May 01 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.4-1
- Update to latest upstream release 2.4

* Sat Mar 28 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.3-1
- Remove release pinning (#1803355)
- Update to latest upstream release 2.3

* Thu Feb 06 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.2-1
- Fix build failure (#1791686)
- Update to latest upstream release 2.2

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 06 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.1.1-1
- Update to latest upstream release 2.1.1

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.9.8-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.9.8-3
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat May 25 2019 Fabian Affolter <mail@fabian-affolter.ch> - 1.9.8-1
- Initial package for Fedora
