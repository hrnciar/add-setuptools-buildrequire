%bcond_without tests

Name:		oomd
Summary:	Userspace Out-Of-Memory (OOM) killer
Version:	0.4.0
Release:	6%{dist}
License:	GPLv2
URL:		https://github.com/facebookincubator/oomd/
Source0:	%{url}/archive/v%{version}/%{name}-%{version}.tar.gz
# oomd: fix missing includes for gcc-11
Patch0:         %{url}/commit/e7403438de998a56ccceefa3e25d7af0fdcbffc2.patch
# oomd: one more missing include
Patch1:         %{url}/commit/9f3c61cc34a285133e2a7672a3d12b1ba399b646.patch

ExcludeArch:	i686 armv7hl

BuildRequires:	gcc-c++
BuildRequires:	meson >= 0.45
BuildRequires:	pkgconfig(jsoncpp)
BuildRequires:	pkgconfig(libsystemd)
%if %{with tests}
BuildRequires:	gmock-devel
BuildRequires:	gtest-devel
%endif
BuildRequires:	systemd-rpm-macros
%{?systemd_requires}

%description
Out of memory killing has historically happened inside kernel space. On a
memory overcommitted linux system, malloc(2) and friends usually never fail.
However, if an application dereferences the returned pointer and the system has
run out of physical memory, the linux kernel is forced take extreme measures,
up to and including killing processes. This is sometimes a slow and painful
process because the kernel can spend an unbounded amount of time swapping in
and out pages and evicting the page cache. Furthermore, configuring policy is
not very flexible while being somewhat complicated.

oomd aims to solve this problem in userspace. oomd leverages PSI and cgroupv2
to monitor a system holistically. oomd then takes corrective action in
userspace before an OOM occurs in kernel space. Corrective action is configured
via a flexible plugin system, in which custom code can be written. By default,
this involves killing offending processes. This enables an unparalleled level
of flexibility where each workload can have custom protection rules.
Furthermore, time spent livedlocked in kernelspace is minimized.

%prep
%autosetup -p1

%build
%meson
%meson_build

%if %{with tests}
%check
%meson_test
%endif

%install
%meson_install

%files
%license LICENSE
%doc README.md CONTRIBUTING.md CODE_OF_CONDUCT.md docs/
%{_bindir}/oomd
%{_unitdir}/oomd.service
%{_mandir}/man1/oomd.*
%config(noreplace) %{_sysconfdir}/oomd/

%post
%systemd_post oomd.service

%preun
%systemd_preun oomd.service

%postun
%systemd_postun_with_restart oomd.service

%changelog
* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.4.0-6
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Wed Feb 17 2021 Davide Cavalca <dcavalca@fedoraproject.org> - 0.4.0-5
- Build for EPEL 8
- Make tests conditional
- Replace gcc-11 patch with upstream commits

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Oct 30 2020 Jeff Law <law@redhat.com> - 0.4.0-3
- Fix missing #includes for gcc-11

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun  4 2020 Filipe Brandenburger <filbranden@gmail.com> - 0.4.0-1
- Upgrade to v0.4.0

* Sat May 30 2020 Björn Esser <besser82@fedoraproject.org> - 0.3.2-2
- Rebuild (jsoncpp)

* Wed Feb 19 2020 Filipe Brandenburger <filbranden@gmail.com> - 0.3.2-1
- Update to v0.3.2

* Tue Feb 18 2020 Filipe Brandenburger <filbranden@gmail.com> - 0.3.1-1
- Update to v0.3.1

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 14 2019 Björn Esser <besser82@fedoraproject.org> - 0.2.0-5
- Rebuild (jsoncpp)

* Thu Sep 12 2019 Filipe Brandenburger <filbranden@gmail.com> - 0.2.0-4
- First official build for Fedora
- Exclude 32-bit architectures, which fail to build.

* Tue Sep 10 2019 Filipe Brandenburger <filbranden@gmail.com> - 0.2.0-3
- Initial release of oomd RPM package
