# Generated by rust2rpm 13
%bcond_without check
%global debug_package %{nil}

%global crate actix-utils

Name:           rust-%{crate}
Version:        2.0.0
Release:        2%{?dist}
Summary:        Various network related services and utilities for Actix

# Upstream license specification: MIT OR Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/actix-utils
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Various network related services and utilities for the Actix ecosystem.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-MIT LICENSE-APACHE
%doc CHANGES.md
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
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Sep 21 2020 Fabio Valentini <decathorpe@gmail.com> - 2.0.0-1
- Update to version 2.0.0.

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Feb 11 10:03:52 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.0.6-1
- Update to 1.0.6

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Dec 20 11:27:03 CET 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.4-1
- Update to 1.0.4

* Sat Dec 14 13:33:50 CET 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.3-1
- Update to 1.0.3

* Sat Aug 03 13:54:35 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.5-1
- Update to 0.4.5

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 30 12:04:33 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.2-1
- Update to 0.4.2

* Sat Jun 22 23:32:08 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.1-2
- Regenerate

* Fri May 31 09:19:17 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.1-1
- Initial package
