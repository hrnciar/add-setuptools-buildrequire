# Generated by rust2rpm 16
%bcond_without check
%global debug_package %{nil}

%global crate mailparse

Name:           rust-%{crate}
Version:        0.13.2
Release:        1%{?dist}
Summary:        Simple parser for MIME e-mail messages

# Upstream license specification: 0BSD
License:        0BSD
URL:            https://crates.io/crates/mailparse
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Simple parser for MIME e-mail messages.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE
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
* Sun Feb 07 2021 Fabio Valentini <decathorpe@gmail.com> - 0.13.2-1
- Update to version 0.13.2.
- Fixes RHBZ#1925672

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Nov 29 2020 Fabio Valentini <decathorpe@gmail.com> - 0.13.1-1
- Update to version 0.13.1.
- Fixes RHBZ#1902443

* Mon Oct 19 2020 Fabio Valentini <decathorpe@gmail.com> - 0.13.0-1
- Update to version 0.13.0.

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Josh Stone <jistone@redhat.com> - 0.12.2-1
- Update to 0.12.2

* Mon May 18 07:39:42 CEST 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.12.1-1
- Update to 0.12.1

* Mon Feb 24 07:01:35 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.12.0-1
- Update to 0.12.0

* Sun Feb 23 15:23:00 EET 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.11.0-1
- Update to 0.11.0

* Mon Feb 10 2020 Josh Stone <jistone@redhat.com> - 0.10.4-1
- Update to 0.10.4

* Mon Feb 03 15:52:06 EET 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.10.3-1
- Update to 0.10.3

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 07 2020 Josh Stone <jistone@redhat.com> - 0.10.2-1
- Update to 0.10.2

* Tue Dec 10 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.10.1-1
- Update to 0.10.1

* Wed Nov 27 15:40:25 CET 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.9.2-1
- Initial package
