%bcond_with check
%global debug_package %{nil}

%global crate biscuit

Name:           rust-%{crate}
Version:        0.5.0
Release:        3%{?dist}
Summary:        Library to work with Javascript Object Signing and Encryption(JOSE)

# Upstream license specification: MIT
License:        MIT
URL:            https://crates.io/crates/biscuit
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
# RHBZ 1869980
ExcludeArch:    s390x %{power64}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Library to work with Javascript Object Signing and Encryption(JOSE), including
JSON Web Tokens (JWT), JSON Web Signature (JWS) and JSON Web Encryption (JWE).}

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

%package     -n %{name}+strict-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+strict-devel %{_description}

This package contains library source intended for building other packages
which use "strict" feature of "%{crate}" crate.

%files       -n %{name}+strict-devel
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
* Tue Apr 06 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 0.5.0-3
- Update to 0.5.0

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0~beta2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 22 2020 Peter Robinson <pbrobinson@fedorapeople.org> - 0.5.0~beta2-1
- Initial package
