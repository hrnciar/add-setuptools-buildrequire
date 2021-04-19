Summary:        Simple TTY terminal I/O application
Name:           tio
Version:        1.32
Release:        5%{?dist}
License:        GPLv2+
URL:            https://tio.github.io/
Source0:        https://github.com/tio/tio/releases/download/v%{version}/%{name}-%{version}.tar.xz
Source1:        https://github.com/tio/tio/releases/download/v%{version}/%{name}-%{version}.tar.xz.asc
Source2:        gpgkey-101BAC1C15B216DBE07A3EEA2BDB4A0944FA00B1.gpg
BuildRequires: make
BuildRequires:  gnupg2
BuildRequires:  gcc

%description
Tio is a simple TTY terminal application which features a straightforward
commandline interface to easily connect to TTY devices for basic input/output.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%setup -q

%build
%configure --disable-silent-rules
%make_build

%install
%make_install

%files
%license COPYING
%doc AUTHORS ChangeLog README
%{_bindir}/%{name}
%dir %{_datadir}/bash-completion/
%dir %{_datadir}/bash-completion/completions/
%{_datadir}/bash-completion/completions/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.32-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.32-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.32-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.32-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 18 2019 Robert Scheck <robert@fedoraproject.org> 1.32-1
- Upgrade to 1.32 (#1720889)

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.27-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.27-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.27-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Nov 29 2017 Robert Scheck <robert@fedoraproject.org> 1.27-1
- Upgrade to 1.27

* Mon Oct 16 2017 Robert Scheck <robert@fedoraproject.org> 1.25-1
- Upgrade to 1.25

* Sun Oct 01 2017 Robert Scheck <robert@fedoraproject.org> 1.24-2
- Changes to match with Fedora Packaging Guidelines (#1497549)

* Sun Oct 01 2017 Robert Scheck <robert@fedoraproject.org> 1.24-1
- Upgrade to 1.24
- Initial spec file for Fedora and Red Hat Enterprise Linux
