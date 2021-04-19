# Generated by rust2rpm 16
%bcond_without check
%global debug_package %{nil}

%global crate varlink_parser

Name:           rust-%{crate}
Version:        4.1.0
Release:        1%{?dist}
Summary:        Crate for parsing varlink interface definition files

# Upstream license specification: MIT/Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/varlink_parser
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Crate for parsing varlink interface definition files.}

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
* Mon Mar 29 2021 Fabio Valentini <decathorpe@gmail.com> - 4.1.0-1
- Update to version 4.1.0.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Sep 15 2020 Fabio Valentini <decathorpe@gmail.com> - 4.0.4-1
- Update to version 4.0.4.

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 28 15:03:07 CET 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 4.0.3-1
- Update to 4.0.3

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 16 2019 Harald Hoyer <harald@redhat.com> - 4.0.2-1
- Update to 4.0.2

* Sat Feb 16 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 4.0.1-1
- Update to 4.0.1

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Dec 06 2018 Josh Stone <jistone@redhat.com> - 2.2.2-1
- Update to 2.2.2

* Fri Nov 30 2018 Josh Stone <jistone@redhat.com> - 2.2.1-1
- Update to 2.2.1

* Thu Nov 29 2018 Josh Stone <jistone@redhat.com> - 2.2.0-1
- Update to 2.2.0

* Mon Nov 26 2018 Josh Stone <jistone@redhat.com> - 2.1.1-1
- Update to 2.1.1

* Sat Nov 17 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.1.0-2
- Adapt to new packaging

* Tue Oct 09 2018 Josh Stone <jistone@redhat.com> - 2.1.0-1
- Update to 2.1.0

* Mon Oct 08 2018 Josh Stone <jistone@redhat.com> - 2.0.0-1
- Update to 2.0.0

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 22 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.1.0-1
- Initial package
