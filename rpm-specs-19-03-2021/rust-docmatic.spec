# Generated by rust2rpm 13
%bcond_without check
%global debug_package %{nil}

%global crate docmatic

Name:           rust-%{crate}
Version:        0.1.2
Release:        8%{?dist}
Summary:        Test Rust examples in your documentation

# Upstream license specification: MIT
# https://github.com/assert-rs/docmatic/issues/6
License:        MIT
URL:            https://crates.io/crates/docmatic
Source:         %{crates_source}
# Initial patched metadata
# * Bump to which 4.0
Patch0:         docmatic-fix-metadata.diff

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging
%if %{with check}
BuildRequires:  /usr/bin/rustdoc
%endif

%global _description %{expand:
Test Rust examples in your documentation.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       /usr/bin/rustdoc

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-MIT LICENSE-APACHE
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
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Sep 16 2020 Fabio Valentini <decathorpe@gmail.com> - 0.1.2-7
- Bump to which 4.0.

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-6
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Dec 10 2019 Josh Stone <jistone@redhat.com> - 0.1.2-3
- Bump to which 3.0

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Apr 27 09:21:50 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.2-1
- Initial package
