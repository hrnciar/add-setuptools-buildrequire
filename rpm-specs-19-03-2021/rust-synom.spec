# Generated by rust2rpm
# * Tests are run in infrastructure
%bcond_with check
%global debug_package %{nil}

%global crate synom

Name:           rust-%{crate}
Version:        0.11.3
Release:        17%{?dist}
Summary:        Stripped-down Nom parser used by Syn

# Upstream license specification: MIT/Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/synom
Source0:        https://crates.io/api/v1/crates/%{crate}/%{version}/download#/%{crate}-%{version}.crate
# Initial patched metadata
# * No paths
# * Bump unicode-xid to 0.1, https://github.com/dtolnay/syn/commit/98d27033fd3d39dc41cd82988d36bbb0152b2c43
Patch0:         synom-fix-metadata.diff

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-packaging
BuildRequires:  (crate(unicode-xid/default) >= 0.1.0 with crate(unicode-xid/default) < 0.2.0)
%if %{with check}
BuildRequires:  (crate(syn/full) >= 0.11.0 with crate(syn/full) < 0.12.0)
BuildRequires:  (crate(syn/parsing) >= 0.11.0 with crate(syn/parsing) < 0.12.0)
%endif

%global _description \
Stripped-down Nom parser used by Syn.

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
%{cargo_registry}/%{crate}-%{version}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.3-16
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 30 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.11.3-11
- Adapt to new packaging

* Sat Jul 28 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.11.3-10
- Rebuild to trigger tests

* Sat Jul 21 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.11.3-9
- Rebuild to trigger tests

* Sat Jul 21 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.11.3-8
- Run tests in infrastructure

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.11.3-6
- Rebuild to get back in repos

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 08 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.11.3-4
- Rebuild for rust-packaging v5

* Thu Jun 15 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.11.3-3
- Bump unicode-xid to 0.1

* Wed Jun 14 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.11.3-2
- Port to use rust-packaging

* Sun Mar 05 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.11.3-1
- Update to 0.11.3

* Tue Feb 28 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.11.2-1
- Update to 0.11.2

* Sat Feb 25 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.11.0-1
- Initial package
