Name:           jacktrip
Version:        1.3.0
Release:        2%{?dist}
Summary:        A system for high-quality audio network performance over the Internet

License:        MIT
URL:            https://github.com/%{name}/%{name}
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  meson, gcc-c++
BuildRequires:  doxygen, help2man
BuildRequires:  qt5-qtbase-devel
BuildRequires:  jack-audio-connection-kit-devel

%description
JackTrip is a Linux and Mac OS X-based system used for multi-machine
network performance over the Internet. It supports any number of
channels (as many as the computer/network can handle) of
bidirectional, high quality, uncompressed audio signal steaming.

%package        doc
Summary:        HTML documentation for %{name}
BuildArch:      noarch

%description    doc
This package contains the documentation in HTML format for %{name}.

%prep
%autosetup
rm -rf externals

%build
%meson
%meson_build
doxygen %{name}_doxygen
find WWW -name "*.md5" -delete
find WWW -name "*.map" -delete

%install
%meson_install
help2man -N -n "%{summary}" %{buildroot}%{_bindir}/%{name} > %{name}.1
install -D -m 0644 %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

%check
%meson_test

%files
%doc README.md CHANGESLOG.txt
%license LICENSE
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%files doc
%doc WWW/html

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Jan 16 2021 Iñaki Úcar <iucar@fedoraproject.org> - 1.3.0-1
- Update to v1.3.0

* Sat Oct 24 2020 Iñaki Úcar <iucar@fedoraproject.org> - 1.2.1-1
- Initial packaging for Fedora
