%bcond_with check
%global debug_package %{nil}

%global custom_cargo_build /usr/bin/env PROTOC=%{_bindir}/protoc PROTOC_INCLUDe=%{_includedir} CARGO_HOME=.cargo RUSTC_BOOTSTRAP=1 %{_bindir}/cargo build %{_smp_mflags} -Z avoid-dev-deps --release
%global custom_cargo_test /usr/bin/env PROTOC=%{_bindir}/protoc PROTOC_INCLUDe=%{_includedir} CARGO_HOME=.cargo RUSTC_BOOTSTRAP=1 %{_bindir}/cargo test %{_smp_mflags} -Z avoid-dev-deps --release --no-fail-fast

%global crate parsec-client

Name:           rust-%{crate}
Version:        0.11.0
Release:        3%{?dist}
Summary:        Parsec Client library for the Rust ecosystem

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            https://crates.io/crates/parsec-client
Source:         %{crates_source}
Patch1:         parsec-client-fix-metadata.diff

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  protobuf-compiler
BuildRequires:  rust-packaging

%global _description %{expand:
Parsec Client library for the Rust ecosystem.}

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

%package     -n %{name}+testing-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+testing-devel %{_description}

This package contains library source intended for building other packages
which use "testing" feature of "%{crate}" crate.

%files       -n %{name}+testing-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
export PROTOC=%{_bindir}/protoc
export PROTOC_INCLUDE=%{_includedir}
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%custom_cargo_build

%install
export PROTOC=%{_bindir}/protoc
export PROTOC_INCLUDE=%{_includedir}
%cargo_install

%if %{with check}
%check
%custom_cargo_test
%endif

%changelog
* Mon Feb 15 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 0.11.0-3
- Rebuild against parsec-interface 0.23.0

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Oct 22 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 0.11.0-1
- Update to 0.11.0

* Fri Oct 02 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 0.10.0-1
- Update to 0.10.0

* Wed Sep 16 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 0.9.0-3
- Another system protobuf fix

* Wed Sep 09 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 0.9.0-2
- Fixes for system protobuf

* Tue Sep 08 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 0.9.0-1
- Initial package
