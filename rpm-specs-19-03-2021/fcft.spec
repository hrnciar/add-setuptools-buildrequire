Name:           fcft
Version:        2.3.2
Release:        3%{?dist}
Summary:        Simple library for font loading and glyph rasterization

# main source:  MIT
# unicode/*:    Unicode
License:        MIT and Unicode
URL:            https://codeberg.org/dnkl/%{name}
Source0:        %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  meson >= 0.54

BuildRequires:  pkgconfig(check)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(harfbuzz)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(scdoc)
BuildRequires:  pkgconfig(tllist)
# require *-static for header-only library
BuildRequires:  tllist-static

%description
fcft is a small font loading and glyph rasterization library built
on top of FontConfig, FreeType2 and pixman.
It can load and cache fonts from a fontconfig-formatted name string,
e.g. Monospace:size=12, optionally with user configured fallback fonts.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -n %{name}
cp unicode/LICENSE LICENSE.Unicode


%build
%meson
%meson_build


%install
%meson_install
# license will be installed to the correct location with rpm macros
rm -f %{buildroot}%{_docdir}/%{name}/LICENSE


%check
%meson_test


%files
%license LICENSE LICENSE.Unicode
%{_libdir}/lib%{name}.so.3*
%dir %{_docdir}/%{name}
%{_docdir}/%{name}/CHANGELOG.md
%{_docdir}/%{name}/README.md

%files devel
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_mandir}/man3/%{name}*.3*


%changelog
* Mon Mar 08 2021 Aleksei Bavshin <alebastr@fedoraproject.org> - 2.3.2-3
- Rebuild for tllist 1.0.5

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Jan 23 2021 Aleksei Bavshin <alebastr@fedoraproject.org> - 2.3.2-1
- Initial import (#1912855)
