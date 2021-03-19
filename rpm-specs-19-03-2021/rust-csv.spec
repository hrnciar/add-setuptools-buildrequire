# Generated by rust2rpm 16
%bcond_without check
%global debug_package %{nil}

%global crate csv

Name:           rust-%{crate}
Version:        1.1.5
Release:        2%{?dist}
Summary:        Fast CSV parsing with support for serde

# Upstream license specification: Unlicense/MIT
License:        Unlicense or MIT
URL:            https://crates.io/crates/csv
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Fast CSV parsing with support for serde.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license COPYING LICENSE-MIT UNLICENSE
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
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Nov 27 2020 Fabio Valentini <decathorpe@gmail.com> - 1.1.5-1
- Update to version 1.1.5.
- Fixes RHBZ#1902298

* Wed Nov 04 2020 Fabio Valentini <decathorpe@gmail.com> - 1.1.4-1
- Update to version 1.1.4.
- Fixes RHBZ#1894191

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 23 2020 Josh Stone <jistone@redhat.com> - 1.1.3-1
- Update to 1.1.3

* Tue Jan 07 2020 Josh Stone <jistone@redhat.com> - 1.1.2-1
- Update to 1.1.2

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jul 06 11:35:10 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.1.1-1
- Update to 1.1.1

* Thu Jun 27 07:25:28 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.1.0-1
- Update to 1.1.0

* Thu Jun 20 16:47:21 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.7-4
- Regenerate

* Sun Jun 09 15:12:40 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.7-3
- Regenerate

* Sun May 12 08:37:15 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.7-2
- Update serde_bytes to 0.11

* Mon Apr 15 2019 Josh Stone <jistone@redhat.com> - 1.0.7-1
- Update to 1.0.7

* Fri Apr 05 2019 Josh Stone <jistone@redhat.com> - 1.0.6-1
- Update to 1.0.6

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 08 2019 Josh Stone <jistone@redhat.com> - 1.0.5-1
- Update to 1.0.5

* Sat Nov 10 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.2-3
- Fix summary

* Fri Nov 09 2018 Robert-André Mauchin <zebob.m@gmail.com> - 1.0.2-2
- Adapt to new packaging

* Tue Sep 25 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.2-1
- Update to 1.0.2

* Tue Sep 25 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.1-2
- Exclude unneeded files in other way

* Thu Aug 30 2018 Josh Stone <jistone@redhat.com> - 1.0.1-1
- Update to 1.0.1

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 14 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.0-1
- Initial package
