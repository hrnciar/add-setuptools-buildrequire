# Generated by rust2rpm 15
%bcond_without check
%global debug_package %{nil}

%global crate lzma-sys

Name:           rust-%{crate}
Version:        0.1.17
Release:        2%{?dist}
Summary:        Raw bindings to liblzma

# Upstream license specification: MIT/Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/lzma-sys
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Raw bindings to liblzma which contains an implementation of LZMA and xz stream
encoding/decoding.
High level Rust bindings are available in the `xz2` crate.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       (pkgconfig(liblzma) >= 5.2.4 with pkgconfig(liblzma) < 6.0.0)

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-MIT LICENSE-APACHE
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+static-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+static-devel %{_description}

This package contains library source intended for building other packages
which use "static" feature of "%{crate}" crate.

%files       -n %{name}+static-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
# No bundled libs
rm -vrf xz-* config.h
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires
echo '(pkgconfig(liblzma) >= 5.2.4 with pkgconfig(liblzma) < 6.0.0)'

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Nov 06 2020 Fabio Valentini <decathorpe@gmail.com> - 0.1.17-1
- Update to version 0.1.17.
- Fixes RHBZ#1887198

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri May 15 2020 Josh Stone <jistone@redhat.com> - 0.1.16-1
- Update to 0.1.16

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Nov 23 2019 Josh Stone <jistone@redhat.com> - 0.1.15-1
- Update to 0.1.15

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Mar 07 2019 Josh Stone <jistone@redhat.com> - 0.1.14-1
- Update to 0.1.14

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 08 2019 Josh Stone <jistone@redhat.com> - 0.1.13-1
- Update to 0.1.13

* Fri Dec 07 2018 Josh Stone <jistone@redhat.com> - 0.1.12-1
- Update to 0.1.12
- Adapt to new packaging

* Thu Oct 11 2018 Josh Stone <jistone@redhat.com> - 0.1.11-1
- Update to 0.1.11

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.10-1
- Update to 0.1.10

* Wed Apr 25 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.9-3
- Bump filetime to 0.2

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 13 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.9-1
- Initial package
