# Generated by rust2rpm 13
%bcond_with check
%global debug_package %{nil}

%global crate pkcs11

Name:           rust-%{crate}
Version:        0.5.0
Release:        2%{?dist}
Summary:        Rust PKCS#11 Library

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            https://crates.io/crates/pkcs11
Source:         %{crates_source}
# Initial patched metadata
Patch0:         pkcs11-fix-metadata.diff
# fix not in a release yet: https://github.com/mheese/rust-pkcs11/commit/901ae8f147586585f81f9ae8a625caf9dc8d76fc
Patch1:         pkcs11-fix-libloading.patch

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Rust PKCS#11 Library.}

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
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Sep 15 00:35:27 BST 2020 Peter Robinson <pbrobinson@gmail.com> - 0.5.0-1
- Initial package