# Generated by rust2rpm 13
%bcond_without check
%global debug_package %{nil}

# The /usr/bin/dotenv is already provided by other packages
%global __cargo_is_bin() false

%global crate dotenv

Name:           rust-%{crate}
Version:        0.15.0
Release:        4%{?dist}
Summary:        `dotenv` implementation for Rust

# Upstream license specification: MIT
# https://github.com/dotenv-rs/dotenv/issues/47
License:        MIT
URL:            https://crates.io/crates/dotenv
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
`dotenv` implementation for Rust.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+clap-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+clap-devel %{_description}

This package contains library source intended for building other packages
which use "clap" feature of "%{crate}" crate.

%files       -n %{name}+clap-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+cli-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+cli-devel %{_description}

This package contains library source intended for building other packages
which use "cli" feature of "%{crate}" crate.

%files       -n %{name}+cli-devel
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
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.0-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 12 16:13:43 CEST 2020 Igor Raits <i.gnatenko.brain@gmail.com> - 0.15.0-1
- Initial package
