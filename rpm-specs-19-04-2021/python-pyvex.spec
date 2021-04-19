%global srcname pyvex

# Has arch-specific dependencies, so cannot build as noarch.
ExcludeArch: ppc64le s390x
%global debug_package %{nil}

Name:           python-%{srcname}
Version:        9.0.6136
Release:        1%{?dist}
Summary:        Python interface to libVEX and the VEX intermediate representation

# Core is BSD, but code in pyvex_c is GPL because it links statically
# against VEX. The files e4c_lite.h, host_generic_maddf.c, and
# host_generic_maddf.h are LGPL.
License:        BSD and GPLv3+ and LGPLv3
URL:            https://github.com/angr/pyvex
Source0:        %{pypi_source}
Source1:        PACKAGE-LICENSING
Source2:        LICENSE-other

BuildRequires:  gcc

%description
A Python interface to libVEX and the VEX intermediate representation.

%package -n python3-%{srcname}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-cffi
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
A Python interface to libVEX and the VEX intermediate representation.

%prep
rm -f %{srcname}.egg-info/
%autosetup -n %{srcname}-%{version} -p1

%build
%py3_build

%install
%py3_install
mv pyvex_c/LICENSE LICENSE-pyvex_c
cp %{SOURCE1} .
cp %{SOURCE2} .

%files -n python3-%{srcname}
%doc README.md
%license PACKAGE-LICENSING
%license LICENSE
%license LICENSE-pyvex_c
%license LICENSE-other
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info/
%{python3_sitelib}/pyvex/

%changelog
* Tue Mar 02 2021 Fabian Affolter <mail@fabian-affolter.ch> - 9.0.6136-1
- Update to latest upstream release 9.0.6136 (#1929355)

* Tue Feb 16 2021 Fabian Affolter <mail@fabian-affolter.ch> - 9.0.5903-1
- Update to latest upstream release 9.0.5903 (#1905673)

* Fri Feb 12 2021 Fabian Affolter <mail@fabian-affolter.ch> - 9.0.5811-1
- Update to latest upstream release 9.0.5811 (#1905673)

* Tue Feb 09 2021 Fabian Affolter <mail@fabian-affolter.ch> - 9.0.5739-1
- Update to latest upstream release 9.0.5739 (#1905673)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 9.0.5450-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 20 2021 Fabian Affolter <mail@fabian-affolter.ch> - 9.0.5450-1
- Update to latest upstream release 9.0.5450 (#1905673)

* Fri Jan 08 2021 Fabian Affolter <mail@fabian-affolter.ch> - 9.0.5327-1
- Update to latest upstream release 9.0.5327 (#1905673)

* Sun Dec 27 2020 Fabian Affolter <mail@fabian-affolter.ch> - 9.0.5171-1
- Update to latest upstream release 9.0.5171 (#1905673)

* Fri Dec 18 2020 Fabian Affolter <mail@fabian-affolter.ch> - 9.0.5034-1
- Update to new upstream release 9.0.5034 (#1905673)

* Wed Dec 16 2020 Fabian Affolter <mail@fabian-affolter.ch> - 9.0.5002-1
- Update to new upstream release 9.0.5002 (#1905673)

* Wed Nov 25 2020 Fabian Affolter <mail@fabian-affolter.ch> - 9.0.4885-1
- Update to new upstream release 9.0.4885 (#1901722)

* Fri Nov 06 2020 W. Michael Petullo <mike@flyn.org> - 9.0.4663-1
- New upstream version

* Thu Oct 08 2020 W. Michael Petullo <mike@flyn.org> - 9.0.4495-1
- New upstream version

* Sat Aug 01 2020 W. Michael Petullo <mike@flyn.org> - 8.20.7.27-1
- New upstream version

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8.20.7.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 24 2020 W. Michael Petullo <mike@flyn.org> - 8.20.7.6-1
- New upstream version

* Tue Jun 23 2020 W. Michael Petullo <mike@flyn.org> - 8.20.6.8-1
- New upstream version

* Fri Jun 05 2020 W. Michael Petullo <mike@flyn.org> - 8.20.6.1-1
- New upstream version
- Remove unstreamed patch

* Sat May 30 2020 W. Michael Petullo <mike@flyn.org> - 8.20.5.27-2
- Does not build on ppc64le; mark as such

* Fri May 29 2020 W. Michael Petullo <mike@flyn.org> - 8.20.5.27-1
- New upstream version
- Indicate multiple licenses
- Use macro for Source0
- Force build of egg
- Remove unstreamed patch
- Add GCC 10 patch

* Thu May 28 2020 W. Michael Petullo <mike@flyn.org> - 8.20.1.7-2
- Add python3-cffi and gcc to BuildRequires
- Patch to avoid evil spaces issue

* Mon May 25 2020 W. Michael Petullo <mike@flyn.org> - 8.20.1.7-1
- Initial package
