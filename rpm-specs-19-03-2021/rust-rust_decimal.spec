# Generated by rust2rpm 16
%bcond_without check
%global debug_package %{nil}

%global crate rust_decimal

Name:           rust-%{crate}
Version:        1.10.3
Release:        1%{?dist}
Summary:        Decimal Implementation written in pure Rust suitable for financial calculations

# Upstream license specification: MIT
License:        MIT
URL:            https://crates.io/crates/rust_decimal
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Decimal Implementation written in pure Rust suitable for financial
calculations.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE
%doc README.md VERSION.md
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+byteorder-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+byteorder-devel %{_description}

This package contains library source intended for building other packages
which use "byteorder" feature of "%{crate}" crate.

%files       -n %{name}+byteorder-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+bytes-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+bytes-devel %{_description}

This package contains library source intended for building other packages
which use "bytes" feature of "%{crate}" crate.

%files       -n %{name}+bytes-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+db-diesel-postgres-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+db-diesel-postgres-devel %{_description}

This package contains library source intended for building other packages
which use "db-diesel-postgres" feature of "%{crate}" crate.

%files       -n %{name}+db-diesel-postgres-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+diesel-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+diesel-devel %{_description}

This package contains library source intended for building other packages
which use "diesel" feature of "%{crate}" crate.

%files       -n %{name}+diesel-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+legacy-ops-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+legacy-ops-devel %{_description}

This package contains library source intended for building other packages
which use "legacy-ops" feature of "%{crate}" crate.

%files       -n %{name}+legacy-ops-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+serde-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde-devel %{_description}

This package contains library source intended for building other packages
which use "serde" feature of "%{crate}" crate.

%files       -n %{name}+serde-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+serde-arbitrary-precision-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde-arbitrary-precision-devel %{_description}

This package contains library source intended for building other packages
which use "serde-arbitrary-precision" feature of "%{crate}" crate.

%files       -n %{name}+serde-arbitrary-precision-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+serde-bincode-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde-bincode-devel %{_description}

This package contains library source intended for building other packages
which use "serde-bincode" feature of "%{crate}" crate.

%files       -n %{name}+serde-bincode-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+serde-float-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde-float-devel %{_description}

This package contains library source intended for building other packages
which use "serde-float" feature of "%{crate}" crate.

%files       -n %{name}+serde-float-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+serde-str-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde-str-devel %{_description}

This package contains library source intended for building other packages
which use "serde-str" feature of "%{crate}" crate.

%files       -n %{name}+serde-str-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+serde_json-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde_json-devel %{_description}

This package contains library source intended for building other packages
which use "serde_json" feature of "%{crate}" crate.

%files       -n %{name}+serde_json-devel
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
* Sat Feb 27 2021 Fabio Valentini <decathorpe@gmail.com> - 1.10.3-1
- Update to version 1.10.3.
- Fixes RHBZ#1928883

* Sun Feb 07 2021 Fabio Valentini <decathorpe@gmail.com> - 1.10.2-1
- Update to version 1.10.2.
- Fixes RHBZ#1911306

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Dec 12 2020 Fabio Valentini <decathorpe@gmail.com> - 1.8.1-2
- Remove features with missing dependencies (postgres, tokio-postgres).

* Wed Sep 23 2020 Fabio Valentini <decathorpe@gmail.com> - 1.8.1-1
- Update to version 1.8.1.

* Wed Jul 29 2020 Josh Stone <jistone@redhat.com> - 1.7.0-1
- Update to 1.7.0

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed May 20 09:07:19 CEST 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.6.0-1
- Update to 1.6.0

* Fri May 08 2020 Josh Stone <jistone@redhat.com> - 1.5.0-1
- Update to 1.5.0

* Wed Apr 15 2020 Josh Stone <jistone@redhat.com> - 1.4.1-1
- Update to 1.4.1

* Mon Mar 23 06:53:16 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.4.0-1
- Update to 1.4.0

* Fri Feb 28 19:14:48 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.3.0-1
- Update to 1.3.0

* Tue Feb 11 09:58:57 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.2.1-1
- Update to 1.2.1

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Dec 06 17:34:29 CET 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.3-1
- Initial package