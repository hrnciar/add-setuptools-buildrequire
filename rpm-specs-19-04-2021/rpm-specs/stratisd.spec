# Generated by rust2rpm
%bcond_without check
%global __cargo_skip_build 0
%global udevdir %(pkg-config --variable=udevdir udev)

# Not interested in packaging lib
# stratisd is supposed to be daemon used through dbus
%global __cargo_is_lib() false

Name:           stratisd
Version:        2.3.0
Release:        10%{?dist}
Summary:        Daemon that manages block devices to create filesystems

# 0BSD or MIT or ASL 2.0
# ASL 2.0
# ASL 2.0 or Boost
# BSD
# MIT
# MIT or ASL 2.0
# MIT or zlib or ASL 2.0
# MPLv2.0
# Unlicense or MIT
License:        MPLv2.0 and ASL 2.0 and BSD and MIT
URL:            https://github.com/stratis-storage/stratisd
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{url}/releases/download/v%{version}/%{name}-%{version}-vendor.tar.gz

ExclusiveArch:  %{rust_arches}

%if 0%{?rhel} && !0%{?eln}
BuildRequires:  rust-toolset
BuildRequires:  systemd-devel
BuildRequires:  dbus-devel
BuildRequires:  clang
BuildRequires:  /usr/bin/a2x
BuildRequires:  pkgconfig(libcryptsetup) >= 2.3.0
BuildRequires:  pkgconfig(blkid) >= 2.32.0
%else
BuildRequires:  rust-packaging
%endif
BuildRequires:  systemd

%{?systemd_requires}
Requires:       xfsprogs
Requires:       device-mapper-persistent-data
Requires:       clevis-luks >= 15

%description
%{summary}.

%prep
%autosetup -p1
%if 0%{?rhel} && !0%{?eln}
# Source1 is vendored dependencies
%cargo_prep -V 1
%else
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires
echo '/usr/bin/a2x'
echo 'pkgconfig(libcryptsetup) >= 2.3.0'
echo 'pkgconfig(blkid) >= 2.32.0'
%endif

%build
%cargo_build
a2x -f manpage docs/stratisd.txt

%install
%cargo_install

# Daemon should be really private
mkdir -p %{buildroot}%{_libexecdir}
mv %{buildroot}%{_bindir}/stratisd %{buildroot}%{_libexecdir}/stratisd

mkdir -p %{buildroot}%{udevdir}
mv %{buildroot}%{_bindir}/stratis_uuids_to_names %{buildroot}%{udevdir}/stratis_uuids_to_names

install -Dpm0644 -t %{buildroot}%{_datadir}/dbus-1/system.d stratisd.conf
install -Dpm0644 -t %{buildroot}%{_mandir}/man8 docs/stratisd.8
install -Dpm0644 -t %{buildroot}%{_udevrulesdir} udev/11-stratisd.rules
install -Dpm0644 -t %{buildroot}%{_unitdir} stratisd.service
install -Dpm0755 -t %{buildroot}%{_bindir} developer_tools/stratis_migrate_symlinks.sh

%if %{with check}
%check
%cargo_test -- -- --skip real_ --skip loop_ --skip travis_
%endif

%post
%systemd_post stratisd.service

%preun
%systemd_preun stratisd.service

%postun
%systemd_postun_with_restart stratisd.service

%files
%license LICENSE
%doc README.md
%{_libexecdir}/stratisd
%{udevdir}/stratis_uuids_to_names
%{_bindir}/stratis_dbusquery_version
%{_bindir}/stratis_migrate_symlinks.sh
%dir %{_datadir}/dbus-1
%dir %{_datadir}/dbus-1/system.d
%{_datadir}/dbus-1/system.d/stratisd.conf
%{_mandir}/man8/stratisd.8*
%{_unitdir}/stratisd.service
%{_udevrulesdir}/11-stratisd.rules

%changelog
* Wed Mar 17 2021 mulhern <amulhern@redhat.com> - 2.3.0-10
- Use external URL for vendored sources

* Tue Mar 02 2021 Zbigniew J??drzejewski-Szmek <zbyszek@in.waw.pl> - 2.3.0-9
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 15 2021 Igor Raits <ignatenkobrain@fedoraproject.org> - 2.3.0-7
- Fix build on ELN

