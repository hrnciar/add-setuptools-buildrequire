# Generated by rust2rpm 16
# * async-std is not packaged yet
%bcond_with check
%global debug_package %{nil}

%global crate crossterm

Name:           rust-%{crate}0.17
Version:        0.17.7
Release:        2%{?dist}
Summary:        Crossplatform terminal library for manipulating terminals

# Upstream license specification: MIT
License:        MIT
URL:            https://crates.io/crates/crossterm
Source:         %{crates_source}
# Initial patched metadata
# * No windows
# * Bump to parking_lot 0.11
Patch0:         crossterm-fix-metadata.diff

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Crossplatform terminal library for manipulating terminals.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE
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

%package     -n %{name}+event-stream-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+event-stream-devel %{_description}

This package contains library source intended for building other packages
which use "event-stream" feature of "%{crate}" crate.

%files       -n %{name}+event-stream-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+futures-util-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+futures-util-devel %{_description}

This package contains library source intended for building other packages
which use "futures-util" feature of "%{crate}" crate.

%files       -n %{name}+futures-util-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+serde-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde-devel %{_description}

This package contains library source intended for building other packages
which use "serde" feature of "%{crate}" crate.

%files       -n %{name}+serde-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
find -type f -executable -exec chmod -v -x '{}' +
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
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec 01 2020 Fabio Valentini <decathorpe@gmail.com> - 0.17.7-1
- Initial compat package for crossterm 0.17
