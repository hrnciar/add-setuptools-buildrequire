# Generated by rust2rpm 16
# * Tests require internet and a token
%bcond_with check
%global debug_package %{nil}

%global crate feedbin_api

Name:           rust-%{crate}
Version:        0.1.6
Release:        1%{?dist}
Summary:        Rust implementation of the Feedbin REST API

# Upstream license specification: Unlicense
License:        Unlicense
URL:            https://crates.io/crates/feedbin_api
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Rust implementation of the Feedbin REST API.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE
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
* Mon Mar 08 2021 Fabio Valentini <decathorpe@gmail.com> - 0.1.6-1
- Update to version 0.1.6.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Josh Stone <jistone@redhat.com> - 0.1.3-1
- Update to 0.1.3

* Wed Jul 22 2020 Josh Stone <jistone@redhat.com> - 0.1.1-1
- Update to 0.1.1

* Sun Jun 07 12:22:57 CEST 2020 Igor Raits <i.gnatenko.brain@gmail.com> - 0.1.0-1
- Initial package
