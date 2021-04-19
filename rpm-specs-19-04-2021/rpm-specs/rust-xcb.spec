# Generated by rust2rpm 13

# `cargo test` is broken
# https://github.com/rtbo/rust-xcb/issues/60
%bcond_with check
%global debug_package %{nil}

%global crate xcb

Name:           rust-%{crate}
Version:        0.9.0
Release:        5%{?dist}
Summary:        Rust bindings and wrappers for XCB

# Upstream license specification: MIT
License:        MIT
URL:            https://crates.io/crates/xcb
Source:         %{crates_source}
# cElementTree is gone in Python 3.9
# https://github.com/rtbo/rust-xcb/pull/87
Patch0:         %{crate}-0.9.0-fix_etree_import.diff

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging
BuildRequires:  pkgconfig(xcb)
BuildRequires:  python3

%global _description %{expand:
Rust bindings and wrappers for XCB.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       pkgconfig(xcb)

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE
%doc CHANGELOG.md README.md
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+composite-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+composite-devel %{_description}

This package contains library source intended for building other packages
which use "composite" feature of "%{crate}" crate.

%files       -n %{name}+composite-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+damage-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+damage-devel %{_description}

This package contains library source intended for building other packages
which use "damage" feature of "%{crate}" crate.

%files       -n %{name}+damage-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+debug_all-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+debug_all-devel %{_description}

This package contains library source intended for building other packages
which use "debug_all" feature of "%{crate}" crate.

%files       -n %{name}+debug_all-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+dpms-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+dpms-devel %{_description}

This package contains library source intended for building other packages
which use "dpms" feature of "%{crate}" crate.

%files       -n %{name}+dpms-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+dri2-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+dri2-devel %{_description}

This package contains library source intended for building other packages
which use "dri2" feature of "%{crate}" crate.

%files       -n %{name}+dri2-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+dri3-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+dri3-devel %{_description}

This package contains library source intended for building other packages
which use "dri3" feature of "%{crate}" crate.

%files       -n %{name}+dri3-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+ge-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+ge-devel %{_description}

This package contains library source intended for building other packages
which use "ge" feature of "%{crate}" crate.

%files       -n %{name}+ge-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+glx-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+glx-devel %{_description}

This package contains library source intended for building other packages
which use "glx" feature of "%{crate}" crate.

%files       -n %{name}+glx-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+present-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+present-devel %{_description}

This package contains library source intended for building other packages
which use "present" feature of "%{crate}" crate.

%files       -n %{name}+present-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+randr-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+randr-devel %{_description}

This package contains library source intended for building other packages
which use "randr" feature of "%{crate}" crate.

%files       -n %{name}+randr-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+record-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+record-devel %{_description}

This package contains library source intended for building other packages
which use "record" feature of "%{crate}" crate.

%files       -n %{name}+record-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+render-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+render-devel %{_description}

This package contains library source intended for building other packages
which use "render" feature of "%{crate}" crate.

%files       -n %{name}+render-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+res-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+res-devel %{_description}

This package contains library source intended for building other packages
which use "res" feature of "%{crate}" crate.

%files       -n %{name}+res-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+screensaver-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+screensaver-devel %{_description}

This package contains library source intended for building other packages
which use "screensaver" feature of "%{crate}" crate.

%files       -n %{name}+screensaver-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+shape-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+shape-devel %{_description}

This package contains library source intended for building other packages
which use "shape" feature of "%{crate}" crate.

%files       -n %{name}+shape-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+shm-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+shm-devel %{_description}

This package contains library source intended for building other packages
which use "shm" feature of "%{crate}" crate.

%files       -n %{name}+shm-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+sync-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+sync-devel %{_description}

This package contains library source intended for building other packages
which use "sync" feature of "%{crate}" crate.

%files       -n %{name}+sync-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+thread-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+thread-devel %{_description}

This package contains library source intended for building other packages
which use "thread" feature of "%{crate}" crate.

%files       -n %{name}+thread-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+x11-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+x11-devel %{_description}

This package contains library source intended for building other packages
which use "x11" feature of "%{crate}" crate.

%files       -n %{name}+x11-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+xevie-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+xevie-devel %{_description}

This package contains library source intended for building other packages
which use "xevie" feature of "%{crate}" crate.

%files       -n %{name}+xevie-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+xf86dri-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+xf86dri-devel %{_description}

This package contains library source intended for building other packages
which use "xf86dri" feature of "%{crate}" crate.

%files       -n %{name}+xf86dri-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+xf86vidmode-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+xf86vidmode-devel %{_description}

This package contains library source intended for building other packages
which use "xf86vidmode" feature of "%{crate}" crate.

%files       -n %{name}+xf86vidmode-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+xfixes-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+xfixes-devel %{_description}

This package contains library source intended for building other packages
which use "xfixes" feature of "%{crate}" crate.

%files       -n %{name}+xfixes-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+xinerama-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+xinerama-devel %{_description}

This package contains library source intended for building other packages
which use "xinerama" feature of "%{crate}" crate.

%files       -n %{name}+xinerama-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+xinput-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+xinput-devel %{_description}

This package contains library source intended for building other packages
which use "xinput" feature of "%{crate}" crate.

%files       -n %{name}+xinput-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+xkb-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+xkb-devel %{_description}

This package contains library source intended for building other packages
which use "xkb" feature of "%{crate}" crate.

%files       -n %{name}+xkb-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+xlib_xcb-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+xlib_xcb-devel %{_description}

This package contains library source intended for building other packages
which use "xlib_xcb" feature of "%{crate}" crate.

%files       -n %{name}+xlib_xcb-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+xprint-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+xprint-devel %{_description}

This package contains library source intended for building other packages
which use "xprint" feature of "%{crate}" crate.

%files       -n %{name}+xprint-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+xselinux-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+xselinux-devel %{_description}

This package contains library source intended for building other packages
which use "xselinux" feature of "%{crate}" crate.

%files       -n %{name}+xselinux-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+xtest-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+xtest-devel %{_description}

This package contains library source intended for building other packages
which use "xtest" feature of "%{crate}" crate.

%files       -n %{name}+xtest-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+xv-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+xv-devel %{_description}

This package contains library source intended for building other packages
which use "xv" feature of "%{crate}" crate.

%files       -n %{name}+xv-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+xvmc-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+xvmc-devel %{_description}

This package contains library source intended for building other packages
which use "xvmc" feature of "%{crate}" crate.

%files       -n %{name}+xvmc-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jun 27 2020 Michel Alexandre Salim <salimma@fedoraproject.org> - 0.9.0-3
- devel package now pulls in pkgconfig(xcb) for building dependents

* Mon Jun  8 2020 Michel Alexandre Salim <salimma@fedoraproject.org> - 0.9.0-2
- add missing BR on python3
- Fix build on Python 3.9

* Fri May 22 12:59:18 PDT 2020 Michel Alexandre Salim <salimma@fedoraproject.org> - 0.9.0-1
- Initial package