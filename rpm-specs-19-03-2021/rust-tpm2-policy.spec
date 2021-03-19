%bcond_with check
%global debug_package %{nil}

%global crate tpm2-policy

Name:           rust-%{crate}
Version:        0.3.1
Release:        3%{?dist}
Summary:        Specify and send TPM2 policies to satisfy object authorization

# Upstream license specification: EUPL-1.2
License:        EUPL-1.2
URL:            https://crates.io/crates/tpm2-policy
Source:         %{crates_source}
Patch1:         tpm2-policy-fix-metadata.diff

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Specify and send TPM2 policies to satisfy object authorization.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE
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
* Mon Feb 15 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 0.3.1-3
- Update tss-esapi version requirements

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Dec  3 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 0.3.1-1
- Update to 0.3.1

* Thu Dec  3 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 0.3.0-1
- Update to 0.3.0

* Thu Aug 13 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 0.2.0-1
- Update to 0.2.0

* Mon Aug 03 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 0.1.0-1
 - Initial package
