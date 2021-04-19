# Generated by rust2rpm 17
%bcond_without check
%global debug_package %{nil}

%global crate smawk

Name:           rust-%{crate}
Version:        0.3.1
Release:        1%{?dist}
Summary:        Functions for finding row-minima in a totally monotone matrix

# Upstream license specification: MIT
License:        MIT
URL:            https://crates.io/crates/smawk
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Functions for finding row-minima in a totally monotone matrix.}

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
* Wed Mar 03 2021 Fabio Valentini <decathorpe@gmail.com> - 0.3.1-1
- Update to version 0.3.1.
- Fixes RHBZ#1922635

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec 29 17:22:57 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.3.0-1
- Drop ndarray feature due to the broken deps

* Sun Dec 27 14:56:50 CET 2020 Igor Raits <igor.raits@gmail.com> - 0.3.0-1
- Initial package
