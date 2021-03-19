# Generated by rust2rpm 16
%bcond_without check
%global debug_package %{nil}

%global crate zstd-sys
%global upstream_version 1.4.20+zstd.1.4.9

Name:           rust-%{crate}
Version:        1.4.20
Release:        1%{?dist}
Summary:        Low-level bindings for the zstd compression library

# Upstream license specification: MIT/Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/zstd-sys
Source:         %{crates_source %{crate} %{upstream_version}}
# Initial patched metadata
# * Remove zstd version from version field
# * Make pkg-config default
# * Temporarily downgrade bindgen from 0.57 to 0.56
Patch0:         zstd-sys-fix-metadata.diff

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Low-level bindings for the zstd compression library.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       pkgconfig(libzstd)

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

%package     -n %{name}+bindgen-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+bindgen-devel %{_description}

This package contains library source intended for building other packages
which use "bindgen" feature of "%{crate}" crate.

%files       -n %{name}+bindgen-devel
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

%package     -n %{name}+non-cargo-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+non-cargo-devel %{_description}

This package contains library source intended for building other packages
which use "non-cargo" feature of "%{crate}" crate.

%files       -n %{name}+non-cargo-devel
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
# Remove bundled zstd
rm -rf zstd/

%generate_buildrequires
%cargo_generate_buildrequires -a
echo "pkgconfig(libzstd)"
echo "bindgen"
echo "llvm-devel"

%build
export LLVM_CONFIG_PATH=/usr/bin/llvm-config-%{__isa_bits}
bindgen %{_includedir}/zstd.h --ctypes-prefix ::libc --blacklist-type max_align_t --size_t-is-usize --rustified-enum '.*' --use-core -o src/bindings.rs --
bindgen %{_includedir}/zstd.h --blacklist-type max_align_t --size_t-is-usize --rustified-enum '.*' --use-core -o src/bindings_std.rs --
%cargo_build -a

%install
%cargo_install

%if %{with check}
%check
export LLVM_CONFIG_PATH=/usr/bin/llvm-config-%{__isa_bits}
%cargo_test -a
%endif

%changelog
* Sat Mar 06 2021 Fabio Valentini <decathorpe@gmail.com> - 1.4.20-1
- Update to version 1.4.20+zstd.1.4.9.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.17-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Nov 27 2020 Fabio Valentini <decathorpe@gmail.com> - 1.4.17-3
- Bump to bindgen 0.56.

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 19 2020 Josh Stone <jistone@redhat.com> - 1.4.17-1
- Update to 1.4.17+zstd.1.4.5

* Sat May 30 2020 Josh Stone <jistone@redhat.com> - 1.4.16-1
- Update to 1.4.16+zstd.1.4.5

* Thu Feb 27 2020 Josh Stone <jistone@redhat.com> - 1.4.15-3
- Bump to bindgen 0.53.1

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Dec 15 23:59:34 CET 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.4.15-1
- Initial package
