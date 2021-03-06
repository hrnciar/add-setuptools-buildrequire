# Generated by rust2rpm 16
%bcond_with check
%global debug_package %{nil}

%global crate libhandy-sys

Name:           rust-%{crate}
Version:        0.7.0
Release:        2%{?dist}
Summary:        Sys part of the rust bindings for libhandy

# Upstream license specification: GPL-3.0-or-later
License:        GPLv3+
URL:            https://crates.io/crates/libhandy-sys
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Sys part of the rust bindings for libhandy.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       pkgconfig(libhandy-1) >= 1

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

%package     -n %{name}+dox-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+dox-devel %{_description}

This package contains library source intended for building other packages
which use "dox" feature of "%{crate}" crate.

%files       -n %{name}+dox-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+v1_0-devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       pkgconfig(libhandy-1) >= 1

%description -n %{name}+v1_0-devel %{_description}

This package contains library source intended for building other packages
which use "v1_0" feature of "%{crate}" crate.

%files       -n %{name}+v1_0-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires
echo 'pkgconfig(libhandy-1) >= 1'

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Dec 26 12:45:45 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.7.0-1
- Update to 0.7.0

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 09 2020 Josh Stone <jistone@redhat.com> - 0.6.0-1
- Update to 0.6.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 23 2020 Josh Stone <jistone@redhat.com> - 0.5.0-1
- Update to 0.5.0

* Tue Dec 10 2019 Josh Stone <jistone@redhat.com> - 0.3.1-1
- Update to 0.3.1

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun May 05 17:03:55 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.0-1
- Initial package
