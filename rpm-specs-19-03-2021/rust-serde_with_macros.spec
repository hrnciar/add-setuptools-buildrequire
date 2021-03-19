# Generated by rust2rpm 16
%bcond_without check
%global debug_package %{nil}

%global crate serde_with_macros

Name:           rust-%{crate}
Version:        1.4.1
Release:        1%{?dist}
Summary:        Proc-macro library for serde_with

# Upstream license specification: MIT OR Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/serde_with_macros
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Proc-macro library for serde_with.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-APACHE LICENSE-MIT
%doc README.md CHANGELOG.md
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
* Sat Feb 27 2021 Fabio Valentini <decathorpe@gmail.com> - 1.4.1-1
- Update to version 1.4.1.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Nov 27 2020 Fabio Valentini <decathorpe@gmail.com> - 1.3.0-1
- Update to version 1.3.0.
- Fixes RHBZ#1900436

* Wed Oct 07 2020 Fabio Valentini <decathorpe@gmail.com> - 1.2.2-1
- Update to version 1.2.2.

* Mon Oct 05 2020 Fabio Valentini <decathorpe@gmail.com> - 1.2.1-1
- Update to version 1.2.1.

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Feb 21 22:11:52 EET 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.1.0-1
- Initial package