%global reponame popub
%global commit 6ffa11c634c1aa877d3f4b79ada19b8e6a92dae9
%global commitdate 20171007
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%if 0%{!?_unitdir:1}
%global _unitdir /usr/lib/systemd/system
%endif

Name:    %{reponame}
Version: 0
Release: 0.11.%{commitdate}git%{shortcommit}%{?dist}
Summary: Publish a service from localhost onto your server
License: GPLv3+
URL:     https://github.com/m13253/%{name}
Source0: %{url}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

ExclusiveArch: %{?go_arches:%{go_arches}}%{!?go_arches:%{ix86} x86_64 %{arm}}
BuildRequires: make
BuildRequires: %{?go_compiler:compiler(go-compiler)}%{!?go_compiler:golang}
%{?systemd_requires}
BuildRequires: systemd

%if ! 0%{?gobuild:1}
%define gobuild(o:) go build -ldflags "${LDFLAGS:-} -B 0x$(head -c20 /dev/urandom|od -An -tx1|tr -d ' \\n')" -a -v -x %{?**};
%endif

%if ! 0%{?gotest:1}
%define gotest() go test -ldflags "${LDFLAGS:-}" %{?**}
%endif

%description
%{summary}.

%package local
Summary: Publish a service from localhost onto your server - client side
Provides: portpub-local%{?_isa} = %{version}-%{release}
Obsoletes: portpub-local <= 0-0.2

%description local
%{summary}.
Local side package.

%package relay
Summary: Publish a service from localhost onto your server - server side
Provides: portpub-relay%{?_isa} = %{version}-%{release}
Obsoletes: portpub-relay <= 0-0.2

%description relay
%{summary}.
Server side package.

%prep
%setup -q -n %{name}-%{commit}

%build
cd %{reponame}-local
%gobuild -o %{reponame}-local

cd ../%{reponame}-relay
%gobuild -o %{reponame}-relay

%install
sed -i '/daemon-reload/d' systemd/Makefile
%make_install PREFIX=%{_prefix}

%post local
%systemd_post %{name}-local@.service

%preun local
%systemd_preun %{name}-local@.service

%postun local
%systemd_postun_with_restart %{name}-local@.service

%post relay
%systemd_post %{name}-relay@.service

%preun relay
%systemd_preun %{name}-relay@.service

%postun relay
%systemd_postun_with_restart %{name}-relay@.service

%files local
%doc README.md
%license COPYING
%{_bindir}/%{name}-local
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/local
%{_unitdir}/%{name}-local@.service

%files relay
%doc README.md
%license COPYING
%{_bindir}/%{name}-relay
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/relay
%{_unitdir}/%{name}-relay@.service

%changelog
* Tue Mar 02 2021 Zbigniew J??drzejewski-Szmek <zbyszek@in.waw.pl> - 0-0.11.20171007git6ffa11c
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.10.20171007git6ffa11c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9.20171007git6ffa11c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8.20171007git6ffa11c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7.20171007git6ffa11c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6.20171007git6ffa11c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5.20171007git6ffa11c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4.20171007git6ffa11c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Oct 16 2017 Zamir SUN <zsun@fedoraproject.org> - 0-0.3.20171007git6ffa11c
- Update to newest upstream.

* Mon Oct 02 2017 Zamir SUN <zsun@fedoraproject.org> - 0-0.2.20170920git4698f9a
- Add support for EPEL

* Mon Sep 18 2017 mosquito <sensor.wen@gmail.com> - 0-0.1.20170406git25cf44e
- Rename to popub
- Improve makefile

* Sat Sep 09 2017 Zamir SUN <zsun@fedoraproject.org> - 0-0.1.20170406gitccd226a
- Initial with git version ccd226a.
