%global relver 1.2

Name:       lightdm-gtk-greeter-settings
Version:    %{relver}.2
Release:    13%{?dist}
Summary:    Settings editor for LightDM GTK+ Greeter

License:    GPLv3
URL:        https://launchpad.net/lightdm-gtk-greeter-settings
Source0:    https://launchpad.net/%{name}/%{relver}/%{version}/+download/%{name}-%{version}.tar.gz

BuildArch:  noarch

BuildRequires:  desktop-file-utils
BuildRequires:  intltool
BuildRequires:  python3-devel
BuildRequires:  python3-distutils-extra
BuildRequires:  python3-setuptools

Requires:  lightdm-gtk
Requires:  python3-gobject

%description
Just a small dialog to make it easier for users to modify the settings
of lightdm-gtk-greeter.


%prep
%autosetup -p 1
rm -f PKG-INFO

# Rename the ubuntu references to fedora
sed -i -e 's@com.ubuntu.pkexec@com.fedora.pkexec@g' com.ubuntu.pkexec.lightdm-gtk-greeter-settings.policy.in \
 po/*
mv com.ubuntu.pkexec.lightdm-gtk-greeter-settings.policy.in com.fedora.pkexec.lightdm-gtk-greeter-settings.policy.in


%build
%py3_build


%install
# %%py3_install des not work properly here.
%{__python3} setup.py install --root=$RPM_BUILD_ROOT --optimize=1

# Remove shebang from files
for lib in %{buildroot}%{python3_sitelib}/lightdm_gtk_greeter_settings/*.py; do
 sed '1{\@^#!/usr/bin/env python@d}' $lib > $lib.new &&
 touch -r $lib $lib.new &&
 mv $lib.new $lib
done

%find_lang %{name}


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%files -f %{name}.lang
%doc NEWS README
%license COPYING
%{_bindir}/lightdm-gtk-greeter-settings
%{_bindir}/lightdm-gtk-greeter-settings-pkexec
%{python3_sitelib}/lightdm_gtk_greeter_settings-%{version}-py*.egg-info
%{python3_sitelib}/lightdm_gtk_greeter_settings/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/lightdm-gtk-greeter-settings*
%{_datadir}/lightdm-gtk-greeter-settings/
%{_datadir}/polkit-1/actions/com.fedora.pkexec.lightdm-gtk-greeter-settings.policy


%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hron??ok <mhroncok@redhat.com> - 1.2.2-11
- Rebuilt for Python 3.9

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hron??ok <mhroncok@redhat.com> - 1.2.2-9
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hron??ok <mhroncok@redhat.com> - 1.2.2-8
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hron??ok <mhroncok@redhat.com> - 1.2.2-4
- Rebuilt for Python 3.7

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.2.2-2
- Remove obsolete scriptlets

* Fri Jan 05 2018 Bj??rn Esser <besser82@fedoraproject.org> - 1.2.2-1
- New upstream release (rhbz#1530973, 1531497)

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hron??ok <mhroncok@redhat.com> - 1.2.0-5
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Sat Jul 04 2015 Leigh Scott <leigh123linux@googlemail.com> - 1.2.0-1
- Initial build
