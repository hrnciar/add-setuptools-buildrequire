Name:           pamix
Version:        1.6
Release:        2%{?dist}
Summary:        PulseAudio terminal mixer
License:        MIT
URL:            https://github.com/patroclos/PAmix
Source0:        https://github.com/patroclos/PAmix/archive/%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ncurses-devel
BuildRequires:  pulseaudio-libs-devel
# Libs are required automatically, server can be remote
Recommends:     pulseaudio

%description
PAmix is a simple, terminal-based mixer for PulseAudio inspired by pavucontrol.

%prep
%autosetup -n PAmix-%{version}

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%config(noreplace) %{_sysconfdir}/%{name}.conf

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Nov 14 2020 Petr Šabata <contyk@redhat.com> - 1.6-1
- Initial packaging
