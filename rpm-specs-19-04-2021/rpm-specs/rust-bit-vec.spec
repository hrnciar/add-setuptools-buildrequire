# Generated by rust2rpm 16
%bcond_without check
%global debug_package %{nil}

%global crate bit-vec

Name:           rust-%{crate}
Version:        0.6.3
Release:        2%{?dist}
Summary:        Vector of bits

# Upstream license specification: MIT/Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/bit-vec
Source:         %{crates_source}
# Initial patched metadata
# * Remove unneeded files
Patch0:         bit-vec-fix-metadata.diff

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Vector of bits.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-MIT LICENSE-APACHE
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

%package     -n %{name}+serde-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde-devel %{_description}

This package contains library source intended for building other packages
which use "serde" feature of "%{crate}" crate.

%files       -n %{name}+serde-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+serde_no_std-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde_no_std-devel %{_description}

This package contains library source intended for building other packages
which use "serde_no_std" feature of "%{crate}" crate.

%files       -n %{name}+serde_no_std-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+serde_std-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde_std-devel %{_description}

This package contains library source intended for building other packages
which use "serde_std" feature of "%{crate}" crate.

%files       -n %{name}+serde_std-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+std-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+std-devel %{_description}

This package contains library source intended for building other packages
which use "std" feature of "%{crate}" crate.

%files       -n %{name}+std-devel
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
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec 07 2020 Fabio Valentini <decathorpe@gmail.com> - 0.6.3-1
- Update to version 0.6.3.
- Fixes RHBZ#1904400

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed May 06 2020 Josh Stone <jistone@redhat.com> - 0.6.2-1
- Update to 0.6.2

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 09 2019 Josh Stone <jistone@redhat.com> - 0.6.1-1
- Update to 0.6.1

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 27 17:15:22 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.5.1-2
- Regenerate

* Thu Mar 21 07:59:22 CET 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.5.1-1
- Update to 0.5.1

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Oct 06 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.5.0-1
- Initial package
