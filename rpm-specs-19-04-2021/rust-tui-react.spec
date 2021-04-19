# Generated by rust2rpm 17
%bcond_without check
%global debug_package %{nil}

%global crate tui-react

Name:           rust-%{crate}
Version:        0.14.0
Release:        2%{?dist}
Summary:        TUI widgets using a react-like paradigm

# Upstream license specification: MIT
License:        MIT
URL:            https://crates.io/crates/tui-react
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
TUI widgets using a react-like paradigm, allowing mutable component state and
render properties.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE
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
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 10 19:51:19 CET 2021 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.14.0-1
- Update to 0.14.0 (Fixes: RHBZ#1912189)

* Tue Dec  1 2020 Fabio Valentini <decathorpe@gmail.com> - 0.13.0-1
- Update to version 0.13.0.
- Fixes RHBZ#1855495

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 22 2020 Josh Stone <jistone@redhat.com> - 0.4.1-1
- Update to 0.4.1

* Sun May 10 14:45:03 CEST 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.4.0-1
- Update to 0.4.0

* Wed Apr 08 2020 Josh Stone <jistone@redhat.com> - 0.3.0-1
- Update to 0.3.0

* Mon Mar 30 08:10:57 CEST 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.2.2-1
- Update to 0.2.2

* Tue Feb 25 02:05:21 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.2.1-1
- Update to 0.2.1

* Mon Feb 24 20:44:07 EET 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.2.0-1
- Initial package