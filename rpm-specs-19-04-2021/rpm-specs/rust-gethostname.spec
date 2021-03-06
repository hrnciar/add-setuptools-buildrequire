# Generated by rust2rpm 13
%bcond_without check
%global debug_package %{nil}

%global crate gethostname

Name:           rust-%{crate}
Version:        0.2.1
Release:        4%{?dist}
Summary:        Gethostname for all platforms

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            https://crates.io/crates/gethostname
Source:         %{crates_source}
# Initial patched metadata
# * No windows
Patch0:         gethostname-fix-metadata.diff

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Gethostname for all platforms.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE
%doc README.md CHANGELOG.md
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
%if %{with check}
echo '/usr/bin/hostname'
%endif

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Dec 21 00:15:45 EET 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.2.1-1
- Update to 0.2.1

* Fri Dec 13 18:37:54 CET 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.0-4
- Update patch

* Sat Dec 07 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.2.0-3
- Spec file fixes

* Sun Nov 24 03:51:34 EET 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.2.0-1
- Initial package
