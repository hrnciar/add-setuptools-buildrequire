# Generated by rust2rpm 17
%bcond_with check
%global debug_package %{nil}

%global crate ring

Name:           rust-%{crate}
Version:        0.16.19
Release:        2%{?dist}
Summary:        Safe, fast, small crypto using Rust

# https://github.com/briansmith/ring/issues/902
License:        ISC and OpenSSL and MIT

URL:            https://crates.io/crates/ring
Source:         %{crates_source}
# Initial patched metadata
Patch0:         ring-fix-metadata.diff

ExclusiveArch:  %{rust_arches}
# RHBZ 1869980
ExcludeArch:    s390x %{power64}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Safe, fast, small crypto using Rust.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE
%doc doc/link-to-readme.md
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+alloc-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+alloc-devel %{_description}

This package contains library source intended for building other packages
which use "alloc" feature of "%{crate}" crate.

%files       -n %{name}+alloc-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+dev_urandom_fallback-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+dev_urandom_fallback-devel %{_description}

This package contains library source intended for building other packages
which use "dev_urandom_fallback" feature of "%{crate}" crate.

%files       -n %{name}+dev_urandom_fallback-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+internal_benches-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+internal_benches-devel %{_description}

This package contains library source intended for building other packages
which use "internal_benches" feature of "%{crate}" crate.

%files       -n %{name}+internal_benches-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+once_cell-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+once_cell-devel %{_description}

This package contains library source intended for building other packages
which use "once_cell" feature of "%{crate}" crate.

%files       -n %{name}+once_cell-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+slow_tests-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+slow_tests-devel %{_description}

This package contains library source intended for building other packages
which use "slow_tests" feature of "%{crate}" crate.

%files       -n %{name}+slow_tests-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+std-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+std-devel %{_description}

This package contains library source intended for building other packages
which use "std" feature of "%{crate}" crate.

%files       -n %{name}+std-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+test_logging-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+test_logging-devel %{_description}

This package contains library source intended for building other packages
which use "test_logging" feature of "%{crate}" crate.

%files       -n %{name}+test_logging-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+wasm32_c-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+wasm32_c-devel %{_description}

This package contains library source intended for building other packages
which use "wasm32_c" feature of "%{crate}" crate.

%files       -n %{name}+wasm32_c-devel
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
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 03 15:05:55 CET 2021 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.16.19-1
- Update to 0.16.19

* Thu Jul 30 2020 Peter Robinson <pbrobinson@fedorapeople.org> - 0.16.15-1
- Initial package