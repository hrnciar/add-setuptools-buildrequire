# Generated by rust2rpm 17
%bcond_without check
%global debug_package %{nil}

%global crate syn-mid

Name:           rust-%{crate}
Version:        0.5.3
Release:        2%{?dist}
Summary:        Providing the features between "full" and "derive" of syn

# Upstream license specification: Apache-2.0 OR MIT
License:        ASL 2.0 or MIT
URL:            https://crates.io/crates/syn-mid
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Providing the features between "full" and "derive" of syn.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-APACHE LICENSE-MIT
%doc CHANGELOG.md README.md
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+clone-impls-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+clone-impls-devel %{_description}

This package contains library source intended for building other packages
which use "clone-impls" feature of "%{crate}" crate.

%files       -n %{name}+clone-impls-devel
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
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan 05 20:29:25 CET 2021 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.5.3-1
- Update to 0.5.3 (Fixes: RHBZ#1912935)

* Tue Dec 29 18:12:27 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.5.2-1
- Update to 0.5.2 (Fixes: RHBZ#1911482)

* Mon Nov 09 2020 Fabio Valentini <decathorpe@gmail.com> - 0.5.1-1
- Update to version 0.5.1.
- Fixes RHBZ#1888330

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Feb 10 2020 Josh Stone <jistone@redhat.com> - 0.5.0-1
- Update to 0.5.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Dec 06 21:18:19 CET 2019 Robert-Andr?? Mauchin <zebob.m@gmail.com> - 0.4.0-1
- Initial package
