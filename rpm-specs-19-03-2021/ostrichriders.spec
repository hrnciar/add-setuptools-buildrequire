Summary: Knights flying on ostriches compete against other riders
Name: ostrichriders
Version: 0.6.5
Release: 5%{?dist}
License: GPLv3+
Url: http://www.identicalsoftware.com/ostrichriders
Source: http://www.identicalsoftware.com/ostrichriders/%{name}-%{version}.tgz
BuildRequires: make
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: SFML-devel
BuildRequires: desktop-file-utils
BuildRequires: fontconfig-devel
BuildRequires: pkgconfig
BuildRequires: libappstream-glib
Requires: hicolor-icon-theme

%description
Enemy knights are invading the kingdom. As one of the elite ostrich riders,
it is your duty to defend the kingdom. With lance in hand you fly off.
Remember to stay above your opponent least you fall to his lance. Collect the
eggs least your opponent hatches stronger than before. Work together with
other knights.

%prep
%setup -q

%build
%make_build

%install
%make_install PREFIX=%{_prefix}

%check
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/*.appdata.xml

%files
%license LICENCE
%doc README
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{_datadir}/appdata/%{name}.appdata.xml

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Feb 28 2019 Dennis Payne <dulsi@identicalsoftware.com> - 0.6.5-1
- Add arcade mode.

* Sun Feb 18 2018 Dennis Payne <dulsi@identicalsoftware.com> - 0.6.4-3
- Add build requirement of gcc-c++.

* Fri Sep 16 2016 Dennis Payne <dulsi@identicalsoftware.com> - 0.6.4-2
- Added app data validation
- Used some macros for common tasks
- Require hicolor icon theme
- Mark license file correctly

* Thu Sep 15 2016 Dennis Payne <dulsi@identicalsoftware.com> - 0.6.4-1
- New release.

* Sat Apr 16 2016 R??mi Verschelde <akien@mageia.org> - 0.6.3-2
- Add support for DESTDIR parameter, and overriding BINDIR and PREFIX
- Make binary name lowercase

* Thu Mar 10 2016 Dennis Payne <dulsi@identicalsoftware.com> - 0.6.3-1
- Moved install into the makefile.

* Thu Feb 11 2016 Dennis Payne <dulsi@identicalsoftware.com> - 0.6.2-1
- First ostrich riders spec file.
