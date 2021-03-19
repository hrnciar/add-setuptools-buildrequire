# Generated by rust2rpm 16
# * Test files are not distributed on crates.io
%bcond_with check
%global debug_package %{nil}

%global __cargo_is_bin() false

%global crate escargot

Name:           rust-%{crate}
Version:        0.5.1
Release:        1%{?dist}
Summary:        Cargo API written in Paris

# Upstream license specification: MIT OR Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/escargot
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Cargo API written in Paris.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-APACHE LICENSE-MIT
%doc README.md CHANGELOG.md CONTRIBUTING.md
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+cargo_unstable-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+cargo_unstable-devel %{_description}

This package contains library source intended for building other packages
which use "cargo_unstable" feature of "%{crate}" crate.

%files       -n %{name}+cargo_unstable-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+print-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+print-devel %{_description}

This package contains library source intended for building other packages
which use "print" feature of "%{crate}" crate.

%files       -n %{name}+print-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+strict_unstable-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+strict_unstable-devel %{_description}

This package contains library source intended for building other packages
which use "strict_unstable" feature of "%{crate}" crate.

%files       -n %{name}+strict_unstable-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+test_unstable-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+test_unstable-devel %{_description}

This package contains library source intended for building other packages
which use "test_unstable" feature of "%{crate}" crate.

%files       -n %{name}+test_unstable-devel
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
* Mon Feb 08 2021 Fabio Valentini <decathorpe@gmail.com> - 0.5.1-1
- Update to version 0.5.1.
- Fixes RHBZ#1923784

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Mar 04 13:44:47 EET 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.5.0-1
- Initial package