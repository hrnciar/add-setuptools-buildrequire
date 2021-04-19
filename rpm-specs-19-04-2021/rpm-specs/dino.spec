Name:       dino
Version:    0.2.0
Release:    3%{?dist}

License:    GPLv3
Summary:    Modern XMPP ("Jabber") Chat Client using GTK+/Vala
URL:        https://github.com/dino/dino
Source0:    %{url}/releases/download/v%{version}/dino-%{version}.tar.gz
Source1:    %{url}/releases/download/v%{version}/dino-%{version}.tar.gz.asc
# dino.im has a published Web Key Directory[0], which is the URL used here. However, I also verified
# that the key matched what was available via public key servers. I also verified that the key was
# indeed the key that generated the signature for the release tarball for dino-0.1.0, ensuring that
# both the signature and tarball were retrieved from GitHub over TLS. Lastly, a couple users
# in the official Dino MUC chat room, chat@dino.im, verified the full release key ID, and my
# connection to that chat room used CA verified TLS. I believe the WKD verification is strong
# enough, but I feel more confident given my secondary (though admittedly weaker)
# verifications.
#
# [0] https://wiki.gnupg.org/WKD
Source2:    https://dino.im/.well-known/openpgpkey/hu/kf5ictsogs7pr4rbewa9ie1he85r9ghc

BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: gpgme-devel
BuildRequires: gnupg2
BuildRequires: gtk+-devel
BuildRequires: gtk3-devel
BuildRequires: libgee-devel
BuildRequires: libgcrypt-devel
BuildRequires: libsignal-protocol-c-devel
BuildRequires: libsoup-devel
BuildRequires: ninja-build
BuildRequires: qrencode-devel
BuildRequires: sqlite-devel
BuildRequires: vala
BuildRequires: make

Recommends: webp-pixbuf-loader
Requires:   filesystem
Requires:   hicolor-icon-theme


%description
A modern XMPP ("Jabber") chat client using GTK+/Vala.


%package devel
Summary:    Development files for dino

Requires:   dino%{?_isa} == %{version}-%{release}


%description devel
Development files for dino.


%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1 -n %{name}-%{version}

# Remove the bundled library
rm .gitmodules
rm -r plugins/signal-protocol/libsignal-protocol-c


%build
# Use the system version of libsignal-protocol-c instead of the bundled one.
export SHARED_SIGNAL_PROTOCOL=true
%configure
%make_build


%install
%make_install
%find_lang %{name}
%find_lang %{name}-omemo
%find_lang %{name}-openpgp


%check
make test
desktop-file-validate %{buildroot}/%{_datadir}/applications/im.dino.Dino.desktop


%files -f %{name}.lang -f %{name}-omemo.lang -f %{name}-openpgp.lang
%license LICENSE
%doc README.md
%{_bindir}/dino
%{_datadir}/applications/im.dino.Dino.desktop
%{_datadir}/dbus-1/services/im.dino.Dino.service
%{_datadir}/icons/hicolor/scalable/apps/im.dino.Dino.svg
%{_datadir}/icons/hicolor/scalable/status/*.svg
%{_datadir}/icons/hicolor/symbolic/apps/im.dino.Dino-symbolic.svg
%{_datadir}/metainfo/im.dino.Dino.appdata.xml
%{_libdir}/dino
%{_libdir}/libdino.so.0*
%{_libdir}/libqlite.so.0*
%{_libdir}/libxmpp-vala.so.0*


%files devel
%{_datadir}/vala/vapi/dino.*
%{_datadir}/vala/vapi/qlite.*
%{_datadir}/vala/vapi/xmpp-vala.*
%{_includedir}/dino.h
%{_includedir}/dino_i18n.h
%{_includedir}/qlite.h
%{_includedir}/xmpp-vala.h
%{_libdir}/libdino.so
%{_libdir}/libqlite.so
%{_libdir}/libxmpp-vala.so


%changelog
* Wed Feb 17 2021 Randy Barlow <bowlofeggs@fedoraproject.org> - 0.2.0-3
- Add a dependency on webp-pixbuf-loader (#1929149).

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov 16 2020 Randy Barlow <bowlofeggs@fedoraproject.org> - 0.2.0-1
- Update to 0.2.0 (#1897438).
- https://github.com/dino/dino/releases/tag/v0.2.0
- https://dino.im/blog/2020/11/dino-0.2-release/

* Mon Nov 16 2020 Randy Barlow <bowlofeggs@fedoraproject.org> - 0.1.1-1
- Update to 0.1.1 (#1897438).
- https://github.com/dino/dino/releases/tag/v0.1.1

* Sat Aug 15 2020 Randy Barlow <bowlofeggs@fedoraproject.org> - 0.1.0-2
- Fix FTBFS.

* Fri Jan 31 2020 Randy Barlow <bowlofeggs@fedoraproject.org> - 0.1.0-1
- Update to the first Dino release.
- https://dino.im/blog/2020/01/dino-0.1-release/
- https://github.com/dino/dino/compare/11c18cdf...v0.1.0

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-0.18.20191216.git.11c18cd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild
