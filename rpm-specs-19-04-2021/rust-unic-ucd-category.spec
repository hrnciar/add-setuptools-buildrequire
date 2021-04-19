# Generated by rust2rpm 9
%bcond_with check
%global debug_package %{nil}

%global crate unic-ucd-category

Name:           rust-%{crate}
Version:        0.9.0
Release:        5%{?dist}
Summary:        UNIC — Unicode Character Database — General Category

# Upstream license specification: MIT/Apache-2.0
# https://github.com/open-i18n/rust-unic/issues/267
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/unic-ucd-category
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-packaging
BuildRequires:  (crate(matches/default) >= 0.1.0 with crate(matches/default) < 0.2.0)
BuildRequires:  (crate(unic-char-property/default) >= 0.9.0 with crate(unic-char-property/default) < 0.10.0)
BuildRequires:  (crate(unic-char-range/default) >= 0.9.0 with crate(unic-char-range/default) < 0.10.0)
BuildRequires:  (crate(unic-ucd-version/default) >= 0.9.0 with crate(unic-ucd-version/default) < 0.10.0)

%global _description %{expand:
UNIC — Unicode Character Database — General Category.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%{cargo_registry}/%{crate}-%{version}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 11:41:50 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.9.0-1
- Initial package
