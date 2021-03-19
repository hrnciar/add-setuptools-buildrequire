%global _firewalld_dir %{_prefix}/lib/firewalld

Name:           et
Version:        6.1.4
Release:        1%{?dist}
Summary:        Remote shell that survives IP roaming and disconnect

License:        ASL 2.0
URL:            https://mistertea.github.io/EternalTerminal/
Source0:        https://github.com/MisterTea/EternalTerminal/archive/et-v%{version}.tar.gz
Source1:        et.xml
# SIGSTKSZ is no longer constant in glibc > 2.33 but a function returning a long
# cast the result before taking max
Patch0:         et-6.1.4-fix-sentry-breakpad-sigstksz.patch
# ditto with MINSIGSTKSZ
Patch1:         et-6.1.4-fix-catch2-minsigstksz.patch
# allow disabling sentry
# bz #1939775: bundled sentry-native does not compile
# ppc64le: external_imported/sentry-native/external/third_party/lss/linux_syscall_support.h:3927:25: error: '__NR_mmap2' was not declared in this scope
# s390x:   external_imported/sentry-native/external/breakpad/src/common/linux/memory_mapped_file.cc:74:7: error: 'sys_fstat64' was not declared in this scope; did you mean 'sys_fstatfs'?
Patch2:         et-6.1.4-allow-disabling-sentry.patch

BuildRequires:  boost-devel
BuildRequires:  cmake3
BuildRequires:  firewalld-filesystem
BuildRequires:  gcc-c++
BuildRequires:  gflags-devel
BuildRequires:  libatomic
BuildRequires:  libcurl-devel
BuildRequires:  libsodium-devel
BuildRequires:  libutempter-devel
BuildRequires:  ncurses-devel
BuildRequires:  openssl-devel
BuildRequires:  protobuf-compiler
BuildRequires:  protobuf-lite-devel
BuildRequires:  systemd

# Bundled libraries
Provides:       bundled(base64) = 0
# Catch2 is only a test framework
Provides:       bundled(cotire) = 1.8.0
Provides:       bundled(cpp-httplib) = 0.8.4
Provides:       bundled(cxxopts) = 2.2.0
Provides:       bundled(easyloggingpp) = 9.96.7
Provides:       bundled(msgpack) = 3.3.0
Provides:       bundled(nlohmann_json) = 3.9.1
Provides:       bundled(PlatformFolders) = 4.0.0
# sanitizers-cmake is only used when building
%ifnarch ppc64le s390x
Provides:       bundled(sentry-native) = 0.4.7
%endif
Provides:       bundled(simpleini) = 4.17
Provides:       bundled(sole) = 1.0.1
Provides:       bundled(ThreadPool) = 0
Provides:       bundled(UniversalStacktrace) = 0
# vcpkg is disabled


%{?systemd_requires}

%description
Eternal Terminal (ET) is a remote shell that automatically reconnects without
interrupting the session.


%prep
%autosetup -p1 -n EternalTerminal-et-v%{version}


%build
%cmake . \
%ifarch ppc64le s390x
  -DDISABLE_SENTRY=TRUE \
%endif
  -DDISABLE_VCPKG=TRUE
%cmake_build


%install
%cmake_install
mkdir -p \
  %{buildroot}%{_unitdir} \
  %{buildroot}%{_sysconfdir} \
  %{buildroot}%{_firewalld_dir}/services
install -m 0644 -p systemctl/et.service %{buildroot}%{_unitdir}/et.service
install -m 0644 -p etc/et.cfg %{buildroot}%{_sysconfdir}/et.cfg
install -m 0644 %{SOURCE1} %{buildroot}%{_firewalld_dir}/services/et.xml


%check
%if 0%{?fedora}
%ctest
%else
%ctest --verbose
%endif


%post
%systemd_post et.service
%firewalld_reload

%preun
%systemd_preun et.service

%postun
%systemd_postun_with_restart et.service
%firewalld_reload


%files
%license LICENSE
%doc README.md
%{_bindir}/et
%{_bindir}/etserver
%{_bindir}/etterminal
%{_bindir}/htm
%{_bindir}/htmd
%dir %{_firewalld_dir}
%dir %{_firewalld_dir}/services
%{_firewalld_dir}/services/et.xml
%config(noreplace) %{_sysconfdir}/et.cfg
%{_unitdir}/et.service
# external dependency, used only for building
# once PlatformFolders is packaged, this can be removed
%exclude %{_includedir}/sago/platform_folders.h
%exclude %{_libdir}/cmake/platform_folders
%exclude %{_libdir}/libplatform_folders.a
%ifarch ppc64le s390x
%exclude %{_usr}/lib/debug/%{_libdir}/libplatform_folders.so-*.debug
%exclude %{_libdir}/libplatform_folders.so
%else
%exclude %{_libdir}/libplatform_folders.a
%endif


