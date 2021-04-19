# Generated by rust2rpm 13
%bcond_without check
%global debug_package %{nil}

%global crate quickcheck

Name:           rust-%{crate}0.9
Version:        0.9.2
Release:        1%{?dist}
Summary:        Automatic property based testing with shrinking

# Upstream license specification: Unlicense/MIT
License:        Unlicense or MIT
URL:            https://crates.io/crates/quickcheck
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Automatic property based testing with shrinking.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license UNLICENSE LICENSE-MIT COPYING
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

%package     -n %{name}+env_logger-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+env_logger-devel %{_description}

This package contains library source intended for building other packages
which use "env_logger" feature of "%{crate}" crate.

%files       -n %{name}+env_logger-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+log-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+log-devel %{_description}

This package contains library source intended for building other packages
which use "log" feature of "%{crate}" crate.

%files       -n %{name}+log-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+regex-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+regex-devel %{_description}

This package contains library source intended for building other packages
which use "regex" feature of "%{crate}" crate.

%files       -n %{name}+regex-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+unstable-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+unstable-devel %{_description}

This package contains library source intended for building other packages
which use "unstable" feature of "%{crate}" crate.

%files       -n %{name}+unstable-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+use_logging-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+use_logging-devel %{_description}

This package contains library source intended for building other packages
which use "use_logging" feature of "%{crate}" crate.

%files       -n %{name}+use_logging-devel
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
* Thu Mar 25 2021 Fabio Valentini <decathorpe@gmail.com> - 0.9.2-1
- Initial compat package for quickcheck 0.9