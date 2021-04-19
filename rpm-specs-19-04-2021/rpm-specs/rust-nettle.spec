# Generated by rust2rpm 16
%bcond_without check
%global debug_package %{nil}

%global crate nettle

Name:           rust-%{crate}
Version:        7.0.1
Release:        1%{?dist}
Summary:        Rust bindings for the Nettle cryptographic library

# Upstream license specification: LGPL-3.0/GPL-2.0/GPL-3.0
# https://gitlab.com/sequoia-pgp/nettle-rs/-/issues/33
License:        LGPLv3 or GPLv2 or GPLv3
URL:            https://crates.io/crates/nettle
Source:         %{crates_source}
# Initial patched metadata
# * remove feature for vendoring nettle
Patch0:         nettle-fix-metadata.diff
# * drop two elliptic curves that are disabled in nettle in Fedora:
#   - nettle_get_secp_192r1
#   - nettle_get_secp_224r1
Patch1:         0001-drop-secp192r1-and-secp224r1-elliptic-curves.patch

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Rust bindings for the Nettle cryptographic library.}

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
* Thu Apr 08 2021 Fabio Valentini <decathorpe@gmail.com> - 7.0.1-1
- Initial package
