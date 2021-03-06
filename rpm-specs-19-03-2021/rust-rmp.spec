# Generated by rust2rpm 13
%bcond_without check
%global debug_package %{nil}

%global crate rmp

Name:           rust-%{crate}
Version:        0.8.9
Release:        4%{?dist}
Summary:        Pure Rust MessagePack serialization implementation

# Upstream license specification: MIT
License:        MIT
URL:            https://crates.io/crates/rmp
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Pure Rust MessagePack serialization implementation.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%doc CHANGELOG.md README.md
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
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 07 2020 Josh Stone <jistone@redhat.com> - 0.8.9-1
- Update to 0.8.9

* Thu Sep 12 23:44:23 CEST 2019 Robert-Andr?? Mauchin <zebob.m@gmail.com> - 0.8.8-1
- Release 0.8.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jul 21 10:08:59 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.8.7-3
- Regenerate

* Thu Apr 11 14:36:33 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.8.7-2
- Run tests in infrastructure

* Thu Mar 28 07:18:34 CET 2019 Robert-Andr?? Mauchin <zebob.m@gmail.com> - 0.8.7-1
- Initial package
