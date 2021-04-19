# Generated by rust2rpm 16
%bcond_without check
%global debug_package %{nil}

%global crate liquid

Name:           rust-%{crate}
Version:        0.22.0
Release:        1%{?dist}
Summary:        Liquid templating language for Rust

# Upstream license specification: MIT
License:        MIT
URL:            https://crates.io/crates/liquid
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Liquid templating language for Rust.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE
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

%package     -n %{name}+liquid-lib-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+liquid-lib-devel %{_description}

This package contains library source intended for building other packages
which use "liquid-lib" feature of "%{crate}" crate.

%files       -n %{name}+liquid-lib-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+stdlib-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+stdlib-devel %{_description}

This package contains library source intended for building other packages
which use "stdlib" feature of "%{crate}" crate.

%files       -n %{name}+stdlib-devel
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

* Fri Feb 19 2021 Fabio Valentini <decathorpe@gmail.com> - 0.21.5-1
- Update to version 0.21.5.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Nov 10 2020 Fabio Valentini <decathorpe@gmail.com> - 0.21.4-1
- Update to version 0.21.4.

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 10 2020 Josh Stone <jistone@redhat.com> - 0.20.1-1
- Update to 0.20.1

* Sun Mar 22 15:22:58 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.20.0-1
- Initial package