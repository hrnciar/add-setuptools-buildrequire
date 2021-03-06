# Generated by rust2rpm 13
# * circular deps with diesel
%bcond_with check
%global debug_package %{nil}

%global crate diesel_derives

Name:           rust-%{crate}
Version:        1.4.1
Release:        4%{?dist}
Summary:        Internal crate to Diesel

# Upstream license specification: MIT OR Apache-2.0
# https://github.com/diesel-rs/diesel/pull/2395
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/diesel_derives
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
You should not use this crate directly, it is internal to Diesel.}

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

%package     -n %{name}+mysql-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+mysql-devel %{_description}

This package contains library source intended for building other packages
which use "mysql" feature of "%{crate}" crate.

%files       -n %{name}+mysql-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+nightly-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+nightly-devel %{_description}

This package contains library source intended for building other packages
which use "nightly" feature of "%{crate}" crate.

%files       -n %{name}+nightly-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+postgres-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+postgres-devel %{_description}

This package contains library source intended for building other packages
which use "postgres" feature of "%{crate}" crate.

%files       -n %{name}+postgres-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+sqlite-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+sqlite-devel %{_description}

This package contains library source intended for building other packages
which use "sqlite" feature of "%{crate}" crate.

%files       -n %{name}+sqlite-devel
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
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 12 17:46:32 CEST 2020 Igor Raits <i.gnatenko.brain@gmail.com> - 1.4.1-1
- Initial package
