# Generated by rust2rpm 13
# https://github.com/AlexEne/rust_hawktracer_sys/issues/6
%ifnarch %{ix86} %{arm}
%bcond_without check
%endif
%global debug_package %{nil}

%global crate rust_hawktracer_sys

Name:           rust-%{crate}
Version:        0.4.2
Release:        7%{?dist}
Summary:        Sys crate for the rust_hawktracer library

# Upstream license specification: MIT/Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/rust_hawktracer_sys
Source:         %{crates_source}
# Initial patched metadata
# * Bump bindgen to 0.54, https://github.com/AlexEne/rust_hawktracer_sys/pull/12
# * Bump bindgen to 0.56, https://github.com/AlexEne/rust_hawktracer_sys/pull/14
Patch0:         rust_hawktracer_sys-fix-metadata.diff
Patch1:         0001-Upgrade-to-bindgen-0.53.1.patch

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Sys crate for the rust_hawktracer library.}

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

%package     -n %{name}+bindgen-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+bindgen-devel %{_description}

This package contains library source intended for building other packages
which use "bindgen" feature of "%{crate}" crate.

%files       -n %{name}+bindgen-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+generate_bindings-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+generate_bindings-devel %{_description}

This package contains library source intended for building other packages
which use "generate_bindings" feature of "%{crate}" crate.

%files       -n %{name}+generate_bindings-devel
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

%package     -n %{name}+pkg_config-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+pkg_config-devel %{_description}

This package contains library source intended for building other packages
which use "pkg_config" feature of "%{crate}" crate.

%files       -n %{name}+pkg_config-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep
sed -i "s|\r||g" README.md src/internals/mod.rs
rm -rf hawktracer/tools/

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
* Sat Apr 03 2021 Fabio Valentini <decathorpe@gmail.com> - 0.4.2-7
- Bump bindgen to 0.57.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Nov 27 2020 Fabio Valentini <decathorpe@gmail.com> - 0.4.2-5
- Bump bindgen to 0.56.

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri May 29 2020 Josh Stone <jistone@redhat.com> - 0.4.2-3
- Bump bindgen to 0.54

* Thu Feb 27 2020 Josh Stone <jistone@redhat.com> - 0.4.2-2
- Bump bindgen to 0.53.1

* Tue Feb 11 04:00:12 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.4.2-1
- Update to 0.4.2

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Dec 21 02:31:46 CET 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.3.0-1
- Initial package
