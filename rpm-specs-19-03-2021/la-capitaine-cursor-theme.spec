%global tname   La-Capitaine

Name:           la-capitaine-cursor-theme
Version:        3
Release:        9%{?dist}
Summary:        X-cursor theme inspired by macOS and based on KDE Breeze

License:        LGPLv3
URL:            https://github.com/keeferrourke/capitaine-cursors
Source0:        %{url}/archive/r%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  inkscape
BuildRequires:  xcursorgen
Suggests:       la-capitaine-icon-theme

%description
This is an x-cursor theme inspired by macOS and based on KDE Breeze. The source
files were made in Inkscape, and the theme was designed to pair well with my
icon pack, La Capitaine.


%prep
%autosetup -n capitaine-cursors-r%{version}


%build
./build.sh


%install
mkdir -p                %{buildroot}/%{_datadir}/icons/%{tname}
cp -rfa dist/cursors    %{buildroot}/%{_datadir}/icons/%{tname}/
find %{buildroot} -size 0 -delete


%post
/bin/touch --no-create %{_datadir}/icons/%{tname} &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/%{tname} &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/%{tname} &>/dev/null || :
fi

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/%{tname} &>/dev/null || :


%files
%license COPYING
%doc README.md
%{_datadir}/icons/%{tname}
%ghost %{_datadir}/icons/%{tname}/icon-theme.cache


%changelog
* Tue Mar 02 2021 Peter Hutterer <peter.hutterer@redhat.com> 3-9
- Reduce BuildRequires to xcursorgen, it's the the only tool from
  xorg-x11-apps that we need.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Sep 14 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 3-5
- Update to r3
- Packaging fixes

* Wed Mar 15 2017 Laurent Tréguier <laurent@treguier.org> - 2-1
- Initial package
