# Generated by rust2rpm 16
%bcond_without check
%global debug_package %{nil}

%global crate filetime

Name:           rust-%{crate}
Version:        0.2.14
Release:        1%{?dist}
Summary:        Platform-agnostic accessors of timestamps in File metadata

# Upstream license specification: MIT/Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/filetime
Source:         %{crates_source}
# Initial patched metadata
# * No redox/windows
Patch0:         filetime-fix-metadata.diff

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Platform-agnostic accessors of timestamps in File metadata.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-MIT LICENSE-APACHE
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
* Thu Mar 04 2021 Fabio Valentini <decathorpe@gmail.com> - 0.2.14-1
- Update to version 0.2.14.
- Fixes RHBZ#1918884

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Nov 07 2020 Fabio Valentini <decathorpe@gmail.com> - 0.2.13-1
- Update to version 0.2.13.
- Fixes RHBZ#1895055

* Tue Aug 04 2020 Josh Stone <jistone@redhat.com> - 0.2.12-1
- Update to 0.2.12

* Thu Jul 30 2020 Josh Stone <jistone@redhat.com> - 0.2.11-1
- Update to 0.2.11

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu May 07 2020 Josh Stone <jistone@redhat.com> - 0.2.10-1
- Update to 0.2.10

* Wed Apr 01 2020 Josh Stone <jistone@redhat.com> - 0.2.9-1
- Update to 0.2.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 19 2019 Josh Stone <jistone@redhat.com> - 0.2.8-1
- Update to 0.2.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun 22 13:10:52 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.6-2
- Regenerate

* Wed May 15 21:15:32 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.6-1
- Update to 0.2.6

* Tue Apr 23 19:10:21 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.5-1
- Update to 0.2.5

* Thu Mar 14 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.4-3
- Adapt to new packaging

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Nov 18 2018 Josh Stone <jistone@redhat.com> - 0.2.4-1
- Update to 0.2.4

* Tue Nov 13 2018 Josh Stone <jistone@redhat.com> - 0.2.3-1
- Update to 0.2.3

* Sat Nov 10 2018 Josh Stone <jistone@redhat.com> - 0.2.2-1
- Update to 0.2.2

* Tue Oct 30 2018 Josh Stone <jistone@redhat.com> - 0.2.1-3
- Adapt to new packaging

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri May 04 2018 Josh Stone <jistone@redhat.com> - 0.2.1-1
- Update to 0.2.1

* Wed Apr 25 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.0-1
- Update to 0.2.0

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.15-1
- Update to 0.1.15

* Mon Jan 08 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.14-2
- Rebuild for rust-packaging v5

* Tue Nov 07 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.14-1
- Update to 0.1.14

* Wed Jun 14 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.10-2
- Port to use rust-packaging

* Sun Feb 26 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.10-1
- Initial package
