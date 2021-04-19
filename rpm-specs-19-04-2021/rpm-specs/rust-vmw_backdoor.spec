# Generated by rust2rpm 13
%bcond_without check
%global debug_package %{nil}

%global crate vmw_backdoor

Name:           rust-%{crate}
Version:        0.2.0
Release:        2%{?dist}
Summary:        Pure-Rust library for VMware host-guest protocol ("VMXh backdoor")

# Upstream license specification: MIT/Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/vmw_backdoor
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Pure-Rust library for VMware host-guest protocol ("VMXh backdoor").}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%{cargo_registry}/%{crate}-%{version_no_tilde}/
%doc README.md
%license COPYRIGHT LICENSE-APACHE-2.0 LICENSE-MIT

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
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Oct 21 2020 Sohan Kunkerkar <sohank2602@gmail.com> - 0.2.0-1
- Update to 0.2.0

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 11 2020 Josh Stone <jistone@redhat.com> - 0.1.3-1
- Update to 0.1.3

* Sat Apr 25 15:45:50 UTC 2020 Robert Fairley <rfairley@redhat.com> - 0.1.2-1
- Initial package