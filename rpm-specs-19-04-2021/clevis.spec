Name:           clevis
Version:        18
Release:        1%{?dist}
Summary:        Automated decryption framework

License:        GPLv3+
URL:            https://github.com/latchset/%{name}
Source0:        https://github.com/latchset/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.xz
Source1:        clevis.sysusers

BuildRequires:  git-core
BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  asciidoc
BuildRequires:  ninja-build
BuildRequires:  bash-completion

BuildRequires:  libjose-devel >= 8
BuildRequires:  libluksmeta-devel >= 8
BuildRequires:  audit-libs-devel
BuildRequires:  libudisks2-devel
BuildRequires:  openssl-devel

BuildRequires:  tpm2-tools >= 4.0.0
BuildRequires:  desktop-file-utils
BuildRequires:  pkgconfig
BuildRequires:  systemd
BuildRequires:  systemd-rpm-macros
BuildRequires:  dracut
BuildRequires:  tang >= 6
BuildRequires:  curl
BuildRequires:  cracklib-dicts
BuildRequires:  luksmeta
BuildRequires:  openssl
BuildRequires:  diffutils
BuildRequires:  cryptsetup
BuildRequires:  jq

Requires:       tpm2-tools >= 4.0.0
Requires:       coreutils
Requires:       jose >= 8
Requires:       curl
Requires:       jq
Requires(pre):  shadow-utils
Recommends:     cracklib-dicts
Recommends:     clevis-pin-tpm2

%description
Clevis is a framework for automated decryption. It allows you to encrypt
data using sophisticated unlocking policies which enable decryption to
occur automatically.

The clevis package provides basic encryption/decryption policy support.
Users can use this directly; but most commonly, it will be used as a
building block for other packages. For example, see the clevis-luks
and clevis-dracut packages for automatic root volume unlocking of LUKSv1
volumes during early boot.

%package luks
Summary:        LUKS integration for clevis
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cryptsetup
Requires:       luksmeta >= 8

%description luks
LUKS integration for clevis. This package allows you to bind a LUKS
volume to a clevis unlocking policy. For automated unlocking, an unlocker
will also be required. See, for example, clevis-dracut and clevis-udisks2.

%package systemd
Summary:        systemd integration for clevis
Requires:       %{name}-luks%{?_isa} = %{version}-%{release}
%if 0%{?fedora} > 27
Requires:       systemd%{?_isa} >= 235-3
%else
%if 0%{?fedora} == 27
Requires:       systemd%{?_isa} >= 234-9
%else
%if 0%{?fedora} == 26
Requires:       systemd%{?_isa} >= 233-7
%else
Requires:       systemd%{?_isa} >= 236
%endif
%endif
%endif

%description systemd
Automatically unlocks LUKS _netdev block devices from /etc/crypttab.

%package dracut
Summary:        Dracut integration for clevis
Requires:       %{name}-systemd%{?_isa} = %{version}-%{release}
Requires:       dracut-network

%description dracut
Automatically unlocks LUKS block devices in early boot.

%package udisks2
Summary:        UDisks2/Storaged integration for clevis
Requires:       %{name}-luks%{?_isa} = %{version}-%{release}

%description udisks2
Automatically unlocks LUKS block devices in desktop environments that
use UDisks2 or storaged (like GNOME).

%prep
%autosetup -S git

%build
%meson -Duser=clevis -Dgroup=clevis
%meson_build

%install
%meson_install
install -p -D -m 0644 %{SOURCE1} %{buildroot}%{_sysusersdir}/clevis.conf

%check
desktop-file-validate \
  %{buildroot}/%{_sysconfdir}/xdg/autostart/%{name}-luks-udisks2.desktop
%meson_test

%pre
%sysusers_create_compat %{SOURCE1}
# Add clevis user to tss group.
if getent group tss >/dev/null && ! groups %{name} | grep -q "\btss\b"; then
    usermod -a -G tss %{name} &>/dev/null
fi
exit 0

%posttrans
# In case the clevis-luks-askpass is enabled, make sure it's using the
# correct target, which changed in v14.
[ "$(find /etc/systemd/system/ -name "clevis-luks-askpass*")" ] || exit 0
find /etc/systemd/system/ -name "clevis-luks-askpass*" \
     | grep -q cryptsetup.target.wants && exit 0

