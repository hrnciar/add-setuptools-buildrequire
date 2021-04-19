%global forgeurl https://github.com/CarVac/librtprocess
%global commit bc2f53bc041478ff6d8c804940fcd8611c731a87

%forgemeta

Name:           librtprocess
Version:        0.12.0
Release:        1%{?dist}
Summary:        RawTherapee's processing algorithms

License:        GPLv3
URL:            %{forgeurl}
Source0:        %{forgesource}

# Fix build with GCC11
Patch100:       librtprocess-0.12.0-gcc11.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  make

%description
This is a project that aims to make some of RawTherapee's highly optimized
raw processing routines readily available for other FOSS photo editing
software.
The goal is to move certain source files from RawTherapee into this library.
Thus, any changes to the source can be done here and will be used by the
projects which use librtprocess.


%package devel
Summary:        Libraries, includes, etc. used to develop an application with librtprocess
License:        GPLv3
Requires:       %{name}%{_isa} = %{version}-%{release}

%description devel
These are the files needed to develop an application using librtprocess.


%prep
%forgeautosetup -p1


%build
%cmake
%cmake_build


%install
%cmake_install


%files
%license LICENSE.txt
%doc README.md
%{_libdir}/*.so.0
%{_libdir}/*.so.0.0.1

%files devel
%{_includedir}/rtprocess
%{_libdir}/*.so
%{_libdir}/pkgconfig/rtprocess.pc
%{_libdir}/cmake/rtprocess/


%changelog
* Sun Mar 07 2021 Mattia Verga <mattia.verga@protonmail.com> - 0.12.0-1
- Initial import
