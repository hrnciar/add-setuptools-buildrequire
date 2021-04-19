%global commit      64f8f0a806c83fc37e17e72619fce01f1d7dc27d
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate  20210216

%global srcname calculator
%global appname io.elementary.calculator

Name:           elementary-calculator
Summary:        Calculator app designed for elementary
Version:        1.6.0
Release:        3.%{commitdate}git%{shortcommit}%{?dist}
License:        GPLv3+

URL:            https://github.com/elementary/%{srcname}
Source0:        %{url}/archive/%{commit}/%{srcname}-%{shortcommit}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson >= 0.43
BuildRequires:  vala

BuildRequires:  pkgconfig(granite) >= 6.0.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.11.6

Provides:       pantheon-calculator = %{version}-%{release}
Obsoletes:      pantheon-calculator < 0.1.3-5


%description
A simple calculator for everyday use.

It supports basic and some scientific calculations, including trigonometry
functions (sin, cos, and tan).


%prep
%autosetup -n %{srcname}-%{commit} -p1


%build
%meson
%meson_build


%install
%meson_install

%find_lang %{appname}


%check
desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/%{appname}.desktop

appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.appdata.xml


%files -f %{appname}.lang
%license COPYING
%doc README.md

%{_bindir}/%{appname}

%{_datadir}/applications/%{appname}.desktop
%{_datadir}/glib-2.0/schemas/%{appname}.gschema.xml
%{_datadir}/metainfo/%{appname}.appdata.xml


%changelog
* Thu Feb 18 2021 Fabio Valentini <decathorpe@gmail.com> - 1.6.0-3.20210216git64f8f0a
- Bump to commit 64f8f0a. Rebuilt for granite 6 soname bump.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Dec 26 2020 Fabio Valentini <decathorpe@gmail.com> - 1.6.0-1
- Update to version 1.6.0.

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Apr 03 2020 Fabio Valentini <decathorpe@gmail.com> - 1.5.5-1
- Update to version 1.5.5.

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 26 2019 Fabio Valentini <decathorpe@gmail.com> - 1.5.4-1
- Update to version 1.5.4.

* Fri Nov 22 2019 Fabio Valentini <decathorpe@gmail.com> - 1.5.3-1
- Update to version 1.5.3.

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Mar 08 2019 Fabio Valentini <decathorpe@gmail.com> - 1.5.2-1
- Update to version 1.5.2.

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 16 2018 Fabio Valentini <decathorpe@gmail.com> - 1.5.1-1
- Update to version 1.5.1.

* Wed Aug 29 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.5-1
- Update to version 0.1.5.

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4-2
- Rebuild for granite5 soname bump.

* Wed Jun 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4-1
- Initial package renamed from pantheon-calculator.

