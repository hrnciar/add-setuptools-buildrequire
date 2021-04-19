%global commit ac4555d1f4af4c3755d058a34da126acb9fc58d2
%global shortcommit ac4555d
%global gitdate 20180819

Name:           iyfct
Version:        1.0.2
Release:        %{gitdate}git.%{shortcommit}%{?dist}.6
Summary:        Side scrolling endless runner game

#See LICENSE file in source for details
#All code are GPLv3
#All assets are CC-BY 3.0
License:        GPLv3 and CC-BY
URL:            https://github.com/SimonLarsen/iyfct
Source0:        https://github.com/SimonLarsen/%{name}/archive/%{commit}.tar.gz#/%{name}-%{shortcommit}.tar.gz
#Patch for appdata, manpage, execution script, and desktop file
Patch0:         %{name}-appdata.patch

BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  ImageMagick
BuildArch:      noarch
Requires:       love

# List the arches that love builds on
ExclusiveArch: %{arm} %{ix86} x86_64 aarch64 ppc64le

#From README
%description
The goal of the game is to survive as long as you can.
Jump over trains with closed doors and try (as much as possible) to run
through trains with open doors to avoid birds and tunnels.

%prep
%autosetup -p1 -n %{name}-%{commit}
sed -i 's/VERSION/%{version}/g' appdata/%{name}.6
#Strip some formating out of the README
sed 's/h[[:digit:]]. //g' README.textile > README

%build
#love "binary" files are just zipped sources, but should exclude appdata/docs
zip -r %{name}.love . -x appdata/* -x appdata/ -x LICENSE -x README -x README.textile
#Generate icon (based on splash.png)
convert gfx/splash.png -crop 128x52+0+0 -background "#ECF3C9" -gravity center -extent 128x128! %{name}.png

%install
#Install love file
install -p -D -m 0644 %{name}.love \
  %{buildroot}/%{_datadir}/%{name}/%{name}.love
#Install execution script
install -p -D -m 0755 appdata/%{name} \
  %{buildroot}/%{_bindir}/%{name}
#Install manpage
install -p -D -m 0644 appdata/%{name}.6 \
  %{buildroot}/%{_mandir}/man6/%{name}.6
#Install appdata.xml and verify
install -p -D -m 0644 appdata/%{name}.appdata.xml \
  %{buildroot}/%{_datadir}/appdata/%{name}.appdata.xml
appstream-util validate-relax --nonet \
  %{buildroot}/%{_datadir}/appdata/%{name}.appdata.xml
#Install desktop, icon:
desktop-file-install \
  --dir %{buildroot}%{_datadir}/applications \
  appdata/%{name}.desktop
install -p -D -m 0644 %{name}.png \
  %{buildroot}/%{_datadir}/pixmaps/%{name}.png

%files
%license LICENSE
%doc README
%{_mandir}/man6/%{name}.*
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{_datadir}/appdata/%{name}.appdata.xml

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-20180819git.ac4555d.6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-20180819git.ac4555d.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Mar 12 2020 Jeremy Newton <alexjnewt at hotmail dot com> - 1.0.2-20180819git.ac4555d.4
- Rebuilt for correct exclusive arch

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-20180819git.ac4555d.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-20180819git.ac4555d.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-20180819git.ac4555d.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Aug 25 2018 Jeremy Newton <alexjnewt at hotmail dot com> - 1.0.2-20180819git.ac4555d
- Bump snapshot for Love 11 (f29+)

* Thu Aug 23 2018 Jeremy Newton <alexjnewt at hotmail dot com> - 1.0.2-20160510git.7fe93a4
- Initial package
