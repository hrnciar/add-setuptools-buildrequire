# Generated by rust2rpm 16
%bcond_without check
%global debug_package %{nil}

%global crate adler

Name:           rust-%{crate}
Version:        1.0.1
Release:        2%{?dist}
Summary:        Simple clean-room implementation of the Adler-32 checksum

# Upstream license specification: 0BSD OR MIT OR Apache-2.0
License:        0BSD or MIT or ASL 2.0
URL:            https://crates.io/crates/adler
Source:         %{crates_source}

# https://github.com/jonas-schievink/adler/issues/8
# patch a doc test that depends on byte order
Patch1:         0001-fix-endianness-in-doctests.patch

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Simple clean-room implementation of the Adler-32 checksum.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-0BSD LICENSE-APACHE LICENSE-MIT
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

%package     -n %{name}+std-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+std-devel %{_description}

This package contains library source intended for building other packages
which use "std" feature of "%{crate}" crate.

%files       -n %{name}+std-devel
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
* Thu Feb 25 2021 Fabio Valentini <decathorpe@gmail.com> - 1.0.1-2
- Patch a doc test that depends on byte order.

* Thu Feb 25 2021 Fabio Valentini <decathorpe@gmail.com> - 1.0.1-1
- Update to version 1.0.1.
- Fixes RHBZ#1895724

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Oct 01 2020 Fabio Valentini <decathorpe@gmail.com> - 0.2.3-1
- Initial package
