# Generated by rust2rpm 13
%bcond_without check
%global debug_package %{nil}

%global crate crates-io

Name:           rust-%{crate}
Version:        0.32.0
Release:        3%{?dist}
Summary:        Helpers for interacting with crates.io

# Upstream license specification: MIT OR Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/crates-io
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Helpers for interacting with crates.io.}

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
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.32.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.32.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Apr 23 2020 Josh Stone <jistone@redhat.com> - 0.32.0-1
- Update to 0.32.0

* Thu Mar 12 2020 Josh Stone <jistone@redhat.com> - 0.31.0-1
- Update to 0.31.0

* Sat Feb 29 07:19:30 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.30.0-1
- Update to 0.30.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.28.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Dec 07 2019 Josh Stone <jistone@redhat.com> - 0.28.0-1
- Update to 0.28.0

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.24.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 07 2019 Josh Stone <jistone@redhat.com> - 0.24.0-1
- Update to 0.24.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Dec 06 2018 Josh Stone <jistone@redhat.com> - 0.20.0-1
- Update to 0.20.0

* Sat Nov 17 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.19.0-1
- Update to 0.19.0

* Tue Nov 13 2018 Josh Stone <jistone@redhat.com> - 0.18.0-2
- Adapt to new packaging

* Sun Oct 21 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.18.0-1
- Update to 0.18.0

* Sat Aug 04 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.17.0-1
- Update to 0.17.0

* Sat Jul 28 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.16.0-2
- Rebuild to trigger tests

* Sun Jul 22 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.16.0-1
- Initial package
