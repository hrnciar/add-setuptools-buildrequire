# Generated by rust2rpm 16
# * Tests require internet and a token
%bcond_with check
%global debug_package %{nil}

%global crate newsblur_api

Name:           rust-%{crate}
Version:        0.1.1
Release:        1%{?dist}
Summary:        Rust implementation of the NewsBlur-API

# Upstream license specification: GPL-3.0-or-later
License:        GPLv3+
URL:            https://crates.io/crates/newsblur_api
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Rust implementation of the NewsBlur-API.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE
%doc README.md
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
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
* Mon Mar 08 2021 Fabio Valentini <decathorpe@gmail.com> - 0.1.1-1
- Initial package
