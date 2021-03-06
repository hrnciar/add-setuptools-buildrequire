# Generated by rust2rpm 16
%bcond_with check
%global debug_package %{nil}

%global crate structopt

Name:           rust-%{crate}0.2
Version:        0.2.18
Release:        7%{?dist}
Summary:        Parse command line argument by defining a struct

# Upstream license specification: Apache-2.0/MIT
License:        ASL 2.0 or MIT
URL:            https://crates.io/crates/structopt
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Parse command line argument by defining a struct.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-MIT LICENSE-APACHE
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

%package     -n %{name}+color-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+color-devel %{_description}

This package contains library source intended for building other packages
which use "color" feature of "%{crate}" crate.

%files       -n %{name}+color-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+debug-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+debug-devel %{_description}

This package contains library source intended for building other packages
which use "debug" feature of "%{crate}" crate.

%files       -n %{name}+debug-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+doc-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+doc-devel %{_description}

This package contains library source intended for building other packages
which use "doc" feature of "%{crate}" crate.

%files       -n %{name}+doc-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+nightly-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+nightly-devel %{_description}

This package contains library source intended for building other packages
which use "nightly" feature of "%{crate}" crate.

%files       -n %{name}+nightly-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+no_cargo-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+no_cargo-devel %{_description}

This package contains library source intended for building other packages
which use "no_cargo" feature of "%{crate}" crate.

%files       -n %{name}+no_cargo-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+paw-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+paw-devel %{_description}

This package contains library source intended for building other packages
which use "paw" feature of "%{crate}" crate.

%files       -n %{name}+paw-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+suggestions-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+suggestions-devel %{_description}

This package contains library source intended for building other packages
which use "suggestions" feature of "%{crate}" crate.

%files       -n %{name}+suggestions-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+wrap_help-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+wrap_help-devel %{_description}

This package contains library source intended for building other packages
which use "wrap_help" feature of "%{crate}" crate.

%files       -n %{name}+wrap_help-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+yaml-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+yaml-devel %{_description}

This package contains library source intended for building other packages
which use "yaml" feature of "%{crate}" crate.

%files       -n %{name}+yaml-devel
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
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.18-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 01 2021 Fabio Valentini <decathorpe@gmail.com> - 0.2.18-6
- Remove features with missing dependencies (clap/lints).

* Mon Dec 28 13:33:18 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.2.18-5
- Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.18-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Dec 17 08:23:07 CET 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.18-1
- Initial package
