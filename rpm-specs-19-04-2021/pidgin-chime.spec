%global pidginver 2.13.0
%if 0%{?rhel} == 7
# Building 2.14.0 with the V/V bits on EPEL7 is non-trivial. IM only for now.
%global pidginver 2.10.11
%endif

%bcond_without evolution # with

Name:           pidgin-chime
Summary:        Pidgin/libpurple protocol plugin for Amazon Chime
Version:        1.3
Release:        10%{?dist}

License:        LGPLv2
URL:            https://github.com/awslabs/%{name}
Source0:        ftp://ftp.infradead.org/pub/%{name}/%{name}-%{version}.tar.gz

BuildRequires: make
BuildRequires:  pkgconfig(pidgin) >= %{pidginver}
BuildRequires:  pkgconfig(purple) >= %{pidginver}
BuildRequires:  pkgconfig(gnutls) >= 3.2.0
BuildRequires:  pkgconfig(farstream-0.2)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-app-1.0)
BuildRequires:  pkgconfig(gstreamer-rtp-1.0)
BuildRequires:  pkgconfig(gstreamer-video-1.0)
BuildRequires:  pkgconfig(opus)
BuildRequires:  pkgconfig(libprotobuf-c)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libsoup-2.4) >= 2.50
BuildRequires:  ImageMagick
%if %{with evolution}
BuildRequires:  pkgconfig(evolution-calendar-3.0)
BuildRequires:  pkgconfig(evolution-shell-3.0)
BuildRequires:  pkgconfig(evolution-data-server-1.2)
BuildRequires:  pkgconfig(libebook-1.2)
# libecal changed from -1.2 to -2.0 in e-d-s 3.33.2
# Any conditional BR would be based on %_fedora and be distro-specific
# anyway, so we might as well just not BR it at all, depending on the
# equally distro-specific knowledge that it's in e-d-s-devel with the
# rest.
#BuildRequires:  pkgconfig(libecal-1.2)
%endif # with evolution
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  libtool
BuildRequires:  autoconf
BuildRequires:  automake

Requires:       purple-chime%{?_isa} = %{version}-%{release}
Requires:       evolution-chime
Requires:       pidgin >= %{pidginver}

%description
A plugin for the Pidgin multi-protocol instant messenger, to support Amazon
Chime.

This package provides the icon set for Pidgin, and a UI plugin to indicate
seen messages.

%package -n purple-chime
Summary:  Libpurple protocol plugin for Amazon Chime

%description -n purple-chime
A plugin for the Pidgin multi-protocol instant messenger, to support Amazon
Chime.

This package provides the Amazon Chime protocol support for the libpurple
messaging library, which is used by Pidgin and other tools.


%if %{with evolution}
%package -n evolution-chime
Summary:  Evolution plugin for Amazon Chime
Requires: pidgin-chime = %{version}-%{release}

%description -n evolution-chime
A plugin for Evolution that allows you to create meetings in Amazon Chime.
%endif # with evolution

%prep
%setup -q

%build
%configure \
%if %{without evolution}
  --without-evolution \
%endif # without evolution
  --with-certsdir=%{_sysconfdir}/pki/purple-chime/cacerts;
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
%find_lang %{name}

%check
make %{?_smp_mflags} check

%files
%{_datadir}/pixmaps/pidgin/protocols/*/chime*
%{_libdir}/pidgin/chimeseen.so

%files -n purple-chime -f %{name}.lang
%{_libdir}/purple-2/libchimeprpl.so
%{_libdir}/farstream-0.2/libapp-transmitter.so
%{_libdir}/gstreamer-1.0/libgstchime.so
%dir %{_sysconfdir}/pki/purple-chime
%dir %{_sysconfdir}/pki/purple-chime/cacerts
%{_sysconfdir}/pki/purple-chime/cacerts/*.pem

%license LICENSE
%doc README.md TODO

%if %{with evolution}
%files -n evolution-chime
%{_libdir}/evolution/modules/module-event-from-template.so
%endif # with evolution

%changelog
* Fri Feb 12 2021 Kalev Lember <klember@redhat.com> - 1.3-10
- Rebuilt for evolution-data-server soname bump

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 14 08:30:06 CET 2021 Adrian Reber <adrian@lisas.de> - 1.3-8
- Rebuilt for protobuf 3.14

* Wed Jan 13 16:41:22 CET 2021 Adrian Reber <adrian@lisas.de> - 1.3-7
- Rebuilt for protobuf 3.14

* Thu Sep 24 2020 Adrian Reber <adrian@lisas.de> - 1.3-6
- Rebuilt for protobuf 3.13

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 13 2020 Kevin Fenzi <kevin@scrye.com> - 1.3-4
- Rebuild for new evolution-data-server.

* Sun Jun 14 2020 Adrian Reber <adrian@lisas.de> - 1.3-3
- Rebuilt for protobuf 3.12

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov  8 2019 David Woodhouse <dwmw2@infradead.org> - 1.3-1
- Update to 1.3 (crash fixes)

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 21 2019 David Woodhouse <dwmw2@infradead.org> - 1.2-1
- Update to 1.2 (signin and search fixes, libecal-2.0 compatibility)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri May 25 2018 David Woodhouse <dwmw2@infradead.org> - 1.1-1
- Update to 1.1 (fixes signin incompatibility)

* Mon May  7 2018 David Woodhouse <dwmw2@infradead.org> - 1.0-1
- Initial packaging.
