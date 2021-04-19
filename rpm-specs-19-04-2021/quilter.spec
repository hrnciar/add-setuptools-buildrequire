%global uuid    io.github.lainsce.Quilter

Name:           quilter
Version:        3.3.0
Release:        2%{?dist}
Summary:        Focus on your writing

# The entire source code is GPLv3+ except:
# * BSD:        highlight.js
# * OFL:        QuiltMono.ttf
License:        GPLv3+ and BSD and OFL
URL:            https://github.com/lainsce/quilter
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  intltool
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtksourceview-4)
BuildRequires:  pkgconfig(gtkspell3-3.0)
BuildRequires:  pkgconfig(libhandy-1)
BuildRequires:  pkgconfig(libmarkdown)
BuildRequires:  pkgconfig(webkit2gtk-4.0)

Requires:       fontpackages-filesystem
Requires:       hicolor-icon-theme
Provides:       bundled(highlight.js) = 9.10.0

%description
Focus on your writing and write beautiful solid stories with the Focus Mode in
tow in this Markdown editor.

- Work on a story, one file at a time.
- Save your documents anywhere, even on existing files.
- Preview your story in the Preview Mode.
- Configure whether to have Focus Mode or not.
- Configure whether to have Dark Mode or not.
- Configure whether to have Sepia Mode or not.
- Fullscreen your writing area with F11.
- Search anytime with the shortcut Ctrl + F.
- Quit anytime with the shortcut Ctrl + Q.


%prep
%autosetup -p1


%build
# fix build issue against libhandy 1.2 pre-releases
export VALAFLAGS=--disable-since-check
%meson
%meson_build


%install
%meson_install
%find_lang %{uuid}


%check
## <release> timestamp is in the future
# appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml

desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%files -f %{uuid}.lang
%license LICENSE
%doc README.md AUTHORS
%{_bindir}/%{uuid}
%{_datadir}/%{uuid}/
%{_datadir}/applications/*.desktop

# Some things might not work as expected because of removed included font
%{_datadir}/fonts/truetype/quilt

%{_datadir}/glib-2.0/schemas/*.gschema.xml
%{_datadir}/gtksourceview-4/styles/*.xml
%{_datadir}/icons/hicolor/*/*/*.svg
%{_metainfodir}/*.appdata.xml


%changelog
* Fri Feb 19 2021 Fabio Valentini <decathorpe@gmail.com> - 3.3.0-2
- Rebuilt for granite 6 soname bump.

* Sat Feb 13 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 3.3.0-1
- build(update): 3.3.0

* Thu Feb 04 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 3.2.4-1
- build(update): 3.2.4

* Wed Feb 03 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 3.2.3-1
- build(update): 3.2.3

* Wed Feb 03 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 3.2.0-1
- build(update): 3.2.0

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 25 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 3.1.5-1
- build(update): 3.1.5

* Sat Jan 23 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 3.1.1-1
- build(update): 3.1.1

* Sat Jan 23 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 3.1.0-1
- build(update): 3.1.0

* Fri Jan 22 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 3.0.3-1
- build(update): 3.0.3

* Thu Jan 21 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 3.0.2-1
- build(update): 3.0.2

* Wed Jan 20 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 3.0.1-1
- build(update): 3.0.1

* Fri Dec 18 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 2.5.2-1
- build(update): 2.5.2

* Wed Aug 26 00:28:45 EEST 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 2.5.1-1
- Update to 2.5.1

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 22 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 2.5.0-1
- Update to 2.5.0

* Sat Apr 04 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 2.2.2-1
- Update to 2.2.2

* Sat Mar 28 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 2.2.1-1
- Update to 2.2.1

* Sat Mar 21 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 2.2.0-1
- Update to 2.2.0

* Fri Mar 06 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 2.1.2-1
- Update to 2.1.2

* Tue Feb 11 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 2.1.1-1
- Update to 2.1.1

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 15 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 2.1.0-1
- Update to 2.1.0

* Wed Aug 28 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 2.0.0-1
- Update to 2.0.0

* Wed Jul 31 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 1.9.3-1
- Update to 1.9.3

* Wed Jun 05 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 1.9.0-1.20190605git076ac9e
- Update to 1.9.0-20190605git076ac9e

* Thu Apr 25 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 1.8.4-2.20190425git5c7a1ca
- Initial package
