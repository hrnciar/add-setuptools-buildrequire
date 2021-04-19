%global extension   emoji-selector
%global uuid        %{extension}@maestroschan.fr

Name:           gnome-shell-extension-%{extension}
Version:        20
Release:        2%{?dist}
Summary:        GNOME Shell extension for copying emojis to the clipboard
# The entire source code is GPLv3 except convenience.js which is BSD
License:        GPLv3 and BSD
URL:            https://github.com/maoschanz/emoji-selector-for-gnome
Source0:        %{url}/archive/%{version}/%{extension}-%{version}.tar.gz
BuildArch:      noarch
Requires:       gnome-shell-extension-common
Recommends:     gnome-extensions-app
Recommends:     twitter-twemoji-fonts


%description
This extension provides a parametrable popup menu displaying most emojis,
clicking on an emoji copies it to the clipboard.  An appropriate font like
'Twitter Color Emoji' or 'JoyPixels Color' should be installed on your system
for a better visual result.


%prep
%autosetup -n %{extension}-for-gnome-%{version}

# relocate things we don't want copied into the extensions directory
mv %{uuid}/locale .
mv %{uuid}/schemas .


%install
install -d -m 0755 %{buildroot}%{_datadir}/gnome-shell/extensions

# install main extension files
cp -r --preserve=mode,timestamps %{uuid} %{buildroot}%{_datadir}/gnome-shell/extensions

# install the schema file
install -D -p -m 0644 \
    schemas/org.gnome.shell.extensions.%{extension}.gschema.xml \
    %{buildroot}%{_datadir}/glib-2.0/schemas/%{uuid}.gschema.xml

# install locale files
mv locale/zh{_,-}Hans
for mo in locale/*/LC_MESSAGES/*.mo; do
    install -D -p -m 0644 $mo %{buildroot}%{_datadir}/$mo
done
%find_lang %{extension}


%files -f %{extension}.lang
%license LICENSE
%doc README.md
%{_datadir}/gnome-shell/extensions/%{uuid}
%{_datadir}/glib-2.0/schemas/%{uuid}.gschema.xml


%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Oct 25 2020 Carl George <carl@george.computer> - 20-1
- Latest upstream

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 19-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 05 2020 Carl George <carl@george.computer> - 19-2
- Update license field

* Tue May 12 2020 Carl George <carl@george.computer> - 19-1
- Latest upstream
- Install locale files correctly

* Sun Apr 26 2020 Carl George <carl@george.computer> - 17-1
- Initial package
