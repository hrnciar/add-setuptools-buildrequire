%global sysname sgtk_menu

Name:           sgtk-menu
Version:        1.4.1
Release:        3%{?dist}
Summary:        GTK launcher for sway & other WMs

License:        GPLv3+
URL:            https://github.com/nwg-piotr/sgtk-menu
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
This project is an attempt to create a launcher, that behaves decently on sway,
but also works on other window managers. It may or may not work on some DEs - I
don't care much about it. For what I managed to test so far, see the
Compatibility chart.


%prep
%autosetup -n %{name}-%{version}

# Remove shebang from Python libraries
for lib in sgtk_menu/*.py; do
 sed '1{\@^#!/usr/bin/env python@d}' $lib > $lib.new &&
 touch -r $lib $lib.new &&
 mv $lib.new $lib
done


%build
%py3_build


%install
%py3_install


%files
%license LICENSE
%doc README.md examples/
%{_bindir}/%{name}
%{_bindir}/sgtk-bar
%{_bindir}/sgtk-dmenu
%{_bindir}/sgtk-grid
%{python3_sitelib}/%{sysname}-*.egg-info/
%{python3_sitelib}/%{sysname}/


%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.4.1-1
- Update to 1.4.1

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.3.1-4
- Rebuilt for Python 3.9

* Wed Feb 26 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.3.1-3
- Packaging fixes

* Wed Feb 26 2020 Bob Hepple <bob.hepple@gmail.com> - 1.3.1-1.fc31.wef
- Initial version of the package
