# Generated by rust2rpm 16
# * Test files are not shipped
%bcond_with check
%global debug_package %{nil}

%global crate jpeg-decoder

Name:           rust-%{crate}
Version:        0.1.22
Release:        1%{?dist}
Summary:        JPEG decoder

# Upstream license specification: MIT / Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/jpeg-decoder
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
JPEG decoder.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-MIT LICENSE-APACHE
%doc README.md CHANGELOG.md
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+rayon-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+rayon-devel %{_description}

This package contains library source intended for building other packages
which use "rayon" feature of "%{crate}" crate.

%files       -n %{name}+rayon-devel
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
* Wed Mar 03 2021 Fabio Valentini <decathorpe@gmail.com> - 0.1.22-1
- Update to version 0.1.22.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.20-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Josh Stone <jistone@redhat.com> - 0.1.20-1
- Update to 0.1.20

* Wed Apr 29 2020 Josh Stone <jistone@redhat.com> - 0.1.19-1
- Update to 0.1.19

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 16 2019 Josh Stone <jistone@redhat.com> - 0.1.18-1
- Update to 0.1.18

* Sun Sep 01 19:36:11 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.16-1
- Update to 0.1.16

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 23 10:56:37 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.15-2
- Regenerate

* Fri Mar 15 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.15-1
- Initial package