find /etc/systemd/system/ -name "clevis-luks-askpass*" -exec rm {} +
systemctl enable clevis-luks-askpass.path >/dev/null 2>&1 || :
exit 0

%files
%license COPYING
%{_datadir}/bash-completion/
%{_bindir}/%{name}-decrypt-tang
%{_bindir}/%{name}-decrypt-tpm2
%{_bindir}/%{name}-decrypt-sss
%{_bindir}/%{name}-decrypt
%{_bindir}/%{name}-encrypt-tang
%{_bindir}/%{name}-encrypt-tpm2
%{_bindir}/%{name}-encrypt-sss
%{_bindir}/%{name}
%{_mandir}/man1/%{name}-encrypt-tang.1*
%{_mandir}/man1/%{name}-encrypt-tpm2.1*
%{_mandir}/man1/%{name}-encrypt-sss.1*
%{_mandir}/man1/%{name}-decrypt.1*
%{_mandir}/man1/%{name}.1*
%{_sysusersdir}/clevis.conf

%files luks
%{_mandir}/man7/%{name}-luks-unlockers.7*
%{_mandir}/man1/%{name}-luks-unlock.1*
%{_mandir}/man1/%{name}-luks-unbind.1*
%{_mandir}/man1/%{name}-luks-bind.1*
%{_mandir}/man1/%{name}-luks-list.1.*
%{_mandir}/man1/%{name}-luks-edit.1.*
%{_mandir}/man1/%{name}-luks-regen.1.*
%{_mandir}/man1/%{name}-luks-report.1.*
%{_mandir}/man1/%{name}-luks-pass.1.*
%{_bindir}/%{name}-luks-unlock
%{_bindir}/%{name}-luks-unbind
%{_bindir}/%{name}-luks-bind
%{_bindir}/%{name}-luks-common-functions
%{_bindir}/%{name}-luks-list
%{_bindir}/%{name}-luks-edit
%{_bindir}/%{name}-luks-regen
%{_bindir}/%{name}-luks-report
%{_bindir}/%{name}-luks-pass

%files systemd
%{_libexecdir}/%{name}-luks-askpass
%{_unitdir}/%{name}-luks-askpass.path
%{_unitdir}/%{name}-luks-askpass.service

%files dracut
%{_prefix}/lib/dracut/modules.d/60%{name}
%{_prefix}/lib/dracut/modules.d/60%{name}-pin-sss/module-setup.sh
%{_prefix}/lib/dracut/modules.d/60%{name}-pin-tang/module-setup.sh
%{_prefix}/lib/dracut/modules.d/60%{name}-pin-tpm2/module-setup.sh

%files udisks2
%{_sysconfdir}/xdg/autostart/%{name}-luks-udisks2.desktop
%attr(4755, root, root) %{_libexecdir}/%{name}-luks-udisks2

%changelog
* Thu Apr 15 2021 Sergio Correia <scorreia@redhat.com> - 18-1
- Update to new clevis upstream release, v18.

* Wed Apr 14 2021 Sergio Correia <scorreia@redhat.com> - 17-1
- Update to new clevis upstream release, v17.

* Tue Mar 16 2021 Sergio Correia <scorreia@redhat.com> - 16-2
- Fix for -t option in clevis luks bind - backport upstream commit ea0d0c20

* Tue Feb 09 2021 Sergio Correia <scorreia@redhat.com> - 16-1
- Update to new clevis upstream release, v16.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov 23 08:14:40 GMT 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 15-3
- Upstream patch for tpm-tools 5.0 support

* Thu Oct 29 2020 Sergio Correia <scorreia@redhat.com> - 15-2
- Add jq to dependencies

* Wed Oct 28 2020 Sergio Correia <scorreia@redhat.com> - 15-1
- Update to new clevis upstream release, v15.

* Tue Sep 08 2020 Sergio Correia <scorreia@redhat.com> - 14-5
- Suppress output in pre scriptlet when adjusting users/groups
  Resolves: rhbz#1876729

* Tue Sep 08 2020 Sergio Correia <scorreia@redhat.com> - 14-4
- Backport upstream PR#230 - clevis-luks-askpass now exits cleanly
  when receives a SIGTERM
  Resolves: rhbz#1876001

