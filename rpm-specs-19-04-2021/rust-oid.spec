# Generated by rust2rpm 13
%bcond_without check
%global debug_package %{nil}

%global crate oid

Name:           rust-%{crate}
Version:        0.2.0
Release:        2%{?dist}
Summary:        Rust-native library for building, parsing, and formating Object Identifiers (OIDs)

# Upstream license specification: MIT OR Apache-2.0
# https://github.com/UnnecessaryEngineering/oid/issues/5
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/oid
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Rust-native library for building, parsing, and formating Object Identifiers
(OIDs).}

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

%package     -n %{name}+serde-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde-devel %{_description}

This package contains library source intended for building other packages
which use "serde" feature of "%{crate}" crate.

%files       -n %{name}+serde-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+serde_support-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde_support-devel %{_description}

This package contains library source intended for building other packages
which use "serde_support" feature of "%{crate}" crate.

%files       -n %{name}+serde_support-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+std-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+std-devel %{_description}

This package contains library source intended for building other packages
which use "std" feature of "%{crate}" crate.

%files       -n %{name}+std-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+u32-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+u32-devel %{_description}

This package contains library source intended for building other packages
which use "u32" feature of "%{crate}" crate.

%files       -n %{name}+u32-devel
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
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Sep 11 15:33:24 BST 2020 Peter Robinson <pbrobinson@gmail.com> - 0.2.0-1
- Initial package
