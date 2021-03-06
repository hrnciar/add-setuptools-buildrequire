# Generated by rust2rpm 13
%bcond_without check
%global debug_package %{nil}

%global crate escaper

Name:           rust-%{crate}
Version:        0.1.0
Release:        3%{?dist}
Summary:        Library for HTML entity encoding and decoding

# Upstream license specification: Apache-2.0 / MIT / MPL-2.0
License:        ASL 2.0 or MIT or MPLv2.0
URL:            https://crates.io/crates/escaper
Source:         %{crates_source}
# Initial patched metadata
# * Drop num, upgrade rand, https://github.com/dignifiedquire/rust-escaper/pull/2
Patch0:         escaper-fix-metadata.diff

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Library for HTML entity encoding and decoding.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-MIT LICENSE-APACHE
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
# Drop num for real
sed -i -e "/extern crate num;/d" tests/test.rs benches/bench.rs
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
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 12 17:10:24 CEST 2020 Igor Raits <i.gnatenko.brain@gmail.com> - 0.1.0-1
- Initial package
