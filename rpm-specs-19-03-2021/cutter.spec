%global __provides_exclude_from ^%{_libdir}/%{name}/module/.*\\.so$
%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

Summary: Unit Testing Framework for C/C++
Name: cutter
Version: 1.2.7
Release: 4%{?dist}
License: LGPLv3+
URL: http://cutter.sourceforge.net/
Source: http://downloads.sourceforge.net/cutter/cutter-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  gcc
BuildRequires: intltool
BuildRequires: glib2-devel
BuildRequires: libsoup-devel
BuildRequires: gtk2-devel
BuildRequires: autoconf
BuildRequires: make
Obsoletes:     %{name}-gstreamer < 1.2.3

# Disable inspect test case because of changed gdk_pixbuf_get_pixels
Patch0:	test-disable-gdk_pixbuf_get_pixels.patch
# Fix source code trace position
Patch1:	test-fix-position-in-trace.patch

%description
Cutter is a xUnit family Unit Testing Framework for C/C++.
Cutter provides easy to write test and easy to debug code environment.

%package devel
Summary:        Libraries and header files for Cutter development
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Libraries and header files for Cutter.
Cutter is a xUnit family Unit Testing Framework for C/C++.
Cutter provides easy to write test and easy to debug code environment.

%package gui
Summary:        GUI Test module for Cutter
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description gui
GUI Test module for Cutter.
Cutter is a xUnit family Unit Testing Framework for C/C++.
Cutter provides easy to write test and easy to debug code environment.

%package report
Summary:        PDF report module for Cutter
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description report
PDF report module for Cutter.
Cutter is a xUnit family Unit Testing Framework for C/C++.
Cutter provides easy to write test and easy to debug code environment.

%prep
%autosetup -p1 
# follow guide line: https://fedoraproject.org/wiki/Packaging:No_Bundled_Libraries
# bundled pcre library is required for older version of glib (2.12) only.
#rm -fr glib-compatible/pcre/*.{c,h}
# replace to proper directory
sed -i 's|/usr/local/share/doc/cutter|%{_pkgdocdir}|g' doc/cutter.man
sed -i 's|/usr/local/share/doc/cutter/ja|%{_pkgdocdir}|g' doc/cutter.jman

%build
autoconf
%configure --disable-bfd
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
sed -i -e 's| -shared | -Wl,--as-needed\0|g' libtool
V=1 make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
# remove needless config directory of sample. this one will be generated by autogen.sh.
# already fixed in upstream.
rm -fr %{buildroot}%{_datadir}/cutter/stack/config
find %{buildroot} -name '*.la' -delete
%find_lang %{name} --with-man --all-name

# Disabled tests until upstream fixes the issue https://github.com/clear-code/cutter/issues/27
%check
make check LD_LIBRARY_PATH=$(pwd)/cppcutter/.libs:$(pwd)/cutter/.libs:$(pwd)/gdkcutter-pixbuf/.libs:$(pwd)/soupcutter/.libs:$(pwd)/test/lib/.libs

%ldconfig_scriptlets

