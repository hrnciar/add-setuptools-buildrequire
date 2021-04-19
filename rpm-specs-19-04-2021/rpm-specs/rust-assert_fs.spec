# Generated by rust2rpm 16
%bcond_without check
%global debug_package %{nil}

%global crate assert_fs

Name:           rust-%{crate}
Version:        1.0.1
Release:        1%{?dist}
Summary:        Filesystem fixtures and assertions for testing

# Upstream license specification: MIT OR Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/assert_fs
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Filesystem fixtures and assertions for testing.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-APACHE LICENSE-MIT
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
* Mon Feb 08 2021 Fabio Valentini <decathorpe@gmail.com> - 1.0.1-1
- Update to version 1.0.1.
- Fixes RHBZ#1923821

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Mar 29 16:30:50 CEST 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.0.0-2
- Update globwalk to 0.8

* Fri Mar 27 11:03:45 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.0.0-1
- Update to 1.0.0

* Wed Mar 04 12:57:53 EET 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.13.1-1
- Initial package