# Generated by rust2rpm 10
%bcond_without check
%global debug_package %{nil}

%global crate spin

Name:           rust-%{crate}
Version:        0.5.2
Release:        5%{?dist}
Summary:        Synchronization primitives based on spinning

# Upstream license specification: MIT
License:        MIT
URL:            https://crates.io/crates/spin
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Synchronization primitives based on spinning. They may contain data, are usable
without `std`, and static initializers are available.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE
%doc README.md
%{cargo_registry}/%{crate}-%{version}/
%exclude %{cargo_registry}/%{crate}-%{version}/script

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
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 20 2019 Josh Stone <jistone@redhat.com> - 0.5.2-1
- Update to 0.5.2

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 27 17:18:02 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.5.0-2
- Regenerate

* Sat Mar 09 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.5.0-1
- Update to 0.5.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Nov 13 2018 Josh Stone <jistone@redhat.com> - 0.4.10-1
- Update to 0.4.10
- Adapt to new packaging

* Sun Oct 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.9-2
- Run tests in infrastructure

* Sat Sep 08 2018 Josh Stone <jistone@redhat.com> - 0.4.9-1
- Update to 0.4.9

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 23 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.8-2
- Adopt to new macro

* Sun Apr 22 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.8-1
- Update to 0.4.8

* Wed Mar 14 2018 Josh Stone <jistone@redhat.com> - 0.4.7-1
- Update to 0.4.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 08 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.6-2
- Rebuild for rust-packaging v5

* Sun Nov 05 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.6-1
- Update to 0.4.6

* Wed Jun 14 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.5-2
- Port to use rust-packaging

* Sat Feb 18 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.5-1
- Initial package
