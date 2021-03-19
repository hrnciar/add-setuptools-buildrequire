# Generated by rust2rpm 16
%bcond_without check

%global crate leb128

Name:           rust-%{crate}
Version:        0.2.4
Release:        2%{?dist}
Summary:        DWARF's LEB128 encoding library and REPL

# Upstream license specification: Apache-2.0/MIT
License:        ASL 2.0 or MIT
URL:            https://crates.io/crates/leb128
Source:         %{crates_source}
# Use latest version of dependency
Patch0:         dependency-version.diff
# Add exclusions to Cargo.toml
# Cf. upstream PR: https://github.com/gimli-rs/leb128/pull/17
Patch1:         exclude.diff

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Read and write DWARF's "Little Endian Base 128" (LEB128) variable length
integer encoding.}

%description %{_description}

%if ! %{__cargo_skip_build}
%package     -n %{crate}
Summary:        %{summary}

%description -n %{crate} %{_description}

%files       -n %{crate}
%doc ./README.md
%license LICENSE-APACHE LICENSE-MIT
%{_bindir}/leb128-repl
%endif

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%doc ./README.md
%license LICENSE-APACHE LICENSE-MIT
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
# Fix permissions - Upstream PR: https://github.com/gimli-rs/leb128/pull/16
chmod -x benches/bench.rs

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
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Nov 21 20:04:58 CET 2020 Olivier Lemasle <o.lemasle@gmail.com> - 0.2.4-1
- Initial package
