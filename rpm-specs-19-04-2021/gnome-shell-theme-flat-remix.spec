%global vergit  20210226

Name:           gnome-shell-theme-flat-remix
Version:        0.0.%{vergit}
Release:        1%{?dist}
Summary:        Pretty simple theme inspired on material design
BuildArch:      noarch

License:        CC-BY-SA
URL:            https://drasite.com/flat-remix-gnome
Source:         https://github.com/daniruiz/flat-remix-gnome/archive/%{vergit}/%{name}-%{version}.tar.gz

Requires:       gnome-shell >= 3.36

Recommends:     flat-remix-gtk2-theme
Recommends:     flat-remix-gtk3-theme
Recommends:     flat-remix-icon-theme
Recommends:     flat-remix-theme

%description
Flat Remix GNOME theme is a pretty simple shell theme inspired on material
design following a modern design using "flat" colors with high contrasts and
sharp borders.

Themes:
- Flat Remix
- Flat Remix Dark
- Flat Remix Darkest
- Flat Remix Miami
- Flat Remix Miami Dark

Variants:
- Full Panel: No topbar spacing


%prep
%autosetup -n flat-remix-gnome-%{vergit}


%install
mkdir -p %{buildroot}%{_datadir}/themes/
cp -ap Flat-Remix* %{buildroot}%{_datadir}/themes/


%files
%license LICENSE
%doc README.md CHANGELOG
%{_datadir}/themes/Flat-Remix-Blue*/
%{_datadir}/themes/Flat-Remix-Green*/
%{_datadir}/themes/Flat-Remix-Miami*/
%{_datadir}/themes/Flat-Remix-Red*/
%{_datadir}/themes/Flat-Remix-Yellow*/


%changelog
* Fri Feb 26 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 0.0.20210226-1
- Update to 20210226

* Thu Feb 18 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 0.0.20210202-1
- Update to 20210202

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.20201205-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Dec  5 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.0.20201205-1
- Update to 20201205

* Fri Oct 23 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.0.20201022-1
- Update to 20201022

* Sun Sep 27 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.0.20200926-1
- Update to 20200926

* Sat Sep 12 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.0.20200905-1
- Update to 20200905

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.20200617-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 17 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.0.20200617-1
- Update to 20200617

* Tue May 26 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.0.20200502-1
- Update to 20200502

* Sun Apr 12 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.0.20200412-1
- Update to 20200412

* Mon Apr 06 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.0.20200405-1
- Update to 20200405

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.20190829-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Sep 13 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.0.20190829-1
- Update to 20190829

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.20190530-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat May 04 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.0.20190530-1
- Initial package
