# Generated by rust2rpm 17
%bcond_without check
%global debug_package %{nil}

%global crate obfstr

Name:           rust-%{crate}
Version:        0.2.4
Release:        1%{?dist}
Summary:        Compiletime string constant obfuscation for Rust

# Upstream license specification: MIT
License:        MIT
URL:            https://crates.io/crates/obfstr
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Compiletime string constant obfuscation for Rust.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license license.txt
%doc readme.md
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+unsafe_static_str-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+unsafe_static_str-devel %{_description}

This package contains library source intended for building other packages
which use "unsafe_static_str" feature of "%{crate}" crate.

%files       -n %{name}+unsafe_static_str-devel
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
* Sun Feb 07 2021 Fabio Valentini <decathorpe@gmail.com> - 0.2.4-1
- Update to version 0.2.4.
- Fixes RHBZ#1923208

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan 12 09:48:19 CET 2021 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.2.2-1
- Update to 0.2.2 (Fixes: RHBZ#1915101)

* Sat Dec 26 12:39:51 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.2.1-1
- Update to 0.2.1

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun 21 17:44:52 CEST 2020 Igor Raits <i.gnatenko.brain@gmail.com> - 0.1.1-1
- Initial package
