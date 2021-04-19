# Generated by rust2rpm 16
%bcond_without check
%global debug_package %{nil}

%global crate rustc-demangle

Name:           rust-%{crate}
Version:        0.1.18
Release:        3%{?dist}
Summary:        Rust compiler symbol demangling

# Upstream license specification: MIT/Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/rustc-demangle
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Rust compiler symbol demangling.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-MIT LICENSE-APACHE
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
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Dec 11 2020 Fabio Valentini <decathorpe@gmail.com> - 0.1.18-2
- Remove dependencies on compiler internals.

* Sun Oct 25 2020 Fabio Valentini <decathorpe@gmail.com> - 0.1.18-1
- Update to version 0.1.18.

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Dec 20 19:34:07 CET 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.16-2
- Regenerate

* Wed Nov 20 2019 Josh Stone <jistone@redhat.com> - 0.1.16-1
- Update to 0.1.16

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun 22 10:46:41 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.15-2
- Regenerate

* Fri May 31 2019 Josh Stone <jistone@redhat.com> - 0.1.15-1
- Update to 0.1.15

* Sat Apr 13 2019 Josh Stone <jistone@redhat.com> - 0.1.14-1
- Update to 0.1.14

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 08 2019 Josh Stone <jistone@redhat.com> - 0.1.13-1
- Update to 0.1.13

* Thu Dec 20 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.9-3
- Run tests in infrastructure

* Fri Nov 02 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.9-2
- Adapt to new packaging

* Thu Jul 19 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.9-1
- Update to 0.1.9

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri May 04 2018 Josh Stone <jistone@redhat.com> - 0.1.8-1
- Update to 0.1.8

* Tue Feb 27 2018 Josh Stone <jistone@redhat.com> - 0.1.7-1
- Update to 0.1.7

* Sun Feb 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.6-1
- Update to 0.1.6

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 08 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.5-2
- Rebuild for rust-packaging v5

* Mon Nov 06 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.5-1
- Update to 0.1.5

* Tue Jun 13 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.4-2
- Port to use rust-packaging

* Sun Feb 26 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.4-1
- Update to 0.1.4

* Sun Feb 12 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.3-3
- Sync with rust2rpm generator

* Fri Feb 10 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.3-2
- Sync with rust2rpm generator

* Fri Feb 10 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.3-1
- Initial package