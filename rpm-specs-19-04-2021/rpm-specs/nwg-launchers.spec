Name:           nwg-launchers
Version:        0.4.4
Release:        1%{?dist}
Summary:        GTK-based launchers for sway and other window managers

License:        GPLv3+
URL:            https://github.com/nwg-piotr/%{name}
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  meson

BuildRequires:  cmake(nlohmann_json)
BuildRequires:  pkgconfig(gtkmm-3.0)

%description
GTK-based launchers: application grid, button bar, menu, dmenu
for sway and other window managers.
The project priorities are:
 - it must work well on sway;
 - it should work as well as possible on Wayfire, i3, dwm and Openbox.


%prep
%autosetup -p1


%build
%meson
%meson_build


%install
%meson_install


# This set of application launchers is written for minimalistic keyboard-oriented
# environments and is not intended to be used with major DEs such as GNOME or KDE.
# Therefore, upstream does not provide .desktop files and we're not generating
# them downstream
%files
%license LICENSE
%doc README.md
%doc examples/nwgbar
%{_bindir}/nwgbar
%{_bindir}/nwgdmenu
%{_bindir}/nwggrid
%dir %{_datadir}/%{name}/
%{_datadir}/%{name}/nwgbar/
%{_datadir}/%{name}/nwgdmenu/
%{_datadir}/%{name}/nwggrid/


%changelog
* Sat Jan 30 2021 Aleksei Bavshin <alebastr@fedoraproject.org> - 0.4.4-1
- Update to 0.4.4

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 06 2021 Aleksei Bavshin <alebastr89@gmail.com> - 0.4.3-1
- Update to 0.4.3

* Fri Nov 06 2020 Aleksei Bavshin <alebastr89@gmail.com> - 0.4.2-1
- Update to 0.4.2

* Thu Nov 05 2020 Aleksei Bavshin <alebastr89@gmail.com> - 0.4.1-1
- Update to 0.4.1

* Tue Sep 22 2020 Aleksei Bavshin <alebastr89@gmail.com> - 0.4.0-1
- Update to 0.4.0

* Thu Sep 17 2020 Aleksei Bavshin <alebastr89@gmail.com> - 0.3.4-1
- Initial import (#1878898)
