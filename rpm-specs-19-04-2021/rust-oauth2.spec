# Generated by rust2rpm 17
%bcond_without check
%global debug_package %{nil}

%global crate oauth2

Name:           rust-%{crate}
Version:        3.0.0
Release:        2%{?dist}
Summary:        Extensible, strongly-typed implementation of OAuth2

# Upstream license specification: MIT/Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/oauth2
Source:         %{crates_source}
# Initial patched metadata
# * Bump sha2 to 0.9
# * Remove dependency on rust-crypto
# * Relax unicode-normalization dep
# * Relax hex dep
# * Set "reqwest-010" as default
Patch0:         oauth2-fix-metadata.diff

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Extensible, strongly-typed implementation of OAuth2.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%doc examples README.md
%license LICENSE-MIT LICENSE-APACHE
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+async-trait-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+async-trait-devel %{_description}

This package contains library source intended for building other packages
which use "async-trait" feature of "%{crate}" crate.

%files       -n %{name}+async-trait-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+curl-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+curl-devel %{_description}

This package contains library source intended for building other packages
which use "curl" feature of "%{crate}" crate.

%files       -n %{name}+curl-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+futures-0-1-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+futures-0-1-devel %{_description}

This package contains library source intended for building other packages
which use "futures-0-1" feature of "%{crate}" crate.

%files       -n %{name}+futures-0-1-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+futures-0-3-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+futures-0-3-devel %{_description}

This package contains library source intended for building other packages
which use "futures-0-3" feature of "%{crate}" crate.

%files       -n %{name}+futures-0-3-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+futures-01-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+futures-01-devel %{_description}

This package contains library source intended for building other packages
which use "futures-01" feature of "%{crate}" crate.

%files       -n %{name}+futures-01-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+futures-03-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+futures-03-devel %{_description}

This package contains library source intended for building other packages
which use "futures-03" feature of "%{crate}" crate.

%files       -n %{name}+futures-03-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+http-0-2-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+http-0-2-devel %{_description}

This package contains library source intended for building other packages
which use "http-0-2" feature of "%{crate}" crate.

%files       -n %{name}+http-0-2-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+reqwest-0-10-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+reqwest-0-10-devel %{_description}

This package contains library source intended for building other packages
which use "reqwest-0-10" feature of "%{crate}" crate.

%files       -n %{name}+reqwest-0-10-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+reqwest-010-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+reqwest-010-devel %{_description}

This package contains library source intended for building other packages
which use "reqwest-010" feature of "%{crate}" crate.

%files       -n %{name}+reqwest-010-devel
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
%cargo_test -- --lib
%cargo_test -- --doc
%endif

%changelog
* Mon Apr 12 16:04:00 CEST 2021 Jens Reimann <jreimann@redhat.com> - 3.0.0-2
- Drop reqwest 0.9 feature from the build
* Thu Apr 08 08:20:51 CEST 2021 Jens Reimann <jreimann@redhat.com> - 3.0.0-1
- Initial package