# Generated by rust2rpm 13
%bcond_without check
%global debug_package %{nil}

%global crate dlib

Name:           rust-%{crate}
Version:        0.4.2
Release:        4%{?dist}
Summary:        Helper macros for handling manually loading optional system libraries

# Upstream license specification: MIT
License:        MIT
URL:            https://crates.io/crates/dlib
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Helper macros for handling manually loading optional system libraries.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE.txt
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

%package     -n %{name}+dlopen-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+dlopen-devel %{_description}

This package contains library source intended for building other packages
which use "dlopen" feature of "%{crate}" crate.

%files       -n %{name}+dlopen-devel
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
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri May 29 2020 Josh Stone <jistone@redhat.com> - 0.4.2-1
- Update to 0.4.2

* Fri May 22 14:19:03 PDT 2020 Michel Alexandre Salim <salimma@fedoraproject.org> - 0.4.1-1
- Initial package
