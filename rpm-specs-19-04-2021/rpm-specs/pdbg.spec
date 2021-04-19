Name:           pdbg
Version:        3.2
Release:        2%{?dist}
Summary:        PowerPC FSI Debugger

License:        ASL 2.0
URL:            https://github.com/open-power/pdbg
Source0:        https://github.com/open-power/pdbg/archive/v%{version}/%{name}-%{version}.tar.gz
# https://github.com/open-power/pdbg/commit/9d17f334ee71e396e6180ee498248925fb54dc32
Patch0:         pdbg-3.2-libfdt.patch

BuildRequires:  gcc
BuildRequires:  autoconf automake libtool
BuildRequires:  dtc
BuildRequires:  make
BuildRequires:  ragel
BuildRequires:  libfdt-devel

# makes sense only on the host (Power-based) and the BMC (usually an embedded Arm system)
ExclusiveArch:  ppc64le

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        libs
Summary:        Library files for %{name}

%description    libs
The %{name}-libs package contains libraries for %{name}.


%description
pdbg is a simple application to allow debugging of the host POWER processors
from the BMC and the host itself. It works in a similar way to JTAG programmers
for embedded system development in that it allows you to access GPRs, SPRs and
system memory.


%prep
%autosetup -p1


%build
sh ./bootstrap.sh
%configure --disable-static
%make_build


%install
%make_install

rm -f %{buildroot}%{_libdir}/*.la


%files
%doc README.md
%{_bindir}/%{name}

%files libs
%license COPYING
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc



%changelog
* Wed Feb 03 2021 Dan Horák <dan@danny.cz> - 3.2-2
- review feedback

* Tue Jan 12 2021 Dan Horák <dan@danny.cz> - 3.2-1
- updated to 3.2

* Tue Oct 13 2020 Dan Horák <dan@danny.cz> - 3.1-1
- updated to 3.1

* Thu Sep 10 2020 Dan Horák <dan@danny.cz> - 3.0-1
- initial Fedora package
