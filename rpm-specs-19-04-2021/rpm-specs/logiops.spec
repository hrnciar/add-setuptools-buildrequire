Name:    logiops
Version: 0.2.3
Release: 6%{?dist}
Summary: Unofficial driver for Logitech mice and keyboard

License: GPLv3
URL:     https://github.com/PixlOne/logiops

Source0: https://github.com/PixlOne/logiops/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  systemd-devel
BuildRequires:  systemd-udev
BuildRequires:  systemd-rpm-macros
BuildRequires:  libconfig-devel
BuildRequires:  libevdev-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++

%description
This is an unofficial driver for Logitech mice and keyboard.

This is currently only compatible with HID++ >2.0 devices.

%prep
%setup -q -n %{name}-%{version}

%build
%{cmake}
%{cmake_build}

%install
%{cmake_install}

%post
%systemd_post logid.service

%preun
%systemd_preun logid.service

%postun
%systemd_postun_with_restart logid.service

%files
%{_bindir}/logid
%{_unitdir}/logid.service
%license LICENSE
%doc README.md
%doc TESTED.md
%doc logid.example.cfg

%changelog
* Tue Apr 13 2021 Nicolas De Amicis <deamicis@bluewin.ch> - 0.2.3-6
- New version 0.2.3

* Wed Mar 31 2021 Jonathan Wakely <jwakely@redhat.com> - 0.2.2-5
- Rebuilt for removed libstdc++ symbols (#1937698)

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.2.2-4
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Mon Feb 15 2021 Nicolas De Amicis <deamicis@bluewin.ch> - 0.2.2-3
- Fix build error (thread import) see bug 1923298

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 31 2020 Nicolas De Amicis <deamicis@bluewin.ch> - 0.2.2-1
- Initial packaging
