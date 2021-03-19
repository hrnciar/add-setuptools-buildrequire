# force out-of-tree build for spec compatibility with older releases
%undefine __cmake_in_source_build

Name:           ballerburg
Version:        1.2.0
Release:        17%{?dist}
Summary:        Two players, two castles, and a hill in between

License:        GPLv3+
URL:            http://baller.tuxfamily.org/
Source0:        http://download.tuxfamily.org/baller/%{name}-%{version}.tar.gz
Source1:        http://baller.tuxfamily.org/king.png
Source2:        %{name}.desktop
Source3:        %{name}.appdata.xml

BuildRequires:  gcc
BuildRequires:  cmake
BuildRequires:  SDL-devel >= 1.2.0
BuildRequires:  gettext
BuildRequires:  ImageMagick
BuildRequires:  libappstream-glib
BuildRequires:  desktop-file-utils
Requires:       hicolor-icon-theme


%description
Two castles, separated by a mountain, try to defeat each other with their
cannonballs, either by killing the opponent's king or by weakening the
opponent enough so that the king capitulates.

Ballerburg was originally written 1987 by Eckhard Kruse, for the Atari ST
machines (which were brand new computers at that point in time). Over 25
years later, here's finally the adaption of the original source code to
modern operating systems.


%prep
%setup -q


%build
%cmake -DCMAKE_BUILD_TYPE:STRING=Debug
%cmake_build


%install
%cmake_install

# Install additional docs
install -p -m 644 LIESMICH.txt README.txt doc/authors.txt \
  %{buildroot}%{_pkgdocdir}

# Install icons
for px in 32 48 64 256; do
  mkdir -p %{buildroot}%{_datadir}/icons/hicolor/${px}x${px}/apps
  convert -gravity south \
    -resize ${px}x${px} \
    -extent ${px}x${px} \
    -background white \
    %{SOURCE1} \
    %{buildroot}%{_datadir}/icons/hicolor/${px}x${px}/apps/%{name}.png
done

# Install desktop file
desktop-file-install \
  --dir=%{buildroot}%{_datadir}/applications \
  %{SOURCE2}

# Install appdata
install -d %{buildroot}%{_datadir}/metainfo
install -p -m 0644 %{SOURCE3} \
  %{buildroot}%{_datadir}/metainfo
appstream-util validate-relax --nonet \
  %{buildroot}%{_datadir}/metainfo/%{name}.appdata.xml


%find_lang %{name}


%files -f %{name}.lang
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man6/ballerburg.6*
%{_datadir}/metainfo/%{name}.appdata.xml
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/*
%doc %{_pkgdocdir}
%license COPYING.txt


%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-16
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Feb 24 2018 Andrea Musuruane <musuruan@gmail.com> - 1.2.0-10
- Added license tag

* Wed Feb 21 2018 Andrea Musuruane <musuruan@gmail.com> - 1.2.0-9
- Added gcc dependency
- Used new AppData directory
- Spec file clean up

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.2.0-7
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Apr 03 2015 Andrea Musuruane <musuruan@gmail.com> - 1.2.0-1
- Updated to new upstream release
- Added appdata file

* Fri Oct 10 2014 Andrea Musuruane <musuruan@gmail.com> - 1.1.0-2
- Dropped cleaning at the beginning of %%install

* Fri Oct 10 2014 Andrea Musuruane <musuruan@gmail.com> - 1.1.0-1
- First release

