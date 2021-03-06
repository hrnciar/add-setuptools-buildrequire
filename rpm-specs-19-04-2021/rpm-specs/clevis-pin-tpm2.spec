%bcond_without check
%global __cargo_skip_build 0
%global __cargo_is_lib() false

Name:           clevis-pin-tpm2
Version:        0.3.0
Release:        1%{?dist}
Summary:        Clevis PIN for unlocking with TPM2 supporting Authorized Policies

License:        EUPL 1.2
URL:            https://github.com/fedora-iot/clevis-pin-tpm2/
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         clevis-pin-tpm2-fix-metadata.diff

ExclusiveArch:  %{rust_arches}
# RHBZ 1869980
ExcludeArch:    s390x %{power64}

BuildRequires:  rust-packaging
Requires:       clevis

%description
%{summary}.

%prep
%autosetup -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install
ln -s /usr/bin/clevis-pin-tpm2 %{buildroot}/usr/bin/clevis-encrypt-tpm2plus
ln -s /usr/bin/clevis-pin-tpm2 %{buildroot}/usr/bin/clevis-decrypt-tpm2plus

%if %{with check}
%check
%cargo_test -- -- --skip real_ --skip loop_ --skip travis_
%endif

%files
%license LICENSE
%{_bindir}/clevis-pin-tpm2
%{_bindir}/clevis-*-tpm2plus

%changelog
* Tue Apr 06 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 0.3.0-1
- Update to 0.3.0

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Dec  3 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 0.2.0-1
- Update to 0.2.0

* Tue Nov 10 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 0.1.4-1
- Update to 0.1.4

* Sat Aug 29 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 0.1.3-1
- Update to 0.1.3

* Tue Aug 25 2020 Patrick Uiterwijk <patrick@puiterwijk.org> - 0.1.2-2
- Add symlink to clevis-{en,de}crypt-tpm2plus

* Fri Aug 21 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 0.1.2-1
- Update to 0.1.2

* Thu Aug 13 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 0.1.1-1
- Update to 0.1.1

* Mon Aug  3 2020 Peter Robinson <pbrobinson@fedoraproject.org> 0.0.1-1
- Initial release
