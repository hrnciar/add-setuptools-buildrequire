# Generated by rust2rpm 15
%bcond_without check
%global debug_package %{nil}

%global crate v_escape_derive

Name:           rust-%{crate}
Version:        0.8.4
Release:        2%{?dist}
Summary:        Procedural macro package for v_escape

# Upstream license specification: MIT/Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/v_escape_derive
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Procedural macro package for v_escape.}

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
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov 09 2020 Fabio Valentini <decathorpe@gmail.com> - 0.8.4-1
- Update to version 0.8.4.
- Fixes RHBZ#1887222

* Thu Oct 01 2020 Fabio Valentini <decathorpe@gmail.com> - 0.8.3-1
- Update to version 0.8.3.

* Mon Sep 21 2020 Fabio Valentini <decathorpe@gmail.com> - 0.8.1-1
- Update to version 0.8.1.

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Sep 26 13:10:50 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.5.6-1
- Update to 0.5.6

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun 22 23:32:49 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.5.3-2
- Regenerate

* Thu May 30 18:17:29 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.5.3-1
- Initial package