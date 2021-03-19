# Generated by rust2rpm 13
# * loom isn't packaged
%bcond_with check
%global debug_package %{nil}

%global crate tokio-sync

Name:           rust-%{crate}
Version:        0.1.8
Release:        4%{?dist}
Summary:        Synchronization utilities

# Upstream license specification: MIT
License:        MIT
URL:            https://crates.io/crates/tokio-sync
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Synchronization utilities.}

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
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Feb 06 2020 Josh Stone <jistone@redhat.com> - 0.1.8-1
- Update to 0.1.8

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Nov 23 2019 Josh Stone <jistone@redhat.com> - 0.1.7-1
- Update to 0.1.7

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 21 22:07:11 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.6-2
- Regenerate

* Thu Jun 06 2019 Josh Stone <jistone@redhat.com> - 0.1.6-1
- Update to 0.1.6

* Tue Apr 23 15:11:04 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.5-1
- Update to 0.1.5

* Wed Mar 13 2019 Josh Stone <jistone@redhat.com> - 0.1.4-1
- Update to 0.1.4

* Fri Mar 01 2019 Josh Stone <jistone@redhat.com> - 0.1.3-1
- Update to 0.1.3

* Thu Feb 21 2019 Josh Stone <jistone@redhat.com> - 0.1.2-1
- Update to 0.1.2

* Mon Feb 11 2019 Josh Stone <jistone@redhat.com> - 0.1.1-1
- Update to 0.1.1

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 25 2019 Josh Stone <jistone@redhat.com> - 0.1.0-1
- Initial package
