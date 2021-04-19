# Generated by rust2rpm 16
%bcond_without check
%global debug_package %{nil}

%global crate cxx-build

Name:           rust-%{crate}
Version:        0.5.10
Release:        2%{?dist}
Summary:        C++ code generator for integrating `cxx` crate into a Cargo build

# Upstream license specification: MIT OR Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/cxx-build
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
C++ code generator for integrating `cxx` crate into a Cargo build.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license        LICENSE-APACHE
%license        LICENSE-MIT
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
%cargo_generate_buildrequires -a

%build
%cargo_build -a

%install
%cargo_install -a

%if %{with check}
%check
%cargo_test -a
%endif

%changelog
* Wed Feb 10 2021 Jan Staněk <jstanek@redhat.com> - 0.5.10-2
- Mark license files

* Mon Feb 01 11:47:39 CET 2021 Jan Staněk <jstanek@redhat.com> - 0.5.10-1
- Initial package
