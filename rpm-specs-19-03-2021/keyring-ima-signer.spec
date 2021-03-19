%bcond_without check
%global __cargo_skip_build 0
%global __cargo_is_lib() false

Name:           keyring-ima-signer
Version:        0.1.0
Release:        2%{?dist}
Summary:        An IMA file signing tool using the kernel keyring

License:        EUPL 1.2
URL:            https://github.com/fedora-iot/keyring-ima-signer/
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
# https://github.com/fedora-iot/keyring-ima-signer/pull/12
Patch0:         12.patch

ExclusiveArch:  %{rust_arches}
BuildRequires:  rust-packaging

%description
The IMA (Integrity Measurement Architecture) is a key component of the
Linux integrity subsystem designed to ensure integrity, authenticity,
and confidentiality of systems including hardware root of trusts (TPM).

This tool allows signing of files in userspace, inclusding options of
including the signature in xattr or a .sig file, using signing keys
stored in the kernel keyring to ensure they're not recoverable.

%prep
%autosetup -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test -- -- --skip real_ --skip loop_ --skip travis_
%endif

%files
%license LICENSE
%doc README.md
%{_bindir}/keyring-ima-signer

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Dec 17 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 0.1.0-1
- Initial release
