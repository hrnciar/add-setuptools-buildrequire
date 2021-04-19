Name:          gr-hpsdr
URL:           https://github.com/Tom-McDermott/gr-hpsdr
Version:       1.2
Release:       21%{?dist}
License:       GPLv3+
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: gnuradio-devel
BuildRequires: cppunit-devel
BuildRequires: doxygen
BuildRequires: pybind11-devel
BuildRequires: boost-filesystem
BuildRequires: boost-system
BuildRequires: python3-devel
BuildRequires: log4cpp-devel
BuildRequires: gmp-devel
BuildRequires: orc-devel
BuildRequires: libunwind-devel
Summary:       GNU Radio modules for OpenHPSDR Hermes / Metis and Red Pitaya
Source0:       %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
# https://github.com/Tom-McDermott/gr-hpsdr/issues/6
Patch0:        gr-hpsdr-1.2-build-fix.patch
# https://github.com/Tom-McDermott/gr-hpsdr/issues/7
Patch1:        gr-hpsdr-1.2-soname-fix.patch
# https://github.com/Tom-McDermott/gr-hpsdr/pull/10
Patch2:        gr-hpsdr-1.2-swig-build-fix.patch
Patch3:        gr-hpsdr-1.2-gnuradio38.patch
# https://github.com/Tom-McDermott/gr-hpsdr/issues/16
# this patch is untested and probably uncomplete, it wasn't sent upstream
Patch4:        gr-hpsdr-1.2-gnuradio39.patch

%description
GNU Radio modules for OpenHPSDR Hermes / Metis and Red Pitaya using the
OpenHpsdr protocol.

%package devel
Summary:          Development files for gr-hpsdr
Requires:         %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for gr-hpsdr.

%package doc
Summary:          Documentation files for gr-hpsdr
Requires:         %{name} = %{version}-%{release}
BuildArch:        noarch

%description doc
Documentation files for gr-hpsdr.

%prep
%setup -q
%patch0 -p1 -b .build-fix
%patch1 -p1 -b .soname-fix
%patch2 -p1 -b .swig-build-fix
%patch3 -p1 -b .gnuradio38
%patch4 -p1 -b .gnuradio39

%build
%cmake -DENABLE_DOXYGEN=on -DGR_PKG_DOC_DIR=%{_docdir}/%{name}
%cmake_build

%install
%cmake_install

%ldconfig_scriptlets

%files
%exclude %{_docdir}/%{name}/html
%exclude %{_docdir}/%{name}/xml
%license license.txt
%doc README.md

%{_libdir}/*.so.*
%{python3_sitearch}/hpsdr
%{_datadir}/gnuradio/grc/blocks/*

%files devel
%{_includedir}/hpsdr
%{_libdir}/*.so

%files doc
%doc %{_docdir}/%{name}/html
%doc %{_docdir}/%{name}/xml

%changelog
* Thu Mar 25 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 1.2-21
- Rebuilt for new gnuradio

* Tue Feb 23 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 1.2-20
- Added support for gnuradio 3.9
  Resolves: rhbz#1923392
  Resolves: rhbz#1925571

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 24 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 1.2-18
- Rebuilt for new gnuradio

* Wed Aug  5 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 1.2-17
- Fixed FTBFS
  Resolves: rhbz#1863819

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-16
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.2-14
- Rebuilt for Python 3.9

* Tue Apr 14 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 1.2-13
- Rebuilt for new gnuradio

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 12 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 1.2-11
- Switched to Python 3
  Resolves: rhbz#1738960

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 24 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 1.2-9
- Rebuilt for new gnuradio

* Fri Mar 22 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 1.2-8
- Fixed FTBFS
  Resolves: rhbz#1675055

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 25 2019 Jonathan Wakely <jwakely@redhat.com> - 1.2-6
- Rebuilt for Boost 1.69

* Wed Jan  9 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 1.2-5
- Rebuilt for new gnuradio

* Thu Jul 19 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 1.2-4
- More fixes according to review

* Wed Jul  4 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 1.2-3
- More fixes according to review

* Wed Jul  4 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 1.2-2
- Various fixes according to review

* Tue Jul  3 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 1.2-1
- Initial version
