# Generated by rust2rpm 17
%bcond_with check
%global debug_package %{nil}

%global crate cryptoki-sys

Name:           rust-%{crate}
Version:        0.1.1
Release:        2%{?dist}
Summary:        FFI wrapper around the PKCS #11 API

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            https://crates.io/crates/cryptoki-sys
Source:         %{crates_source}
Patch0:         cryptoki-sys-fix-metadata.diff

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
FFI wrapper around the PKCS #11 API.}

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

%package     -n %{name}+bindgen-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+bindgen-devel %{_description}

This package contains library source intended for building other packages
which use "bindgen" feature of "%{crate}" crate.

%files       -n %{name}+bindgen-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+generate-bindings-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+generate-bindings-devel %{_description}

This package contains library source intended for building other packages
which use "generate-bindings" feature of "%{crate}" crate.

%files       -n %{name}+generate-bindings-devel
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
* Tue Apr 06 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 0.1.1-2
- Always run generate-bindings

* Mon Apr 05 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 0.1.1-1
- Update to 0.1.1

* Mon Apr 05 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 0.1.0-2
- rebuild

* Fri Mar 26 09:59:25 GMT 2021 Peter Robinson <pbrobinson@gmail.com> - 0.1.0-1
- Initial package