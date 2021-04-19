Name: gxkb
Version: 0.9.0
Release: 2%{?dist}
Summary: X11 keyboard indicator and switcher

License: GPLv2+
URL: https://github.com/zen-tools/gxkb
Source0: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: automake
BuildRequires: desktop-file-utils
BuildRequires: gcc
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(libwnck-3.0)
BuildRequires: pkgconfig(libxklavier)
BuildRequires: make

%description
gxkb is a tiny indicator applet which allows to quickly switch between
different keyboard layouts in X. A flag corresponding to the country of the
active layout is shown in the indicator area. The applet is written in C and
uses GTK+ library and therefore does not depend on any GNOME components.


%prep
%autosetup -n %{name}-%{version} -p1


%build
./autogen.sh
%configure
%make_build


%install
%make_install

# Move license file in proper location
mkdir -p %{buildroot}%{_licensedir}/%{name}/
mv %{buildroot}%{_docdir}/%{name}/COPYING %{buildroot}%{_licensedir}/%{name}/


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%files
%doc README.md
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*.xpm
%{_docdir}/%{name}/
%{_licensedir}/%{name}/
%{_mandir}/man1/*.1.*


%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Dec 12 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.9.0-1
- Initial package
