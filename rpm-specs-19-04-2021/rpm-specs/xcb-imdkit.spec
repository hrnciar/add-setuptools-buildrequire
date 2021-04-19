Name:       xcb-imdkit
Version:    1.0.3
Release:    1%{?dist}
Summary:    Input method development support for xcb
# source files in src/xlibi18n use the "old style" MIT license known as NTP.
License:    LGPLv2 and MIT
URL:        https://github.com/fcitx/xcb-imdkit
Source:     https://download.fcitx-im.org/fcitx5/%{name}/%{name}-%{version}.tar.xz
Source1:    https://download.fcitx-im.org/fcitx5/%{name}/%{name}-%{version}.tar.xz.sig
Source2:    https://pgp.key-server.io/download/0x8E8B898CBF2412F9

BuildRequires:  gnupg2
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-keysyms)
BuildRequires:  pkgconfig(xcb-util)

%description
xcb-imdkit is an implementation of xim protocol in xcb, 
comparing with the implementation of IMDkit with Xlib, 
and xim inside Xlib, it has less memory foot print, 
better performance, and safer on malformed client.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Devel files for xcb-imdkit

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup

%build
%cmake
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%license LICENSES/LGPL-2.1-only.txt
%doc README.md
%{_libdir}/lib%{name}.so.1*

%files devel
%{_includedir}/xcb-imdkit/
%{_libdir}/cmake/XCBImdkit/
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/xcb-imdkit.pc

%changelog
* Mon Mar 22 2021 Qiyu Yan <yanqiyu@fedoraproject.org> - 1.0.3-1
- Update to 1.0.3 upstream release

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 13 10:48:01 CST 2021 Qiyu Yan <yanqiyu@fedoraproject.org> - 1.0.2-1
- update to 1.0.2 upstream release

* Sat Dec  5 00:34:45 CST 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 1.0.1-1
- Update to 1.0.1 upstream release
- Sobump libxcb-imdkit.so.0 -> libxcb-imdkit.so.1

* Tue Nov  3 18:28:22 CST 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 1.0.0-1
- update to 1.0.0 upstream release

* Fri Oct 16 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 0-0.4.20201016git33f5c35
- update to upstream commit
- commit 33f5c35daf543c0faac1041c2896306b82baff64

* Sun Aug 30 23:37:45 CST 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 0-0.3.20200811gitd6609a7
- rebuilt to push

* Sun Aug 16 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 0-0.2.20200811gitd6609a7
- Change according to review 

* Wed Aug 12 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 0-0.1.20200811gitd6609a7
- initial package

