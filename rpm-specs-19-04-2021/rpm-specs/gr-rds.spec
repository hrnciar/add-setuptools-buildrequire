%global git_commit 649bb528fe721242d7ec64d2ef2f56e0030e286e
%global git_date 20191111

%global git_short_commit %(echo %{git_commit} | cut -c -8)
%global git_suffix %{git_date}git%{git_short_commit}

Name:           gr-rds
Version:        1.1.0
Release:        18.%{git_suffix}%{?dist}
Summary:        GNU Radio FM RDS Receiver
License:        GPLv3+
URL:            https://github.com/bastibl/gr-rds
Source0:        https://github.com/bastibl/%{name}/archive/%{git_commit}/%{name}-%{git_suffix}.tar.gz
# https://github.com/bastibl/gr-rds/pull/34
Patch0:         gr-rds-1.1.0-boost173.patch
# https://github.com/bastibl/gr-rds/issues/41
# https://github.com/bastibl/gr-rds/pull/42
Patch1:         gr-rds-1.1.0-gnuradio39.patch
BuildRequires:  gnuradio-devel
BuildRequires:  pybind11-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  python3-devel
BuildRequires:  log4cpp-devel
BuildRequires:  gmp-devel
BuildRequires:  orc-devel
BuildRequires:  libunwind-devel
Requires:       gr-osmosdr

%description
%{summary}.


%package devel
Summary:          Development files for gr-rds
Requires:         %{name}%{?_isa} = %{version}-%{release}

%description devel
%{summary}.


%package doc
Summary:        Documentation files for gr-rds
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description doc
%{summary}.


%prep
%autosetup -p1 -n %{name}-%{git_commit}


%build
%cmake -DENABLE_DOXYGEN=off -DGR_PKG_DOC_DIR=%{_docdir}/%{name}
%cmake_build


%install
%cmake_install

mkdir -p %{buildroot}%{_docdir}/%{name}/examples
install -p -m 644 examples/* %{buildroot}%{_docdir}/%{name}/examples


%files
%doc README.md
%{_libdir}/libgnuradio-rds*.so.*
%{python3_sitearch}/rds/
%{_datadir}/gnuradio/grc/blocks/rds_*.yml

%files devel
%{_includedir}/rds/
%{_libdir}/libgnuradio-rds*.so
%{_libdir}/cmake/rds/*.cmake

%files doc
%doc %{_docdir}/%{name}/examples

%changelog
* Fri Apr  9 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 1.1.0-18.20191111git649bb528
- Updated gnuradio-3.9 patch from the upstream PR

* Thu Mar 25 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 1.1.0-17.20191111git649bb528
- Rebuilt for new gnuradio

* Wed Feb 24 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 1.1.0-16.20191111git649bb528
- Added support for gnuradio-3.9 (experimental, untested)
  Resolves: rhbz#1923613
  Resolves: rhbz#1925573

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-15.20191111git649bb528
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 24 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 1.1.0-14.20191111git649bb528
- Rebuilt for new gnuradio

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-13.20191111git649bb528
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-12.20191111git649bb528
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.1.0-11.20191111git649bb528
- Rebuilt for Python 3.9

* Tue Apr 14 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 1.1.0-10.20191111git649bb528
- Rebuilt for new gnuradio

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-9.20191111git649bb528
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 12 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 1.1.0-8.20191111git649bb528
- New version
- Switched to Python 3
  Resolves: rhbz#1738957

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 24 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 1.1.0-6
- Rebuilt for new gnuradio

* Thu Jan 31 2019 Kalev Lember <klember@redhat.com> - 1.1.0-5
- Rebuilt for Boost 1.69

* Wed Jan  9 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 1.1.0-4
- Rebuilt for new gnuradio

* Wed Jul 18 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 1.1.0-3
- Rebuilt for new gnuradio

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 18 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 1.1.0-1
- New version
- Dropped gcc6 patch (not needed)

* Mon Jun 18 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.32.20150513git201f32b
- Rebuilt for new gnuradio
- Disabled parallel build

* Tue Feb  6 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.31.20150513git201f32b
- Rebuilt for new boost

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.30.20150513git201f32b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.29.20150513git201f32b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 21 2017 Kalev Lember <klember@redhat.com> - 0-0.28.20150513git201f32b
- Rebuilt for Boost 1.64

* Wed May 24 2017 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.27.20150513git201f32b
- Rebuilt for new gnuradio

* Tue Feb 21 2017 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.26.20150513git201f32b
- Rebuilt for new gr-osmosdr

* Wed Feb 08 2017 Kalev Lember <klember@redhat.com> - 0-0.25.20150513git201f32b
- Rebuilt for Boost 1.63

* Fri Sep 16 2016 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.24.20150513git201f32b
- Rebuilt for new gnuradio

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.23.20150513git201f32b
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon Jul 04 2016 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.22.20150513git201f32b
- Rebuilt for new gnuradio

* Wed Feb 10 2016 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.21.20150513git201f32b
- Rebuilt for new gnuradio

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.20.20150513git201f32b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Feb 02 2016 Jonathan Wakely <jwakely@redhat.com> - 0-0.19.20150513git201f32b
- Patched for GCC 6 compatibility

* Mon Jan 18 2016 Jonathan Wakely <jwakely@redhat.com> - 0-0.18.20150513git201f32b
- Rebuilt for Boost 1.60

* Mon Jan 04 2016 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.17.20150513git201f32b
- Rebuilt for new gnuradio

* Tue Dec 15 2015 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.16.20150513git201f32b
- Rebuilt for new gnuradio

* Mon Nov 23 2015 Dan Horák <dan@danny.cz> - 0-0.15.20150513git201f32b
- updated to new snapshot with cleaned BRs

* Thu Nov  5 2015 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.14.20141117gitff1ca15
- Rebuilt for new gnuradio

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 0-0.13.20141117gitff1ca15
- Rebuilt for Boost 1.59

* Thu Aug 13 2015 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.12.20141117gitff1ca15
- Rebuilt for new gnuradio

* Mon Aug 03 2015 Dan Horák <dan@danny.cz> - 0-0.11.20141117gitff1ca15
- rebuild for boost 1.58

* Tue Jul 28 2015 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.10.20141117gitff1ca15
- Rebuilt for new gnuradio

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.9.20141117gitff1ca15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 16 2015 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.8.20141117gitff1ca15
- Rebuilt for new gnuradio

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0-0.7.20141117gitff1ca15
- Rebuilt for GCC 5 C++11 ABI change

* Sat Mar  7 2015 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.6.20141117gitff1ca15
- rebuilt for new gnuradio

* Fri Feb  6 2015 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.5.20141117gitff1ca15
- rebuilt for new boost

* Thu Nov 20 2014 Dan Horák <dan@danny.cz> - 0-0.4.20141117gitff1ca15
- updated to git ff1ca15 (20141117)

* Sat Nov 15 2014 Dan Horák <dan@danny.cz> - 0-0.3.20141024gitc3b1c31
- updated to git c3b1c31 (20141024)
- switched to standard github Source
- added docs and devel subpackages
- fix issues from review

* Tue Oct 21 2014 Dan Horák <dan@danny.cz> - 0-0.2.20141006git841b6307
- updated to git 841b6307 (20141006)

* Sun Sep 14 2014 Dan Horák <dan@danny.cz> - 0-0.1.20140823gitd11ece06
- initial Fedora version
