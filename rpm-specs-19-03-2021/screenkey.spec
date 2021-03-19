%global py_name Screenkey
Name:		screenkey
Version:	1.2
Release:	4%{?dist}
Summary:	A screencast tool to display your keys
License:	GPLv3+
URL:		https://www.thregr.org/~wavexx/software/screenkey
Source0:	https://www.thregr.org/~wavexx/software/screenkey/releases/%{name}-%{version}.tar.gz

BuildArch:	noarch

BuildRequires:	python3-devel
BuildRequires:	python3-setuptools
BuildRequires:	python3-distutils-extra
BuildRequires:	desktop-file-utils
BuildRequires:	intltool
BuildRequires:	gettext

Requires:   python3-gobject
Requires:   python3-cairo
Requires:   slop

Recommends: fontawesome-fonts
Recommends: libappindicator-gtk3

%description
A screencast tool to display your keys, featuring:
* Several keyboard translation methods 
* Key composition/input method support
* Configurable font/size/position
* Highlighting of recent keystrokes
* Improved backspace processing
* Normal/Emacs/Mac caps modes
* Multi-monitor support
* Dynamic recording control etc.


%prep
%setup -q -n %{name}-%{version}
# Remove bundled egg-info
rm -rf %{src_name}.egg-info

%build
%py3_build

%install
%py3_install
#Manually install locale files
install -d -m 0755 %{buildroot}/%{_datadir}/locale
cp -r build/mo/* %{buildroot}/%{_datadir}/locale/
%find_lang %{name}

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop

%files -f %{name}.lang
%doc README.rst NEWS.rst
%license COPYING.txt
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{python3_sitelib}/%{py_name}/
%{python3_sitelib}/%{name}-%{version}-*.egg-info

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Sep 17 2020 Rajeesh K V <rajeeshknambiar@fedoraproject.org> - 1.2-3
- Address Fedora review comments, v2.
- Fix BR typo of python3-gobject
- Add missing BR for intltool and gettext
- Add missing runtime dependency on slop
- Add fontawesome and appindicator recommendation
- Install locale files

* Fri Sep 11 2020 Rajeesh K V <rajeeshknambiar@fedoraproject.org> - 1.2-2
- Address Fedora review comments

* Fri Sep 11 2020 Rajeesh K V <rajeeshknambiar@fedoraproject.org> - 1.2-1
- Initial packaging
