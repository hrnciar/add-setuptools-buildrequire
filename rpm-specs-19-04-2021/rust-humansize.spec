# Generated by rust2rpm 10
%bcond_without check
%global debug_package %{nil}

%global crate humansize

Name:           rust-%{crate}
Version:        1.1.0
Release:        6%{?dist}
Summary:        Configurable crate to easily represent file sizes in a human-readable format

# Upstream license specification: MIT/Apache-2.0
# https://github.com/LeopoldArkham/humansize/issues/16
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/humansize
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Configurable crate to easily represent file sizes in a human-readable format.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%doc README.md
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
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun 22 20:39:37 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.1.0-2
- Regenerate

* Fri May 31 11:25:30 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.1.0-1
- Initial package
