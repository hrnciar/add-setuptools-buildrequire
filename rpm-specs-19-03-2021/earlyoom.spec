%global makeflags PREFIX=%{_prefix} SYSCONFDIR=%{_sysconfdir} SYSTEMDUNITDIR=%{_unitdir}

Name: earlyoom
Version: 1.6.2
Release: 4%{?dist}

License: MIT
URL: https://github.com/rfjakob/%{name}
Summary: Early OOM Daemon for Linux
Source0: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

# https://pagure.io/fedora-workstation/issue/119
Patch0: %{name}-fedora-options.patch

%{?systemd_requires}
BuildRequires: systemd
BuildRequires: pandoc
BuildRequires: gcc
BuildRequires: make

%description
User-space OOM killer daemon that can avoid the system going into the
unresponsive state. It checks the amount of available memory and
free swap up to 10 times a second (less often if there is a lot of free
memory) and kills the largest processes with the highest oom_score.

Percentages are configured through the configuration file.

%prep
%autosetup -p1
sed -e '/systemctl/d' -i Makefile

%build
%set_build_flags
%make_build VERSION=%{version} %{makeflags}

%install
%make_install %{makeflags}

%if 0%{?fedora} && 0%{?fedora} >= 34
%triggerun -- %{name} < 1.6.2-3
# earlyoom preset is removed from fedora-release in F34,
# trigger resetting the service state on upgrade
systemctl --no-reload preset %{name}.service &>/dev/null || :
%endif

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_unitdir}/%{name}.service
%{_mandir}/man1/%{name}.*
%config(noreplace) %{_sysconfdir}/default/%{name}

%changelog
* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.6.2-4
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Feb 16 2021 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.6.2-3
- Trigger resetting the service state, since we're removing the preset in F34

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Oct 15 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 1.6.2-1
- Updated to version 1.6.2.

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 08 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 1.6.1-1
- Updated to version 1.6.1.

* Sat Apr 11 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 1.6-1
- Updated to version 1.6.

* Fri Apr 10 2020 Neal Gompa <ngompa13@gmail.com> - 1.5-2
- Add Supplements to fedora-release-workstation for F32+ to work around RHBZ#1814306

* Mon Mar 23 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 1.5-1
- Updated to version 1.5.

* Tue Mar 03 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 1.4-2
- Fixed RHBZ#1809407 and RHBZ#1809408.

* Mon Mar 02 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 1.4-1
- Updated to version 1.4.

* Fri Feb 28 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 1.3.1-1
- Updated to version 1.3.1.

* Fri Feb 21 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 1.3-4
- Rebuilt for Fedora 32.
- Backported security hardening patches.

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 05 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 1.3-2
- Forwarded version to compiled binary.

* Mon May 27 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 1.3-1
- Updated to version 1.3.

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Nov 05 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 1.2-1
- Updated to version 1.2.

* Wed Aug 15 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 1.1-1
- Initial SPEC release.
