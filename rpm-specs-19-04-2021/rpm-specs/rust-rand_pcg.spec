# Generated by rust2rpm 17
%bcond_without check
%global debug_package %{nil}

%global crate rand_pcg

Name:           rust-%{crate}
Version:        0.3.0
Release:        2%{?dist}
Summary:        Selected PCG random number generators

# Upstream license specification: MIT OR Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/rand_pcg
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Selected PCG random number generators.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%doc README.md CHANGELOG.md
%license COPYRIGHT LICENSE-APACHE LICENSE-MIT
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+serde-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde-devel %{_description}

This package contains library source intended for building other packages
which use "serde" feature of "%{crate}" crate.

%files       -n %{name}+serde-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+serde1-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde1-devel %{_description}

This package contains library source intended for building other packages
which use "serde1" feature of "%{crate}" crate.

%files       -n %{name}+serde1-devel
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
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 03 11:18:03 CET 2021 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.3.0-1
- Update to 0.3.0 (Fixes: RHBZ#1907493)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Oct 23 11:54:29 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.1-1
- Update to 0.2.1

* Sun Aug 04 10:34:54 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.0-1
- Update to 0.2.0

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 20 11:54:28 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.2-4
- Regenerate

* Sun Jun 09 15:47:34 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.2-3
- Regenerate

* Sun Mar 10 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.2-2
- Do not pull optional dependencies

* Sat Feb 23 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.2-1
- Update to 0.1.2

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Dec 12 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.1-3
- Mark bincode as dev-dependency

* Sat Dec 08 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.1-2
- Run tests in infrastructure

* Tue Nov 27 2018 Josh Stone <jistone@redhat.com> - 0.1.1-1
- Initial package