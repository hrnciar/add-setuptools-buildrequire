%global sover 0.6

Name:           yaml-cpp
Version:        0.6.3
Release:        4%{?dist}
Summary:        A YAML parser and emitter for C++
License:        MIT 
URL:            https://github.com/jbeder/yaml-cpp
Source0:        https://github.com/jbeder/yaml-cpp/archive/%{name}-%{version}.tar.gz

Patch0:         CVE-2017-5950.patch

BuildRequires: make
BuildRequires:  cmake gcc gcc-c++

%description
yaml-cpp is a YAML parser and emitter in C++ written around the YAML 1.2 spec.


%package        devel
Summary:        Development files for %{name}
License:        MIT
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package        static
Summary:        Static library for %{name}
License:        MIT
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}

%description    static
The %{name}-static package contains the static library for %{name}.


%prep
%autosetup -p1 -n %{name}-%{name}-%{version}


%build
%cmake -B build_shared \
       -DYAML_CPP_BUILD_TOOLS=OFF \
       -DYAML_BUILD_SHARED_LIBS=ON \
       -DYAML_CPP_BUILD_TESTS=OFF \
       %{nil}
%make_build -C build_shared

%cmake -B build_static \
       -DYAML_CPP_BUILD_TOOLS=OFF \
       -DYAML_BUILD_SHARED_LIBS=OFF \
       -DYAML_CPP_BUILD_TESTS=OFF \
       %{nil}
%make_build -C build_static


%install
%make_install -C build_static yaml-cpp

# Move files so they don't get trampled
mv %{buildroot}%{_libdir}/cmake/%{name} \
   %{buildroot}%{_libdir}/cmake/%{name}-static
mv %{buildroot}%{_libdir}/pkgconfig/%{name}.pc \
   %{buildroot}%{_libdir}/pkgconfig/%{name}-static.pc


%make_install -C build_shared

%ldconfig_scriptlets


%files
%doc CONTRIBUTING.md README.md
%license LICENSE
%{_libdir}/*.so.%{sover}*

%files devel
%{_includedir}/yaml-cpp/
%{_libdir}/*.so
%{_libdir}/cmake/%{name}
%{_libdir}/pkgconfig/%{name}.pc

%files static
%license LICENSE
%{_libdir}/*.a
%{_libdir}/cmake/%{name}-static
%{_libdir}/pkgconfig/%{name}-static.pc


%changelog
* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 15 2019 Richard Shaw <hobbes1069@gmail.com> - 0.6.3-1
- Update to 0.6.3.

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 09 2019 Till Hofmann <thofmann@fedoraproject.org> - 0.6.2-2
- Remove unused boost dependency

* Sun Jun 09 2019 Till Hofmann <thofmann@fedoraproject.org> - 0.6.2-1
- Update to 0.6.2

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 24 2019 Jonathan Wakely <jwakely@redhat.com> - 0.6.1-5
- Rebuilt for Boost 1.69

* Sun Sep 16 2018 Richard Shaw <hobbes1069@gmail.com> - 0.6.1-4
- Add patch for CVE-2017-5950.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Apr 09 2018 Richard Shaw <hobbes1069@gmail.com> - 0.6.1-2
- Fixes improperly generated cmake config files, RHBZ#1558637.

* Sun Feb 18 2018 Richard Shaw <hobbes1069@gmail.com> - 0.6.1-1
- Update to 0.6.1.

* Sun Feb 11 2018 Richard Shaw <hobbes1069@gmail.com> - 0.6.0-1
- Update to 0.6.0.
- Add static library subpackage.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 31 2018 Richard Shaw <hobbes1069@gmail.com> - 0.5.3-9
- Install yaml cmake files, fixes RHBZ#1509421.

* Tue Jan 23 2018 Jonathan Wakely <jwakely@redhat.com> - 0.5.3-8
- Rebuilt for Boost 1.66

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 19 2017 Jonathan Wakely <jwakely@redhat.com> - 0.5.3-6
- Rebuilt for s390x binutils bug

* Tue Jul 04 2017 Jonathan Wakely <jwakely@redhat.com> - 0.5.3-5
- Rebuilt for Boost 1.64

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 Jonathan Wakely <jwakely@redhat.com> - 0.5.3-3
- Rebuilt for Boost 1.63
 
* Fri Jan 27 2017 Jonathan Wakely <jwakely@redhat.com> - 0.5.3-2
- Rebuilt for Boost 1.63

* Tue Aug 23 2016 Richard Shaw <hobbes1069@gmail.com> - 0.5.3-1
- Update to latest upstream release.

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jan 16 2016 Jonathan Wakely <jwakely@redhat.com> - 0.5.1-12
- Rebuilt for Boost 1.60

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 0.5.1-11
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-10
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 0.5.1-9
- rebuild for Boost 1.58

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.5.1-7
- Rebuilt for GCC 5 C++11 ABI change

* Thu Feb 26 2015 Guido Grazioli <guido.grazioli@gmail.com> - 0.5.1-6
- Rebuild for gcc switching default to -std=gnu11

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 0.5.1-5
- Rebuild for boost 1.57.0

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 Petr Machata <pmachata@redhat.com> - 0.5.1-2
- Rebuild for boost 1.55.0

* Thu Nov 14 2013 Richard Shaw <hobbes1069@gmail.com> - 0.5.1-1
- Update to latest upstream release.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Feb 10 2012 Richard Shaw <hobbes1069@gmail.com> - 0.3.0-1
- Update to latest release.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Sep 30 2011 Guido Grazioli <guido.grazioli@gmail.com> - 0.2.7-1
- Update to 0.2.7
- Remove gcc 4.6 patch fixed upstream

* Mon May 09 2011 Guido Grazioli <guido.grazioli@gmail.com> - 0.2.6-1
- Upstream 0.2.6

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Apr 02 2010 Guido Grazioli <guido.grazioli@gmail.com> - 0.2.5-1
- Upstream 0.2.5

* Fri Jan 15 2010 Guido Grazioli <guido.grazioli@gmail.com> - 0.2.4-1
- Upstream 0.2.4

* Sat Oct 17 2009 Guido Grazioli <guido.grazioli@gmail.com> - 0.2.2-2
- Remove duplicate file

* Wed Oct 14 2009 Guido Grazioli <guido.grazioli@gmail.com> - 0.2.2-1
- Initial packaging 
