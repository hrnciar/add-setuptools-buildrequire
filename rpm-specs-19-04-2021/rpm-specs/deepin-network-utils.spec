%global repo dde-network-utils

%if 0%{?fedora}
Name:           deepin-network-utils
%else
Name:           %{repo}
%endif
Version:        5.3.0.8
Release:        1%{?dist}
Summary:        Deepin desktop-environment - network utils
License:        GPLv3
URL:            https://github.com/linuxdeepin/dde-network-utils
%if 0%{?fedora}
Source0:        %{url}/archive/%{version}/%{repo}-%{version}.tar.gz
%else
Source0:        %{name}_%{version}.orig.tar.xz
%endif

BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(dframeworkdbus)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  qt5-linguist
BuildRequires:  pkgconfig(gsettings-qt)
BuildRequires:  make
BuildRequires:  gio-qt-devel
BuildRequires:  gtest-devel

%description
Deepin desktop-environment - network utils.

%package devel
Summary:        Development package for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Header files and libraries for %{name}.

%prep
%autosetup -p1 -n %{repo}-%{version}
sed -i 's|/lib$|/%{_lib}|' dde-network-utils/dde-network-utils.pro

%build
# help find (and prefer) qt5 utilities, e.g. qmake, lrelease
export PATH=%{_qt5_bindir}:$PATH
%qmake_qt5 PREFIX=%{_prefix}
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}

%files
%doc README.md
%{_libdir}/lib*.so.1
%{_libdir}/lib*.so.1.*
%{_datadir}/%{repo}/

%files devel
%{_includedir}/libddenetworkutils/
%{_libdir}/pkgconfig/*.pc
%{_libdir}/lib*.so

%changelog
* Thu Mar 11 2021 Robin Lee <cheeselee@fedoraproject.org> - 5.3.0.8-1
- fix: wrong activeApInfo (zsien)
- fix: 修复已连接的网络与实际显示的不一致 (chenwei)
- Revert "fix: 解决控制中心刚开启网络页，wifi数据页为空的情况" (Zhang Qipeng)
- fix(networkmode): 修复了多次切换热点，概率出现热点模块被自动关闭问题 (Li Tao)
- feat: 添加单元测试代码 (chenwei)
- feat: Initial packit setup (Robin Lee)
- fix: fix lintian error (chenwei)
- fix: 任务栏网络信号值异常 (Xie Chuan)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Nov 10 2020 Robin Lee <cheeselee@fedoraproject.org> - 5.3.0.5-1
- new upstream release: 5.3.0.5

* Tue Sep 29 2020 Robin Lee <cheeselee@fedoraproject.org> - 5.1.0.2-1
- new upstream release: 5.1.0.2

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 05 2019 Robin Lee <cheeselee@fedoraproject.org> - 5.0.1-1
- Release 5.0.1

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 mosquito <sensor.wen@gmail.com> - 0.0.9-1
- Update to 0.0.9

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Dec 12 2018 mosquito <sensor.wen@gmail.com> - 0.0.8.1-1
- Update to 0.0.8.1

* Fri Nov  9 2018 mosquito <sensor.wen@gmail.com> - 0.0.7-1
- Update to 0.0.7

* Thu Aug  2 2018 mosquito <sensor.wen@gmail.com> - 0.0.4-1
- Update to 0.0.4

* Mon Jul 23 2018 mosquito <sensor.wen@gmail.com> - 0.0.3-1
- Initial package build
