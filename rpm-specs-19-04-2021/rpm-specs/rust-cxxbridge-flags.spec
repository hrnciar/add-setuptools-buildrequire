# Generated by rust2rpm 16
%bcond_without check
%global debug_package %{nil}

%global crate cxxbridge-flags

Name:           rust-%{crate}
Version:        0.5.10
Release:        1%{?dist}
Summary:        Compiler configuration of the `cxx` crate (implementation detail)

# Upstream license specification: MIT OR Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/cxxbridge-flags
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Compiler configuration of the `cxx` crate (implementation detail).}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+c++14-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(%{crate}/c++14) = %{version_no_tilde}

%description -n %{name}+c++14-devel %{_description}

This package contains library source intended for building other packages
which use "c++14" feature of "%{crate}" crate.

%files       -n %{name}+c++14-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+c++17-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(%{crate}/c++17) = %{version_no_tilde}

%description -n %{name}+c++17-devel %{_description}

This package contains library source intended for building other packages
which use "c++17" feature of "%{crate}" crate.

%files       -n %{name}+c++17-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+c++20-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(%{crate}/c++20) = %{version_no_tilde}

%description -n %{name}+c++20-devel %{_description}

This package contains library source intended for building other packages
which use "c++20" feature of "%{crate}" crate.

%files       -n %{name}+c++20-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires -a

%build
%cargo_build -a

%install
%cargo_install -a

%if %{with check}
%check
%cargo_test -a
%endif

%changelog
* Mon Feb 01 13:16:01 CET 2021 Jan Staněk <jstanek@redhat.com> - 0.5.10-1
- Initial package
- Manually specify provides for c++XY features (https://pagure.io/fedora-rust/rust2rpm/pull-request/123)
