# Generated by rust2rpm 10
# Upstream doesn't provide the necessary fonts in the crate for the test
# https://gitlab.redox-os.org/redox-os/stb_truetype-rs/issues/22
%bcond_with check
%global debug_package %{nil}

%global crate stb_truetype

Name:           rust-%{crate}
Version:        0.3.1
Release:        5%{?dist}
Summary:        Straight translation of the font loading code in stb_truetype.h from C to Rust

# Upstream license specification: MIT / Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/stb_truetype
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Straight translation of the font loading code in stb_truetype.h from C to Rust.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%doc README.md CHANGELOG.md
%license LICENSE-APACHE LICENSE-MIT
%{cargo_registry}/%{crate}-%{version}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+libm-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+libm-devel %{_description}

This package contains library source intended for building other packages
which use "libm" feature of "%{crate}" crate.

%files       -n %{name}+libm-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+std-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+std-devel %{_description}

This package contains library source intended for building other packages
which use "std" feature of "%{crate}" crate.

%files       -n %{name}+std-devel
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
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Dec 06 00:33:24 CET 2019 Robert-Andr?? Mauchin <zebob.m@gmail.com> - 0.3.1-1
- Release 0.3.1 (#1775915)

* Thu Sep 12 16:54:53 CEST 2019 Robert-Andr?? Mauchin <zebob.m@gmail.com> - 0.3.0-1
- Release 0.3.0 (#1749423)

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Mar 20 09:50:53 CET 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.6-2
- Run tests in infrastructure

* Sat Mar 16 2019 Robert-Andr?? Mauchin <zebob.m@gmail.com> - 0.2.6-1
- Initial package
