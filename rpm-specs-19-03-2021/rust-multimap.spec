# Generated by rust2rpm 13
%bcond_without check
%global debug_package %{nil}

%global crate multimap

Name:           rust-%{crate}
Version:        0.8.2
Release:        2%{?dist}
Summary:        Multimap implementation

# Upstream license specification: MIT/Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/multimap
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Multimap implementation.}

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

%package     -n %{name}+serde-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde-devel %{_description}

This package contains library source intended for building other packages
which use "serde" feature of "%{crate}" crate.

%files       -n %{name}+serde-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+serde_impl-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde_impl-devel %{_description}

This package contains library source intended for building other packages
which use "serde_impl" feature of "%{crate}" crate.

%files       -n %{name}+serde_impl-devel
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
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Aug 26 2020 Josh Stone <jistone@redhat.com> - 0.8.2-1
- Update to 0.8.2

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Mar 30 08:11:35 CEST 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.8.1-1
- Update to 0.8.1

* Sat Feb 29 07:15:52 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.8.0-1
- Update to 0.8.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun 08 11:59:14 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.5.0-1
- Update to 0.5.0

* Sat Mar 09 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.0-7
- Adapt to new packaging

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 08 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.0-3
- Rebuild for rust-packaging v5

* Sun Dec 03 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.0-2
- Fix end-of-line

* Thu Jun 15 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.0-1
- Update to 0.4.0

* Wed Jun 14 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.0-2
- Port to use rust-packaging

* Sun Feb 26 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.0-1
- Initial package