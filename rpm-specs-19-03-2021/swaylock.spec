Name:       swaylock
Version:    1.5
Release:    6%{?dist}
Summary:    Screen locker for Wayland

License:    MIT
URL:        https://github.com/swaywm/swaylock
Source0:    %{url}/archive/%{version}/%{name}-%{version}.tar.gz
Patch1:     swaylock-1.5-fix-version-number.diff
Patch2:     %{url}/commit/235b925df7e1bb82d98f1ac8c02e8f85d0a54ee9.patch#/swaylock-1.5-fix-potential-use-after-free.patch

# Older versions were part of the sway package
Conflicts:      sway < 1.0

BuildRequires:  gcc
BuildRequires:  meson >= 0.48.0
BuildRequires:  pam-devel
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.14
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  scdoc

%description
swaylock is a screen locking utility for Wayland compositors.

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
%config(noreplace) %{_sysconfdir}/pam.d/%{name}

# Co-own completion directories
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/%{name}

%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_%{name}

%dir %{_datadir}/fish
%dir %{_datadir}/fish/vendor_completions.d
%{_datadir}/fish/vendor_completions.d/%{name}.fish


%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Nov 13 2020 Aleksei Bavshin <alebastr@fedoraproject.org> - 1.5-5
- Add patch with fix for memory corruption issue

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 29 2020 Fabio Alessandro Locati <me@fale.io> - 1.5-3
- Fix #1806110

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 23 2020 Jan Stan??k <jstanek@redhat.com> - 1.5-1
- Upgrade to version 1.5 (https://github.com/swaywm/swaylock/releases/tag/1.5)

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon May 06 2019 Jan Stan??k <jstanek@redhat.com> - 1.4-1
- Upgrade to version 1.4 (https://github.com/swaywm/swaylock/releases/tag/1.4)

* Mon Mar 18 2019 Jan Stan??k <jstanek@redhat.com> - 1.3-1
- Initial package import
