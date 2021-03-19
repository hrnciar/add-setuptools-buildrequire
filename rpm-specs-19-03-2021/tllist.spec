# this is a header-only library with architecture-dependent .pc file
%global debug_package %{nil}

Name:           tllist
Version:        1.0.5
Release:        1%{?dist}
Summary:        C header file only implementation of a typed linked list

License:        MIT
URL:            https://codeberg.org/dnkl/%{name}
Source0:        %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  meson >= 0.54

%global  _description %{expand:
%{name} is a C header-only implementation of a linked list that uses
pre-processor macros to implement dynamic types, where the data carrier
is typed to whatever you want; both primitive data types are supported
as well as aggregated ones such as structs, enums and unions.}

%description    %{_description}

%package        devel
Summary:        Development files for %{name}
Provides:       %{name}-static = %{version}-%{release}

%description    devel %{_description}


%prep
%autosetup -p1 -n %{name}


%build
%meson
%meson_build


%install
%meson_install
# license will be installed to correct location with rpm macros
rm -f %{buildroot}%{_docdir}/%{name}/LICENSE


%check
%meson_test


%files devel
%license LICENSE
%{_includedir}/%{name}.h
%{_libdir}/pkgconfig/%{name}.pc
%dir %{_docdir}/%{name}
%{_docdir}/%{name}/README.md

%changelog
* Mon Mar 08 2021 Aleksei Bavshin <alebastr@fedoraproject.org> - 1.0.5-1
- Update to 1.0.5 (fixes rhbz#1925943)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 11 2021 Aleksei Bavshin <alebastr@fedoraproject.org> - 1.0.4-1
- Initial import (#1912853)
