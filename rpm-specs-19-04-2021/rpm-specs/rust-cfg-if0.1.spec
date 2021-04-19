# Generated by rust2rpm 16
%bcond_without check
%global debug_package %{nil}

%global crate cfg-if

Name:           rust-%{crate}0.1
Version:        0.1.10
Release:        3%{?dist}
Summary:        Macro to ergonomically define an item depending on a large number of #[cfg] parameters

# Upstream license specification: MIT/Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/cfg-if
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Macro to ergonomically define an item depending on a large number of #[cfg]
parameters. Structured like an if-else chain, the first matching branch is the
item that gets emitted.}

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
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Nov 24 2020 Fabio Valentini <decathorpe@gmail.com> - 0.1.10-2
- Remove dependencies on compiler internals.

* Wed Oct 14 2020 Fabio Valentini <decathorpe@gmail.com> - 0.1.10-1
- Initial compat package for cfg-if 0.1
