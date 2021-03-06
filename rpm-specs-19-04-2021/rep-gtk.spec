Name:           rep-gtk
Version:        0.90.8.3
Release:        11%{?dist}
Summary:        GTK+ binding for librep Lisp environment
License:        GPLv2+
URL:            http://sawfish.wikia.com/
Source0:        http://download.tuxfamily.org/librep/%{name}/%{name}_%{version}.tar.bz2

BuildRequires: make
BuildRequires:  gtk2-devel
BuildRequires:  autoconf
BuildRequires:  libtool
BuildRequires:  librep-devel >= 0.90.5
Requires:       librep >= 0.90.5

%description
This is a binding of GTK+ for the librep Lisp interpreter. It is based
on Marius Vollmer's guile-gtk package (initially version 0.15, updated
to 0.17), with a new glue-code generator.

%package devel
Summary:        Development files for rep-gtk
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig

%description devel
Link libraries and C header files for librep development.

%prep
%setup -q -n %{name}_%{version}

%build
./autogen.sh --nocfg
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
find %{buildroot}%{_libdir} -name \*.la -exec rm '{}' \;

%files
%license COPYING
%doc NEWS README* TODO
%{_libdir}/rep/*

%files devel
%{_includedir}/rep-gtk/
%{_libdir}/pkgconfig/rep-gtk.pc

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.90.8.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.90.8.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.90.8.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.90.8.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.90.8.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.90.8.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.90.8.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.90.8.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.90.8.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.90.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Aug  5 2016 Kim B. Heino <b@bbbs.net> - 0.90.8.3-1
- Upgrade to 0.90.8.3

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.90.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.90.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Nov  4 2014 Kim B. Heino <b@bbbs.net> - 0.90.8.2-1
- Update to 0.90.8.2

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.90.8.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.90.8.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.90.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.90.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jan 17 2013 Kim B. Heino <b@bbbs.net> - 0.90.8.1-1
- Update to 0.90.8.1

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.90.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Mar 26 2012 Kim B. Heino <b@bbbs.net> - 0.90.8-1
- Update to 0.90.8

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.90.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.90.7-2
- Rebuild for new libpng

* Mon Aug 22 2011 Kim B. Heino <b@bbbs.net> - 0.90.7-1
- Update to 0.90.7

* Sun Jul 31 2011 Kim B. Heino <b@bbbs.net> - 0.90.6-2
- Update BR and R versions

* Sat Jul 30 2011 Kim B. Heino <b@bbbs.net> - 0.90.6-1
- Update to 0.90.6

* Wed Apr 20 2011 Kim B. Heino <b@bbbs.net> - 0.90.5-4
- don't use %%{_host} which can be modified by configure on non-x86 arches

* Wed Apr 13 2011 Kim B. Heino <b@bbbs.net> - 0.90.5-3
- Fix files list, remove post/postun

* Fri Apr  1 2011 Kim B. Heino <b@bbbs.net> - 0.90.5-2
- Fix dynamic loading

* Thu Mar 31 2011 Kim B. Heino <b@bbbs.net> - 0.90.5-1
- Update to 0.90.5

* Sat Sep 25 2010 Kim B. Heino <b@bbbs.net> - 0.90.4-1
- fix doc-files, url, misc fixes

* Sun Jan 10 2010 Kim B. Heino <b@bbbs.net> - 0.90.3-1
- fix devel package, fix rpmlint warnings

* Sat Sep 05 2009 Kim B. Heino <b@bbbs.net>
- add dist-tag

* Wed May 06 2009 Christopher Bratusek <zanghar@freenet.de>
- require gtk2 instead of gtk+
- add --libdir=_libdir to configure flags

* Mon May 04 2009 Christopher Bratusek <zanghar@freenet.de>
- fixup files section

* Sun Jan 18 2009 Christopher Bratusek <zanghar@freenet.de>
- several updates

* Thu Jan 01 2009 Christopher Bratusek <nano-master@gmx.de>
- drop -glade package
- drop -gnome package
- source archive is a .tar.bz2
- configure magic

* Tue Jun 13 2000 John Harper <john@dcs.warwick.ac.uk>
- use better macros

* Fri Sep 17 1999 John Harper <john@dcs.warwick.ac.uk>
- specify installdir when installing

* Tue Sep 14 1999 Aron Griffis <agriffis@bigfoot.com>
- 0.4 spec file update: added buildroot
