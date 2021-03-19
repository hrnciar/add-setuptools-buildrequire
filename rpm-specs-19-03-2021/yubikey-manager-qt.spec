%global bname ykman-gui
Name: yubikey-manager-qt
Summary: Application for configuring any YubiKey over all USB interfaces
Version: 1.2.0
Release: 1%{?dist}
URL: https://developers.yubico.com/yubikey-manager-qt/
Source0: https://developers.yubico.com/%{name}/Releases/%{name}-%{version}.tar.gz
Source1: https://developers.yubico.com/%{name}/Releases/%{name}-%{version}.tar.gz.sig
Source2:  gpgkey-6690D8BC.gpg

License: BSD

BuildRequires: gnupg2
BuildRequires: annobin
BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: python3
BuildRequires: libyubikey
BuildRequires: python3-yubikey-manager >= 4
BuildRequires: qt5-qtbase-devel qt5-qtdeclarative-devel qt5-qtquickcontrols2-devel
BuildRequires: qt5-qtquickcontrols qt5-qtgraphicaleffects pyotherside
BuildRequires: desktop-file-utils
Requires:      pyotherside 
Requires:      qt5-qtquickcontrols

%description
Cross-platform application for configuring any YubiKey over all USB interfaces.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%setup -q -n %{name}
sed -i 's|python |python3 |g' ykman-cli/ykman-cli.pro
sed -i 's|python |python3 |g' ykman-gui/ykman-gui.pro


%build
#qmake-qt5 QMAKE_CFLAGS+="%{optflags}" QMAKE_CXXFLAGS+="%{optflags}" QMAKE_STRIP="/bin/true";
%{qmake_qt5}
#make %{?_smp_mflags}
%{make_build}

%install
make install INSTALL_ROOT="%{buildroot}"
mkdir -p %{buildroot}%{_datadir}/pixmaps
install -p -m 0644 resources/icons/ykman.png %{buildroot}%{_datadir}/pixmaps/
desktop-file-install --dir=%{buildroot}%{_datadir}/applications resources/%{bname}.desktop

%files
%license COPYING
%doc NEWS README
%{_bindir}/%{bname}
%{_datadir}/applications/%{bname}.desktop
%{_datadir}/pixmaps/ykman.png

%changelog
* Wed Mar 17 2021 Jakub Jelen <jjelen@redhat.com> - 1.2.0-1
- New upstream release (#1939620)

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Nov 24 2020 Jakub Jelen <jjelen@redhat.com> - 1.1.5-3
- Add missing dependency (#1900902)

* Tue Sep 22 2020 Jakub Jelen <jjelen@redhat.com> - 1.1.5-2
- First release for Fedora 

