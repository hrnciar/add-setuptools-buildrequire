# Generated by rust2rpm 10
%bcond_with check
%global debug_package %{nil}

%global crate hyper

Name:           rust-%{crate}0.10
Version:        0.10.16
Release:        7%{?dist}
Summary:        Modern HTTP library

# Upstream license specification: MIT
License:        MIT
URL:            https://crates.io/crates/hyper
Source:         %{crates_source}
# Initial patched metadata
# * Bump base64 to 0.10
Patch0:         hyper-fix-metadata.diff

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Modern HTTP library.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE
%{cargo_registry}/%{crate}-%{version}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+nightly-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+nightly-devel %{_description}

This package contains library source intended for building other packages
which use "nightly" feature of "%{crate}" crate.

%files       -n %{name}+nightly-devel
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
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.16-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.16-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.16-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Sep 11 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org>  - 0.10.16-4
- Disable tests

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun 22 16:11:56 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.10.16-2
- Regenerate

* Mon Jun 03 2019 Josh Stone <jistone@redhat.com> - 0.10.16-1
- Update to 0.10.16

* Sun Feb 10 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.10.15-3
- Run tests in infrastructure

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Nov 15 2018 Josh Stone <jistone@redhat.com> - 0.10.15-1
- Update to 0.10.15
- Adapt to new packaging

* Sun Jul 15 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.10.13-1
- Initial package
