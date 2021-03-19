# Generated by rust2rpm 17
%bcond_without check
%global debug_package %{nil}

%global crate half

Name:           rust-%{crate}
Version:        1.7.1
Release:        2%{?dist}
Summary:        Half-precision floating point f16 and bf16 types for Rust

# Upstream license specification: MIT/Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/half
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Half-precision floating point f16 and bf16 types for Rust implementing the IEEE
754-2008 standard binary16 and bfloat16 types.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

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

%package     -n %{name}+alloc-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+alloc-devel %{_description}

This package contains library source intended for building other packages
which use "alloc" feature of "%{crate}" crate.

%files       -n %{name}+alloc-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+bytemuck-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+bytemuck-devel %{_description}

This package contains library source intended for building other packages
which use "bytemuck" feature of "%{crate}" crate.

%files       -n %{name}+bytemuck-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+num-traits-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+num-traits-devel %{_description}

This package contains library source intended for building other packages
which use "num-traits" feature of "%{crate}" crate.

%files       -n %{name}+num-traits-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+serde-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde-devel %{_description}

This package contains library source intended for building other packages
which use "serde" feature of "%{crate}" crate.

%files       -n %{name}+serde-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+serialize-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serialize-devel %{_description}

This package contains library source intended for building other packages
which use "serialize" feature of "%{crate}" crate.

%files       -n %{name}+serialize-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+std-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+std-devel %{_description}

This package contains library source intended for building other packages
which use "std" feature of "%{crate}" crate.

%files       -n %{name}+std-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+use-intrinsics-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+use-intrinsics-devel %{_description}

This package contains library source intended for building other packages
which use "use-intrinsics" feature of "%{crate}" crate.

%files       -n %{name}+use-intrinsics-devel
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
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 17 09:38:37 CET 2021 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.7.1-1
- Update to 1.7.1 (Fixes: RHBZ#1917105)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun May 10 14:26:13 CEST 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.6.0-1
- Update to 1.6.0

* Wed Mar 04 2020 Josh Stone <jistone@redhat.com> - 1.5.0-1
- Update to 1.5.0

* Mon Feb 10 2020 Josh Stone <jistone@redhat.com> - 1.4.1-1
- Update to 1.4.1

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Oct 13 11:15:06 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.4.0-1
- Update to 1.4.0

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 19 23:55:52 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.3.0-4
- Regenerate

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Nov 10 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.3.0-2
- Adapt to new packaging

* Wed Oct 03 2018 Josh Stone <jistone@redhat.com> - 1.3.0-1
- Update to 1.3.0

* Sat Sep 08 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.2.0-1
- Initial package