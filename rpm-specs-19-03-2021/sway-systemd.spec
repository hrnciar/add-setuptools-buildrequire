%if 0%{?fedora} >= 34
%bcond_without  cgroups
%else
%bcond_with     cgroups
%endif

Name:           sway-systemd
Version:        0.1.1
Release:        1%{?dist}
Summary:        Systemd integration for Sway session

License:        MIT
URL:            https://github.com/alebastr/sway-systemd
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  meson
BuildRequires:  pkgconfig(systemd)
BuildRequires:  systemd-rpm-macros

%if %{with cgroups}
Requires:       python3dist(dbus-next)
Requires:       python3dist(i3ipc)
Requires:       python3dist(psutil)
Requires:       python3dist(python-xlib)
%endif
Requires:       sway
Requires:       systemd
Recommends:     /usr/bin/dbus-update-activation-environment

%description
%{summary}.

The goal of this project is to provide a minimal set of configuration files
and scripts required for running Sway in a systemd environment.

This includes several areas of integration:
 - Propagate required variables to the systemd user session environment.
 - Define sway-session.target for starting user services.
%{?with_cgroups: - Place GUI applications into a systemd scopes for systemd-oomd compatibility.}

%prep
%autosetup


%build
%meson \
    -Dcgroups=%{?with_cgroups:enabled}%{!?with_cgroups:disabled}
%meson_build


%install
%meson_install


%files
%license LICENSE
%doc README.md
%config(noreplace) %{_sysconfdir}/sway/config.d/10-systemd-session.conf
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/session.sh
%{_userunitdir}/sway-session.target

%if %{with cgroups}
%config(noreplace) %{_sysconfdir}/sway/config.d/10-systemd-cgroups.conf
%{_libexecdir}/%{name}/assign-cgroups.py
%endif

%changelog
* Wed Mar 10 2021 Aleksei Bavshin <alebastr@fedoraproject.org> - 0.1.1-1
- Initial import (#1932728)
