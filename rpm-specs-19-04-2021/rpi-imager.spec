Name:           rpi-imager
Version:        1.6.1
Release:        1%{?dist}
Summary:        Graphical user-interface to write disk images and format SD cards

License:        ASL 2.0
URL:            https://github.com/raspberrypi/%{name}
Source0:        %{URL}/archive/v%{version}/%{name}.tar.gz#/%{name}-%{version}.tar.gz

# Needed to validate the desktop and metainfo files
BuildRequires:  libappstream-glib
BuildRequires:  desktop-file-utils

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  cmake
BuildRequires:  libarchive-devel
BuildRequires:  libcurl-devel
BuildRequires:  openssl-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtquickcontrols2-devel
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  qt5-linguist

Requires:       udisks2
Requires:       hicolor-icon-theme

%description
Graphical user-interface to download and write Raspberry Pi disk images, or
write custom disk images and format SD cards.

%prep
%autosetup

%build
%cmake .
%cmake_build

%install
%cmake_install
desktop-file-install \
    --add-category="X-GNOME-Utilities" \
    %{buildroot}%{_datadir}/applications/%{name}.desktop

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.metainfo.xml

%files
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_metainfodir}/%{name}.metainfo.xml
%license license.txt
%doc README.md

%changelog
* Thu Apr 08 2021 K. de Jong <keesdejong@fedoraproject.org> - 1.6.1-1
- New upstream release

* Fri Mar 19 2021 K. de Jong <keesdejong@fedoraproject.org> - 1.6-1
- First release
- Applied patch to fix custom disk image selection menu, for more info
please check: https://github.com/raspberrypi/rpi-imager/issues/159
