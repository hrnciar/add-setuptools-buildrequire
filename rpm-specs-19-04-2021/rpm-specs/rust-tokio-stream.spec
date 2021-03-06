# Generated by rust2rpm 16
# * async-stream is not packaged yet
%bcond_with check
%global debug_package %{nil}

%global crate tokio-stream

Name:           rust-%{crate}
Version:        0.1.5
Release:        1%{?dist}
Summary:        Utilities to work with Stream and tokio

# Upstream license specification: MIT
License:        MIT
URL:            https://crates.io/crates/tokio-stream
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Utilities to work with `Stream` and `tokio`.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE
%doc CHANGELOG.md
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+fs-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+fs-devel %{_description}

This package contains library source intended for building other packages
which use "fs" feature of "%{crate}" crate.

%files       -n %{name}+fs-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+io-util-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+io-util-devel %{_description}

This package contains library source intended for building other packages
which use "io-util" feature of "%{crate}" crate.

%files       -n %{name}+io-util-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+net-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+net-devel %{_description}

This package contains library source intended for building other packages
which use "net" feature of "%{crate}" crate.

%files       -n %{name}+net-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+signal-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+signal-devel %{_description}

This package contains library source intended for building other packages
which use "signal" feature of "%{crate}" crate.

%files       -n %{name}+signal-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+sync-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+sync-devel %{_description}

This package contains library source intended for building other packages
which use "sync" feature of "%{crate}" crate.

%files       -n %{name}+sync-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+time-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+time-devel %{_description}

This package contains library source intended for building other packages
which use "time" feature of "%{crate}" crate.

%files       -n %{name}+time-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+tokio-util-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+tokio-util-devel %{_description}

This package contains library source intended for building other packages
which use "tokio-util" feature of "%{crate}" crate.

%files       -n %{name}+tokio-util-devel
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
* Thu Mar 25 2021 Fabio Valentini <decathorpe@gmail.com> - 0.1.5-1
- Initial package
