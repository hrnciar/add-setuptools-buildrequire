# Generated by rust2rpm 13
%bcond_with check
%global debug_package %{nil}

%global crate itertools

Name:           rust-%{crate}0.8
Version:        0.8.2
Release:        3%{?dist}
Summary:        Extra iterator adaptors, iterator methods, free functions, and macros

# Upstream license specification: MIT/Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/itertools
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Extra iterator adaptors, iterator methods, free functions, and macros.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-MIT LICENSE-APACHE
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+use_std-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+use_std-devel %{_description}

This package contains library source intended for building other packages
which use "use_std" feature of "%{crate}" crate.

%files       -n %{name}+use_std-devel
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
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Mar 17 17:19:16 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.8.2-1
- Initial package
