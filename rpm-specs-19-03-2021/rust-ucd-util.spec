# Generated by rust2rpm 13
%bcond_without check
%global debug_package %{nil}

%global crate ucd-util

Name:           rust-%{crate}
Version:        0.1.8
Release:        3%{?dist}
Summary:        Small utility library for working with the Unicode character database

# Upstream license specification: MIT/Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/ucd-util
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Small utility library for working with the Unicode character database.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-MIT LICENSE-APACHE LICENSE-UNICODE
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
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Mar 13 2020 Josh Stone <jistone@redhat.com> - 0.1.8-1
- Update to 0.1.8

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Josh Stone <jistone@redhat.com> - 0.1.7-1
- Update to 0.1.7

* Wed Jan 15 2020 Josh Stone <jistone@redhat.com> - 0.1.6-1
- Update to 0.1.6

* Sun Jul 28 18:14:57 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.5-1
- Update to 0.1.5

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 20 09:37:11 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.3-4
- Regenerate

* Sun Jun 09 11:05:52 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.3-3
- Regenerate

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Nov 16 2018 Josh Stone <jistone@redhat.com> - 0.1.3-1
- Update to 0.1.3

* Tue Nov 13 2018 Josh Stone <jistone@redhat.com> - 0.1.2-1
- Update to 0.1.2

* Fri Oct 26 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.1-4
- Adapt to new packaging

* Sun Oct 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.1-3
- Run tests in infrastructure

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 07 2018 Josh Stone <jistone@redhat.com> - 0.1.1-1
- Initial package
