# Generated by rust2rpm 13
%bcond_without check
%global debug_package %{nil}

%global crate cssparser

Name:           rust-%{crate}
Version:        0.27.2
Release:        4%{?dist}
Summary:        Rust implementation of CSS Syntax Level 3

# Upstream license specification: MPL-2.0
License:        MPLv2.0
URL:            https://crates.io/crates/cssparser
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Rust implementation of CSS Syntax Level 3.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE
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

%package     -n %{name}+bench-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+bench-devel %{_description}

This package contains library source intended for building other packages
which use "bench" feature of "%{crate}" crate.

%files       -n %{name}+bench-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+dummy_match_byte-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+dummy_match_byte-devel %{_description}

This package contains library source intended for building other packages
which use "dummy_match_byte" feature of "%{crate}" crate.

%files       -n %{name}+dummy_match_byte-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+serde-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde-devel %{_description}

This package contains library source intended for building other packages
which use "serde" feature of "%{crate}" crate.

%files       -n %{name}+serde-devel
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
# https://github.com/servo/rust-cssparser/issues/213
%cargo_test -- --doc
%endif

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.27.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.27.2-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.27.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Feb 15 13:25:32 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.27.2-1
- Update to 0.27.2

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.25.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 15 2020 Josh Stone <jistone@redhat.com> - 0.25.9-1
- Update to 0.25.9
- Bump to autocfg 1

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.25.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jul 07 15:05:26 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.25.8-1
- Update to 0.25.8

* Sat Jul 06 11:23:45 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.25.7-1
- Update to 0.25.7

* Thu May 30 17:59:18 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.25.6-1
- Update to 0.25.6

* Tue Apr 30 09:40:06 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.25.5-1
- Update to 0.25.5

* Wed Apr 03 2019 Josh Stone <jistone@redhat.com> - 0.25.3-1
- Update to 0.25.3

* Sun Feb 10 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.25.2-1
- Update to 0.25.2

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.24.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Oct 04 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.24.1-1
- Update to 0.24.1

* Sun Jul 29 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.24.0-3
- Bump encoding_rs to 0.8

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.24.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Josh Stone <jistone@redhat.com> - 0.24.0-1
- Update to 0.24.0

* Sat Jun 23 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org>
- Adopt to new macro

* Thu Jun 14 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.23.10-1
- Update to 0.23.10

* Tue Jun 05 2018 Josh Stone <jistone@redhat.com> - 0.23.9-1
- Update to 0.23.9

* Thu May 03 2018 Josh Stone <jistone@redhat.com> - 0.23.7-1
- Update to 0.23.7

* Sat Apr 28 2018 Josh Stone <jistone@redhat.com> - 0.23.6-1
- Update to 0.23.6

* Tue Apr 17 2018 Josh Stone <jistone@redhat.com> - 0.23.5-1
- Update to 0.23.5

* Wed Apr 04 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.23.4-1
- Update to 0.23.4

* Mon Mar 26 2018 Josh Stone <jistone@redhat.com> - 0.23.2-4
- Bump itoa to 0.4.0

* Fri Mar 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.23.2-3
- Bump syn to 0.12, quote to 0.4

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.23.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 24 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.23.2-1
- Initial package
