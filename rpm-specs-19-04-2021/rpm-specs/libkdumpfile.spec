Name:           libkdumpfile
Version:        0.4.0
Release:        2%{?dist}
Summary:        Kernel coredump file access

License:        LGPLv3+ or GPLv2+
URL:            https://github.com/ptesarik/libkdumpfile
Source0:        %{url}/releases/download/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  doxygen
BuildRequires:  make
BuildRequires:  sed
BuildRequires:  lzo-devel
BuildRequires:  python3-devel
BuildRequires:  snappy-devel
BuildRequires:  zlib-devel

%description
libkdumpfile is a library to read kdump-compressed kernel core dumps.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Documentation for %{name}

%description    doc
The %{name}-doc package contains documentation for %{name}.

%package        python
Summary:        Python bindings for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    python
The %{name}-python package contains Python bindings for %{name}.

%package        util
Summary:        Utilities to read kernel core dumps
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    util
The %{name}-devel package contains misc utilities built with %{name}.

%prep
%autosetup
# Remove unneeded shebang
sed -e "\|#!/usr/bin/env python|d" -i python/*/*.py

%build
%configure --disable-static
%make_build
%{__make} doxygen-doc


%install
%make_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%files
%license COPYING COPYING.GPLv2 COPYING.GPLv3 COPYING.LGPLv3
%doc README.md NEWS 
%{_libdir}/libaddrxlat.so.1*
%{_libdir}/libkdumpfile.so.8*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/libaddrxlat.pc
%{_libdir}/pkgconfig/libkdumpfile.pc

%files doc
%license COPYING COPYING.GPLv2 COPYING.GPLv3 COPYING.LGPLv3
%doc doc/html

%files python
%{python3_sitelib}/addrxlat
%{python3_sitearch}/_addrxlat.so*
%{python3_sitelib}/kdumpfile
%{python3_sitearch}/_kdumpfile.so*

%files util
%{_bindir}/*

%changelog
* Fri Apr  2 2021 Davide Cavalca <dcavalca@fedoraproject.org> - 0.4.0-2
- Fix license

* Fri Feb 26 2021 Davide Cavalca <dcavalca@fedoraproject.org> - 0.4.0-1
- Initial package
