Name:      libnumbertext
Version:   1.0.6
Release:   2%{?dist}
Summary:   Number to number name and money text conversion library

#The entire source code is dual license LGPLv3+ or BSD, except for
#the data files hr.sor, sr.sor and sh.sor which are tri license
#CC-BY-SA or LGPLv3+ or BSD
License:   (LGPLv3+ or BSD) and (LGPLv3+ or BSD or CC-BY-SA)
URL:       https://github.com/Numbertext/libnumbertext
Source:    https://github.com/Numbertext/libnumbertext/releases/download/%{version}/libnumbertext-%{version}.tar.xz

BuildRequires: autoconf, automake, libtool, gcc-c++
BuildRequires: make

%description
Language-neutral NUMBERTEXT and MONEYTEXT functions for LibreOffice Calc

%package devel
Requires: libnumbertext = %{version}-%{release}
Summary: Files for developing with libnumbertext

%description devel
Includes and definitions for developing with libnumbertext

%prep
%autosetup -p1

%build
autoreconf -v --install --force
%configure --disable-silent-rules --disable-static --disable-werror --with-pic
%make_build

%check
make check

%install
rm -rf $RPM_BUILD_ROOT
%make_install
rm -f $RPM_BUILD_ROOT/%{_libdir}/*.la

%ldconfig_scriptlets

%files
%doc AUTHORS ChangeLog NEWS THANKS
%license COPYING
%{_bindir}/spellout
%{_libdir}/*.so.*
%{_datadir}/libnumbertext

%files devel
%{_includedir}/libnumbertext
%{_libdir}/pkgconfig/libnumbertext.pc
%{_libdir}/*.so

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 08 2020 Caolán McNamara <caolanm@redhat.com> - 1.0.6-1
- latest version

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 14 2020 Tom Stellard <tstellar@redhat.com> - 1.0.5-5
- Use make macros
- https://fedoraproject.org/wiki/Changes/UseMakeBuildInstallMacro

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 16 2018 Caolán McNamara <caolanm@redhat.com> - 1.0.5-1
- latest version

* Thu Aug 16 2018 Caolán McNamara <caolanm@redhat.com> - 1.0.3-1
- latest version

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 12 2018 Caolán McNamara <caolanm@redhat.com> - 1.0.2-3
- fix changelog order
- remove clean section
- set COPYING as license
- use LT_INIT

* Mon Jun 11 2018 Caolán McNamara <caolanm@redhat.com> - 1.0.2-2
- clarify extra license option of the sh/sr/hr data files

* Mon Jun 11 2018 Caolán McNamara <caolanm@redhat.com> - 1.0.2-1
- initial version
