# Generated by rust2rpm 10
%bcond_without check
%global debug_package %{nil}

%global crate delta_e

Name:           rust-%{crate}
Version:        0.2.1
Release:        7%{?dist}
Summary:        Pure-Rust implementation of the CIEDE2000 algorithm

# Upstream license specification: MIT
License:        MIT
URL:            https://crates.io/crates/delta_e
Source:         %{crates_source}
# Initial patched metadata
# * Bump lab to 0.8, https://github.com/elliotekj/DeltaE/pull/5
Patch0:         delta_e-fix-metadata.diff

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
DeltaE is a pure-Rust implementation of the CIEDE2000 algorithm.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE
%doc README.md CHANGELOG.md
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
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Dec 09 20:06:14 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.2.1-6
- Bump lab to 0.8

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 24 21:38:08 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.1-1
- Update to 0.2.1

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Nov 03 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.0-2
- Adapt to new packaging

* Thu Oct 04 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.0-1
- Initial package