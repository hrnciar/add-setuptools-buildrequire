%global commit      ae2d2966a7ceb65b0e4a0c72ca31bd7fceb76857
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date        20190828

%global appname com.github.JannikHv.Gydl

Name:           gydl
Version:        0.1.1
Release:        6.%{date}git%{shortcommit}%{?dist}
Summary:        GUI wrapper around youtube-dl program

License:        GPLv3+
URL:            https://github.com/JannikHv/gydl
Source0:        %{url}/archive/%{commit}/%{name}-%{version}.%{date}git%{shortcommit}.tar.gz

# fix(appdata): add type to launchable
# https://github.com/JannikHv/gydl/pull/34
Patch0:         %{url}/pull/34.patch

BuildArch:      noarch

BuildRequires:  desktop-file-utils
BuildRequires:  intltool
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  python3-devel
BuildRequires:  youtube-dl
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(pygobject-3.0)
Requires:       hicolor-icon-theme
Requires:       youtube-dl

%description
Gydl (Graphical Youtube-dl) is a GUI wrapper around the already existing
youtube-dl program.

It's developed with a dialog driven experience in mind. This provides a quick
and easy video or audio downloads without disturbances.

%prep
%autosetup -p1 -n %{name}-%{commit}

%build
%meson
%meson_build

%install
%meson_install
%find_lang Gydl

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{appname}.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/%{appname}.desktop

%files -f Gydl.lang
%license LICENSE
%doc README.md
%{_bindir}/%{name}.py
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/*/*.svg
%{_metainfodir}/*.appdata.xml

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-6.20190113git63dbddc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-5.20190113git63dbddc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-4.20190113git63dbddc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Aug 15 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.1.1-3.20190113git63dbddc
- Initial package
