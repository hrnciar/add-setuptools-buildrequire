# Generated by rust2rpm 16
%bcond_without check
%global debug_package %{nil}

%global crate cmake

Name:           rust-%{crate}
Version:        0.1.45
Release:        2%{?dist}
Summary:        Build dependency for running cmake to build a native library

# Upstream license specification: MIT/Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/cmake
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging
BuildRequires:  /usr/bin/cmake

%global _description %{expand:
Build dependency for running `cmake` to build a native library.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       /usr/bin/cmake

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
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.45-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Nov 19 2020 Fabio Valentini <decathorpe@gmail.com> - 0.1.45-1
- Update to version 0.1.45.
- Fixes RHBZ#1898177

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.44-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon May 18 2020 Josh Stone <jistone@redhat.com> - 0.1.44-1
- Update to 0.1.44

* Thu May 14 2020 Josh Stone <jistone@redhat.com> - 0.1.43-1
- Update to 0.1.43

* Mon Feb 17 19:44:33 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.1.42-3
- Update requires

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.42-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 20 2019 Josh Stone <jistone@redhat.com> - 0.1.42-1
- Update to 0.1.42

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.40-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun 01 2019 Josh Stone <jistone@redhat.com> - 0.1.40-1
- Update to 0.1.40

* Thu May 09 2019 Josh Stone <jistone@redhat.com> - 0.1.39-1
- Update to 0.1.39

* Mon Apr 08 2019 Josh Stone <jistone@redhat.com> - 0.1.38-1
- Update to 0.1.38

* Thu Mar 28 2019 Josh Stone <jistone@redhat.com> - 0.1.37-1
- Update to 0.1.37

* Tue Mar 26 2019 Josh Stone <jistone@redhat.com> - 0.1.36-1
- Update to 0.1.36
- Adapt to new packaging

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.35-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Oct 01 2018 Josh Stone <jistone@redhat.com> - 0.1.35-1
- Update to 0.1.35

* Mon Sep 17 2018 Josh Stone <jistone@redhat.com> - 0.1.34-1
- Update to 0.1.34

* Thu Aug 30 2018 Josh Stone <jistone@redhat.com> - 0.1.33-1
- Update to 0.1.33

* Sat Aug 04 2018 Josh Stone <jistone@redhat.com> - 0.1.32-1
- Update to 0.1.32

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.31-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri May 04 2018 Josh Stone <jistone@redhat.com> - 0.1.31-1
- Update to 0.1.31

* Fri Apr 13 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.30-1
- Update to 0.1.30

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.29-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 08 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.29-2
- Rebuild for rust-packaging v5

* Sat Dec 09 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.29-1
- Update to 0.1.29

* Sat Nov 18 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.28-1
- Update to 0.1.28

* Thu Jun 15 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.24-1
- Update to 0.1.24

* Wed Jun 14 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.21-2
- Port to use rust-packaging

* Tue Feb 28 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.21-1
- Update to 0.1.21

* Sun Feb 26 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.20-1
- Initial package
