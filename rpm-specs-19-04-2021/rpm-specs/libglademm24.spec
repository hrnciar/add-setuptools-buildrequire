%global apiver 2.4
%global so_version 1

%bcond_without autoreconf

Name:           libglademm24
Version:        2.6.7
Release:        26%{?dist}
Summary:        C++ wrapper for libglade

License:        LGPLv2+
URL:            http://www.gtkmm.org/
Source0:        http://ftp.gnome.org/pub/GNOME/sources/libglademm/2.6/libglademm-%{version}.tar.bz2

BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  m4

%if %{with autoreconf}
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
%endif

BuildRequires:  gtkmm24-devel >= 2.6.0
BuildRequires:  libglade2-devel >= 2.6.1

%description
This package provides a C++ interface for libglademm. It is a
subpackage of the GTKmm project.  The interface provides a convenient
interface for C++ programmers to create Gnome GUIs with GTK+'s
flexible object-oriented framework.


%package devel
Summary:        Headers for developing programs that will use libglademm
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains the headers that programmers will need to develop
applications which will use libglademm, part of GTKmm, the C++ interface to the
GTK+.


%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch

%description    doc
Documentation for %{name}.


%prep
%setup -q -n libglademm-%{version}

%if %{with autoreconf}
# - AC_PROG_LIBTOOL is obsolete
# - Need some help finding m4 macros
# - Drop obsolete and unavailable GLIBMM_CHECK_PERL macro
#   (https://mail.gnome.org/archives/commits-list/2009-September/msg01850.html)
sed -r -i \
    -e 's/AC_PROG_LIBTOOL/LT_INIT/' \
    -e 's/(AC_CONFIG_)AUX(_DIR\(.*\))/\1AUX\2\n\1MACRO\2/' \
    -e 's/(GLIBMM_CHECK_PERL)/dnl \1/' \
    configure.in
%endif

# Note that the build system for the Doxygen documentation is too obsolete to
# easily rebuild it, so we use the pre-built documentation from the release
# tarball.


%build
%if %{with autoreconf}
AUTOHEADER=/bin/true autoreconf -fiv
%endif
%configure
%make_build


%install
%make_install
find %{buildroot} -type f -name '*.la' -print -delete

install -d %{buildroot}%{_pkgdocdir}
install -t %{buildroot}%{_pkgdocdir} -m 0644 \
    AUTHORS ChangeLog NEWS README
# The TODO file is omitted, as it is an empty file.
mv -v %{buildroot}%{_datadir}/doc/gnomemm-*/libglademm-%{apiver}/* \
    %{buildroot}%{_pkgdocdir}/


%files
%license COPYING
%{_libdir}/libglademm-%{apiver}.so.%{so_version}
%{_libdir}/libglademm-%{apiver}.so.%{so_version}.*


%files devel
%{_includedir}/libglademm-%{apiver}
%{_libdir}/libglademm-%{apiver}.so
%{_libdir}/libglademm-%{apiver}
%{_libdir}/pkgconfig/libglademm-%{apiver}.pc


%files doc
%license COPYING
%doc %{_pkgdocdir}
%doc %{_datadir}/devhelp/


%changelog
* Thu Feb 25 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 2.6.7-26
- Whitespace changes
- Drop obsolete %%ldconfig_scriptlets macro
- Use much stricter file globs
- Split documentation into a -doc subpackage
- Do install the devhelp book
- Rebuild autotools-generated files
- Drop unnecessary configure options: --disable-static is the default, and
  --enable-docs is not recognized
- Simplify find-and-remove command for unwanted .la files

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.7-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.7-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.7-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.7-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.7-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.7-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.7-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.7-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.7-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.7-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.7-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.7-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Apr 27 2015 Nils Philippsen <nils@redhat.com> - 2.6.7-13
- rebuild for C++11 ABI

* Thu Mar 19 2015 Devrim Gündüz <devrim@gunduz.org> - 2.6.7-12
- Rebuilt

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 2.6.7-5
- Rebuild for new libpng

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Sep 24 2008 Denis Leroy <denis@poolshark.org> - 2.6.7-1
- Update to upstream 2.6.7

* Mon Feb 11 2008 Denis Leroy <denis@poolshark.org> - 2.6.6-1
- Update to 2.6.6, bugfix

* Mon Sep 17 2007 Denis Leroy <denis@poolshark.org> - 2.6.4-1
- Update to 2.6.4
- License tag update

* Tue Oct 10 2006 Denis Leroy <denis@poolshark.org> - 2.6.3-2
- Added dist tag

* Mon Aug 28 2006 Denis Leroy <denis@poolshark.org> - 2.6.3-1
- Update to version 2.6.3

* Tue Feb 28 2006 Denis Leroy <denis@poolshark.org> - 2.6.2-1
- Update to version 2.6.2

* Fri Nov 25 2005 Denis Leroy <denis@poolshark.org> - 2.6.1-2
- Disable static libraries

* Mon Sep 19 2005 Denis Leroy <denis@poolshark.org> - 2.6.1-1
- Update to 2.6.1

* Thu Apr 28 2005 Denis Leroy <denis@poolshark.org> - 2.6.0-1
- Upgrade to 2.6.0

* Fri Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Mon Jun 27 2004 Denis Leroy <denis@poolshark.org> - 0:2.4.1-0.fdr.1
- Upgrade to 2.4.1
- Moved docs to regular directory, disabled devhelp

* Thu Sep 25 2003 Eric Bourque <ericb@computer.org>
- Initial build.
