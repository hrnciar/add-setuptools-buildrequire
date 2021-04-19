# Generated by rust2rpm 13
%bcond_without check
%global debug_package %{nil}

%global crate raw-window-handle

Name:           rust-%{crate}
Version:        0.3.3
Release:        3%{?dist}
Summary:        Interoperability library for Rust Windowing applications

# Upstream license specification: MIT
License:        MIT
URL:            https://crates.io/crates/raw-window-handle
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Interoperability library for Rust Windowing applications.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%doc README.md CHANGELOG.md
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

%package     -n %{name}+nightly-docs-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+nightly-docs-devel %{_description}

This package contains library source intended for building other packages
which use "nightly-docs" feature of "%{crate}" crate.

%files       -n %{name}+nightly-docs-devel
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
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 17:24:38 CEST 2020 returntrip <stefano@figura.im> - 0.3.3-1
- Initial package
