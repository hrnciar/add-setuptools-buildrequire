# Generated by rust2rpm 16
%bcond_without check
%global debug_package %{nil}

%global crate trust-dns-native-tls

Name:           rust-%{crate}
Version:        0.20.1
Release:        1%{?dist}
Summary:        Trust-DNS is a safe and secure DNS library

# Upstream license specification: MIT/Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/trust-dns-native-tls
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Trust-DNS is a safe and secure DNS library. This is an extension for the Trust-
DNS client to use native-tls for TLS.}

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

%package     -n %{name}+dns-over-native-tls-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+dns-over-native-tls-devel %{_description}

This package contains library source intended for building other packages
which use "dns-over-native-tls" feature of "%{crate}" crate.

%files       -n %{name}+dns-over-native-tls-devel
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
# Test data is missing
%cargo_test -- -- --skip tests::test_tls_client_stream_ipv4
%endif

%changelog
* Sun Mar 28 2021 Fabio Valentini <decathorpe@gmail.com> - 0.20.1-1
- Update to version 0.20.1.

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

* Sun Apr 19 12:16:25 CEST 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.19.4-1
- Update to 0.19.4

* Fri Feb 28 16:57:22 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.19.3-1
- Update to 0.19.3

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Dec 25 18:00:11 CET 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.18.0-1
- Update to 0.18.0

* Sat Dec 14 15:19:39 CET 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.18.0~alpha.2-1
- Update to 0.18.0~alpha.2

* Fri Dec 13 01:07:04 CET 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.7.0-1
- Release 0.7.0

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 08:59:04 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6.3-1
- Initial package
