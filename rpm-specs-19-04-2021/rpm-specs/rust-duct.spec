# Generated by rust2rpm 16
%bcond_without check
%global debug_package %{nil}

# https://github.com/oconnor663/duct.rs/issues/73
%global __cargo_is_bin() false

%global crate duct

Name:           rust-%{crate}
Version:        0.13.5
Release:        1%{?dist}
Summary:        Library for running child processes

# Upstream license specification: MIT
License:        MIT
URL:            https://crates.io/crates/duct
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Library for running child processes.}

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
* Sun Feb 07 2021 Fabio Valentini <decathorpe@gmail.com> - 0.13.5-1
- Update to version 0.13.5.
- Fixes RHBZ#1925327

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.4-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Apr 14 2020 Josh Stone <jistone@redhat.com> - 0.13.4-1
- Update to 0.13.4

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 19 2019 Josh Stone <jistone@redhat.com> - 0.13.3-1
- Update to 0.13.3

* Thu Sep 26 19:57:37 CEST 2019 Robert-Andr?? Mauchin <zebob.m@gmail.com> - 0.13.0-1
- Release 0.13.0 (#1754305)

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jul 07 16:23:40 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.12.0-1
- Initial package
