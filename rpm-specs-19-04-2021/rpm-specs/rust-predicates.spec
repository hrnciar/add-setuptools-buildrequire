# Generated by rust2rpm 16
%bcond_without check
%global debug_package %{nil}

%global crate predicates

Name:           rust-%{crate}
Version:        1.0.7
Release:        1%{?dist}
Summary:        Implementation of boolean-valued predicate functions

# Upstream license specification: MIT/Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/predicates
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Implementation of boolean-valued predicate functions.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-APACHE LICENSE-MIT
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

%package     -n %{name}+difference-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+difference-devel %{_description}

This package contains library source intended for building other packages
which use "difference" feature of "%{crate}" crate.

%files       -n %{name}+difference-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+float-cmp-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+float-cmp-devel %{_description}

This package contains library source intended for building other packages
which use "float-cmp" feature of "%{crate}" crate.

%files       -n %{name}+float-cmp-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+normalize-line-endings-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+normalize-line-endings-devel %{_description}

This package contains library source intended for building other packages
which use "normalize-line-endings" feature of "%{crate}" crate.

%files       -n %{name}+normalize-line-endings-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+regex-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+regex-devel %{_description}

This package contains library source intended for building other packages
which use "regex" feature of "%{crate}" crate.

%files       -n %{name}+regex-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+unstable-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+unstable-devel %{_description}

This package contains library source intended for building other packages
which use "unstable" feature of "%{crate}" crate.

%files       -n %{name}+unstable-devel
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
* Thu Mar 04 2021 Fabio Valentini <decathorpe@gmail.com> - 1.0.7-1
- Update to version 1.0.7.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec 29 2020 Fabio Valentini <decathorpe@gmail.com> - 1.0.6-1
- Update to version 1.0.6.
- Fixes RHBZ#1911389

* Mon Oct 26 2020 Fabio Valentini <decathorpe@gmail.com> - 1.0.5-1
- Update to version 1.0.5.

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Mar 23 18:34:35 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.0.4-1
- Update to 1.0.4

* Wed Mar 04 13:00:16 EET 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.0.3-1
- Initial package
