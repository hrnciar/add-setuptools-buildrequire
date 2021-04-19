# Generated by rust2rpm 11
%bcond_without check
%global debug_package %{nil}

%global crate websocket

Name:           rust-%{crate}
Version:        0.24.0
Release:        4%{?dist}
Summary:        WebSocket (RFC6455) library for Rust

# Upstream license specification: MIT
License:        MIT
URL:            https://crates.io/crates/websocket
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
WebSocket (RFC6455) library for Rust.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE
%doc README.md ROADMAP.md
%{cargo_registry}/%{crate}-%{version}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+async-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+async-devel %{_description}

This package contains library source intended for building other packages
which use "async" feature of "%{crate}" crate.

%files       -n %{name}+async-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+async-ssl-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+async-ssl-devel %{_description}

This package contains library source intended for building other packages
which use "async-ssl" feature of "%{crate}" crate.

%files       -n %{name}+async-ssl-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+bytes-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+bytes-devel %{_description}

This package contains library source intended for building other packages
which use "bytes" feature of "%{crate}" crate.

%files       -n %{name}+bytes-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+futures-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+futures-devel %{_description}

This package contains library source intended for building other packages
which use "futures" feature of "%{crate}" crate.

%files       -n %{name}+futures-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+native-tls-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+native-tls-devel %{_description}

This package contains library source intended for building other packages
which use "native-tls" feature of "%{crate}" crate.

%files       -n %{name}+native-tls-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+nightly-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+nightly-devel %{_description}

This package contains library source intended for building other packages
which use "nightly" feature of "%{crate}" crate.

%files       -n %{name}+nightly-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+sync-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+sync-devel %{_description}

This package contains library source intended for building other packages
which use "sync" feature of "%{crate}" crate.

%files       -n %{name}+sync-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+sync-ssl-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+sync-ssl-devel %{_description}

This package contains library source intended for building other packages
which use "sync-ssl" feature of "%{crate}" crate.

%files       -n %{name}+sync-ssl-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+tokio-codec-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+tokio-codec-devel %{_description}

This package contains library source intended for building other packages
which use "tokio-codec" feature of "%{crate}" crate.

%files       -n %{name}+tokio-codec-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+tokio-io-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+tokio-io-devel %{_description}

This package contains library source intended for building other packages
which use "tokio-io" feature of "%{crate}" crate.

%files       -n %{name}+tokio-io-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+tokio-reactor-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+tokio-reactor-devel %{_description}

This package contains library source intended for building other packages
which use "tokio-reactor" feature of "%{crate}" crate.

%files       -n %{name}+tokio-reactor-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+tokio-tcp-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+tokio-tcp-devel %{_description}

This package contains library source intended for building other packages
which use "tokio-tcp" feature of "%{crate}" crate.

%files       -n %{name}+tokio-tcp-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+tokio-tls-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+tokio-tls-devel %{_description}

This package contains library source intended for building other packages
which use "tokio-tls" feature of "%{crate}" crate.

%files       -n %{name}+tokio-tls-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

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
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.24.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.24.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.24.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Dec 05 14:41:35 CET 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.24.0-1
- Update to 0.24.0

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.22.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun 22 12:42:32 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.22.4-2
- Regenerate

* Thu May 02 08:49:24 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.22.4-1
- Update to 0.22.4

* Wed Mar 13 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.22.3-1
- Initial package
