# Generated by rust2rpm 13
%bcond_without check
%global debug_package %{nil}

%global crate xkbcommon

Name:           rust-%{crate}
Version:        0.4.0
Release:        5%{?dist}
Summary:        Rust bindings and wrappers for libxkbcommon

# Upstream license specification: MIT
License:        MIT
URL:            https://crates.io/crates/xkbcommon
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Rust bindings and wrappers for libxkbcommon.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       libxkbcommon-devel

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%doc README.md
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

%package     -n %{name}+memmap-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+memmap-devel %{_description}

This package contains library source intended for building other packages
which use "memmap" feature of "%{crate}" crate.

%files       -n %{name}+memmap-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+wayland-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+wayland-devel %{_description}

This package contains library source intended for building other packages
which use "wayland" feature of "%{crate}" crate.

%files       -n %{name}+wayland-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+x11-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+x11-devel %{_description}

This package contains library source intended for building other packages
which use "x11" feature of "%{crate}" crate.

%files       -n %{name}+x11-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+xcb-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+xcb-devel %{_description}

This package contains library source intended for building other packages
which use "xcb" feature of "%{crate}" crate.

%files       -n %{name}+xcb-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires
echo 'libxkbcommon-devel'

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Mar 26 07:13:49 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.4.0-3
- Add missing Requires

* Tue Mar 24 11:28:00 PST 2020 Nikhil Jha - 0.4.0-2
- Add license to package

* Thu Feb 27 17:19:14 PST 2020 Nikhil Jha - 0.4.0-1
- Initial package
