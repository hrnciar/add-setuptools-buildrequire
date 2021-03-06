%global commit bc2f76c4be6f45621fbbea3ca8c666e3182f6377
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global gitdate 20190520
%global fgittag %{gitdate}.git%{shortcommit}

Summary: GNOME Monitor Configuration Tool
Name: gnome-monitor-config
Version: 0
Release: 0.5%{?fgittag:.%{fgittag}}%{?dist}
#Note that the license isn't included in source yet, see this pull request:
#https://github.com/jadahl/gnome-monitor-config/pull/1
License: GPLv2+
URL: https://github.com/jadahl/gnome-monitor-config
Source0:  https://github.com/jadahl/%{name}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

BuildRequires: meson
BuildRequires: ninja-build
BuildRequires: gcc
BuildRequires: cairo-devel

%description
A CLI configuration tool used for changing monitor settings in GNOME.
This can be used in Wayland, with functionality similar to xrandr on X11.

%prep
%autosetup -n %{name}-%{commit}

%build
%meson
%meson_build

%install
install -m 755 */src/%{name} -D %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5.20190520.gitbc2f76c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4.20190520.gitbc2f76c
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.20190520.gitbc2f76c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.20190520.gitbc2f76c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri May 31 2019 Jeremy Newton <alexjnewt AT hotmail DOT com> 0-0.1.20190520.gitbc2f76c
- Intial Package
