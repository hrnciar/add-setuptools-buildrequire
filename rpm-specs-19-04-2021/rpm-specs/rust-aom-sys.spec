# Generated by rust2rpm 16
%bcond_without check
%global debug_package %{nil}

%global crate aom-sys

Name:           rust-%{crate}
Version:        0.2.1
Release:        4%{?dist}
Summary:        FFI bindings to aom

# Upstream license specification: MIT
License:        MIT
URL:            https://crates.io/crates/aom-sys
Source:         %{crates_source}
# Initial patched metadata
# * bump to bindgen 0.56: https://github.com/rust-av/aom-rs/pull/36
# * bump to bindgen 0.57: https://github.com/rust-av/aom-rs/pull/38
Patch0:         aom-sys-fix-metadata.diff

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
FFI bindings to aom.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       pkgconfig(aom) >= 0.1.0

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

%package     -n %{name}+build_sources-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+build_sources-devel %{_description}

This package contains library source intended for building other packages
which use "build_sources" feature of "%{crate}" crate.

%files       -n %{name}+build_sources-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires
echo 'pkgconfig(aom) >= 0.1.0'

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
* Sat Apr 03 2021 Fabio Valentini <decathorpe@gmail.com> - 0.2.1-4
- Bump to bindgen 0.56.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Nov 27 2020 Fabio Valentini <decathorpe@gmail.com> - 0.2.1-2
- Bump to bindgen 0.56.

* Tue Oct 20 2020 Fabio Valentini <decathorpe@gmail.com> - 0.2.1-1
- Update to version 0.2.1.

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri May 29 2020 Josh Stone <jistone@redhat.com> - 0.1.4-2
- Bump to bindgen 0.54

* Wed Apr 29 2020 Josh Stone <jistone@redhat.com> - 0.1.4-1
- Update to 0.1.4

* Wed Feb 26 2020 Josh Stone <jistone@redhat.com> - 0.1.3-3
- Bump bindgen to 0.53.1

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Dec 06 23:28:44 CET 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.1.3-1
- Release 0.1.3

* Wed Jul 31 18:41:18 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.1.2-3
- Bump bindgen to 0.51

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May 15 08:34:56 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.2-1
- Update to 0.1.2

* Tue Apr 02 2019 Josh Stone <jistone@redhat.com> - 0.1.1-2
- bump bindgen to 0.49

* Wed Mar 20 13:57:30 CET 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.1.1-1
- Release 0.1.1

* Wed Mar 20 09:39:58 CET 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.0-2
- Run tests in infrastructure

* Sat Mar 09 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.1.0-1
- Initial package