%changelog
* Tue Mar 16 2021 Michel Alexandre Salim <salimma@fedoraproject.org> - 6.1.4-1
- Update to 6.1.4
- Fix for SIGSTKSZ/MINSIGSTKSZ non-constant on glibc > 2.33
- Declare bundled libraries

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 6.0.13-4
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 14 08:47:13 CET 2021 Adrian Reber <adrian@lisas.de> - 6.0.13-2
- Rebuilt for protobuf 3.14

* Thu Nov 19 2020 Michel Alexandre Salim <salimma@fedoraproject.org> - 6.0.13-1
- Update to 6.0.13

* Thu Nov  5 2020 Filipe Brandenburger <filbranden@gmail.com> - 6.0.11-3
- Go back to using protobuf-lite on epel8, since the -devel package
  for it is now available (rhbz#1787458).

* Thu Sep 24 2020 Adrian Reber <adrian@lisas.de> - 6.0.11-2
- Rebuilt for protobuf 3.13

* Mon Aug  3 2020 Michel Alexandre Salim <salimma@fedoraproject.org> - 6.0.11-1
- Update to 6.0.11
- Use the new option to specify linking against the full protobuf on EPEL
- Adjust for cmake macro changes

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.7-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun 14 2020 Adrian Reber <adrian@lisas.de> - 6.0.7-2
- Rebuilt for protobuf 3.12

* Tue Mar  3 2020 Michel Alexandre Salim <salimma@fedoraproject.org> - 6.0.7-1
- Update to 6.0.7

* Tue Feb 18 2020 Michel Alexandre Salim <salimma@fedoraproject.org> - 6.0.6-1
- Update to 6.0.6

* Sat Feb  1 2020 Michel Alexandre Salim <salimma@fedoraproject.org> - 6.0.5-1
- Update to 6.0.5
- Build for EPEL 8

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Dec  1 2019 Michel Alexandre Salim <salimma@fedoraproject.org> - 6.0.4-1
- Update to 6.0.4

* Sun Sep 22 2019 Michel Alexandre Salim <salimma@fedoraproject.org> - 6.0.3-1
- Update to 6.0.3

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon May 27 2019 Michel Alexandre Salim <salimma@fedoraproject.org> - 5.1.10-1
- Update to 5.1.10

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 16 2019 Jason Gauci <jgmath2000@gmail.com> - 5.1.9-1
- https://github.com/MisterTea/EternalTerminal/releases/tag/et-v5.1.9

* Wed Nov 21 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 5.1.8-3
- Rebuild for protobuf 3.6

* Wed Oct 31 2018 Sérgio Basto <sergio@serjux.com> - 5.1.8-2
- Make it possible build it on EPEL 7

* Mon Oct 29 2018 Michel Alexandre Salim <salimma@fedoraproject.org> - 5.1.8-1
- https://github.com/MisterTea/EternalTerminal/releases/tag/et-v5.1.8

* Wed Oct 17 2018 Michel Alexandre Salim <salimma@fedoraproject.org> - 5.1.7-1%{?dist}
- https://github.com/MisterTea/EternalTerminal/releases/tag/et-v5.1.7
- https://github.com/MisterTea/EternalTerminal/releases/tag/et-v5.1.6

* Tue Oct  9 2018 Jason Gauci <jgmath2000@gmail.com> - 5.1.5-2%{?dist}
- https://github.com/MisterTea/EternalTerminal/releases/tag/et-v5.1.5
- https://github.com/MisterTea/EternalTerminal/releases/tag/et-v5.1.4
- https://github.com/MisterTea/EternalTerminal/releases/tag/et-v5.1.3
- https://github.com/MisterTea/EternalTerminal/releases/tag/et-v5.1.2
- https://github.com/MisterTea/EternalTerminal/releases/tag/et-v5.1.1

* Fri Aug 24 2018 Michel Alexandre Salim <salimma@fedoraproject.org> - 5.1.0-1%{?dist}
- Update to 5.1.0

* Tue Aug 14 2018 Michel Alexandre Salim <salimma@fedoraproject.org> - 5.0.7-2%{?dist}
- add BR on gcc-c++

* Thu Aug  9 2018 Michel Alexandre Salim <salimma@fedoraproject.org> - 5.0.7-1%{?dist}
- Initial package
