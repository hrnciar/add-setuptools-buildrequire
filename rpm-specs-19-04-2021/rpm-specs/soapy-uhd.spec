Name:		soapy-uhd
Version:	0.4.1
Release:	1%{?dist}
Summary:	Soapy SDR plugins for UHD supported SDR devices
License:	GPLv3
URL:		https://github.com/pothosware/SoapyUHD
Source:		%{URL}/archive/%{name}-%{version}.tar.gz
BuildRequires:	make
BuildRequires:	gcc-c++
BuildRequires:	cmake
BuildRequires:	uhd-devel
BuildRequires:	SoapySDR-devel
BuildRequires:	boost-devel
# For module directories
Requires:	uhd
Requires:	SoapySDR

%description
Soapy SDR plugins for UHD supported SDR devices.

%prep
%autosetup -n SoapyUHD-%{name}-%{version}

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%license COPYING
%doc README.md Changelog.txt
%{_libdir}/SoapySDR/modules*.*/*.so
%{_libdir}/uhd/modules/*.so

%changelog
* Mon Feb  8 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 0.4.1-1
- New version

* Mon Feb  8 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 0.3.6-5
- Rebuilt for new uhd
  Resolves: rhbz#1925575
- Updated cmake macros

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 24 2020 Jeff Law <law@redhat.com> - 0.3.6-2
- Use __cmake_in_source_build

* Thu Apr 16 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 0.3.6-1
- Initial version
