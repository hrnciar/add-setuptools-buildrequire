# Generated by rust2rpm 11
%bcond_without check
%global debug_package %{nil}

%global crate ascii

Name:           rust-%{crate}
Version:        1.0.0
Release:        4%{?dist}
Summary:        ASCII-only equivalents to `char`, `str` and `String`

# Upstream license specification: Apache-2.0 / MIT
License:        ASL 2.0 or MIT
URL:            https://crates.io/crates/ascii
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
ASCII-only equivalents to `char`, `str` and `String`.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-MIT LICENSE-APACHE
%doc README.md RELEASES.md
%{cargo_registry}/%{crate}-%{version}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+serde-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde-devel %{_description}

This package contains library source intended for building other packages
which use "serde" feature of "%{crate}" crate.

%files       -n %{name}+serde-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+serde_test-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde_test-devel %{_description}

This package contains library source intended for building other packages
which use "serde_test" feature of "%{crate}" crate.

%files       -n %{name}+serde_test-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+std-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+std-devel %{_description}

This package contains library source intended for building other packages
which use "std" feature of "%{crate}" crate.

%files       -n %{name}+std-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep
# Spurious executable perms on all files
# (triggers brp-mangle-shebang)
# https://github.com/tomprogrammer/rust-ascii/issues/68
find . -executable -type f -exec chmod -x '{}' +;

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
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Dec 13 17:12:40 CET 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.0.0-1
- Update to 1.0.0

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jul 07 15:03:17 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.9.2-1
- Update to 0.9.2

* Thu Mar 14 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.9.1-1
- Initial package