%files -f %{name}.lang
%doc README README.ja NEWS NEWS.ja TODO FEATURES FEATURES.ja TUTORIAL TUTORIAL.ja USERS USERS.ja license/fdl-1.3.txt license/lgpl-3.txt
%{_bindir}/*
%dir %{_libdir}/cutter
%dir %{_libdir}/cutter/module
%dir %{_libdir}/cutter/module/factory
%dir %{_libdir}/cutter/module/factory/loader-customizer
%dir %{_libdir}/cutter/module/factory/report
%dir %{_libdir}/cutter/module/factory/ui
%dir %{_libdir}/cutter/module/report
%dir %{_libdir}/cutter/module/ui
%{_libdir}/cutter/module/factory/loader-customizer/cpp-integration-factory.so
%{_libdir}/cutter/module/factory/report/xml_factory.so
%{_libdir}/cutter/module/factory/stream/
%{_libdir}/cutter/module/factory/ui/console_factory.so
%{_libdir}/cutter/module/loader-customizer/cpp-integration.so
%{_libdir}/cutter/module/report/xml.so
%{_libdir}/cutter/module/stream/
%{_libdir}/cutter/module/ui/console.so
%{_libdir}/libcutter.so.*
%{_libdir}/libcppcutter.so.*
%{_libdir}/libsoupcutter.so.*
%{_libdir}/libgdkcutter-pixbuf.so.*
%{_mandir}/man1/*
%dir %{_datadir}/cutter
%dir %{_datadir}/cutter/icons
%dir %{_datadir}/cutter/license
%{_datadir}/cutter/icons/*
%{_datadir}/cutter/license/*

%files devel
%dir %{_datadir}/gtk-doc/
%dir %{_datadir}/gtk-doc/html/
%doc %{_datadir}/gtk-doc/html/cutter/
%dir %{_includedir}/cutter
%{_includedir}/cutter/*
%{_libdir}/libcutter.so
%{_libdir}/libcppcutter.so
%{_libdir}/libsoupcutter.so
%{_libdir}/libgdkcutter-pixbuf.so
%{_libdir}/pkgconfig/*
%{_datadir}/aclocal/*
%dir %{_datadir}/cutter
%dir %{_datadir}/cutter/stack
%{_datadir}/cutter/stack/*

%files gui
%{_libdir}/cutter/module/factory/ui/gtk_factory.so
%{_libdir}/cutter/module/ui/gtk.so
%dir %{_datadir}/cutter/ui
%{_datadir}/cutter/ui/*

%files report
%{_libdir}/cutter/module/factory/report/pdf_factory.so
%{_libdir}/cutter/module/report/pdf.so

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 3 2019 Kentaro hayashi <hayashi@clear-code.com> - 1.2.7-1
- New upstream release.

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Oct 05 2017 Kentaro Hayashi <hayashi@clear-code.com> - 1.2.6-1
- New upstream release.
- Drop needless patch files.
  fix-conflicting-types-of-remove.patch
  cppcutter-stop-to-use-inline-instance-method-in-dest.patch
- Enable test again.

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jun 17 2017 Filipe Rosset <rosset.filipe@gmail.com> - 1.2.5-5
- Rebuilt to fix FTBFS rhbz#1423320 (disabled tests)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Aug 12 2016 Kentaro Hayashi <hayashi@clear-code.com> - 1.2.5-3
- Add fix-conflicting-types-of-remove.patch to fix FTBFS on F25.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 20 2016 HAYASHI Kentaro <hayashi@clear-code.com> - 1.2.5-1
- New upstream release.
  Removed needless all patches which are introduced at 1.2.4-4.
- Apply patch (cppcutter-stop-to-use-inline-instance-method-in-dest.patch)
  to fix test failure about cppcutter.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Feb 13 2015 HAYASHI Kentaro <hayashi@clear-code.com> - 1.2.4-4
- Fix FTBFS on F-21 and above (#1182957).
  Reported by Mamoru Tasaka.
  Add support-gdk-pixbuf-2.31.0-or-later.patch to fix it.
- Fix to support newer version of GLib error message
  Add support-g-key-file-error-quark-2.43-or-later-message.patch
- Add patches to fix crash test_limit_block bug.
  test-ensure-dropping-source-ID-when-callback-is-removed.patch
  gcut-egg-fix-a-bug-that-source-is-removed-twice.patch
  gcut-egg-fix-a-bug-that-timeout-source-is-removed-twice.patch

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 29 2014 HAYASHI Kentaro <hayashi@clear-code.com> - 1.2.4-1
- New upstream release.

* Fri Feb 28 2014 HAYASHI Kentaro <hayashi@clear-code.com> - 1.2.3-2
- Add missing Obsolete: for dropped gstreamer package (#1070967).

* Mon Feb 10 2014 HAYASHI Kentaro <hayashi@clear-code.com> - 1.2.3-1
- New upstream release.
- Remove needless patches(Patch0 and Patch1). These patches are already merged into Cutter 1.2.3.
- Drop gstreamer package support.

* Thu Dec 12 2013 Ville Skyttä <ville.skytta@iki.fi> - 1.2.2-6
- Fix doc paths in man pages when doc dir is unversioned (#993715).

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jan 30 2013 HAYASHI Kentaro <hayashi@clear-code.com> - 1.2.2-4
- remove needless %%defattr.
- remove needless Requires:.
- aggregate redundant %%dir ownership to cutter base package.
- update gstreamer package description.
- don't export private module soname.
- remove unused shared library dependency.

* Tue Jan 15 2013 HAYASHI Kentaro <hayashi@clear-code.com> - 1.2.2-3
- update packages Summary: section.
- change Group: from Development/Tools to Development/Libraries.
- remove needless BuiltRoot: tag.
- add arch-specific macro to Requires: tag.
- remove needless %%clean.
- add license file to %%doc.
- collect manual pages by %%find_lang additional option.
- remove bundled pcre library explicitly.
- fix default doc directory path in manual page.
- split gtk related module into -gui subpackage.
- add %%check section.
- split pdf related module into -report subpackage.
- split gstreamer related module into -gstreamer subpackage.

* Tue Dec 18 2012 HAYASHI Kentaro <hayashi@clear-code.com> - 1.2.2-2
- split libraries and header files into devel package

* Mon Dec 17 2012 HAYASHI Kentaro <hayashi@clear-code.com> - 1.2.2-1
- fix rpmlint issues
- follow fedora packaging guidelines

* Mon Oct 29 2012 HAYASHI Kentaro <hayashi@clear-code.com> - 1.2.2-0
- new upstream release.

* Wed Aug 15 2012 HAYASHI Kentaro <hayashi@clear-code.com> - 1.2.1-0
- new upstream release.

* Sat Dec 31 2011 Kouhei Sutou <kou@clear-code.com> - 1.2.0-0
- new upstream release.

* Sat Oct 22 2011 Kouhei Sutou <kou@clear-code.com> - 1.1.9-0
- new upstream release.

* Sun Jul 31 2011 Kouhei Sutou <kou@clear-code.com> - 1.1.8-0
- new upstream release.

* Sun Feb 13 2011 Kouhei Sutou <kou@clear-code.com> - 1.1.7-0
- new upstream release.

* Wed Feb 09 2011 Kouhei Sutou <kou@clear-code.com> - 1.1.6-0
- new upstream release.

* Mon Sep 06 2010 Kouhei Sutou <kou@clear-code.com>
- (1.1.5-0)
- new upstream release

* Thu Jun 10 2010 Kouhei Sutou <kou@clear-code.com>
- (1.1.4-0)
- new upstream release

* Tue Apr 13 2010 Kouhei Sutou <kou@clear-code.com>
- (1.1.3-0)
- new upstream release

* Sat Apr 03 2010 Kouhei Sutou <kou@clear-code.com>
- (1.1.2-0)
- new upstream release

* Wed Mar 3 2010 Kouhei Sutou <kou@clear-code.com>
- (1.1.1-0)
- new upstream release

* Tue Nov 3 2009 Kouhei Sutou <kou@clear-code.com>
- (1.1.0-0)
- new upstream release

* Tue Oct 20 2009 Kouhei Sutou <kou@clear-code.com>
- (1.0.9-0)
- new upstream release

* Sat Aug 29 2009 Kouhei Sutou <kou@clear-code.com>
- (1.0.8-0)
- new upstream release

* Thu May 21 2009 Kouhei Sutou <kou@clear-code.com>
- (1.0.7-1)
- initial RPM