Name:           dtkcore
Version:        5.4.0
Release:        1%{?dist}
Summary:        Deepin tool kit core modules
License:        LGPLv3+
URL:            https://github.com/linuxdeepin/dtkcore
%if 0%{?fedora}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
%else
Source0:        %{name}_%{version}.orig.tar.xz
%endif
BuildRequires:  gcc-c++
BuildRequires:  annobin
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(gsettings-qt)
BuildRequires:  make
# since f30
Obsoletes:      deepin-tool-kit <= 0.3.3
Obsoletes:      deepin-tool-kit-devel <= 0.3.3
Obsoletes:      dtksettings <= 0.1.7
Obsoletes:      dtksettings-devel <= 0.1.7

%description
Deepin tool kit core modules.

%package devel
Summary:        Development package for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       qt5-qtbase-devel%{?_isa}

%description devel
Header files and libraries for %{name}.

%prep
%autosetup -p1

%build
# help find (and prefer) qt5 utilities, e.g. qmake, lrelease
export PATH=%{_qt5_bindir}:$PATH
%qmake_qt5 PREFIX=%{_prefix} \
           DTK_VERSION=%{version} \
           LIB_INSTALL_DIR=%{_libdir} \
           BIN_INSTALL_DIR=%{_libexecdir}/dtk5 \
           TOOL_INSTALL_DIR=%{_libexecdir}/dtk5
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}

%files
%doc README.md
%license LICENSE
%{_libdir}/lib%{name}.so.5*
%dir %{_libexecdir}/dtk5/
%{_libexecdir}/dtk5/dtk-settings
%{_libexecdir}/dtk5/dtk-license.py
%{_libexecdir}/dtk5/dtk-translate.py
%{_libexecdir}/dtk5/deepin-os-release

%files devel
%doc doc/Specification.md
%{_includedir}/libdtk-*/
%{_qt5_archdatadir}/mkspecs/features/*.prf
%{_qt5_archdatadir}/mkspecs/modules/*.pri
%{_libdir}/cmake/Dtk/
%{_libdir}/cmake/DtkCore/
%{_libdir}/cmake/DtkCMake/
%{_libdir}/cmake/DtkTools/
%{_libdir}/pkgconfig/dtkcore.pc
%{_libdir}/lib%{name}.so
%{_datadir}/glib-2.0/schemas/*

%changelog
* Thu Mar 11 2021 Robin Lee <cheeselee@fedoraproject.org> - 5.4.0-1
- fix: 解析desktop文件中多国语言不支持短名 (liuyang)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.2.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Nov 27 2020 Robin Lee <cheeselee@fedoraproject.org> - 5.2.2.16-1
- new upstream release: 5.2.2.16

* Tue Sep 22 2020 Robin Lee <cheeselee@fedoraproject.org> - 5.2.2.15-1
- new upstream release: 5.2.2.15

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 05 2019 Robin Lee <cheeselee@fedoraproject.org> - 2.1.1-1
- Release 2.1.1

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.16.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 17 2019 Robin Lee <cheeselee@fedoraproject.org> - 2.0.16.1-1
- Update to 2.0.16.1

* Fri Mar 15 2019 Robin Lee <cheeselee@fedoraproject.org> - 2.0.9.17-2
- Obsoletes deepin-tool-kit and dtksettings

* Tue Feb 26 2019 Robin Lee <cheeselee@fedoraproject.org> - 2.0.9.17-1
- Update to 2.0.9.17

* Thu Jan 31 2019 mosquito <sensor.wen@gmail.com> - 2.0.9.15-1
- Update to 2.0.9.15

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.9.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 01 2019 Rex Dieter <rdieter@fedoraproject.org> - 2.0.9.11-2
- use %%_qt5_bindir, %%ldconfig-scriptlets
- -devel: own %%{_libdir}/cmake/Dtk* dirs
- %%files: less globs, explicitly list items related to ABI/API

* Wed Dec 12 2018 mosquito <sensor.wen@gmail.com> - 2.0.9.11-1
- Update to 2.0.9.11

* Thu Nov 29 2018 mosquito <sensor.wen@gmail.com> - 2.0.9.9-1
- Update to 2.0.9.9

* Fri Nov  9 2018 mosquito <sensor.wen@gmail.com> - 2.0.9.8-1
- Update to 2.0.9.8

* Sat Aug 25 2018 mosquito <sensor.wen@gmail.com> - 2.0.9-4
- Fix symbol

* Tue Jul 31 2018 Florian Weimer <fweimer@redhat.com> - 2.0.9-3
- Rebuild with fixed binutils

* Mon Jul 30 2018 Zamir SUN <zsun@fedoraproject.org> - 2.0.9-2
- Fix lrelease version
- Merge fix from mosquito https://github.com/FZUG/repo/commit/23905bd6e097f89f61ac93819f65365024096c24

* Wed Jul 25 2018 Zamir SUN <zsun@fedoraproject.org> - 2.0.9-1
- Update to 2.0.9

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 16 2018 mosquito <sensor.wen@gmail.com> - 2.0.6-1
- Update to 2.0.6

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Dec 28 2017 mosquito <sensor.wen@gmail.com> - 2.0.5.3-1
- Update to 2.0.5.3

* Mon Nov 27 2017 mosquito <sensor.wen@gmail.com> - 2.0.5.2-1
- Update to 2.0.5.2

* Tue Oct 17 2017 mosquito <sensor.wen@gmail.com> - 2.0.1-1
- Update to 2.0.1

* Sun Aug 20 2017 mosquito <sensor.wen@gmail.com> - 2.0.0-1
- Update to 2.0.0

* Sat Jul 29 2017 mosquito <sensor.wen@gmail.com> - 0.3.3-1
- Initial build
