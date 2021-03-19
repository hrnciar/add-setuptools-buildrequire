%{?python_enable_dependency_generator}

%global srcname fido2

Name:           python-%{srcname}
Version:        0.9.1
Release:        2%{?dist}
Summary:        Functionality for FIDO 2.0, including USB device communication

# Main code is BSD
# pyu2f is APLv2
# public_suffix_list.dat is MPLv2
License:        BSD and ASL 2.0 and MPLv2.0
URL:            https://github.com/Yubico/python-fido2
Source0:        https://github.com/Yubico/python-%{srcname}/archive/%{version}/python-%{name}-%{version}.tar.gz
# Deal with old setuptools on EPEL7
Patch0:         python-fido2-setup.patch
BuildArch:      noarch

%global _description\
Provides library functionality for communicating with a FIDO device over USB\
as well as verifying attestation and assertion signatures.\
\
WARNING: This project is in beta. Expect things to change or break at any time!\
\
This library aims to support the FIDO U2F and FIDO 2.0 protocols for\
communicating with a USB authenticator via the Client-to-Authenticator\
Protocol (CTAP 1 and 2). In addition to this low-level device access, classes\
defined in the fido2.client and fido2.server modules implement higher level\
operations which are useful when interfacing with an Authenticator, or when\
implementing a Relying Party.\
\
For usage, see the examples/ directory.

%description %_description


%package -n python%{python3_pkgversion}-%{srcname}
Summary: %summary
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-cryptography
BuildRequires:  python%{python3_pkgversion}-six
# For tests
BuildRequires:  python%{python3_pkgversion}-mock
BuildRequires:  python%{python3_pkgversion}-pyfakefs >= 3.4
%if %{undefined __pythondist_requires}
Requires:       python%{python3_pkgversion}-cryptography
Recommends:     python%{python3_pkgversion}-pyscard
Requires:       python%{python3_pkgversion}-six
%endif
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%description -n python%{python3_pkgversion}-%{srcname} %_description


%prep
%autosetup -p1

%build
%py3_build

%install
%py3_install

%check
# EL8 has old python-cryptography that makes a few tests fail
# https://github.com/Yubico/python-fido2/issues/111
%{__python3} -m unittest discover -v %{?el8:|| :}


%files -n python%{python3_pkgversion}-%{srcname}
%license COPYING*
%doc NEWS README.adoc examples
%{python3_sitelib}/%{srcname}-*.egg-info/
%{python3_sitelib}/%{srcname}/


%changelog
* Wed Feb 10 2021 Orion Poplawski <orion@nwra.com> - 0.9.1-2
- Drop python2 / python3_other support
- Skip failing tests on EL8

* Thu Feb 04 2021 Orion Poplawski <orion@nwra.com> - 0.9.1-1
- Update to 0.9.1

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 25 2021 Orion Poplawski <orion@nwra.com> - 0.9.0-1
- Update to 0.9.0

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 24 2020 Orion Poplawski <orion@nwra.com> - 0.8.1-4
- Add BR on python-setuptools

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.8.1-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 25 2019 Orion Poplawski <orion@nwra.com> - 0.8.1-1
- Update to 0.8.1

* Thu Oct 24 2019 Orion Poplawski <orion@nwra.com> - 0.7.2-1
- Update to 0.7.2

* Thu Sep 26 2019 Orion Poplawski <orion@nwra.com> - 0.7.1-1
- Update to 0.7.1

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.7.0-2
- Rebuilt for Python 3.8

* Sun Aug 11 2019 Orion Poplawski <orion@nwra.com> - 0.7.0-1
- Update to 0.7.0

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat May 11 2019 Orion Poplawski <orion@nwra.com> - 0.6.0-1
- Update to 0.6.0

* Thu Mar 14 2019 Orion Poplawski <orion@nwra.com> - 0.5.0-4
- Fix for python3 on EPEL

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 01 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.5.0-2
- Enable python dependency generator

* Mon Dec 31 2018 Orion Poplawski <orion@nwra.com> - 0.5.0-1
- Update to 0.5.0

* Mon Dec 3 2018 Orion Poplawski <orion@nwra.com> - 0.4.0-2
- Fix License
- Remove tab and fix permissions

* Fri Nov 30 2018 Orion Poplawski <orion@nwra.com> - 0.4.0-1
- Initial Fedora package
