%global	project_name	idxd-config
%global	debug_package	%{nil}

Name:		accel-config
Version:	3.0.1
Release:	1%{?dist}
Summary:	Configure accelerator subsystem devices
# The entire source code is under GPLv2 except for accel-config
# library which is mostly LGPLv2.1, ccan/list which is BSD-MIT and
# the rest of ccan which is CC0.
License:	GPLv2 and LGPLv2+ and MIT and CC0
URL:		https://github.com/intel/%{project_name}
Source0:	%{URL}/archive/%{name}-v%{version}.tar.gz

Requires:	%{name}-libs%{?_isa} = %{version}-%{release}
BuildRequires:	gcc
BuildRequires:	autoconf
BuildRequires:	asciidoc
BuildRequires:	xmlto
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	pkgconfig(libkmod)
BuildRequires:	pkgconfig(uuid)
BuildRequires:	pkgconfig(json-c)
BuildRequires:	pkgconfig(libudev)
BuildRequires:	systemd
BuildRequires: make

# accel-config is for configuring Intel DSA (Data-Streaming
# Accelerator) subsystem in the Linux kernel. It supports x86_64 only.
ExclusiveArch:	x86_64

%description
Utility library for configuring the accelerator subsystem.

%package devel
Summary:	Development files for libaccfg
License:	LGPLv2+
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package libs
Summary:	Configuration library for accelerator subsystem devices
# All source code of configuration library is LGPLv2.1, except
# ccan/list which is BSD-MIT and the rest of ccan/ which is CC0.
License:	LGPLv2+ and MIT and CC0
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description libs
Libraries for %{name}.

%prep
%autosetup -n %{project_name}-%{name}-v%{version}

%build
echo %{version} > version
./autogen.sh
%configure --disable-static --disable-silent-rules
%make_build

%install
%make_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%check
make check

%files
%license Documentation/COPYING licenses/BSD-MIT licenses/CC0
%license licenses/accel-config-licenses LICENSE_GPL_2_0
%{_bindir}/%{name}
%{_mandir}/man1/%{name}*
%{_sysconfdir}/%{name}/%{name}.conf.sample

%files libs
%doc README.md
%license Documentation/COPYING licenses/BSD-MIT licenses/CC0
%license licenses/accel-config-licenses accfg/lib/LICENSE_LGPL_2_1
%{_libdir}/lib%{name}.so.*

%files devel
%license Documentation/COPYING
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/lib%{name}.pc

%changelog
* Thu Feb 18 2021 Yunying Sun <yunying.sun@intel.com> - 3.0.1-1
- Updated to 3.0.1 release
- Removed ix86 support as so far it supports x86_64 only
- Updated licenses following upstream

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Nov 6 2020 Yunying Sun <yunying.sun@intel.com> - 2.8-1
- Initial Packaging
