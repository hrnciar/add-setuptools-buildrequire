# Generated by rust2rpm 13
%bcond_without check
%global debug_package %{nil}

%global crate pest_meta

Name:           rust-%{crate}
Version:        2.1.3
Release:        3%{?dist}
Summary:        Pest meta language parser and validator

# Upstream license specification: MIT/Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/pest_meta
Source:         %{crates_source}
# Initial patched metadata
# * Remove sha-1 build-dep because build.rs is not shipped
Patch0:         pest_meta-fix-metadata.diff

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Pest meta language parser and validator.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-APACHE LICENSE-MIT
%doc _README.md
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
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Feb 23 10:27:28 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 2.1.3-1
- Update to 2.1.3

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 16 15:40:37 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.1.2-1
- Update to 2.1.2

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 20 09:44:41 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.1.1-2
- Regenerate

* Mon Apr 15 2019 Josh Stone <jistone@redhat.com> - 2.1.1-1
- Update to 2.1.1

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 08 2019 Josh Stone <jistone@redhat.com> - 2.1.0-1
- Update to 2.1.0

* Sat Nov 10 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.0.3-1
- Initial package
