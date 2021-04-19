# Generated by rust2rpm 16
%bcond_without check
%global debug_package %{nil}

%global crate dirs-sys-next

Name:           rust-%{crate}
Version:        0.1.2
Release:        2%{?dist}
Summary:        System-level helper functions for the dirs and directories crates

# Upstream license specification: MIT OR Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/dirs-sys-next
Source:         %{crates_source}
# Initial patched metadata
# * No windows/redox
Patch0:         dirs-sys-next-fix-metadata.diff

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
System-level helper functions for the dirs and directories crates.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-MIT LICENSE-APACHE
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
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Jan 09 2021 Fabio Valentini <decathorpe@gmail.com> - 0.1.2-1
- Update to version 0.1.2.
- Fixes RHBZ#1914495

* Sun Dec 27 11:08:23 CET 2020 Igor Raits <igor.raits@gmail.com> - 0.1.1-1
- Initial package (Closes: RHBZ#1911048)