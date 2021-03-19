# Generated by rust2rpm 17
%bcond_without check
%global debug_package %{nil}

%global crate ruma-client-api

Name:           rust-%{crate}
Version:        0.10.0~alpha.2
Release:        2%{?dist}
Summary:        Types for the endpoints in the Matrix client-server API

# Upstream license specification: MIT
# https://github.com/ruma/ruma/issues/386
License:        MIT
URL:            https://crates.io/crates/ruma-client-api
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Types for the endpoints in the Matrix client-server API.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
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

%package     -n %{name}+unstable-exhaustive-types-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+unstable-exhaustive-types-devel %{_description}

This package contains library source intended for building other packages
which use "unstable-exhaustive-types" feature of "%{crate}" crate.

%files       -n %{name}+unstable-exhaustive-types-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+unstable-pre-spec-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+unstable-pre-spec-devel %{_description}

This package contains library source intended for building other packages
which use "unstable-pre-spec" feature of "%{crate}" crate.

%files       -n %{name}+unstable-pre-spec-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+unstable-synapse-quirks-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+unstable-synapse-quirks-devel %{_description}

This package contains library source intended for building other packages
which use "unstable-synapse-quirks" feature of "%{crate}" crate.

%files       -n %{name}+unstable-synapse-quirks-devel
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
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0~alpha.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 03 15:57:52 CET 2021 Igor Raits <igor.raits@gmail.com> - 0.10.0~alpha.2-1
- Initial package
