Name:           virtualpg
Version:        2.0.1
Release:        4%{?dist}
Summary:        A loadable dynamic extension to both SQLite and SpatiaLite

# VirtualPG is licensed under the MPL tri-license terms; you are free to choose the best-fit license between:
# - MPL 1.1
# - GPL v2.0 or any subsequent version
# - LGPL v2.1 or any subsequent version
License:        MPLv1.1 or GPLv2+ or LGPLv2+
URL:            https://www.gaia-gis.it/fossil/virtualpg/index
Source0:        http://www.gaia-gis.it/gaia-sins/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  libspatialite-devel
BuildRequires:  libpq-devel
BuildRequires:  sqlite-devel


%description
Virtualpg supports direct SQL access to PostgreSQL and PostGIS tables,
enabling simple and straightforward data exchanges between these two
popular open source Spatial DBMSs.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -p1 -n %{name}-%{version}


%build
%configure --disable-static
# Get rid of undesirable hardcoded rpaths; workaround libtool reordering
# -Wl,--as-needed after all the libraries.
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|CC="\(.*g..\)"|CC="\1 -Wl,--as-needed"|' \
    -i libtool
%make_build


%install
%make_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'


%files
%license COPYING
%doc AUTHORS README
%{_libdir}/lib%{name}.so.*
# The unversioned mod_ also needs to be in the main package
%{_libdir}/mod_%{name}.so*

%files devel
%{_includedir}/%{name}.h
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc


%changelog
* Mon Feb 08 2021 Pavel Raiskup <praiskup@redhat.com> - 2.0.1-4
- rebuild for libpq ABI fix rhbz#1908268

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Nov 14 2020 Sandro Mani <manisandro@gmail.com> - 2.0.1-2
- Drop 0 bytes changelog
- Reformulate description
- Add libtool fix
- Remove ldconfig scriptlets

* Fri Nov 13 2020 Sandro Mani <manisandro@gmail.com> - 2.0.1-1
- Initial package
