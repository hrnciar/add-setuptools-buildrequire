# Generated by rust2rpm 13
%bcond_without check
%global debug_package %{nil}

%global crate json

Name:           rust-%{crate}
Version:        0.12.4
Release:        3%{?dist}
Summary:        JSON implementation in Rust

# Upstream license specification: MIT/Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/json
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
JSON implementation in Rust.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%doc README.md
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
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Mar 18 11:20:37 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.12.4-1
- Update to 0.12.4

* Tue Mar 17 2020 Josh Stone <jistone@redhat.com> - 0.12.3-1
- Update to 0.12.3

* Thu Mar 12 2020 Josh Stone <jistone@redhat.com> - 0.12.2-1
- Update to 0.12.2

* Wed Feb 19 16:25:07 PST 2020 Josh Stone <jistone@redhat.com> - 0.12.1-1
- Initial package
