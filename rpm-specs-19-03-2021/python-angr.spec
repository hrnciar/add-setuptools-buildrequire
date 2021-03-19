%global srcname angr

# Have arch-specific dependencies, so cannot build as noarch.
# No ppc64le python-pyvex.
ExcludeArch: ppc64le s390x
%global debug_package %{nil}

Name:           python-%{srcname}
Version:        9.0.6136
Release:        1%{?dist}
Summary:        Multi-architecture binary analysis toolkit

License:        BSD and ASL 2.0
URL:            https://angr.io/
Source0:        %{pypi_source}
Source1:        PACKAGE-LICENSING
Source2:        LICENSE-ASL-2.0
Patch0:         angr-9.0.4663-unicorn-1.0.2.patch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  gcc-c++
BuildRequires:  libffi-devel
BuildRequires:  unicorn-devel
BuildRequires:  python3-pyvex
BuildRequires:  python3-unicorn

%description
angr is a platform-agnostic binary analysis framework with the ability
to perform dynamic symbolic execution and various static analyses on
binaries.

%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
angr is a platform-agnostic binary analysis framework with the ability
to perform dynamic symbolic execution and various static analyses on
binaries.

%prep
%autosetup -n %{srcname}-%{version} -p1

%build
%py3_build

%install
%py3_install
cp %{SOURCE1} .
cp %{SOURCE2} .

%files -n python3-%{srcname}
%doc README.md
%license PACKAGE-LICENSING
%license LICENSE
%license LICENSE-ASL-2.0
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info/
%{python3_sitelib}/angr/

%changelog
* Tue Mar 02 2021 Fabian Affolter <mail@fabian-affolter.ch> - 9.0.6136-1
- Update to latest upstream release 9.0.6136 (#1901693)

* Tue Feb 16 2021 Fabian Affolter <mail@fabian-affolter.ch> - 9.0.5903-1
- Update to latest upstream release 9.0.5903 (#1901693)

* Fri Feb 12 2021 Fabian Affolter <mail@fabian-affolter.ch> - 9.0.5811-1
- Update to latest upstream release 9.0.5811 (#1901693)

* Tue Feb 09 2021 Fabian Affolter <mail@fabian-affolter.ch> - 9.0.5739-1
- Update to latest upstream release 9.0.5739 (#1901693)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 9.0.5450-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 20 2021 Fabian Affolter <mail@fabian-affolter.ch> - 9.0.5450-1
- Update to latest upstream release 9.0.5450 (#1901693)

* Fri Jan 08 2021 Fabian Affolter <mail@fabian-affolter.ch> - 9.0.5327-1
- Update to latest upstream release 9.0.5327 (#1901693)

* Sun Dec 27 2020 Fabian Affolter <mail@fabian-affolter.ch> - 9.0.5171-1
- Update to latest upstream release 9.0.5171 (#1901693)

* Fri Dec 18 2020 Fabian Affolter <mail@fabian-affolter.ch> - 9.0.5034-1
- Update to new upstream release 9.0.5034 (#1901693)

* Wed Dec 16 2020 Fabian Affolter <mail@fabian-affolter.ch> - 9.0.5002-1
- Update to new upstream release 9.0.5002 (#1901693)

* Wed Nov 25 2020 Fabian Affolter <mail@fabian-affolter.ch> - 9.0.4885-1
- Update to new upstream release 9.0.4885 (#1901693)

* Tue Nov 10 2020 W. Michael Petullo <mike@flyn.org> - 9.0.4663-2
- Patch to build against unicorn 1.0.2

* Mon Nov 09 2020 W. Michael Petullo <mike@flyn.org> - 9.0.4663-1
- New upstream version

* Thu Oct 08 2020 W. Michael Petullo <mike@flyn.org> - 9.0.4495-1
- New upstream version

* Sat Aug 01 2020 W. Michael Petullo <mike@flyn.org> - 8.20.7.27-1
- New upstream version

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8.20.6.8-6
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8.20.6.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 W. Michael Petullo <mike@flyn.org> - 8.20.6.8-4
- Exclude ppc64le, because python-pyvex not available on ppc64le

* Tue Jun 23 2020 W. Michael Petullo <mike@flyn.org> - 8.20.6.8-3
- Add note about dual license 

* Mon Jun 22 2020 W. Michael Petullo <mike@flyn.org> - 8.20.6.8-2
- Add some BuildRequires

* Sat Jun 20 2020 W. Michael Petullo <mike@flyn.org> - 8.20.6.8-1
- New upstream version
- BuildRequires gcc-c++
- Use pypi_source macro

* Mon May 25 2020 W. Michael Petullo <mike@flyn.org> - 8.20.1.7-1
- Initial package
