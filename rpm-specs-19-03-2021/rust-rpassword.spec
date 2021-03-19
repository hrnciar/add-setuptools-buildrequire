# Generated by rust2rpm 16
%bcond_without check
%global debug_package %{nil}

%global crate rpassword

Name:           rust-%{crate}
Version:        5.0.1
Release:        2%{?dist}
Summary:        Read passwords in console applications

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            https://crates.io/crates/rpassword
Source:         %{crates_source}
# Initial patched metadata
# * Drop windows dependencies
Patch0:         rpassword-fix-metadata.diff

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Read passwords in console applications.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-APACHE
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
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 20 2021 Fabio Valentini <decathorpe@gmail.com> - 5.0.1-1
- Update to version 5.0.1.
- Fixes RHBZ#1918059

* Tue Dec 15 2020 Fabio Valentini <decathorpe@gmail.com> - 5.0.0-1
- Update to version 5.0.0.

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 27 2020 Josh Stone <jistone@redhat.com> - 4.0.5-1
- Update to 4.0.5

* Thu Dec 05 22:03:54 CET 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 4.0.3-1
- Update to 4.0.3

* Thu Dec 05 14:23:37 CET 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 4.0.2-1
- Update to 4.0.2

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun 22 16:18:08 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.0.2-2
- Regenerate

* Sat Apr 20 10:06:18 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.0.2-1
- Update to 3.0.2

* Fri Mar 29 14:47:57 CET 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.0.1-1
- Update to 3.0.1

* Sat Mar 23 20:10:55 CET 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.0.0-1
- Update to 3.0.0

* Wed Mar 13 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.1.0-1
- Initial package
