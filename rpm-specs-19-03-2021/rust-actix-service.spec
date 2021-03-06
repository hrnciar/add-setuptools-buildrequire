# Generated by rust2rpm 13
%bcond_without check
%global debug_package %{nil}

%global crate actix-service

Name:           rust-%{crate}
Version:        1.0.6
Release:        2%{?dist}
Summary:        Actix service

# Upstream license specification: MIT OR Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/actix-service
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Service trait and combinators for representing asynchronous request/response
operations.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-MIT LICENSE-APACHE
%doc CHANGES.md README.md
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
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Sep 12 2020 Josh Stone <jistone@redhat.com> - 1.0.6-1
- Update to 1.0.6

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Mar 02 08:51:48 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.0.5-1
- Update to 1.0.5

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Dec 27 08:24:29 CET 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.1-1
- Update to 1.0.1

* Sat Dec 14 13:18:23 CET 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.0-1
- Update to 1.0.0

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 23 11:06:09 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.1-2
- Regenerate

* Thu Jun 06 13:58:50 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.1-1
- Update to 0.4.1

* Fri May 31 09:17:02 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.0-1
- Initial package
