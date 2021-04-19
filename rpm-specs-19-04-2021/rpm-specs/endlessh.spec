Summary:	SSH tarpit that slowly sends an endless banner 
Name:		endlessh
Version:	1.1
Release:	4%{?dist}

License:	Unlicense
URL:		https://github.com/skeeto/endlessh
Source0:	https://github.com/skeeto/endlessh/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:		0001-Fix-binary-path-in-endlessh.service.patch
Patch1:		0002-Config-change-to-port-2222.patch
Patch2:		9e66ab19d6b57ae96b161a8acd11bec1a76670c2.patch

BuildRequires:	make
BuildRequires:	gcc
BuildRequires:	git
BuildRequires:	systemd-rpm-macros
Requires:	systemd

%description
Endlessh is an SSH tarpit that very slowly sends an endless, random SSH banner.
It keeps SSH clients locked up for hours or even days at a time. The purpose is
to put your real SSH server on another port and then let the script kiddies get
stuck in this tarpit instead of bothering a real server.

%prep
%autosetup -n %{name}-%{version} -S git

%build
# Makefile doesn't allow overriding from environment, change it
sed -i -e "s:^CFLAGS.*:CFLAGS = %{optflags}:" Makefile
%make_build

%install
make install PREFIX=%{buildroot}%{_prefix}
install -d -m755 %{buildroot}%{_sysconfdir}/%{name}
install -m644 ./util/smf/endlessh.conf %{buildroot}/%{_sysconfdir}/%{name}/config
install -d -m755 %{buildroot}/%{_unitdir}
install -m644 ./util/endlessh.service %{buildroot}/%{_unitdir}/%{name}.service

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files
%{_bindir}/*
%{_mandir}/man1/*
%{_unitdir}/%{name}.service

%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/config

%doc README.md
%license UNLICENSE


%changelog
* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.1-4
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Dec 4 2020 Mikel Olasagasti Uranga <mikel@olasagasti.info> - 1.1-2
- Changes after revision in #1904172

* Thu Dec 3 2020 Mikel Olasagasti Uranga <mikel@olasagasti.info> - 1.1-1
- First version
