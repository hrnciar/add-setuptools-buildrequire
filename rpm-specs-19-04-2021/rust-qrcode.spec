# Generated by rust2rpm 13
%bcond_without check
%global debug_package %{nil}

# Binary is useless
%global __cargo_is_bin() false

%global crate qrcode

Name:           rust-%{crate}
Version:        0.12.0
Release:        3%{?dist}
Summary:        QR code encoder in Rust

# Upstream license specification: MIT OR Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/qrcode
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
QR code encoder in Rust.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-MIT.txt LICENSE-APACHE.txt
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

%package     -n %{name}+bench-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+bench-devel %{_description}

This package contains library source intended for building other packages
which use "bench" feature of "%{crate}" crate.

%files       -n %{name}+bench-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+image-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+image-devel %{_description}

This package contains library source intended for building other packages
which use "image" feature of "%{crate}" crate.

%files       -n %{name}+image-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+svg-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+svg-devel %{_description}

This package contains library source intended for building other packages
which use "svg" feature of "%{crate}" crate.

%files       -n %{name}+svg-devel
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
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Mar 19 2020 Josh Stone <jistone@redhat.com> - 0.12.0-1
- Update to 0.12.0

* Mon Feb 17 11:09:42 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.11.2-3
- Update image to 0.23

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 07 2020 Josh Stone <jistone@redhat.com> - 0.11.2-1
- Update to 0.11.2

* Mon Dec 30 11:10:50 CET 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.11.1-1
- Update to 0.11.1

* Sun Sep 01 20:47:12 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.11.0-1
- Update to 0.11.0

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jul 07 15:04:04 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.10.1-1
- Update to 0.10.1

* Sat Jun 22 14:53:24 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.10.0-2
- Regenerate

* Sat Apr 20 13:09:05 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.10.0-1
- Update to 0.10.0

* Fri Mar 15 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.9.0-1
- Initial package
