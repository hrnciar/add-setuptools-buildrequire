Name:             zathura-ps
Version:          0.2.6
Release:          7%{?dist}
Summary:          PS support for zathura via libspectre
License:          zlib
URL:              http://pwmt.org/projects/zathura/plugins/%{name}
Source0:          http://pwmt.org/projects/zathura/plugins/download/%{name}-%{version}.tar.xz
BuildRequires:    binutils
BuildRequires:    cairo-devel
# Needed to validate the desktop file
BuildRequires:    desktop-file-utils
BuildRequires:    gcc
BuildRequires:    girara-devel
BuildRequires:    glib2-devel
# Needed to validate appdata
BuildRequires:    libappstream-glib
BuildRequires:    libspectre-devel
BuildRequires:    meson >= 0.43
BuildRequires:    zathura-devel >= 0.3.8
Requires:         zathura >= 0.3.8

%description
The zathura-ps plugin adds PostScript support to zathura by
using the libspectre library.

%prep
%setup -q

%build
%meson
%meson_build

%install
%meson_install
desktop-file-validate %{buildroot}/%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.metainfo.xml

%files
%license LICENSE
%doc AUTHORS
%{_libdir}/zathura/libps.so
%{_datadir}/applications/org.pwmt.zathura-ps.desktop
%{_datadir}/metainfo/org.pwmt.zathura-ps.metainfo.xml

%changelog
* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Apr 10 2018 Petr ??abata <contyk@redhat.com> - 0.2.6-1
- 0.2.6 bump

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Jan 15 2017 Petr ??abata <contyk@redhat.com> - 0.2.4-1
- 0.2.4 bump

* Fri Feb 26 2016 Petr ??abata <contyk@redhat.com> - 0.2.3-1
- 0.2.3 bump

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jul 02 2015 Petr ??abata <contyk@redhat.com> - 0.2.2-10
- Install the desktop file correctly

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 10 2015 Petr ??abata <contyk@redhat.com> - 0.2.2-8
- Rebuild for new girara

* Tue Jun 09 2015 Petr ??abata <contyk@redhat.com> - 0.2.2-7
- Fix the dep list, install LICENSE with the %%license macro

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Mar 06 2014 Fran??ois Cami <fcami@fedoraproject.org> - 0.2.2-4
- Rebuilt after upgrading girara & friends

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed May 29 2013 Petr ??abata <contyk@redhat.com> - 0.2.2-2
- Fix a debuginfo regression (#967954)

* Fri Mar 29 2013 Kevin Fenzi <kevin@scrye.com> 0.2.1-1
- Update to 0.2.1

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jan 12 2013 Fran??ois Cami <fcami@fedoraproject.org> - 0.2.0-3
- force-require zathura.

* Sun Dec 02 2012 Fran??ois Cami <fcami@fedoraproject.org> - 0.2.0-2
- remove EL5 specific stuff.

* Sun Dec 02 2012 Fran??ois Cami <fcami@fedoraproject.org> - 0.2.0-1
- Initial package.
