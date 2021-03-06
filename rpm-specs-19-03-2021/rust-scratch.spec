# Generated by rust2rpm 16
%bcond_without check
%global debug_package %{nil}

%global crate scratch

Name:           rust-%{crate}
Version:        1.0.0
Release:        3%{?dist}
Summary:        Shared compile-time directory

# Upstream license specification: MIT OR Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/scratch
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Compile-time temporary directory shared by multiple crates and erased by `cargo
clean`.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%doc README.md
%license LICENSE-APACHE
%license LICENSE-MIT
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
* Mon Feb 15 2021 Jan Staněk <jstanek@redhat.com> - 1.0.0-3
- Shorten summary field

* Wed Feb 10 2021 Jan Staněk <jstanek@redhat.com> - 1.0.0-2
- Mark license files

* Mon Feb 01 13:02:33 CET 2021 Jan Staněk <jstanek@redhat.com> - 1.0.0-1
- Initial package
