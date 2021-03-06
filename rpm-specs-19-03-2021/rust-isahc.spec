# Generated by rust2rpm 13
# * test-case ^1 is not packaged
# * tracing-subscriber ^0.2 is not packaged
%bcond_with check
%global debug_package %{nil}

%global crate isahc

Name:           rust-%{crate}
Version:        0.9.10
Release:        2%{?dist}
Summary:        Practical HTTP client that is fun to use

# Upstream license specification: MIT
License:        MIT
URL:            https://crates.io/crates/isahc
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Practical HTTP client that is fun to use.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE LICENSE-CC-BY
%doc README.md INTERNALS.md
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+chrono-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+chrono-devel %{_description}

This package contains library source intended for building other packages
which use "chrono" feature of "%{crate}" crate.

%files       -n %{name}+chrono-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+cookies-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+cookies-devel %{_description}

This package contains library source intended for building other packages
which use "cookies" feature of "%{crate}" crate.

%files       -n %{name}+cookies-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+encoding_rs-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+encoding_rs-devel %{_description}

This package contains library source intended for building other packages
which use "encoding_rs" feature of "%{crate}" crate.

%files       -n %{name}+encoding_rs-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+http2-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+http2-devel %{_description}

This package contains library source intended for building other packages
which use "http2" feature of "%{crate}" crate.

%files       -n %{name}+http2-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+json-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+json-devel %{_description}

This package contains library source intended for building other packages
which use "json" feature of "%{crate}" crate.

%files       -n %{name}+json-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+middleware-api-preview-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+middleware-api-preview-devel %{_description}

This package contains library source intended for building other packages
which use "middleware-api-preview" feature of "%{crate}" crate.

%files       -n %{name}+middleware-api-preview-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+mime-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+mime-devel %{_description}

This package contains library source intended for building other packages
which use "mime" feature of "%{crate}" crate.

%files       -n %{name}+mime-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+parking_lot-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+parking_lot-devel %{_description}

This package contains library source intended for building other packages
which use "parking_lot" feature of "%{crate}" crate.

%files       -n %{name}+parking_lot-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+psl-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+psl-devel %{_description}

This package contains library source intended for building other packages
which use "psl" feature of "%{crate}" crate.

%files       -n %{name}+psl-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+publicsuffix-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+publicsuffix-devel %{_description}

This package contains library source intended for building other packages
which use "publicsuffix" feature of "%{crate}" crate.

%files       -n %{name}+publicsuffix-devel
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

%package     -n %{name}+spnego-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+spnego-devel %{_description}

This package contains library source intended for building other packages
which use "spnego" feature of "%{crate}" crate.

%files       -n %{name}+spnego-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+static-curl-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+static-curl-devel %{_description}

This package contains library source intended for building other packages
which use "static-curl" feature of "%{crate}" crate.

%files       -n %{name}+static-curl-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+static-ssl-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+static-ssl-devel %{_description}

This package contains library source intended for building other packages
which use "static-ssl" feature of "%{crate}" crate.

%files       -n %{name}+static-ssl-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+text-decoding-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+text-decoding-devel %{_description}

This package contains library source intended for building other packages
which use "text-decoding" feature of "%{crate}" crate.

%files       -n %{name}+text-decoding-devel
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
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Oct 01 2020 Fabio Valentini <decathorpe@gmail.com> - 0.9.10-1
- Update to version 0.9.10.

* Wed Sep 23 2020 Fabio Valentini <decathorpe@gmail.com> - 0.9.9-1
- Update to version 0.9.9.

* Tue Aug 25 2020 Josh Stone <jistone@redhat.com> - 0.9.8-1
- Update to 0.9.8

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun May 17 16:21:01 CEST 2020 Igor Raits <i.gnatenko.brain@gmail.com> - 0.9.2-1
- Initial package
