# Generated by rust2rpm 16
%bcond_without check
%global debug_package %{nil}

%global crate more-asserts

Name:           rust-%{crate}
Version:        0.2.1
Release:        1%{?dist}
Summary:        Small assertion library for Rust

# Upstream license specification: CC0-1.0
License:        CC0
URL:            https://crates.io/crates/more-asserts
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Small library providing additional assert_* and debug_assert_* macros.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
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
* Sat Nov 21 19:35:01 CET 2020 Olivier Lemasle <o.lemasle@gmail.com> - 0.2.1-1
- Initial package
