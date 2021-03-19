%global apiver 2.6
%global so_version 1

%bcond_without autoreconf

Name:           gconfmm26
Version:        2.28.3
Release:        25%{?dist}
Summary:        C++ wrapper for GConf2

License:        LGPLv2+
URL:            https://gtkmm.org/
%global majmin %(echo %{version} | cut -d . -f -2)
Source0:        https://download.gnome.org/sources/gconfmm/%{majmin}/gconfmm-%{version}.tar.xz

# Do not wrap “#include <gconf/gconf-schema.h>” in “extern "C" {  }” to prevent
# “error: template with C linkage”
#
# See:
#   https://lists.fedoraproject.org/archives/list/
#     devel@lists.fedoraproject.org/thread/
#     J3P4TRHLWNDIKXF76OLYZNAPTABCZ3U5/#6QDPOFWECGRT42AQFD2IO6U33PN3K4GF
# as well as the discussion at:
#   https://gitlab.gnome.org/GNOME/glib/-/merge_requests/1935
#
# Note that gconfmm was archived in the migration to Gnome GitLab, and has been
# considered deprecated by upstream for ten years or so as of 2021, so there is
# no longer an upstream to receive such patches.
Patch0:         gconfmm26-2.28.3-no-extern-c-glib-includes.patch

BuildRequires:  gcc-c++
BuildRequires:  make

%if %{with autoreconf}
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  mm-common
%endif

BuildRequires:  pkgconfig(glibmm-2.4)
BuildRequires:  pkgconfig(gconf-2.0)

# For the documentation:
BuildRequires:  doxygen
BuildRequires:  perl-interpreter
BuildRequires:  perl(Getopt::Long)
# dot
BuildRequires:  graphviz
# xsltproc
BuildRequires:  libxslt
BuildRequires:  pkgconfig(mm-common-libstdc++)
BuildRequires:  pkgconfig(sigc++-2.0)
# Already a BR above:
#BuildRequires:  pkgconfig(glibmm-2.4)
BuildRequires:  pkgconfig(cairomm-1.0)
# Font specified for use in dot diagrams
BuildRequires:  font(freesans)

%description
This package provides a C++ interface for GConf2. It is a sub-package of the
GTKmm project. The interface provides a convenient interface for C++
programmers to create Gnome GUIs with GTK+'s flexible object-oriented
framework.


%package devel
Summary:        Headers for developing programs that will use gconfmm

Requires:       %{name}%{?_isa} = %{version}-%{release}

Requires:       glibmm24-devel%{?_isa}
Requires:       GConf2-devel%{?_isa}

%description devel
This package contains the headers that programmers will need to develop
applications which will use gconfmm, part of GTKmm, the C++ interface to the
GTK+.


%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch

Requires:       libstdc++-docs
Requires:       libsigc++20-doc
Requires:       glibmm24-doc
Requires:       cairomm-doc

%description    doc
Documentation for %{name} can be viewed either through the devhelp
documentation browser or through a web browser at
%{_datadir}/doc/gconfmm-%{apiver}/.


%prep
%autosetup -n gconfmm-%{version} -p1

# We want to rebuild the documentation, so we remove the pre-built
# documentation.
rm docs/reference/gconfmm-%{apiver}.devhelp2
rm docs/reference/gconfmm-%{apiver}.tag
rm -rf docs/reference/html

tmp="$(mktemp)"
for fn in AUTHORS README
do
  iconv --from=ISO-8859-1 --to=UTF-8 "$fn" > "${tmp}"
  touch -r "${fn}" "${tmp}"
  cp -p "${tmp}" "${fn}"
done
rm "${tmp}"

%if %{with autoreconf}
# AC_PROG_LIBTOOL is obsolete
sed -r -i 's/AC_PROG_LIBTOOL/LT_INIT/' configure.ac
%endif


%build
%if %{with autoreconf}
NOCONFIGURE=1 ./autogen.sh
%endif
%configure --enable-warnings=max
%make_build


%install
%make_install
find %{buildroot} -type f -name '*.la' -print -delete

install -t %{buildroot}%{_datadir}/doc/gconfmm-%{apiver} -m 0644 -p \
    AUTHORS ChangeLog NEWS README


%files
%license COPYING COPYING.LIB
%{_libdir}/libgconfmm-%{apiver}.so.%{so_version}
%{_libdir}/libgconfmm-%{apiver}.so.%{so_version}.*


%files devel
%{_includedir}/gconfmm-%{apiver}
%{_libdir}/gconfmm-%{apiver}
%{_libdir}/libgconfmm-%{apiver}.so
%{_libdir}/pkgconfig/gconfmm-%{apiver}.pc


%files doc
%license COPYING COPYING.LIB
%doc %{_datadir}/doc/gconfmm-%{apiver}/
%doc %{_datadir}/devhelp/


%changelog
* Thu Feb 25 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 2.28.3-25
- Switch URLs to HTTPS
- Switch from bz2 tarball to xz tarball

