# Generated by rust2rpm 13
%bcond_without check
%global debug_package %{nil}

%global crate libflate_lz77

Name:           rust-%{crate}
Version:        1.0.0
Release:        4%{?dist}
Summary:        LZ77 encoder for libflate crate

# Upstream license specification: MIT
# https://github.com/sile/libflate/pull/50
License:        MIT
URL:            https://crates.io/crates/libflate_lz77
Source:         %{crates_source}
# Initial patched metadata
# * Update libflate to 1, upstreamed
Patch0:         libflate_lz77-fix-metadata.diff

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
LZ77 encoder for libflate crate.}

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
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon May 18 12:46:00 CEST 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.0.0-2
- Update libflate to 1

* Sun May 17 09:26:18 CEST 2020 Igor Raits <i.gnatenko.brain@gmail.com> - 1.0.0-1
- Initial package