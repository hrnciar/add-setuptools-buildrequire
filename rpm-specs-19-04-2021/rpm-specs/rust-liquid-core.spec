# Generated by rust2rpm 16
%bcond_without check
%global debug_package %{nil}

%global crate liquid-core

Name:           rust-%{crate}
Version:        0.22.0
Release:        1%{?dist}
Summary:        Core liquid functionality

# Upstream license specification: MIT OR Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/liquid-core
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Core liquid functionality.}

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

%package     -n %{name}+derive-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+derive-devel %{_description}

This package contains library source intended for building other packages
which use "derive" feature of "%{crate}" crate.

%files       -n %{name}+derive-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+liquid-derive-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+liquid-derive-devel %{_description}

This package contains library source intended for building other packages
which use "liquid-derive" feature of "%{crate}" crate.

%files       -n %{name}+liquid-derive-devel
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
* Mon Mar 01 2021 Fabio Valentini <decathorpe@gmail.com> - 0.22.0-1
- Update to version 0.22.0.

* Fri Feb 19 2021 Fabio Valentini <decathorpe@gmail.com> - 0.21.3-1
- Update to version 0.21.3.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Nov 10 2020 Fabio Valentini <decathorpe@gmail.com> - 0.21.2-1
- Update to version 0.21.2.

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 19 2020 Josh Stone <jistone@redhat.com> - 0.20.2-1
- Update to 0.20.2

* Wed Jun 10 2020 Josh Stone <jistone@redhat.com> - 0.20.1-1
- Update to 0.20.1

* Sun Mar 22 15:14:43 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.20.0-1
- Initial package