* Mon Feb 15 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 2.28.3-24
- Just use cairomm-doc, not cairomm1.0-doc, as a dependency, since cairomm will
  only provide the 1.0 API/ABI series after all; see
  https://src.fedoraproject.org/rpms/pangomm/pull-request/2 for discussion

* Sun Feb 14 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 2.28.3-23
- Improve comment about upstream status

* Sat Feb 13 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 2.28.3-22
- Whitespace and ordering changes
- Drop obsolete %%ldconfig_scriptlets macro
- Use much stricter file globs
- Properly install both necessary license files, and do so using the %%license
  macro
- Split documentation into a -doc subpackage
- Commit AUTHORS file to UTF-8
- Do not wrap “#include <gconf/gconf-schema.h>” in “extern "C" {  }” to prevent
  “error: template with C linkage”
- Switch library BR’s to pkgconfig(…), and drop unused gtkmm24 BR (and -devel
  dependency)
- Make -devel dependencies arch-specific
- Simplify find-and-remove command for unwanted .la files
- Do not remove the buildroot in %%install
- Drop “--disable-static --enable-shared” options to configure script, as these
  are the defaults anyway
- Use %%make_build/%%make_install macros
- Rebuild autotools-generated files
- Enable more compiler warnings
- Rebuild documentation rather than using the pre-built documentation from the
  source tarball
- Replace obsolete AC_PROG_LIBTOOL macro in configure.ac with LT_INIT
- BR FreeSans font for dot diagrams

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.28.3-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.28.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.28.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.28.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.28.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.28.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.28.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.28.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.28.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.28.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.28.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.28.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.28.3-9
- Rebuilt for GCC 5 C++11 ABI change

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.28.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.28.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.28.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.28.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 27 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.28.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.28.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Oct 26 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.28.3-2
- Rebuilt for glibc bug#747377

* Sat Oct 22 2011 Haïkel Guémar <hguemar@fedoraproject.org> - 2.28.3-1
- upstream 2.28.3
- fix documentation build with glibmm 2.28+

* Tue Oct 18 2011 Haïkel Guémar <hguemar@fedoraproject.org> - 2.28.2-3
- fix FTBFS (patch from kalev)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.28.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Sep 30 2010 Haïkel Guémar <hguemar@fedoraproject.org> - 2.28.2-1
- Update to upstream 2.28.2
- Rename spec file according guidelines
- Rpmlint fixes

* Fri Sep 25 2009 Denis Leroy <denis@poolshark.org> - 2.28.0-1
- Update to upstream 2.28.0

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.24.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.24.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Sep 24 2008 Denis Leroy <denis@poolshark.org> - 2.24.0-1
- Update to upstream 2.24.0

* Wed Mar 12 2008 Denis Leroy <denis@poolshark.org> - 2.22.0-1
- Update to upstream 2.22.0

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.20.0-2
- Autorebuild for GCC 4.3

* Mon Sep 17 2007 Denis Leroy <denis@poolshark.org> - 2.20.0-1
- Update to new stable 2.20.0

* Thu Mar 15 2007 Denis Leroy <denis@poolshark.org> - 2.18.0-1
- Update to Gnome 2.18, to follow GConf2 version

* Mon Aug 28 2006 Denis Leroy <denis@poolshark.org> - 2.16.0-2
- FE6 Rebuild

* Mon Aug 21 2006 Denis Leroy <denis@poolshark.org> - 2.16.0-1
- Update to 2.16.0

* Sun Jun 25 2006 Denis Leroy <denis@poolshark.org> - 2.14.2
- Update to 2.14.2
- Added dist postfix to release field

* Mon Mar 20 2006 Denis Leroy <denis@poolshark.org> - 2.14.0-1
- Update to 2.14.0

* Tue Feb 28 2006 Denis Leroy <denis@poolshark.org> - 2.12.0-3
- Rebuild

* Fri Nov 25 2005 Denis Leroy <denis@poolshark.org> - 2.12.0-2
- Removed static libraries

* Mon Sep 19 2005 Denis Leroy <denis@poolshark.org> - 2.12.0-1
- Update to 2.12.0

* Sat May  7 2005 Denis Leroy <denis@poolshark.org> - 2.10.0-2
- Added patch to fix x86_64 compile

* Thu Apr 28 2005 Denis Leroy <denis@poolshark.org> - 2.10.0-1
- Upgrade to 2.10.0
- Added patch to fix gcc4 warning

* Fri Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Mon Jun 27 2004 Denis Leroy <denis@poolshark.org> - 0:2.6.1-0.fdr.1
- Upgrade to 2.6.1

* Fri Oct 31 2003 Michael Koziarski <michael@koziarski.org> - 2.0.1-0.fdr.2
- Fix BuildRequires
- Add specific version numbers to GConf dependency.

* Sat Oct 18 2003 Michael Koziarski <michael@koziarski.org> - 2.0.1-0.fdr.1
- Initial RPM creation
