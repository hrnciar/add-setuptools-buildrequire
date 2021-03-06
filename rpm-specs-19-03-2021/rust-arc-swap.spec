# Generated by rust2rpm 13
# * model is not packaged, proptest is outdated
%bcond_with check
%global debug_package %{nil}

%global crate arc-swap

Name:           rust-%{crate}
Version:        0.4.7
Release:        3%{?dist}
Summary:        Atomically swappable Arc

# Upstream license specification: Apache-2.0/MIT
License:        ASL 2.0 or MIT
URL:            https://crates.io/crates/arc-swap
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Atomically swappable Arc.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-APACHE LICENSE-MIT
%doc README.md
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+weak-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+weak-devel %{_description}

This package contains library source intended for building other packages
which use "weak" feature of "%{crate}" crate.

%files       -n %{name}+weak-devel
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
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 10 2020 Josh Stone <jistone@redhat.com> - 0.4.7-1
- Update to 0.4.7

* Tue Apr 21 2020 Josh Stone <jistone@redhat.com> - 0.4.6-1
- Update to 0.4.6

* Wed Mar 18 11:12:25 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.4.5-1
- Update to 0.4.5

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 19 08:08:12 CET 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.4-1
- Update to 0.4.4

* Sat Sep 21 13:32:29 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.3-1
- Update to 0.4.3

* Sun Sep 08 09:32:48 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.2-1
- Update to 0.4.2

* Tue Aug 06 08:37:56 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.1-1
- Update to 0.4.1

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun 22 10:20:25 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.11-2
- Regenerate

* Mon Apr 15 2019 Josh Stone <jistone@redhat.com> - 0.3.11-1
- Update to 0.3.11

* Sat Apr 13 2019 Josh Stone <jistone@redhat.com> - 0.3.10-1
- Update to 0.3.10

* Sat Apr 06 11:05:36 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.9-1
- Update to 0.3.9

* Wed Mar 27 22:00:24 CET 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.8-1
- Update to 0.3.8

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 07 2019 Josh Stone <jistone@redhat.com> - 0.3.7-1
- Update to 0.3.7

* Thu Nov 29 2018 Josh Stone <jistone@redhat.com> - 0.3.6-1
- Update to 0.3.6

* Thu Nov 15 2018 Josh Stone <jistone@redhat.com> - 0.3.5-1
- Initial package
