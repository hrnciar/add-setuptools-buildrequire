#
# This package is a static devel only, so no need for debuginfo
# It would just be empty as there are no executables or dynamic libs
#
%global debug_package %{nil}

Name:           libowfat
Version:        0.30
Release:        16%{?dist}
Summary:        Reimplementation of libdjb 
License:        GPLv2
URL:            http://www.fefe.de/libowfat/
Source0:        http://www.fefe.de/%{name}/%{name}-%{version}.tar.xz
BuildRequires:  gcc
BuildRequires: make

%description
This library is a reimplementation of libdjb, which means that it provides
Daniel Bernstein's interfaces (with some extensions).

It contains wrappers around memory allocation, buffered I/O, routines for
formatting and scanning, a full DNS resolver, several socket routines,
wrappers for socket functions, mkfifo, opendir, wait, and an abstraction
around errno. It also includes wrappers for Unix signal functions and a
layer of mmap and sendfile.

The library is available for use with the diet libc.

%package        devel
Summary:        Development files for %{name} (Static library only)
Provides:       %{name}-static = %{version}-%{release}
Provides:       %{name}-static%{?_isa} = %{version}-%{release}

%description    devel
This package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q
sed -i '/^CFLAGS/d;s/install -m/install -pm/g' GNUmakefile

%build
%make_build -f GNUmakefile CFLAGS="%{optflags} -I." 

%install
make -f GNUmakefile install \
        prefix="%{buildroot}%{_prefix}" \
        LIBDIR="%{buildroot}%{_libdir}" \
        INCLUDEDIR="%{buildroot}%{_includedir}/%{name}" \
        MAN3DIR="%{buildroot}%{_mandir}/man3"

%files devel
%doc README TODO CHANGES
%license COPYING
%{_libdir}/%{name}.a
%{_prefix}/include/%{name}/
%{_mandir}/man3/**

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.30-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.30-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.30-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.30-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.30-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jul 18 2018 Kevin Fenzi <kevin@scrye.com> - 0.30-11
- Fix FTBFS by adding BuildRequires: gcc

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.30-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.30-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.30-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.30-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.30-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.30-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Aug 10 2015 Christopher Meng <rpm@cicku.me> - 0.30-4
- Drop ldconfig scriptlet since it's only a static library.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.30-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri May 01 2015 Kevin Fenzi <kevin@scrye.com> 0.30-2
- Drop debuginfo and this time comment why it's dropped. 

* Fri May 01 2015 Kevin Fenzi <kevin@scrye.com> 0.30-1
- Update to 0.30

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.28-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.28-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.28-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.28-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.28-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.28-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.28-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Oct 24 2009 Simon Wesp <cassmodiah@edoraproject.org> - 0.28-4
- Rebuild without dietlibc usage
- No package (in Fedora-Repo) requires libowfat at this time

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.28-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Mar 19 2009 Simon Wesp <cassmodiah@fedoraproject.org> - 0.28-2
- Honor optflags
- Add parallel build
- Correct libdir paths for dietlibc-integration 
- Cosmetical Issues

* Tue Mar 17 2009 Simon Wesp <cassmodiah@fedoraproject.org> - 0.28-1
- New upstream release

* Sun Aug 24 2008 Simon Wesp <cassmodiah@fedoraproject.org> - 0.27-1
- Initial release
