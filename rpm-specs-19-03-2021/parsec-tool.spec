%bcond_without check
%global __cargo_skip_build 0
%global __cargo_is_lib() false

%global custom_cargo_build /usr/bin/env PROTOC=%{_bindir}/protoc PROTOC_INCLUDe=%{_includedir} CARGO_HOME=.cargo RUSTC_BOOTSTRAP=1 %{_bindir}/cargo build %{_smp_mflags} -Z avoid-dev-deps --release
%global custom_cargo_test /usr/bin/env PROTOC=%{_bindir}/protoc PROTOC_INCLUDe=%{_includedir} CARGO_HOME=.cargo RUSTC_BOOTSTRAP=1 %{_bindir}/cargo test %{_smp_mflags} -Z avoid-dev-deps --release --no-fail-fast

Name:          parsec-tool
Version:       0.1.0
Release:       3%{?dist}
Summary:       A PARSEC cli

# ASL 2.0
# BSD
# MIT
# MIT or ASL 2.0
# Unlicense or MIT
License:       ASL 2.0 and BSD and MIT
URL:           https://github.com/parallaxsecond/parsec-tool
Source0:       %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:        parsec-tools-deps.diff

ExclusiveArch: %{rust_arches}
# rhbz 1869980
ExcludeArch:   s390x %{power64}

BuildRequires: protobuf-compiler
BuildRequires: rust-packaging

%description
A tool to communicate with the Parsec service on the command-line.

%prep
%autosetup -p1
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
export PROTOC=%{_bindir}/protoc
export PROTOC_INCLUDE=%{_includedir}
%cargo_test
%endif

%files
%license LICENSE
%{_bindir}/parsec-tool

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec 28 13:26:39 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.1.0-2
- Rebuild

* Thu Oct 22 2020 Peter Robinson <pbrobinson@fedoraproject.org> 0.1.0-1
- Initial packaging
