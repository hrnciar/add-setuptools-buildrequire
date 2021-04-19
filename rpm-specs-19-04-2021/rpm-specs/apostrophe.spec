%global appname org.gnome.gitlab.somas.Apostrophe

Name:           apostrophe
Version:        2.4
Release:        1%{?dist}
Summary:        Distraction free Markdown editor for GNU/Linux made with GTK+

# Entire source code is GPLv3+ except:
# * GPLv2:      help/stump/
# * LGPLv2.1:   apostrophe/plugins/bibtex/gi_composites.py
# * MIT:        apostrophe/latex_to_PNG.py
#               apostrophe/plugins/bibtex/fuzzywuzzy/
License:        GPLv3+ and GPLv2 and LGPLv2.1 and MIT
URL:            https://gitlab.gnome.org/somas/apostrophe
Source0:        %{url}/-/archive/v%{version}/%{name}-v%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  desktop-file-utils
BuildRequires:  intltool
BuildRequires:  libappstream-glib
BuildRequires:  meson >= 0.50.0
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libhandy-1)

Recommends:     gspell

Requires:       hicolor-icon-theme
Requires:       libhandy1
Requires:       python3-cairo
Requires:       python3-enchant
Requires:       python3-Levenshtein
Requires:       python3-pypandoc
Requires:       python3-regex

%description
Apostrophe is a GTK+ based distraction free Markdown editor, mainly developed by
Wolf Vollprecht and Manuel Genovés. It uses pandoc as backend for markdown
parsing and offers a very clean and sleek user interface.


%prep
%autosetup -n %{name}-v%{version} -p1

# W: hidden-file-or-dir
rm apostrophe/.pylintrc


%build
%meson
%meson_build


%install
%meson_install
%find_lang %{name}



%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/%{appname}.desktop


%files -f %{name}.lang
%license LICENSE
%doc README.md AUTHORS tests/markdown_test.md
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/*.desktop
%{_datadir}/glib-2.0/schemas/*.gschema.xml
%{_datadir}/icons/hicolor/*/*/*.svg
%{_metainfodir}/*.xml
%{python3_sitelib}/%{name}/


%changelog
* Wed Mar 10 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 2.4-1
- build(update): 2.4

* Wed Mar 03 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 2.3-1
- build(update): 2.3

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.2.0.3-3
- Rebuilt for Python 3.9

* Fri May 08 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 2.2.0.3-2
- Add patch for compatibility with old pandoc | Thanks to @suve

* Mon May 04 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 2.2.0.3-1
- Update to 2.2.0.3

* Thu Apr 23 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 2.2.0.2-2
- Add few recommended deps

* Mon Apr 20 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 2.2.0.2-1
- Update to 2.2.0.2

* Mon Apr 20 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 2.2.0.1-3
- Update to 2.2.0.1
- Ported to Meson and renamed to Apostrophe now

* Tue Jul 30 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 2.1.5-4
- Initial package
