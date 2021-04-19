Name:           osmpbf
Version:        1.5.0
Release:        3%{?dist}
Summary:        C library to read and write OpenStreetMap PBF files

License:        LGPLv3
URL:            https://github.com/openstreetmap/OSM-binary
Source0:        https://github.com/openstreetmap/OSM-binary/archive/v%{version}/OSM-binary-%{version}.tar.gz

BuildRequires:  cmake make gcc-c++
BuildRequires:  protobuf-devel protobuf-java protobuf-compiler
BuildRequires:  maven-local maven-source-plugin maven-javadoc-plugin

%description
Osmpbf is a Java/C library to read and write OpenStreetMap PBF files.
PBF (Protocol buffer Binary Format) is a binary file format for OpenStreetMap
data that uses Google Protocol Buffers as low-level storage.

%package tools
Summary:        Tools for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description tools
This package contains tools that use %{name}.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains libraries and header files for
developing applications that use %{name}.

%package java
Summary:        Java OpenStreetMap PBF file format library
BuildArch:      noarch

%description java
Osmpbf is a Java/C library to read and write OpenStreetMap PBF files.
PBF (Protocol buffer Binary Format) is a binary file format for OpenStreetMap
data that uses Google Protocol Buffers as low-level storage.

%package javadoc
Summary:        Javadoc for %{name}
BuildArch:      noarch

%description javadoc
This package contains javadoc for %{name}.


%prep
%autosetup -p 1 -n OSM-binary-%{version}
%pom_remove_plugin :protobuf-maven-plugin
%pom_remove_plugin :maven-gpg-plugin


%build
%cmake
%cmake_build
protoc --java_out=src.java src/osmformat.proto
protoc --java_out=src.java src/fileformat.proto
%mvn_build


%install
%cmake_install
rm %{buildroot}/%{_libdir}/libosmpbf.a
%mvn_install


%files
%doc README.md CHANGELOG.md
%license LICENSE
%{_libdir}/libosmpbf.so.1
%{_libdir}/libosmpbf.so.1.*


%files tools
%{_bindir}/*
%{_mandir}/man1/*


%files devel
%{_includedir}/osmpbf
%{_libdir}/libosmpbf.so


%files java -f .mfiles
%license LICENSE


%files javadoc -f .mfiles-javadoc
%license LICENSE


%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 13 16:40:23 CET 2021 Adrian Reber <adrian@lisas.de> - 1.5.0-2
- Rebuilt for protobuf 3.14

* Wed Jan  6 2021 Tom Hughes <tom@compton.nu> - 1.5.0-1
- Update to 1.5.0 upstream release

* Sun Oct 25 2020 Tom Hughes <tom@compton.nu> - 1.4.0-1
- Update to 1.4.0 upstream release

* Thu Sep 24 2020 Adrian Reber <adrian@lisas.de> - 1.3.3-23.20150712git17fd0cc
- Rebuilt for protobuf 3.13

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-22.20150712git17fd0cc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 11 2020 Jiri Vanek <jvanek@redhat.com> - 1.3.3-21.20150712git17fd0cc
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Sun Jun 21 2020 Adrian Reber <adrian@lisas.de> - 1.3.3-20.20150712git17fd0cc
- Rebuilt for protobuf 3.12

* Sun Jun 14 2020 Adrian Reber <adrian@lisas.de> - 1.3.3-19.20150712git17fd0cc
- Rebuilt for protobuf 3.12

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-18.20150712git17fd0cc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-17.20150712git17fd0cc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-16.20150712git17fd0cc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-15.20150712git17fd0cc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Feb 18 2018 Tom Hughes <tom@compton.nu> - 1.3.3-14.20150712git17fd0cc
- Require gcc-c++

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-13.20150712git17fd0cc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 30 2018 Tom Hughes <tom@compton.nu> - 1.3.3-12.20150712git17fd0cc
- Drop ldconfig scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-11.20150712git17fd0cc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-10.20150712git17fd0cc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-9.20150712git17fd0cc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-8.20150712git17fd0cc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Aug 16 2015 Eduardo Mayorga Téllez <mayorga@fedoraproject.org> - 1.3.3-7.20150712git17fd0cc
- Package the Java library

* Wed Jul 22 2015 Tom Hughes <tom@compton.nu> - 1.3.3-6.20150712git17fd0cc
- Don't link to protobuf so user can choose protobuf-lite instead
- Drop protobuf-devel require for the same reason

* Sun Jul 12 2015 Tom Hughes <tom@compton.nu> - 1.3.3-5.20150712git17fd0cc
- Update to new upstream snapshot, dropping merged patch
- Require protobuf-devel in devel package

* Tue Jun 23 2015 Tom Hughes <tom@compton.nu> - 1.3.3-4.20150608git3730430
- Add text of GPLv3

* Tue Jun 23 2015 Tom Hughes <tom@compton.nu> - 1.3.3-3.20150608git3730430
- Fix base package require in devel package

* Tue Jun 16 2015 Tom Hughes <tom@compton.nu> - 1.3.3-2.20150608git3730430
- Install shared library with execute permission
- Link shared library against protobuf
- Correct soname

* Mon Jun  8 2015 Tom Hughes <tom@compton.nu> - 1.3.3-1.20150608git3730430
- Initial build
