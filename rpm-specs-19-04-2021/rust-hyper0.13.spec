# Generated by rust2rpm 16
# * pnet is too new in Fedora
# * examples and UI tests are not included in the crate
%bcond_with check
%global debug_package %{nil}

%global crate hyper

Name:           rust-%{crate}0.13
Version:        0.13.10
Release:        1%{?dist}
Summary:        Fast and correct HTTP library

# Upstream license specification: MIT
License:        MIT
URL:            https://crates.io/crates/hyper
Source:         %{crates_source}
# Initial patched metadata
# * remove nightly-only / internal features
Patch0:         hyper-fix-metadata.diff

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Fast and correct HTTP library.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+runtime-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+runtime-devel %{_description}

This package contains library source intended for building other packages
which use "runtime" feature of "%{crate}" crate.

%files       -n %{name}+runtime-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+socket2-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+socket2-devel %{_description}

This package contains library source intended for building other packages
which use "socket2" feature of "%{crate}" crate.

%files       -n %{name}+socket2-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+stream-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+stream-devel %{_description}

This package contains library source intended for building other packages
which use "stream" feature of "%{crate}" crate.

%files       -n %{name}+stream-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+tcp-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+tcp-devel %{_description}

This package contains library source intended for building other packages
which use "tcp" feature of "%{crate}" crate.

%files       -n %{name}+tcp-devel
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
* Sun Mar 07 2021 Fabio Valentini <decathorpe@gmail.com> - 0.13.10-1
- Initial package