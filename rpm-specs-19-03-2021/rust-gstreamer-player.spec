# Generated by rust2rpm 16
%bcond_without check
%global debug_package %{nil}

%global crate gstreamer-player

Name:           rust-%{crate}
Version:        0.16.5
Release:        2%{?dist}
Summary:        Rust bindings for GStreamer Player library

# Upstream license specification: MIT/Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/gstreamer-player
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Rust bindings for GStreamer Player library.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%doc README.md
%license LICENSE-APACHE LICENSE-MIT
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+dox-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+dox-devel %{_description}

This package contains library source intended for building other packages
which use "dox" feature of "%{crate}" crate.

%files       -n %{name}+dox-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+v1_14-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+v1_14-devel %{_description}

This package contains library source intended for building other packages
which use "v1_14" feature of "%{crate}" crate.

%files       -n %{name}+v1_14-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+v1_16-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+v1_16-devel %{_description}

This package contains library source intended for building other packages
which use "v1_16" feature of "%{crate}" crate.

%files       -n %{name}+v1_16-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+v1_18-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+v1_18-devel %{_description}

This package contains library source intended for building other packages
which use "v1_18" feature of "%{crate}" crate.

%files       -n %{name}+v1_18-devel
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
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Nov 25 2020 Fabio Valentini <decathorpe@gmail.com> - 0.16.5-1
- Update to version 0.16.5.
- Remove features with broken dependencies.
- Fixes RHBZ#1900592

* Wed Sep 09 2020 Josh Stone <jistone@redhat.com> - 0.16.3-1
- Update to 0.16.3

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 09 2020 Josh Stone <jistone@redhat.com> - 0.16.0-1
- Update to 0.16.0

* Tue May 05 2020 Josh Stone <cuviper@gmail.com> - 0.15.5-1
- Update to 0.15.5

* Mon Feb 17 11:34:05 EET 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.15.3-1
- Update to 0.15.3

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 16 2020 Josh Stone <jistone@redhat.com> - 0.15.0-1
- Update to 0.15.0

* Tue Dec 10 2019 Josh Stone <jistone@redhat.com> - 0.14.0-1
- Update to 0.14.0

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun May 05 19:21:11 EEST 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.13.0-1
- Initial package
