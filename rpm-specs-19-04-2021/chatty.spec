%global _build_id_links none
%global __requires_exclude ^libjabber\\.so.*$

Name: chatty
Version: 0.3.0_beta2
Release: 1%{?dist}
Summary: A libpurple messaging client

License: GPLv3+
URL: https://source.puri.sm/Librem5/chatty
Source0: https://source.puri.sm/Librem5/chatty/-/archive/v%{version}/%{name}-v%{version}.tar.gz

# Chatty links against a libpurple private library (libjabber).
# Obviously, Fedora build tooling doesn't support that, so we have to use
# some kind of workaround. This seemed simplest.
# We do not want to provide a private library, which is from another
# project, to be used in other packages.
Patch0:  0001-hacky-hack.patch

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  cmake
BuildRequires:  gcc-c++

BuildRequires:  pkgconfig(libebook-contacts-1.2)
BuildRequires:  pkgconfig(libebook-1.2) >= 3.33.2
BuildRequires:  pkgconfig(libedataserver-1.2) >= 3.33.2
BuildRequires:  pkgconfig(libfeedback-0.0)
BuildRequires:  pkgconfig(libhandy-1) >= 1.0.0
BuildRequires:  pkgconfig(gio-2.0) >= 2.50.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22.0
BuildRequires:  pkgconfig(purple)
BuildRequires:  pkgconfig(sqlite3) >= 3.0.0
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(folks)
BuildRequires:  pkgconfig(gsettings-desktop-schemas)
BuildRequires:  pkgconfig(libgcrypt)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(mm-glib) >= 1.12.0
BuildRequires:  libolm-devel
BuildRequires:  libphonenumber-devel
BuildRequires:  protobuf-devel
BuildRequires:  libappstream-glib
BuildRequires:  desktop-file-utils
BuildRequires:  /usr/bin/xvfb-run
BuildRequires:  /usr/bin/xauth

Requires: hicolor-icon-theme

%description
Chatty is a libpurple based messaging client for mobile phones,
works best with the phosh mobile DE.

%prep

# Copy private libjabber library in so we can build against it
cp `pkg-config --variable=plugindir purple`/libjabber.so.0 /tmp/libjabber.so

%autosetup -p1 -n chatty-v%{version}

%build
%meson
%meson_build

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/sm.puri.Chatty.metainfo.xml

desktop-file-validate %{buildroot}/%{_datadir}/applications/sm.puri.Chatty.desktop

# the upstream meson tests already validate the desktop file
# and the appstream file

LC_ALL=C.UTF-8 xvfb-run sh <<'SH'
%meson_test -t 2
SH

%install
%meson_install

# Adding libjabber to link against
mkdir -p %{buildroot}%{_libdir}
cp `pkg-config --variable=plugindir purple`/libjabber.so.0 %{buildroot}%{_libdir}

# Adding ld.so.conf.d in order to use the libjabber at runtime
mkdir -p %{buildroot}/%{_sysconfdir}/ld.so.conf.d
echo "%{_libdir}/chatty" > %{buildroot}/%{_sysconfdir}/ld.so.conf.d/chatty.conf

%find_lang purism-chatty

# The mesa vulkan bug breaks tests
# https://bugzilla.redhat.com/show_bug.cgi?id=1911130

%files -f purism-chatty.lang
%{_bindir}/chatty
%{_sysconfdir}/xdg/autostart/sm.puri.Chatty-daemon.desktop
%{_datadir}/glib-2.0/schemas/sm.puri.Chatty.gschema.xml
%{_datadir}/applications/sm.puri.Chatty.desktop
%{_datadir}/icons/hicolor/*/apps/sm.puri.Chatty*.svg
%{_metainfodir}/sm.puri.Chatty.metainfo.xml
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/chatty
%{_libdir}/libjabber.so.0
%{_sysconfdir}/ld.so.conf.d/chatty.conf
%doc README.md
%license COPYING


%changelog
* Wed Apr 14 2021 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.3.0_beta2-1
- Update to chatty 0.3.0 beta 2

* Sun Mar 28 2021 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.3.0_beta-2
* Add patch for matrix crash in encrypted rooms

* Fri Mar 26 2021 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.3.0_beta-1
- Update to 0.3.0_beta

* Sat Mar 13 2021 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.2.0-5
- Update for package review

* Mon Feb 15 2021 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.2.0-4
- Build for new evolution dep

* Sat Feb 06 2021 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.2.0-3
- Re-add tests

* Mon Jan 11 2021 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.2.0-2
- Updating for f34

* Mon Nov 16 2020 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.2.0-1
- Update version to 0.2.0

* Tue Nov 03 2020 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.1.17-1
- Update versoin to 0.1.17

* Thu Oct 15 2020 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.1.16-2
- Updating meson tests for timeout

* Sun Sep 27 2020 Nikhil Jha <hi@nikhiljha.com> - 0.1.16-1
- Update version to 0.1.16

* Thu Aug 20 2020 Nikhil Jha <hi@nikhiljha.com> - 0.1.15-1
- Update version to 0.1.15

* Mon Jul 20 2020 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.1.14-1
- Update version to 0.1.14 

* Thu Jun 25 2020 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.1.12-1
- Update version to 0.1.12

* Fri May 29 2020 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.1.11-1
- Update version to 0.1.11
- Remove 2 patches 

* Wed Mar 04 2020 Nikhil Jha <hi@nikhiljha.com> - 0.1.8-3
- Remove the buildid

* Wed Mar 04 2020 Nikhil Jha <hi@nikhiljha.com> - 0.1.8-2
- Bundle libjabber with it

* Mon Mar 02 2020 Nikhil Jha <hi@nikhiljha.com> - 0.1.8-1
- Initial packaging
