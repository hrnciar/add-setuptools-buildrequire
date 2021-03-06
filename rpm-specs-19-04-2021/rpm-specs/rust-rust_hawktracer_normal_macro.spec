# Generated by rust2rpm 13
%bcond_without check
%global debug_package %{nil}

%global crate rust_hawktracer_normal_macro

Name:           rust-%{crate}
Version:        0.4.1
Release:        3%{?dist}
Summary:        Helper crate for hawktracer profiling library

# Upstream license specification: MIT/Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/rust_hawktracer_normal_macro
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Helper crate for hawktracer profiling library.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE LICENSE-APACHE
%doc README.md
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+generate_bindings-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+generate_bindings-devel %{_description}

This package contains library source intended for building other packages
which use "generate_bindings" feature of "%{crate}" crate.

%files       -n %{name}+generate_bindings-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+pkg_config-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+pkg_config-devel %{_description}

This package contains library source intended for building other packages
which use "pkg_config" feature of "%{crate}" crate.

%files       -n %{name}+pkg_config-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+profiling_enabled-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+profiling_enabled-devel %{_description}

This package contains library source intended for building other packages
which use "profiling_enabled" feature of "%{crate}" crate.

%files       -n %{name}+profiling_enabled-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+rust_hawktracer_sys-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+rust_hawktracer_sys-devel %{_description}

This package contains library source intended for building other packages
which use "rust_hawktracer_sys" feature of "%{crate}" crate.

%files       -n %{name}+rust_hawktracer_sys-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep
sed -i "s|\r||g" README.md

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
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Feb 12 2020 Josh Stone <jistone@redhat.com> - 0.4.1-1
- Update to 0.4.1

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Dec 21 01:42:25 CET 2019 Robert-Andr?? Mauchin <zebob.m@gmail.com> - 0.3.0-1
- Initial package
