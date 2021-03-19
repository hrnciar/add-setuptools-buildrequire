Name:           materia-kde
Version:        20201222
Release:        2%{?dist}
Summary:        Port of the popular GTK theme Materia for the Plasma 5 desktop

License:        GPLv3
URL:            https://github.com/PapirusDevelopmentTeam/materia-kde
Source0:        %url/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  make
Recommends:     %{name}-kvantum
Recommends:     %{name}-decorations
Recommends:     %{name}-konsole
Recommends:     %{name}-wallpapers
Recommends:     %{name}-yakuake
Recommends:     papirus-icon-theme

%description
This is a port of the popular GTK theme Materia for Plasma 5 desktop with a few
additions and extras.

In this package you'll find:

 - Aurorae Themes
 - Konsole Color Schemes
 - Kvantum Themes
 - Plasma Color Schemes
 - Plasma Desktop Themes
 - Plasma Look-and-Feel Settings
 - Wallpapers
 - Yakuake Skins

%package kvantum
Summary:    Materia-KDE Kvantum theme
Requires:   kvantum

%description kvantum
This is a port of the popular GTK theme Materia for Plasma 5 desktop with a few
additions and extras.

This package contains the MateriaDark and MateriaLight Kvantum theme.

%package decorations
Summary:    Materia-KDE Aurorae theme

%description decorations
This is a port of the popular GTK theme Materia for Plasma 5 desktop with a few
additions and extras.

This package contains the Aurorae window decorations.

%package konsole
Summary:    Materia-KDE Konsole theme

%description konsole
This is a port of the popular GTK theme Materia for Plasma 5 desktop with a few
additions and extras.

This package contains the MateriaDark Konsole theme.

%package wallpapers
Summary:    Materia-KDE wallpapers

%description wallpapers
This is a port of the popular GTK theme Materia for Plasma 5 desktop with a few
additions and extras.

This package contains the Materia wallpapers.

%package yakuake
Summary:    Materia-KDE Yakuake theme

%description yakuake
This is a port of the popular GTK theme Materia for Plasma 5 desktop with a few
additions and extras.

This package contains the Yakuake theme.

%prep
%autosetup

%build
# Nothing to build

%install
%make_install

%files
%license LICENSE
%doc README.md
%{_datadir}/color-schemes/*.colors
%{_datadir}/plasma/desktoptheme/Materia
%{_datadir}/plasma/desktoptheme/Materia-Color
%{_datadir}/plasma/look-and-feel/com.github.varlesh.materia
%{_datadir}/plasma/look-and-feel/com.github.varlesh.materia-dark
%{_datadir}/plasma/look-and-feel/com.github.varlesh.materia-light

%files decorations
%license LICENSE
%{_datadir}/aurorae/themes/Materia
%{_datadir}/aurorae/themes/Materia-Dark
%{_datadir}/aurorae/themes/Materia-Light

%files konsole
%license LICENSE
%{_datadir}/konsole/*.colorscheme

%files kvantum
%license LICENSE
%{_datadir}/Kvantum/Materia
%{_datadir}/Kvantum/MateriaDark
%{_datadir}/Kvantum/MateriaLight

%files wallpapers
%license LICENSE
%{_datadir}/wallpapers/Materia

%files yakuake
%license LICENSE
%{_datadir}/yakuake/skins/materia-dark
%{_datadir}/yakuake/skins/materia-light

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20201222-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan  1 21:01:18 CET 2021 Robert-André Mauchin <zebob.m@gmail.com> - 20201222-1
- Initial release
