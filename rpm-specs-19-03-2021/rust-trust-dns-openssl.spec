# Generated by rust2rpm 16
%bcond_without check
%global debug_package %{nil}

%global crate trust-dns-openssl

Name:           rust-%{crate}
Version:        0.20.0
Release:        1%{?dist}
Summary:        Trust-DNS is a safe and secure DNS library

# Upstream license specification: MIT/Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/trust-dns-openssl
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Trust-DNS is a safe and secure DNS library. This is an extension for the Trust-
DNS client to use tokio-openssl for TLS.}

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

%package     -n %{name}+dns-over-openssl-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+dns-over-openssl-devel %{_description}

This package contains library source intended for building other packages
which use "dns-over-openssl" feature of "%{crate}" crate.

%files       -n %{name}+dns-over-openssl-devel
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
* Mon Mar 08 2021 Fabio Valentini <decathorpe@gmail.com> - 0.20.0-1
- Update to version 0.20.0.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.19.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Nov 22 2020 Fabio Valentini <decathorpe@gmail.com> - 0.19.6-1
- Update to version 0.19.6.

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.19.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 05 2020 Josh Stone <jistone@redhat.com> - 0.19.5-1
- Update to 0.19.5

* Sun Apr 19 12:15:29 CEST 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.19.4-1
- Update to 0.19.4

* Fri Feb 28 16:59:15 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.19.3-1
- Update to 0.19.3

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Dec 25 17:58:21 CET 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.18.0-1
- Update to 0.18.0

* Sat Dec 14 15:18:35 CET 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.18.0~alpha.2-1
- Update to 0.18.0~alpha.2

* Fri Dec 13 01:11:05 CET 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.7.0-1
- Release 0.7.0

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 09:02:57 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6.3-1
- Initial package