* Sat Sep 05 2020 Sergio Correia <scorreia@redhat.com> - 14-3
- If clevis-luks-askpass is enabled, it may be using a wrong target,
  since that changed in v14. Check and update it, if required.

* Mon Aug 31 2020 Sergio Correia <scorreia@redhat.com> - 14-2
- Update sources file with new v14 release.

* Mon Aug 31 2020 Sergio Correia <scorreia@redhat.com> - 14-1
- Update to new clevis upstream release, v14.

* Sun Aug 02 2020 Benjamin Gilbert <bgilbert@redhat.com> - 13-3
- Downgrade cracklib-dicts to Recommends

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun May 10 2020 Sergio Correia <scorreia@redhat.com> - 13-1
- Update to new clevis upstream release, v13.

* Thu May 07 2020 Sergio Correia <scorreia@redhat.com> - 12-4
- cracklib-dicts should be also listed as a build dependency, since
  it's required for running some of the tests

* Mon Apr 06 2020 Sergio Correia <scorreia@redhat.com> - 12-3
- Make cracklib-dicts a regular dependency

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 20 2020 Sergio Correia <scorreia@redhat.com> - 12-1
- Update to new clevis upstream release, v12.

* Thu Dec 19 2019 Sergio Correia <scorreia@redhat.com> - 11-11
- Backport upstream PR#70 - Handle case where we try to use a partially
  used luksmeta slot
  Resolves: rhbz#1672371

* Thu Dec 05 2019 Sergio Correia <scorreia@redhat.com> - 11-10
- Disable LUKS2 tests for now, since they fail randomly in Koji
  builders, killing the build

* Wed Dec 04 2019 Sergio Correia <scorreia@redhat.com> - 11-9
- Backport of upstream patches and the following fixes:
  - Rework the logic for reading the existing key
  - fix for different output from 'luksAddKey' command w/cryptsetup v2.0.2 (
  - pins/tang: check that key derivation key is available

* Wed Oct 30 2019 Peter Robinson <pbrobinson@fedoraproject.org> 11-8
- Drop need network patch

* Fri Sep 06 2019 Javier Martinez Canillas <javierm@redhat.com> - 11-7
- Add support for tpm2-tools 4.0

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Dec  6 2018 Peter Robinson <pbrobinson@fedoraproject.org> 11-4
- Update patch for work around

* Thu Dec  6 2018 Peter Robinson <pbrobinson@fedoraproject.org> 11-3
- Work around network requirement for early boot

* Fri Nov 09 2018 Javier Martinez Canillas <javierm@redhat.com> - 11-2
- Delete remaining references to the removed http pin
- Install cryptsetup and tpm2_pcrlist in the initramfs
- Add device TCTI library to the initramfs
  Resolves: rhbz#1644876

* Tue Aug 14 2018 Nathaniel McCallum <npmccallum@redhat.com> - 11-1
- Update to v11

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 21 2018 Nathaniel McCallum <npmccallum@redhat.com> - 10-1
- Update to v10

* Tue Feb 13 2018 Nathaniel McCallum <npmccallum@redhat.com> - 9-1
- Update to v9

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Nov 13 2017 Nathaniel McCallum <npmccallum@redhat.com> - 8-1
- Update to v8

* Wed Nov 08 2017 Zbigniew J??drzejewski-Szmek <zbyszek@in.waw.pl> - 7-2
- Rebuild for cryptsetup-2.0.0

* Fri Oct 27 2017 Nathaniel McCallum <npmccallum@redhat.com> - 7-1
- Update to v7

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 27 2017 Nathaniel McCallum <npmccallum@redhat.com> - 6-1
- New upstream release
- Specify unprivileged user/group during configuration
- Move clevis user/group creation to base clevis package

* Mon Jun 26 2017 Nathaniel McCallum <npmccallum@redhat.com> - 5-1
- New upstream release
- Run clevis decryption from udisks2 under an unprivileged user

* Wed Jun 14 2017 Nathaniel McCallum <npmccallum@redhat.com> - 4-1
- New upstream release

* Wed Jun 14 2017 Nathaniel McCallum <npmccallum@redhat.com> - 3-1
- New upstream release

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Nov 18 2016 Nathaniel McCallum <npmccallum@redhat.com> - 2-1
- New upstream release

* Mon Nov 14 2016 Nathaniel McCallum <npmccallum@redhat.com> - 1-1
- First release
