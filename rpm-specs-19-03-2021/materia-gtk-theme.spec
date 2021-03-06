# WIP: split into sub packages

%global vergit 20200916

Name:           materia-gtk-theme
Version:        0.0.%{vergit}
Release:        3%{?dist}
Summary:        Material Design theme for GNOME/GTK based desktop environments
BuildArch:      noarch

License:        GPLv2
URL:            https://github.com/nana-4/materia-theme
Source0:        %{url}/archive/v%{vergit}/%{name}-%{version}.tar.gz

# Not possible to compile with `alpha`, `beta` new GNOME versions.
# https://github.com/nana-4/materia-theme/issues/551
Patch0:         https://github.com/nana-4/materia-theme/commit/8526aeeb045758d2fd8d34d1c5eec742e9692063.patch

BuildRequires:  gnome-shell
BuildRequires:  meson
BuildRequires:  sassc

Requires:       filesystem

Suggests:       flat-remix-icon-theme
Suggests:       papirus-icon-theme

%description
Materia is a Material Design theme for GNOME/GTK based desktop environments.

It supports GTK 2, GTK 3, GNOME Shell, Budgie, Cinnamon, MATE, Unity, Xfce,
LightDM, GDM, Chrome theme, etc.


%prep
%autosetup -n materia-theme-%{vergit} -p1


%build
%meson
%meson_build


%install
%meson_install
find %{buildroot}%{_datadir}/themes -name "COPYING" -exec rm -rf {} \;
find %{buildroot}%{_datadir}/themes -name "index.theme" -exec chmod -x {} \;


%files
%license COPYING
%doc README.md HACKING.md TODO.md
%{_datadir}/themes/Materia*/


%changelog
* Sun Mar 07 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 0.0.20200916-3
- Fix FTBFS 34

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.20200916-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Sep 16 21:53:06 EEST 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.0.20200916-1
- Update to 20200916

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.20200320-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Mar 27 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.0.20200320-1
- Update to 20200320

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.20191017-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 05 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.0.20191017-1
- Update to 20191017

* Tue Sep 24 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.0.20190912-1
- Initial package
