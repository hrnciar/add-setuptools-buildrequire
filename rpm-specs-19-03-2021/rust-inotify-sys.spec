# Generated by rust2rpm 16
%bcond_without check
%global debug_package %{nil}

%global crate inotify-sys

Name:           rust-%{crate}
Version:        0.1.5
Release:        1%{?dist}
Summary:        Inotify bindings for the Rust programming language

# Upstream license specification: ISC
License:        ISC
URL:            https://crates.io/crates/inotify-sys
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Inotify bindings for the Rust programming language.}

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

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
* Thu Mar 04 2021 Fabio Valentini <decathorpe@gmail.com> - 0.1.5-1
- Update to version 0.1.5.
- Fixes RHBZ#1916998

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Nov 11 2020 Fabio Valentini <decathorpe@gmail.com> - 0.1.4-1
- Update to version 0.1.4.
- Fixes RHBZ#1895468

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-7
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Dec 17 10:26:17 CET 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.3-4
- Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 23 10:24:32 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.3-2
- Regenerate

* Mon Mar 11 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.3-1
- Initial package