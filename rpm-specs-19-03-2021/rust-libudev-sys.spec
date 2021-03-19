# Generated by rust2rpm 10
%bcond_without check
%global debug_package %{nil}

%global crate libudev-sys

Name:           rust-%{crate}
Version:        0.1.4
Release:        11%{?dist}
Summary:        FFI bindings to libudev

# Upstream license specification: MIT
License:        MIT
URL:            https://crates.io/crates/libudev-sys
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
FFI bindings to libudev.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       pkgconfig(libudev)

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE
%doc README.md
%{cargo_registry}/%{crate}-%{version}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires
echo 'pkgconfig(libudev)'

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Sep 07 09:24:10 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.4-8
- Regenerate

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Nov 02 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.4-5
- Adapt to new packaging

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 08 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.4-2
- Rebuild for rust-packaging v5

* Sun Jan 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.4-1
- Update to 0.1.4

* Fri Jan 05 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.3-1
- Initial package
