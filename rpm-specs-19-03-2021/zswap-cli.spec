%undefine __cmake_in_source_build

Name: zswap-cli
Version: 0.4.1
Release: 5%{?dist}

Summary: Command-line tool to control zswap options
License: MIT
URL: https://github.com/xvitaly/%{name}
Source0: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: kernel-headers
BuildRequires: glibc-headers
BuildRequires: cxxopts-devel
BuildRequires: ninja-build
BuildRequires: fmt-devel
BuildRequires: systemd
BuildRequires: gcc-c++
BuildRequires: pandoc
BuildRequires: cmake

%{?systemd_requires}

%description
ZSwap-cli is a command-line tool to control zswap options.

%prep
%autosetup

%build
%cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release
%cmake_build

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%install
%cmake_install

%files
%doc README.md docs/*
%license LICENSE
%{_sbindir}/%{name}
%{_unitdir}/%{name}.service
%{_mandir}/man1/%{name}.*
%config(noreplace) %{_sysconfdir}/%{name}.conf

%changelog
* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.4.1-5
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 04 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.4.1-2
- Switch to the new CMake macros.

* Mon Apr 27 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 0.4.1-1
- Updated to version 0.4.1.

* Sun Apr 26 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 0.4.0-1
- Updated to version 0.4.0.

* Wed Apr 22 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 0.3.0-1
- Updated to version 0.3.0.

* Mon Apr 13 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 0.2.0-1
- Updated to version 0.2.0.

* Sat Apr 04 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 0.1.0-1
- Initial SPEC release.
