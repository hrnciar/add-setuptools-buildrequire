%global commit      7c8d74873cb7afc724b458cabf99901189f661a5
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate  20210219

%global srcname settings-daemon
%global appname io.elementary.settings-daemon
%global iface   io.elementary.SettingsDaemon.AccountsService

Name:           elementary-settings-daemon
Version:        1.0.0
Release:        0.1.%{commitdate}git%{shortcommit}%{?dist}
Summary:        Settings Daemon for Pantheon
License:        GPLv3+

URL:            https://github.com/elementary/settings-daemon
Source0:        %{url}/archive/%{commit}/%{srcname}-%{shortcommit}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  meson
BuildRequires:  vala

BuildRequires:  pkgconfig(accountsservice)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(granite) >= 5.3.0
BuildRequires:  pkgconfig(libgeoclue-2.0)

%description
%{summary}.


%prep
%autosetup -n %{srcname}-%{commit} -p1


%build
%meson
%meson_build


%install
%meson_install


%check
desktop-file-validate \
    %{buildroot}/%{_sysconfdir}/xdg/autostart/%{appname}.desktop


%files
%license LICENSE
%doc README.md

%config(noreplace) %{_sysconfdir}/xdg/autostart/%{appname}.desktop

%{_bindir}/%{appname}

%{_datadir}/accountsservice/interfaces/%{iface}.xml
%{_datadir}/dbus-1/interfaces/%{iface}.xml
%{_datadir}/glib-2.0/schemas/%{appname}.gschema.xml


%changelog
* Sat Feb 20 2021 Fabio Valentini <decathorpe@gmail.com> - 1.0.0-0.1.20210219git7c8d748
- Initial package for Fedora.

