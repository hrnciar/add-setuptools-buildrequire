%bcond_with check
%global debug_package %{nil}

%global crate prost-build

Name:           rust-%{crate}
Version:        0.7.0
Release:        2%{?dist}
Summary:        Protocol Buffers implementation for the Rust Language

# Upstream license specification: Apache-2.0
# https://github.com/danburkert/prost/issues/353
License:        ASL 2.0
URL:            https://crates.io/crates/prost-build
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  protobuf-compiler
BuildRequires:  protobuf-devel
BuildRequires:  rust-packaging

%global _description %{expand:
Protocol Buffers implementation for the Rust Language.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
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
/usr/bin/env PROTOC=%{_bindir}/protoc PROTOC_INCLUDE=%{_includedir}
rm -rf third-party/
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
/usr/bin/env PROTOC=%{_bindir}/protoc PROTOC_INCLUDE=%{_includedir}
%cargo_build

%install
/usr/bin/env PROTOC=%{_bindir}/protoc PROTOC_INCLUDE=%{_includedir}
%cargo_install

%if %{with check}
%check
/usr/bin/env PROTOC=%{_bindir}/protoc PROTOC_INCLUDE=%{_includedir}
%cargo_install
%cargo_test
%endif

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan  3 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 0.7.0-1
- Update to 0.7.0

* Fri Sep 18 2020 Fabio Valentini <decathorpe@gmail.com> - 0.6.1-3
- Bump to which 4.

* Mon Sep 07 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 0.6.1-2
- Review updates

* Tue Aug 25 15:31:56 BST 2020 Peter Robinson <pbrobinson@gmail.com> - 0.6.1-1
- Initial package
