%bcond_without  tests
# disable shared libraries to avoid building libneovim-qt-gui.so
# it's only needed for devel package which we're not providing
%undefine       _cmake_shared_libs
%undefine       _cmake_in_source_build

Name:           neovim-qt
Version:        0.2.16.1
Release:        2%{?dist}
Summary:        Qt GUI for Neovim

# main source: ISC
# third-party/oxygen/*.svg: LGPLv3+ (#777)
License:        ISC and LGPLv3+
URL:            https://github.com/equalsraf/%{name}
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  make

BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(msgpack)
BuildRequires:  neovim
%if %{with tests}
BuildRequires:  xorg-x11-server-Xvfb
%endif

Requires:       hicolor-icon-theme
Requires:       neovim

%description
%{summary}.

%prep
%autosetup -p1

%build
%cmake \
    -DUSE_SYSTEM_MSGPACK:BOOL=ON  \
    -DENABLE_TESTS:BOOL=%{?with_tests:ON}%{!?with_tests:OFF}
%cmake_build

%install
%cmake_install

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/nvim-qt.desktop
%if %{with tests}
xvfb-run -a \
%make_build -C %{__cmake_builddir} check
%endif

%files
%license LICENSE
%doc README.md
%{_bindir}/nvim-qt
%{_datadir}/applications/nvim-qt.desktop
%{_datadir}/icons/hicolor/192x192/apps/nvim-qt.png
%{_datadir}/nvim-qt/

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.16.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Nov 07 2020 Aleksei Bavshin <alebastr89@gmail.com> - 0.2.16.1-1
- Initial import (#1891160)
