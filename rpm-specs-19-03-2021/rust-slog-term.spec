# Generated by rust2rpm 16
%bcond_without check
%global debug_package %{nil}

%global crate slog-term

Name:           rust-%{crate}
Version:        2.7.0
Release:        1%{?dist}
Summary:        Unix terminal drain and formatter for slog-rs

# Upstream license specification: MPL-2.0/MIT/Apache-2.0
License:        MPLv2.0 or MIT or ASL 2.0
URL:            https://crates.io/crates/slog-term
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Unix terminal drain and formatter for slog-rs.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-MPL2 LICENSE-MIT LICENSE-APACHE
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

%package     -n %{name}+erased-serde-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+erased-serde-devel %{_description}

This package contains library source intended for building other packages
which use "erased-serde" feature of "%{crate}" crate.

%files       -n %{name}+erased-serde-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+nested-values-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+nested-values-devel %{_description}

This package contains library source intended for building other packages
which use "nested-values" feature of "%{crate}" crate.

%files       -n %{name}+nested-values-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+serde-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde-devel %{_description}

This package contains library source intended for building other packages
which use "serde" feature of "%{crate}" crate.

%files       -n %{name}+serde-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+serde_json-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde_json-devel %{_description}

This package contains library source intended for building other packages
which use "serde_json" feature of "%{crate}" crate.

%files       -n %{name}+serde_json-devel
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
* Sun Feb 07 2021 Fabio Valentini <decathorpe@gmail.com> - 2.7.0-1
- Update to version 2.7.0.
- Fixes RHBZ#1925877

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 02 16:36:43 CEST 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 2.6.0-1
- Update to 2.6.0

* Thu Jan 30 2020 Josh Stone <jistone@redhat.com> - 2.5.0-1
- Update to 2.5.0

* Thu Jan 23 2020 Josh Stone <jistone@redhat.com> - 2.4.2-2
- Bump to thread_local 1

* Sat Dec 14 03:27:02 CET 2019 Robert-André Mauchin <zebob.m@gmail.com> - 2.4.2-1
- Update to 2.4.2

* Sun Jul 28 17:44:26 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.4.1-1
- Update to 2.4.1

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 21 19:45:01 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.4.0-2
- Regenerate

* Sat Apr 27 08:51:09 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.4.0-1
- Initial package
