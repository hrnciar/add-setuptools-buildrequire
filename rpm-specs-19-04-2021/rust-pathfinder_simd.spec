# Generated by rust2rpm 17
%bcond_without check
%global debug_package %{nil}

%global crate pathfinder_simd

Name:           rust-%{crate}
Version:        0.5.0
Release:        3%{?dist}
Summary:        Simple SIMD library

# Upstream license specification: MIT/Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/pathfinder_simd
Source:         %{crates_source}
# Initial patched metadata
# * Bump rustc_version to 0.3, https://github.com/servo/pathfinder/pull/456
Patch0:         pathfinder_simd-fix-metadata.diff

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Simple SIMD library.}

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

%package     -n %{name}+pf-no-simd-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+pf-no-simd-devel %{_description}

This package contains library source intended for building other packages
which use "pf-no-simd" feature of "%{crate}" crate.

%files       -n %{name}+pf-no-simd-devel
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
# this test fails with floating point accuracy issues
%cargo_test -- -- --skip test_f32x4_basic_ops
%endif

%changelog
* Mon Mar 29 20:21:59 CEST 2021 Robert-André Mauchin <zebob.m@gmail.com> - 0.5.0-3
- Bump rustc_version to 0.3

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Sep 19 2020 Fabio Valentini <decathorpe@gmail.com> - 0.5.0-1
- Initial package
