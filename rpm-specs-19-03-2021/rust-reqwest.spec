# Generated by rust2rpm 16
%bcond_without check
%global debug_package %{nil}

%global crate reqwest

Name:           rust-%{crate}
Version:        0.11.1
Release:        1%{?dist}
Summary:        Higher level HTTP client library

# Upstream license specification: MIT/Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/reqwest
Source:         %{crates_source}
# Initial patched metadata
# * No windows/wasm32
Patch0:         reqwest-fix-metadata.diff

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Higher level HTTP client library.}

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

%package     -n %{name}+__internal_proxy_sys_no_cache-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+__internal_proxy_sys_no_cache-devel %{_description}

This package contains library source intended for building other packages
which use "__internal_proxy_sys_no_cache" feature of "%{crate}" crate.

%files       -n %{name}+__internal_proxy_sys_no_cache-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+__tls-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+__tls-devel %{_description}

This package contains library source intended for building other packages
which use "__tls" feature of "%{crate}" crate.

%files       -n %{name}+__tls-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+async-compression-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+async-compression-devel %{_description}

This package contains library source intended for building other packages
which use "async-compression" feature of "%{crate}" crate.

%files       -n %{name}+async-compression-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+blocking-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+blocking-devel %{_description}

This package contains library source intended for building other packages
which use "blocking" feature of "%{crate}" crate.

%files       -n %{name}+blocking-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+brotli-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+brotli-devel %{_description}

This package contains library source intended for building other packages
which use "brotli" feature of "%{crate}" crate.

%files       -n %{name}+brotli-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+cookie_crate-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+cookie_crate-devel %{_description}

This package contains library source intended for building other packages
which use "cookie_crate" feature of "%{crate}" crate.

%files       -n %{name}+cookie_crate-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+cookie_store-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+cookie_store-devel %{_description}

This package contains library source intended for building other packages
which use "cookie_store" feature of "%{crate}" crate.

%files       -n %{name}+cookie_store-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+cookies-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+cookies-devel %{_description}

This package contains library source intended for building other packages
which use "cookies" feature of "%{crate}" crate.

%files       -n %{name}+cookies-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+default-tls-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-tls-devel %{_description}

This package contains library source intended for building other packages
which use "default-tls" feature of "%{crate}" crate.

%files       -n %{name}+default-tls-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+gzip-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+gzip-devel %{_description}

This package contains library source intended for building other packages
which use "gzip" feature of "%{crate}" crate.

%files       -n %{name}+gzip-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+hyper-tls-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+hyper-tls-devel %{_description}

This package contains library source intended for building other packages
which use "hyper-tls" feature of "%{crate}" crate.

%files       -n %{name}+hyper-tls-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+json-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+json-devel %{_description}

This package contains library source intended for building other packages
which use "json" feature of "%{crate}" crate.

%files       -n %{name}+json-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+mime_guess-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+mime_guess-devel %{_description}

This package contains library source intended for building other packages
which use "mime_guess" feature of "%{crate}" crate.

%files       -n %{name}+mime_guess-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+multipart-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+multipart-devel %{_description}

This package contains library source intended for building other packages
which use "multipart" feature of "%{crate}" crate.

%files       -n %{name}+multipart-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+native-tls-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+native-tls-devel %{_description}

This package contains library source intended for building other packages
which use "native-tls" feature of "%{crate}" crate.

%files       -n %{name}+native-tls-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+native-tls-crate-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+native-tls-crate-devel %{_description}

This package contains library source intended for building other packages
which use "native-tls-crate" feature of "%{crate}" crate.

%files       -n %{name}+native-tls-crate-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+serde_json-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde_json-devel %{_description}

This package contains library source intended for building other packages
which use "serde_json" feature of "%{crate}" crate.

%files       -n %{name}+serde_json-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+socks-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+socks-devel %{_description}

This package contains library source intended for building other packages
which use "socks" feature of "%{crate}" crate.

%files       -n %{name}+socks-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+stream-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+stream-devel %{_description}

This package contains library source intended for building other packages
which use "stream" feature of "%{crate}" crate.

%files       -n %{name}+stream-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+time-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+time-devel %{_description}

This package contains library source intended for building other packages
which use "time" feature of "%{crate}" crate.

%files       -n %{name}+time-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+tokio-native-tls-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+tokio-native-tls-devel %{_description}

This package contains library source intended for building other packages
which use "tokio-native-tls" feature of "%{crate}" crate.

%files       -n %{name}+tokio-native-tls-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+tokio-socks-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+tokio-socks-devel %{_description}

This package contains library source intended for building other packages
which use "tokio-socks" feature of "%{crate}" crate.

%files       -n %{name}+tokio-socks-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+tokio-util-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+tokio-util-devel %{_description}

This package contains library source intended for building other packages
which use "tokio-util" feature of "%{crate}" crate.

%files       -n %{name}+tokio-util-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+trust-dns-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+trust-dns-devel %{_description}

This package contains library source intended for building other packages
which use "trust-dns" feature of "%{crate}" crate.

%files       -n %{name}+trust-dns-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+trust-dns-resolver-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+trust-dns-resolver-devel %{_description}

This package contains library source intended for building other packages
which use "trust-dns-resolver" feature of "%{crate}" crate.

%files       -n %{name}+trust-dns-resolver-devel
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
# * skip tests which require internet access
# * skip "file" test which depends on Cargo.lock being present
%cargo_test -- -- \
    --skip test_allowed_methods \
    --skip test_badssl_modern \
    --skip test_badssl_self_signed \
    --skip test_badssl_wrong_host \
    --skip file
%endif

%changelog
* Sat Mar 06 2021 Fabio Valentini <decathorpe@gmail.com> - 0.11.1-1
- Update to version 0.11.1.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Nov 27 2020 Fabio Valentini <decathorpe@gmail.com> - 0.10.9-1
- Update to version 0.10.9.

* Wed Oct 21 2020 Fabio Valentini <decathorpe@gmail.com> - 0.10.8-2
- Bump to tokio-socks 0.3.

* Wed Aug 26 2020 Josh Stone <jistone@redhat.com> - 0.10.8-1
- Update to 0.10.8

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 04 2020 Josh Stone <jistone@redhat.com> - 0.10.6-1
- Update to 0.10.6

* Mon May 18 12:49:32 CEST 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.10.4-2
- Update libflate to 1.0

* Wed Mar 04 2020 Josh Stone <jistone@redhat.com> - 0.10.4-1
- Update to 0.10.4

* Thu Feb 27 2020 Josh Stone <jistone@redhat.com> - 0.10.3-1
- Update to 0.10.3

* Fri Feb 21 2020 Josh Stone <jistone@redhat.com> - 0.10.2-1
- Update to 0.10.2

* Tue Feb 11 10:17:33 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.10.1-1
- Update to 0.10.1

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Dec 26 07:19:05 CET 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.9.24-1
- Update to 0.9.24

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 21 18:20:27 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.9.13-2
- Regenerate

* Tue Apr 02 2019 Josh Stone <jistone@redhat.com> - 0.9.13-1
- Update to 0.9.13

* Thu Mar 21 00:24:21 CET 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.9.12-1
- Update to 0.9.12

* Tue Mar 05 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.9.11-1
- Update to 0.9.11

* Tue Feb 19 2019 Josh Stone <jistone@redhat.com> - 0.9.10-1
- Update to 0.9.10

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jan 26 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.9.9-2
- Run tests in infrastructure

* Sat Jan 26 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.9.9-1
- Initial package