# Generated by rust2rpm 13
%bcond_without check
%global debug_package %{nil}

%global crate getch

Name:           rust-%{crate}
Version:        0.2.1
Release:        3%{?dist}
Summary:        Portable implementation of getch, using _getch on Windows, and termios on Unix

# Upstream license specification: Apache-2.0
# https://nest.pijul.com/pijul_org/getch/discussions/4
License:        ASL 2.0
URL:            https://crates.io/crates/getch
Source:         %{crates_source}
# Initial patched metadata
# * Update termios to 0.3
Patch0:         getch-fix-metadata.diff

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Portable implementation of getch, using _getch on Windows, and termios on Unix.}

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
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Feb 14 10:44:31 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.2.1-1
- Initial package
