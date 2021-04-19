# Generated by rust2rpm 13
# * quantiles is not packaged
# * proptest is too old
# * rand_distr is too old
%bcond_with check
%global debug_package %{nil}

%global crate average

Name:           rust-%{crate}
Version:        0.10.6
Release:        2%{?dist}
Summary:        Calculate statistics iteratively

# Upstream license specification: MIT/Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/average
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Calculate statistics iteratively.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-APACHE LICENSE-MIT
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

%package     -n %{name}+rayon-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+rayon-devel %{_description}

This package contains library source intended for building other packages
which use "rayon" feature of "%{crate}" crate.

%files       -n %{name}+rayon-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+serde-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde-devel %{_description}

This package contains library source intended for building other packages
which use "serde" feature of "%{crate}" crate.

%files       -n %{name}+serde-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+serde-big-array-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde-big-array-devel %{_description}

This package contains library source intended for building other packages
which use "serde-big-array" feature of "%{crate}" crate.

%files       -n %{name}+serde-big-array-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+serde1-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde1-devel %{_description}

This package contains library source intended for building other packages
which use "serde1" feature of "%{crate}" crate.

%files       -n %{name}+serde1-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+serde_derive-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde_derive-devel %{_description}

This package contains library source intended for building other packages
which use "serde_derive" feature of "%{crate}" crate.

%files       -n %{name}+serde_derive-devel
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
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Oct 01 2020 Fabio Valentini <decathorpe@gmail.com> - 0.10.6-1
- Update to version 0.10.6.

* Wed Sep 23 2020 Fabio Valentini <decathorpe@gmail.com> - 0.10.5-1
- Update to version 0.10.5.

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Feb 19 2020 Randy Barlow <bowlofeggs@fedoraproject.org> - 0.10.4-1
- Update to 0.10.4 (#1804707).

* Sun Feb 16 07:44:22 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.10.3-2
- Build with tests

* Tue Jan 21 11:47:04 EST 2020 Randy Barlow <randy@electronsweatshop.com> - 0.10.3-1
- Initial package