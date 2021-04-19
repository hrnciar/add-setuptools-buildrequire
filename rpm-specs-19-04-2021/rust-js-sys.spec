# Generated by rust2rpm 16
# * wasm-bindgen-test is not packaged yet
%bcond_with check
%global debug_package %{nil}

%global crate js-sys

Name:           rust-%{crate}
Version:        0.3.50
Release:        1%{?dist}
Summary:        Bindings for all JS global objects and functions

# Upstream license specification: MIT/Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/js-sys
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Bindings for all JS global objects and functions in all JS environments like
Node.js and browsers, built on `#[wasm_bindgen]` using the `wasm-bindgen`
crate.}

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
* Wed Mar 31 2021 Fabio Valentini <decathorpe@gmail.com> - 0.3.50-1
- Update to version 0.3.50.

* Wed Mar 24 2021 Fabio Valentini <decathorpe@gmail.com> - 0.3.49-1
- Update to version 0.3.49.

* Sat Feb 27 2021 Fabio Valentini <decathorpe@gmail.com> - 0.3.48-1
- Update to version 0.3.48.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.46-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec 08 2020 Fabio Valentini <decathorpe@gmail.com> - 0.3.46-1
- Update to version 0.3.46.

* Wed Sep 23 2020 Fabio Valentini <decathorpe@gmail.com> - 0.3.45-1
- Update to version 0.3.45.

* Wed Jul 22 2020 Peter Robinson <pbrobinson@fedorapeople.org> - 0.3.42-1
- Initial package