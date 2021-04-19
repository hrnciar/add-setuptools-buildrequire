%global forgeurl https://github.com/katie-snow/Ultimarc-linux
%global commit  540d40303d1414f9fe17fbaf178b6aa6e5feb888
%forgemeta

Name:           ultimarc
Version:        1.1.0
Release:        2%{?dist}
Summary:        Library and command line utility to configure Ultimarc boards

License:        GPLv2
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkg-config
BuildRequires:  json-c-devel
BuildRequires:  libusbx-devel
# for libudev specifically
BuildRequires:  systemd-devel

%description
This utility will configure the following Ultimarc boards: ServoStik, PACDrive,
IPAC Ultimate, I-Pac 2, I-Pac 4, Mini-Pac, JPAC, UltraStik 360, PacLED64, U-HID
and U-HID Nano. There is support for the PAC 2015 boards, UltraStik 2015 board
and the previous generation of the PAC boards. It uses JSON configuration files
to configure the different boards. It also supports the ability to change the
device ID of the UltraStik 360 boards, allowing for the configuring of four
different boards at once.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        libs
Summary:        Shared libraries for %{name}

%description    libs
Libraries to configure Ultimarc boards.

%prep
%forgesetup
# collate JSON config examples
mkdir examples
cp -P src/umtool/*.json examples

%build
./autogen.sh
%configure --disable-static
%make_build

%install
%make_install
rm -f %{buildroot}%{_libdir}/libultimarc.la
# Install udev rules
mkdir -p %{buildroot}%{_udevrulesdir}
cp -P 21-ultimarc.rules %{buildroot}%{_udevrulesdir}

%files
%license LICENSE
%doc README.md AUTHORS
%doc examples
%{_bindir}/umtool
%{_udevrulesdir}/21-ultimarc.rules

%files libs
%{_libdir}/libultimarc.so.1*

%files devel
%{_includedir}/ultimarc
%{_libdir}/libultimarc.so
%{_libdir}/pkgconfig/*.pc

%changelog
* Wed Mar 17 2021 Davide Cavalca <dcavalca@fedoraproject.org> - 1.1.0-2.20210314git540d403
- Update build requires

* Sun Mar 14 2021 Davide Cavalca <dcavalca@fedoraproject.org> - 1.1.0-1.20210314git540d403
- Initial package
