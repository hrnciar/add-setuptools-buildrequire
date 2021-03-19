Name:           librttopo
Version:        1.1.0
Release:        3%{?dist}
Summary:        Create and manage SQL/MM topologies

License:        GPLv2+
URL:            https://git.osgeo.org/gitea/rttopo/librttopo
Source0:        https://git.osgeo.org/gitea/rttopo/librttopo/archive/%{name}-%{version}.tar.gz

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  geos-devel
BuildRequires:  libtool
BuildRequires:  make


%description
The RT Topology Library exposes an API to create and manage standard
(ISO 13249 aka SQL/MM) topologies using user-provided data stores.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -p1 -n %{name}


%build
autoreconf -ifv
%configure --disable-static
%make_build


%install
%make_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'


%files
%license COPYING
%doc CREDITS NEWS.md README.md TODO
%{_libdir}/%{name}.so.*

%files devel
%{_includedir}/%{name}.h
%{_includedir}/%{name}_geom.h
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/rttopo.pc


%changelog
* Sat Feb 13 2021 Sandro Mani <manisandro@gmail.com> - 1.1.0-3
- Rebuild (geos)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Nov 13 2020 Sandro Mani <manisandro@gmail.com> 1.1.0-1
- Initial package
