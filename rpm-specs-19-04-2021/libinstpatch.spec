# https://github.com/swami/libinstpatch/issues/34
#
# Since this has never worked, we do not have %%files entries for the result.
%bcond_with introspection

# Fails with
# CMake Error: Error required internal CMake variable not set, cmake may not be
#   built correctly.
# Missing variable is:
# CMAKE_FIND_LIBRARY_PREFIXES
#
# When/if this is fixed, we will probably want a -doc subpackage.
%bcond_with gtkdoc

Name:           libinstpatch
Version:        1.1.6
%global api_version 1.0
%global so_version 2
Release:        1%{?dist}
Summary:        Instrument file software library

URL:            http://www.swamiproject.org/
# The entire source is LGPLv2 except:
#
# Public Domain:
#   libinstpatch/md5.{c,h}
#   examples/*
#
License:        LGPLv2 and Public Domain
# Additionally, the following unused files are removed in %%prep:
#
# GPLv2:
#   utils/ipatch_convert.c
%global forgeurl https://github.com/swami/%{name}/
Source0:        %{forgeurl}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  ninja-build

BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(sndfile)
%if %{with gtkdoc}
# GTKDOC_ENABLED
BuildRequires:  pkgconfig(gtk-doc)
%endif
%if %{with introspection}
# INTROSPECTION_ENABLED
BuildRequires:  pkgconfig(gobject-introspection-1.0)
%endif

# This is a forked copy:
# Changed so as no longer to depend on Colin Plumb's `usual.h' header
# definitions; now uses stuff from dpkg's config.h.
#  - Ian Jackson <ijackson@nyx.cs.du.edu>.
# Josh Coalson: made some changes to integrate with libFLAC.
# Josh Green: made some changes to integrate with libInstPatch.
Provides:       bundled(md5-plumb)

%description
libInstPatch stands for lib-Instrument-Patch and is a library for processing
digital sample based MIDI instrument “patch” files. The types of files
libInstPatch supports are used for creating instrument sounds for wavetable
synthesis. libInstPatch provides an object framework (based on GObject) to load
patch files into, which can then be edited, converted, compressed and saved.


%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       glib2-devel%{?_isa}
Requires:       libsndfile-devel%{?_isa}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package doc
Summary:        Documentation and examples for %{name}
BuildArch:      noarch

%description doc
The %{name}-doc package contains documentation and examples for
%{name}.


%prep
%autosetup

# Remove example for nonexistent Python bindings
find examples -type f -name '*.py' -print -delete


%build
%cmake \
    -DGTKDOC_ENABLED:BOOL=%{?with_gtkdoc:ON}%{!?with_gtkdoc:OFF} \
    -DINTROSPECTION_ENABLED:BOOL=\
%{?with_introspection:ON}%{!?with_introspection:OFF} \
    -GNinja
%cmake_build

%install
%cmake_install


%files
%license COPYING
%doc ABOUT-NLS
%doc AUTHORS
%doc ChangeLog
%doc README.md
%doc TODO.tasks
%{_libdir}/%{name}-%{api_version}.so.%{so_version}
%{_libdir}/%{name}-%{api_version}.so.%{so_version}.*


%files devel
%doc examples
%{_includedir}/%{name}-%{so_version}
%{_libdir}/%{name}-%{api_version}.so
%{_libdir}/pkgconfig/%{name}-%{api_version}.pc


%changelog
* Fri Apr 16 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 1.1.6-1
- New upstream version 1.1.6 with so-version bump from 0 to 2 and altered
  include path
- Upstream tarball now comes from GitHub
- Build with ninja backend instead of make

* Fri Apr 16 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 1.0.0-24.20110806svn386
- Adjust whitespace and ordering to personal preference
- Drop obsolete ldconfig scriptlets
- Use much stricter file globs
- Change library BR’s to pkgconfig() format
- Use autosetup macro
- Correct License field from “LGPLv2+” to “LGPLv2 and GPLv2 and Public Domain”
- Add virtual Provides for bundled MD5 implementation
- Properly install license file
- Add ABOUT-NLS and TODO.tasks to doc files

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-23.20110806svn386
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 03 2020 Erich Eickmeyer <erich@ericheickmeyer.com> - 1.0.0-22.20110806svn386
- Fix for new cmake macros
- Resolves: #1864003

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-21.20110806svn386
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-20.20110806svn386
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-19.20110806svn386
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-18.20110806svn386
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-17.20110806svn386
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-16.20110806svn386
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-15.20110806svn386
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-14.20110806svn386
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-13.20110806svn386
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-12.20110806svn386
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-11.20110806svn386
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-10.20110806svn386
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-9.20110806svn386
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-8.20110806svn386
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-7.20110806svn386
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-6.20110806svn386
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-5.20110806svn386
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-4.20110806svn386
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Aug 07 2011 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 1.0.0-3.20110806svn386
- Include the COPYING file. oops.
- Fix main package Requires of the devel package

* Sat Aug 06 2011 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 1.0.0-2.20110806svn386
- Update to svn after upstream accepted our build patches, switched to cmake and fixed the licensing
- Prepare for submission for review

* Wed Oct 27 2010 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 1.0.0-1
- Update to 1.0.0

* Thu Mar 26 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 1.0.0-0.1.297svn
- Initial Fedora build