* Fri Jan 15 2021 Igor Raits <ignatenkobrain@fedoraproject.org> - 2.3.0-6
- Make package compatible without violating guidelines

* Fri Jan 15 2021 mulhern <amulhern@redhat.com> - 2.3.0-5
- Add both sources at the same time

* Fri Jan 15 2021 mulhern <amulhern@redhat.com> - 2.3.0-4
- Restore RHEL/Fedora compatible spec file, adding some additional changes

* Fri Jan 15 2021 Igor Raits <ignatenkobrain@fedoraproject.org> - 2.3.0-3
- Partially revert previous commit

* Thu Jan 14 2021 mulhern <amulhern@redhat.com> - 2.3.0-2
- Make RHEL/Fedora compatible spec file

* Tue Jan 12 2021 mulhern <amulhern@redhat.com> - 2.3.0-1
- Update to 2.3.0

* Mon Dec 28 13:34:26 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 2.2.1-3
- Rebuild

* Sun Dec 27 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 2.2.1-2
- Rebuild

* Mon Nov 9 2020 mulhern <amulhern@redhat.com> - 2.2.1-1
- Update to 2.2.1

* Mon Oct 19 2020 mulhern <amulhern@redhat.com> - 2.2.0-1
- Update to 2.2.0

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 07 2020 John Baublitz <jbaublitz@redhat.com> - 2.1.0-1
- Update to 2.1.0

* Wed Feb 19 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 2.0.1-2
- Fixup license

* Wed Feb 19 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 2.0.1-1
- Update to 2.0.1

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 07 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.0.0-1
- Update to 2.0.0

* Fri Sep 06 20:52:06 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.5-1
- Update to 1.0.5

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 04 2019 Josh Stone <jistone@redhat.com> - 1.0.4-2
- Bump nix to 0.14

* Tue May 07 08:16:24 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.4-1
- Update to 1.0.4

* Wed Mar 06 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.3-1
- Update to 1.0.3

* Wed Dec 12 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.2-1
- Update to 1.0.2

* Fri Nov 02 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.1-1
- Update to 1.0.1

* Thu Sep 27 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.0-1
- Update to 1.0.0

* Wed Sep 19 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.9.0-4
- Add missing systemd scriptlets

* Wed Sep 19 2018 Tony Asleson <tasleson@redhat.com> - 0.9.0-3
- Add systemd unit file
- Remove systemd activation file

* Tue Sep 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.9.0-2
- Rebuild to workaround pungi bug

* Sat Sep 01 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.9.0-1
- Update to 0.9.0

* Fri Aug 3 2018 Andy Grover <agrover@redhat.com> - 0.5.5-2
- Disable a failing but noncritical test

* Fri Aug 03 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.5.5-1
- Update to 0.5.5

* Thu Jul 19 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.5.4-3
- Upgrade dependencies

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.5.4-1
- Update to 0.5.4

* Fri Jun 22 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.5.3-2
- Add -init version of daemon
- Own dbus-1 directory

* Mon Jun 4 2018 Andy Grover <agrover@redhat.com> - 0.5.3-1
- Update to 0.5.3

* Fri May 4 2018 Andy Grover <agrover@redhat.com> - 0.5.2-2
- Add 0002-Prefix-commands-with-entire-path.patch

* Tue May 1 2018 Andy Grover <agrover@redhat.com> - 0.5.2-1
- Update to 0.5.2

* Tue Apr 03 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.5.1-1
- Update to 0.5.1

* Tue Mar 13 2018 Andy Grover <agrover@redhat.com> - 0.5.0-2
- Add stratisd manpage

* Thu Mar 08 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.5.0-1
- Update to 0.5.0

* Thu Feb 15 2018 Andy Grover <agrover@redhat.com> - 0.1.5-2
- Require packages that contain binaries that we exec: xfsprogs and
  device-mapper-persistent-data

* Sun Feb 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.5-1
- Update to 0.1.5

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 08 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.4-3
- Rebuild for rust-packaging v5

* Mon Jan 08 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.4-2
- Move binary under %%{_libexecdir}
- Add dbus service (so it is activatable)
- Fix rand's version bump

* Sun Jan 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.4-1
- Initial package
