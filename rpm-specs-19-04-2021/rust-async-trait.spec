# Generated by rust2rpm 16
%bcond_without check
%global debug_package %{nil}

%global crate async-trait

Name:           rust-%{crate}
Version:        0.1.48
Release:        1%{?dist}
Summary:        Type erasure for async trait methods

# Upstream license specification: MIT OR Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/async-trait
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Type erasure for async trait methods.}

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
* Sun Mar 28 2021 Fabio Valentini <decathorpe@gmail.com> - 0.1.48-1
- Update to version 0.1.48.
- Fixes RHBZ#1935560

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.42-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec 08 2020 Fabio Valentini <decathorpe@gmail.com> - 0.1.42-1
- Update to version 0.1.42.
- Fixes RHBZ#1900269

* Wed Oct 07 2020 Fabio Valentini <decathorpe@gmail.com> - 0.1.41-1
- Update to version 0.1.41.

* Sat Sep 05 2020 Josh Stone <jistone@redhat.com> - 0.1.40-1
- Update to 0.1.40

* Tue Aug 25 2020 Josh Stone <jistone@redhat.com> - 0.1.38-1
- Update to 0.1.38

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.36-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun 21 09:01:55 CEST 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.1.36-1
- Update to 0.1.36

* Wed May 13 2020 Josh Stone <jistone@redhat.com> - 0.1.31-1
- Update to 0.1.31

* Wed Apr 08 2020 Josh Stone <jistone@redhat.com> - 0.1.30-1
- Update to 0.1.30

* Thu Apr 02 2020 Josh Stone <jistone@redhat.com> - 0.1.29-1
- Update to 0.1.29

* Sun Mar 29 09:49:26 CEST 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.1.27-1
- Update to 0.1.27

* Fri Mar 27 11:06:03 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.1.26-1
- Update to 0.1.26

* Mon Feb 10 2020 Josh Stone <jistone@redhat.com> - 0.1.24-1
- Update to 0.1.24

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Dec 14 14:03:56 CET 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.21-1
- Initial package
