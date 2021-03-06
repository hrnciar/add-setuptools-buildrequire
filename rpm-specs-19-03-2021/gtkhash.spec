# Review at https://bugzilla.redhat.com/show_bug.cgi?id=540328
#
Name:           gtkhash
Version:        1.4
Release:        3%{?dist}
Summary:        GTK+ utility for computing message digests or checksums

License:        GPLv2+
URL:            https://github.com/tristanheaven/gtkhash
Source0:        https://github.com/tristanheaven/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  mhash-devel
BuildRequires:  libb2-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig(libnautilus-extension)
BuildRequires:  pkgconfig(libcaja-extension)
BuildRequires:  pkgconfig(libnemo-extension)
BuildRequires:  pkgconfig(thunarx-3)
BuildRequires:  libappstream-glib
BuildRequires: make

Provides:       gtkhash3 = %{version}-%{release}
Obsoletes:      gtkhash3 < 1.1.1

%description
GtkHash is a GTK+ utility for computing message digests or checksums. Currently
supported hash functions include
* MD2, MD4 and MD5
* SHA1, SHA224, SHA256, SHA384 and SHA512,
* RIPEMD128, RIPEMD160, RIPEMD256 and RIPEMD320
* TIGER128, TIGER160 and TIGER192
* HAVAL128-3, HAVAL160-3, HAVAL192-3, HAVAL224-3 and HAVAL256-3
* SNEFRU128 and SNEFRU256
* ADLER32, CRC32, GOST and WHIRLPOOL

This package contains the GTK+3 version of the program.


%package        nautilus
Summary:        GtkHash extension for nautilus
Requires:       nautilus
Requires:       %{name}3 = %{version}
Requires:       GConf2

%description    nautilus
GtkHash extension for the nautilus file manger. It adds adds an additional tab
called "Checksums" to the file properties dialog.

%package        thunar
Summary:        GtkHash extension for Thunar
Requires:       Thunar
Requires:       %{name} = %{version}

%description    thunar
GtkHash extension for the Thunar file manger. It adds adds an additional tab
called "Checksums" to the file properties dialog.

%package        nemo
Summary:        GtkHash extension for Nemo
Requires:       nemo
Requires:       %{name} = %{version}

%description    nemo
GtkHash extension for the Nemo file manger. It adds adds an additional tab
called "Checksums" to the file properties dialog.

%package        caja
Summary:        GtkHash extension for Caja
Requires:       caja
Requires:       %{name} = %{version}

%description    caja
GtkHash extension for the Caja file manger. It adds adds an additional tab
called "Checksums" to the file properties dialog.

%prep
%setup -q

%build
%configure --with-gtk=3.0 \
  --enable-linux-crypto \
  --enable-gcrypt \
  --enable-glib-checksums \
  --enable-mhash \
  --enable-thunar \
  --enable-nautilus \
  --enable-nemo \
  --enable-caja \
  --disable-schemas-compile \

%make_build

%install

%make_install

%find_lang %{name}

# generic
find %{buildroot} -name '*.la' -exec rm -f {} ';'

appstream-util validate-relax --nonet %{buildroot}/%{_metainfodir}/*.metainfo.xml
appstream-util validate-relax --nonet %{buildroot}/%{_metainfodir}/*.appdata.xml

%files -f %{name}.lang
%license COPYING
%doc AUTHORS NEWS
%{_bindir}/%{name}
%{_datadir}/applications/org.%{name}.%{name}.desktop
%{_datadir}/glib-2.0/schemas/org.%{name}.gschema.xml
%{_datadir}/glib-2.0/schemas/org.%{name}.plugin.gschema.xml
%{_datadir}/icons/hicolor/*/apps/org.%{name}.%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/org.%{name}.%{name}.svg
%{_metainfodir}/org.%{name}.%{name}.appdata.xml

%files nautilus
%{_libdir}/nautilus/extensions-3.0/libgtkhash-properties-nautilus.so
%{_metainfodir}/org.gtkhash.nautilus.metainfo.xml

%files thunar
%{_libdir}/thunarx-3/libgtkhash-properties-thunar.so
%{_metainfodir}/org.gtkhash.thunar.metainfo.xml

%files nemo
%{_libdir}/nemo/extensions-3.0/libgtkhash-properties-nemo.so
%{_metainfodir}/org.gtkhash.nemo.metainfo.xml

%files caja
%{_libdir}/caja/extensions-2.0/libgtkhash-properties-caja.so
%{_datadir}/caja/extensions/libgtkhash-properties-caja.caja-extension
%{_metainfodir}/org.gtkhash.caja.metainfo.xml

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jul 12 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.4-1
- Update to 1.4

* Tue May 26 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.3-1
- Update to 1.3

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Sep 03 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.2-1
- Update to 1.2

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jun 18 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.1.1-3
- Fix other issues

* Mon Jun 18 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.1.1-2
- Add libthunarx-3 as buildrequires

* Mon Jun 18 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.1.1-1
- Update to 1.1.1

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Apr 23 2014 Tom???? Mr??z <tmraz@redhat.com> - 0.6.0-6
- Rebuild for new libgcrypt

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun May 19 2013 Christoph Wickert <cwickert@fedoraproject.org> - 0.6.0-4
- Support for aarch64 (#925514)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Feb 25 2012 Christoph Wickert <cwickert@fedoraproject.org> - 0.6.0-1
- Update to 0.6.0
- Switch to gsettings

* Sat Feb 25 2012 Christoph Wickert <cwickert@fedoraproject.org> - 0.5.0-1
- Update to 0.5.0
- Make extensions require gtkhash(3) base package

* Tue Jan 31 2012 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.0-1
- Update to 0.4.0
- Build GTK+3 version and thunar extension
- Enable gcrypt, glib-checksums and linux-crypto

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.3.0-5
- Rebuild for new libpng

* Thu Feb 24 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.3.0-4
- Rebuild for GTK+ 3.

* Wed Feb 09 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.3.0-3
- Rebuild for nautilus 3.0.

* Mon Nov 23 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.3.0-2
- Rework conditionals

* Sun Nov 22 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.3.0-1
- Update to 0.3.0
- Build nautilus extension as additional package

* Wed Dec 31 2008 Christoph Wickert <cwickert@fedoraproject.org> - 0.2.1-1
- Initial package
