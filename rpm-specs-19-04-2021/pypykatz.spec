%global pypi_name pypykatz

Name:           %{pypi_name}
Version:        0.3.15
Release:        2%{?dist}
Summary:        Python implementation of Mimikatz

License:        MIT
URL:            https://github.com/skelsec/pypykatz
Source0:        %pypi_source
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
Mimikatz implementation in pure Python. It's optimized for offline parsing, 
but has options for live credential dumping as well.

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove shebangs
find ./ -type f -name "*.py" -exec sed -i '/^#!\//, 1d' {} \;
# Fix line endings
sed -i "s|\r||g" README.md

%build
%py3_build

%install
%py3_install

%files
%doc README.md
%license LICENSE
%{_bindir}/*
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}*.egg-info

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Nov 25 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.15-1
- Update to latest upstream release 0.3.15 (#1895744)

* Mon Nov 09 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.14-1
- Update to latest upstream release 0.3.14 (#1895744)

* Wed Sep 23 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.13-1
- Update to latest upstream release 0.3.13 (#1883308)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.12-1
- Update to latest upstream release 0.3.12 (#1851710)

* Mon Jun 29 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.10-1
- Update to latest upstream release 0.3.10 (#1851710)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.3.9-2
- Rebuilt for Python 3.9

* Sun Apr 19 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.9-1
- Update to latest upstream release 0.3.9 (#1800998)

* Tue Apr 14 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.8-1
- LICENSE file is now part of the source tarball
- Update to latest upstream release 0.3.8 (#1800998)

* Fri Mar 27 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.7-1
- Update to latest upstream release 0.3.7 (#1800998)

* Tue Mar 03 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.5-1
- Update to latest upstream release 0.3.5 (#1800998)

* Fri Feb 28 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.4-1
- Update to latest upstream release 0.3.4

* Thu Jan 30 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.3-1
- Update to latest upstream release 0.3.3 (#1790234)

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.0.7-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.0.7-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun 15 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.0.7-1
- Initial package for Fedora
