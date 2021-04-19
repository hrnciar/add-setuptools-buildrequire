%global libseat_sover   1
%global _hardened_build 1

# seatd server is not as useful on Fedora. Disable it by default,
# but leave bcond for those who really wants to use it.
%bcond_with     server

Name:           seatd
Version:        0.5.0
Release:        1%{?dist}
Summary:        Minimal seat management daemon

License:        MIT
URL:            https://sr.ht/~kennylevinsen/seatd/
Source0:        https://git.sr.ht/~kennylevinsen/seatd/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  meson >= 0.53

BuildRequires:  pkgconfig(libsystemd)
%if %{with server}
BuildRequires:  pkgconfig(scdoc)
BuildRequires:  systemd-rpm-macros
%endif


%description
A seat management daemon, that does everything it needs to do.
Nothing more, nothing less. Depends only on libc.


%package -n     libseat
Summary:        Universal seat management library

%description -n libseat
A seat management library allowing applications to use whatever seat
management is available.

Supports:
 * seatd
 * (e)logind
 * embedded seatd for standalone operation

Each backend can be compile-time included and is runtime auto-detected or
manually selected with the LIBSEAT_BACKEND environment variable.

Which backend is in use is transparent to the application, providing a
simple common interface.


%package -n     libseat-devel
Summary:        Development files for libseat
Requires:       libseat%{?_isa} = %{version}-%{release}

%description -n libseat-devel
The libseat-devel package contains libraries and header files for
developing applications that use libseat.


%prep
%autosetup


%build
%global server_feature %{?with_server:enabled}%{!?with_server:disabled}
%meson \
    -Dexamples=disabled         \
    -Dlogind=enabled            \
    -Dseatd=%{server_feature}   \
    -Dserver=%{server_feature}
%meson_build


%install
%meson_install

%if %{with server}
install -D -m644 -pv contrib/systemd/%{name}.service \
    %{buildroot}%{_unitdir}/%{name}.service
%endif


%check
%meson_test


%if %{with server}
%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun %{name}.service

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_unitdir}/%{name}.service
%endif

%files -n libseat
%license LICENSE
%doc README.md
%{_libdir}/libseat.so.%{libseat_sover}

%files -n libseat-devel
%{_includedir}/libseat.h
%{_libdir}/libseat.so
%{_libdir}/pkgconfig/libseat.pc


%changelog
* Wed Apr 14 2021 Aleksei Bavshin <alebastr@fedoraproject.org> - 0.5.0-1
- Initial import (#1949358)
