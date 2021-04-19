# Generated by rust2rpm 16
%bcond_without check
%global debug_package %{nil}

%global crate zstd-safe
%global upstream_version 3.0.1+zstd.1.4.9

Name:           rust-%{crate}
Version:        3.0.1
Release:        1%{?dist}
Summary:        Safe low-level bindings for the zstd compression library

# Upstream license specification: MIT/Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/zstd-safe
Source:         %{crates_source %{crate} %{upstream_version}}
# Initial patched metadata
# * Remove zstd version from version field
# * Add pkg-config feature to build zstd-sys
# * Remove bindgen feature which is the default now
Patch0:         zstd-safe-fix-metadata.diff

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Safe low-level bindings for the zstd compression library.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE
%doc Readme.md
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+debug-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+debug-devel %{_description}

This package contains library source intended for building other packages
which use "debug" feature of "%{crate}" crate.

%files       -n %{name}+debug-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+experimental-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+experimental-devel %{_description}

This package contains library source intended for building other packages
which use "experimental" feature of "%{crate}" crate.

%files       -n %{name}+experimental-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+legacy-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+legacy-devel %{_description}

This package contains library source intended for building other packages
which use "legacy" feature of "%{crate}" crate.

%files       -n %{name}+legacy-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+pkg-config-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+pkg-config-devel %{_description}

This package contains library source intended for building other packages
which use "pkg-config" feature of "%{crate}" crate.

%files       -n %{name}+pkg-config-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+std-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+std-devel %{_description}

This package contains library source intended for building other packages
which use "std" feature of "%{crate}" crate.

%files       -n %{name}+std-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+zstdmt-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+zstdmt-devel %{_description}

This package contains library source intended for building other packages
which use "zstdmt" feature of "%{crate}" crate.

%files       -n %{name}+zstdmt-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%prep
%autosetup -n %{crate}-%{upstream_version} -p1
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
* Sat Mar 06 2021 Fabio Valentini <decathorpe@gmail.com> - 3.0.1-1
- Update to version 3.0.1+zstd.1.4.9.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 19 2020 Josh Stone <jistone@redhat.com> - 2.0.5-1
- Update to 2.0.5+zstd.1.4.5

* Sat Jun 06 2020 Josh Stone <jistone@redhat.com> - 2.0.4-1
- Update to 2.0.4+zstd.1.4.5

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 16 03:41:27 CET 2019 Robert-André Mauchin <zebob.m@gmail.com> - 2.0.3-1
- Initial package
