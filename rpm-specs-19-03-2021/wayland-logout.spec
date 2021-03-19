Name:           wayland-logout
Version:        1.4
Release:        2%{?dist}
Summary:        Simple program that sends SIGTERM to a wayland compositor

License:        MIT
URL:            https://github.com/soreau/%{name}
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  meson >= 0.55

%description
Wayland Logout is an utility designed to kill any wayland compositor
that uses libwayland-server. It looks up the PID for the socket file
by checking the socket path environment variables and sends a SIGTERM
signal. This is useful as a way to logout of a wayland compositor,
as the name implies.

%prep
%autosetup


%build
%meson
%meson_build


%install
%meson_install


%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*


%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Dec 27 2020 Aleksei Bavshin <alebastr@fedoraproject.org> - 1.4-1
- Update to upstream release 1.4

* Wed Nov 18 2020 Aleksei Bavshin <alebastr@fedoraproject.org> - 1.0.1-0.1.20201117gitc9f0bae
- Initial import (#1898448)
