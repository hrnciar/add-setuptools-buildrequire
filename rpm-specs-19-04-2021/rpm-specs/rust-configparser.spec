# Generated by rust2rpm 16
%bcond_without check
%global debug_package %{nil}

%global crate configparser

Name:           rust-%{crate}
Version:        2.0.1
Release:        1%{?dist}
Summary:        Simple configuration parsing utility with no dependencies

# Upstream license specification: MIT OR LGPL-3.0-or-later
License:        MIT or LGPLv3+
URL:            https://crates.io/crates/configparser
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Simple configuration parsing utility with no dependencies that allows you to
parse INI and ini-style syntax. You can use this to write Rust programs which
can be customized by end users easily.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-MIT LICENSE-LGPL
%doc README.md CHANGELOG.md
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
# remove executable bits from files
chmod -x README.md CHANGELOG.md Cargo.toml.orig src/*.rs tests/*.rs
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
* Mon Apr 12 2021 Fabio Valentini <decathorpe@gmail.com> - 2.0.1-1
- Initial package
