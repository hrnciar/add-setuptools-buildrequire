%global _tag 2021.2.20

Name:           deepin-desktop-base
Version:        %{_tag}
Release:        1%{?dist}
Summary:        Base component for Deepin
License:        GPLv3
URL:            https://github.com/linuxdeepin/deepin-desktop-base
Source0:        %{url}/archive/%{_tag}/%{name}-%{_tag}.tar.gz
Source1:        distribution.info
BuildArch:      noarch
Recommends:     deepin-wallpapers
Recommends:     deepin-screensaver
Recommends:     plymouth-theme-deepin
BuildRequires:  make
Requires:       fedora-logos
# since F31
Obsoletes:      deepin-clone <= 1.1.4
Obsoletes:      deepin-qml-widgets <= 2.3.6

%description
This package provides some components for Deepin desktop environment.

- deepin logo
- deepin desktop version
- login screen background image
- language information

%package -n deepin-manual-directory
Summary:        Package that owns the Deepin manual directory

%description -n deepin-manual-directory
This package owns the Deepin manual directory. This is a workaround
before deepin-manual actually comes into Fedora to unblock packaging.

%prep
%setup -q -n %{name}-%{_tag}

# Fix data path
sed -i 's|/usr/lib|%{_datadir}|' Makefile

# Set deepin type to Fedora
sed -i 's|Type=.*|Type=Fedora|; /Type\[/d' files/desktop-version.in

%build
# don't rely on upstream Makefile build since it depends on buildarch
VERSION=20
RELEASE=
sed -e "s|@@VERSION@@|$VERSION|g" -e "s|@@RELEASE@@|$RELEASE|g" files/lsb-release.in > files/lsb-release
sed -e "s|@@VERSION@@|$VERSION|g" -e "s|@@RELEASE@@|$RELEASE|g" files/desktop-version.in > files/desktop-version

%install
%make_install

install -Dm644 %{SOURCE1} -t %{buildroot}%{_datadir}/deepin

# Remove Deepin distro's lsb-release
rm %{buildroot}/etc/lsb-release

# Don't override systemd timeouts
rm -r %{buildroot}/etc/systemd

# Make a symlink for deepin-version
ln -sfv ..%{_datadir}/deepin/desktop-version %{buildroot}%{_sysconfdir}/deepin-version

# Remove UOS logo
rm %{buildroot}%{_datadir}/deepin/uos_logo.svg

# Remove apt-specific templates
rm -r %{buildroot}%{_datadir}/python-apt

mkdir %{buildroot}/%{_datadir}/dman
echo "This package owns the Deepin manual directory. This is a workaround
before deepin-manual actually comes into Fedora to unblock packaging." > %{buildroot}%{_datadir}/dman/README.Fedora

%files
%license LICENSE
%config(noreplace) %{_sysconfdir}/appstore.json
%{_sysconfdir}/deepin-version
%{_datadir}/deepin/
%dir %{_datadir}/distro-info/
%{_datadir}/i18n/i18n_dependent.json
%{_datadir}/i18n/language_info.json
%dir %{_datadir}/plymouth
%{_datadir}/plymouth/deepin-logo.png

%files -n deepin-manual-directory
%{_datadir}/dman

%changelog
* Thu Mar 11 2021 Robin Lee <cheeselee@fedoraproject.org> - 2021.2.20-1
- New release 2021.2.20

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2020.04.12.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Sep 23 2020 Robin Lee <cheeselee@fedoraproject.org> - 2020.04.12.2-1
- New release 2020.04.12-2

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2019.07.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2019.07.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 05 2019 Robin Lee <cheeselee@fedoraproject.org> - 2019.07.10-1
- Release 2019.07.10

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2019.01.28-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Mar 13 2019 Robin Lee <cheeselee@fedoraproject.org> - 2019.01.28-3
- Recommends deepin-screensaver

* Fri Mar  8 2019 Robin Lee <cheeselee@fedoraproject.org> - 2019.01.28-2
- Set deepin type to Fedora
- Own some unowned directories

* Thu Jan 31 2019 mosquito <sensor.wen@gmail.com> - 2019.01.28-1
- Update to 2019.01.28

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2018.10.29-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Nov  9 2018 mosquito <sensor.wen@gmail.com> - 2018.10.29-2
- Add plymouth-theme-deepin dependence

* Fri Nov  9 2018 mosquito <sensor.wen@gmail.com> - 2018.10.29-1
- Update to 2018.10.29

* Sun Oct 28 2018 Zamir SUN <sztsian@gmail.com> - 2018.7.23-2
- Add subpackage deepin-manual-directory to temporary own dman dir.

* Mon Jul 23 2018 mosquito <sensor.wen@gmail.com> - 2018.7.23-1
- Update to 2018.7.23

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2017.11.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2017.11.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Nov 27 2017 mosquito <sensor.wen@gmail.com> - 2017.11.1-1
- Update to 2017.11.1

* Fri Oct 27 2017 mosquito <sensor.wen@gmail.com> - 2016.13.1-1
- Update to 2016.13.1

* Sun Aug  6 2017 mosquito <sensor.wen@gmail.com> - 2016.12.6-1
- Rebuild

* Fri Jul 14 2017 mosquito <sensor.wen@gmail.com> - 2016.12.6-1.git94a22cf
- Update to 2016.12.6

* Fri May 19 2017 mosquito <sensor.wen@gmail.com> - 2016.11.30-1.gita0f52f3
- Update to 2016.11.30

* Tue Jan 17 2017 mosquito <sensor.wen@gmail.com> - 2016.11.29-1.git477c9a7
- Update to 2016.11.29

* Fri Dec 16 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 2016.11.28-1
- Update package to version 2016.11.28

* Sat Dec 03 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 2016.02.03-1
- Update package to version 2016.02.03

* Sun Sep 18 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 2016.02.02-1
- Initial package build
