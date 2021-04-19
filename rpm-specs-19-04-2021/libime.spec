Name:       libime  
Version:    1.0.6
License:    LGPLv2+ and MIT and BSD
Release:    1%{?dist}
Summary:    This is a library to support generic input method implementation
URL:        https://github.com/fcitx/libime
Source:     https://download.fcitx-im.org/fcitx5/%{name}/%{name}-%{version}_dict.tar.xz
Source1:    https://download.fcitx-im.org/fcitx5/%{name}/%{name}-%{version}_dict.tar.xz.sig
Source2:    https://pgp.key-server.io/download/0x8E8B898CBF2412F9

BuildRequires: gnupg2
BuildRequires: cmake
BuildRequires: ninja-build
BuildRequires: gcc-c++
BuildRequires: fcitx5-devel
BuildRequires: boost-devel
BuildRequires: extra-cmake-modules
BuildRequires: python3
BuildRequires: doxygen
BuildRequires: pkgconfig(zlib)
BuildRequires: pkgconfig(bzip2)
BuildRequires: pkgconfig(liblzma)
BuildRequires: pkgconfig(eigen3)
Requires:      %{name}-data


%description
This is a library to support generic input method implementation.

%package data
Summary:        Data files of %{name}
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       hicolor-icon-theme

%description data
The %{name}-data package provides shared data for %{name}.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       boost-devel%{?_isa}

%description devel
Development files for %{name}

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup

%build
%cmake -GNinja
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%license LICENSES/LGPL-2.1-or-later.txt src/libime/core/kenlm/LICENSE
%doc README.md 
%{_bindir}/%{name}_history
%{_bindir}/%{name}_pinyindict
%{_bindir}/%{name}_prediction
%{_bindir}/%{name}_slm_build_binary
%{_bindir}/%{name}_tabledict
%{_bindir}/%{name}_migrate_fcitx4_pinyin
%{_bindir}/%{name}_migrate_fcitx4_table
%{_libdir}/libIMECore.so.0
%{_libdir}/libIMEPinyin.so.0
%{_libdir}/libIMETable.so.0
# upstream's soname and soversion dont match 
# libxxx.so.X* won't work
%{_libdir}/libIMECore.so.*.*
%{_libdir}/libIMEPinyin.so.*.*
%{_libdir}/libIMETable.so.*.*
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/zh_CN.lm
%{_libdir}/%{name}/zh_CN.lm.predict

%files data
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*.dict

%files devel
%{_libdir}/libIMECore.so
%{_libdir}/libIMEPinyin.so
%{_libdir}/libIMETable.so
%{_libdir}/cmake/LibIME*
%{_includedir}/LibIME/



%changelog
* Fri Apr 02 2021 Qiyu Yan <yanqiyu@fedoraproject.org> - 1.0.6-1
- Update to 1.0.6 upstream release

* Mon Mar 22 2021 Qiyu Yan <yanqiyu@fedoraproject.org> - 1.0.5-1
- Update to 1.0.5 upstream release

* Sat Feb 20 2021 Qiyu Yan <yanqiyu@fedoraproject.org> - 1.0.4-1
- update to 1.0.4 upstream release

* Sat Feb 20 2021 Qiyu Yan <yanqiyu@fedoraproject.org> - 1.0.3-1
- update to 1.0.3 upstream release

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2021 Jonathan Wakely <jwakely@redhat.com> - 1.0.3-2
- Rebuilt for Boost 1.75

* Tue Jan 12 22:17:19 CST 2021 Qiyu Yan <yanqiyu@fedoraproject.org> - 1.0.3-1
- update to 1.0.3 upstream release

* Fri Dec  4 17:29:01 CST 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 1.0.2-1
- Update to 1.0.2 upstream release

* Thu Nov  5 16:32:15 CST 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 1.0.1-1
- update to 1.0.1 upstream release

* Tue Nov  3 18:22:05 CST 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 1.0.0-1
- update to 1.0.0 upstream release

* Sat Oct 31 22:11:47 CST 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 0-0.10
- update 
-  to libime commit 22106dcf1681f6a5135a2d7fd35a3775187ca111 

* Fri Oct 16 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 0-0.9
- update to upstream release\
- libime commit 4e2f0e853b9118d8d6d233d139e3b7c9112959b7
- kenlm commit a6e130e7854ffd5d75ba7b29ba2479e7ad3a9244

* Sat Sep 12 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 0-0.8
- Rebuild for fcitx5
- libime commit 32c4b3864c611126fda7a3e6d4e84a89bdf6b66a
- kenlm commit 01c49fe86714276f77be9278d00906fc994256c1

* Sat Aug 29 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 0-0.7.20200829git2aae1a9.s20200829git3ae116d
- update kenlm to commit 3ae116dec6b43555ca05a9c40a06293724768e05
- should fix those endian questions

* Sat Aug 29 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 0-0.6.20200829git2aae1a9.s20200812git96d303c
- fix missing dependences

* Sat Aug 29 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 0-0.5.20200829git2aae1a9.s20200812git96d303c
- upstream issue https://github.com/fcitx/fcitx5-chinese-addons/issues/33
- move some files to prefix/lib64
- bring libime-data back

* Fri Aug 28 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 0-0.4.20200822gitdff3ea6.s20200822git96d303c
- remove the -data package (endian makes the files different)

* Sat Aug 22 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 0-0.3.20200822gitdff3ea6.s20200822git96d303c
- upstream fix of testing on i686
- commit dff3ea6d1600166a5da65e4e7bee72fa8d595daa

* Sun Aug 16 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 0-0.2.20200811gita108d15.s20200811git96d303c
- rebuilt

* Wed Aug 12 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 0-0.1.20200811gita108d15.s20200811git96d303c
- initial package
