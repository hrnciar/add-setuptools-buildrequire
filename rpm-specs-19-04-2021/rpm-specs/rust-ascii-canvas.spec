# Generated by rust2rpm 16
# * tests fail to compile (not all necessary .rs files are included)
%bcond_with check
%global debug_package %{nil}

%global crate ascii-canvas

Name:           rust-%{crate}
Version:        2.0.0
Release:        1%{?dist}
Summary:        Simple canvas for drawing lines and styled text and emitting to the terminal

# Upstream license specification: Apache-2.0/MIT
License:        ASL 2.0 or MIT
URL:            https://crates.io/crates/ascii-canvas
Source:         %{crates_source}
# Initial patched metadata
# * bump term from 0.5 to 0.6:
#   https://github.com/nikomatsakis/ascii-canvas/commit/73c8d76
Patch0:         ascii-canvas-fix-metadata.diff

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Simple canvas for drawing lines and styled text and emitting to the terminal.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-APACHE LICENSE-MIT
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
* Thu Apr 08 2021 Fabio Valentini <decathorpe@gmail.com> - 2.0.0-1
- Initial package