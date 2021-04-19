# Generated by rust2rpm 16
%bcond_without check
%global debug_package %{nil}

%global crate glutin

Name:           rust-%{crate}
Version:        0.26.0
Release:        1%{?dist}
Summary:        Cross-platform OpenGL context provider

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            https://crates.io/crates/glutin
Source:         %{crates_source}
# Initial patched metadata
# * Removes Macos and Windows dependencies
Patch0:         glutin-fix-metadata.diff

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Cross-platform OpenGL context provider.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+glutin_glx_sys-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+glutin_glx_sys-devel %{_description}

This package contains library source intended for building other packages
which use "glutin_glx_sys" feature of "%{crate}" crate.

%files       -n %{name}+glutin_glx_sys-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+serde-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde-devel %{_description}

This package contains library source intended for building other packages
which use "serde" feature of "%{crate}" crate.

%files       -n %{name}+serde-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+wayland-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+wayland-devel %{_description}

This package contains library source intended for building other packages
which use "wayland" feature of "%{crate}" crate.

%files       -n %{name}+wayland-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+wayland-client-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+wayland-client-devel %{_description}

This package contains library source intended for building other packages
which use "wayland-client" feature of "%{crate}" crate.

%files       -n %{name}+wayland-client-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+wayland-egl-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+wayland-egl-devel %{_description}

This package contains library source intended for building other packages
which use "wayland-egl" feature of "%{crate}" crate.

%files       -n %{name}+wayland-egl-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+x11-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+x11-devel %{_description}

This package contains library source intended for building other packages
which use "x11" feature of "%{crate}" crate.

%files       -n %{name}+x11-devel
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
* Sat Feb 06 12:25:00 CET 2021 returntrip <stefano@figura.im> - 0.26.0-1
- Update to version 0.26
- Fixes RHBZ#1906629

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.25.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Oct 15 17:00:09 CEST 2020 returntrip <stefano@figura.im> - 0.25.1-1
- Initial package
