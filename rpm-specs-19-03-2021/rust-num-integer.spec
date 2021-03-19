# Generated by rust2rpm 15
%bcond_without check
%global debug_package %{nil}

%global crate num-integer

Name:           rust-%{crate}
Version:        0.1.44
Release:        2%{?dist}
Summary:        Integer traits and functions

# Upstream license specification: MIT OR Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/num-integer
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Integer traits and functions.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-MIT LICENSE-APACHE
%doc README.md RELEASES.md
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+i128-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+i128-devel %{_description}

This package contains library source intended for building other packages
which use "i128" feature of "%{crate}" crate.

%files       -n %{name}+i128-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+std-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+std-devel %{_description}

This package contains library source intended for building other packages
which use "std" feature of "%{crate}" crate.

%files       -n %{name}+std-devel
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
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.44-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Nov 04 2020 Fabio Valentini <decathorpe@gmail.com> - 0.1.44-1
- Update to version 0.1.44.
- Fixes RHBZ#1893028

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.43-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 12 2020 Josh Stone <jistone@redhat.com> - 0.1.43-1
- Update to 0.1.43

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.42-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 15 2020 Josh Stone <jistone@redhat.com> - 0.1.42-1
- Update to 0.1.42

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.41-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun 22 09:37:07 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.41-3
- Regenerate

* Sun Jun 09 15:22:35 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.41-2
- Regenerate

* Wed May 22 2019 Josh Stone <jistone@redhat.com> - 0.1.41-1
- Update to 0.1.41

* Mon May 20 2019 Josh Stone <jistone@redhat.com> - 0.1.40-1
- Update to 0.1.40

* Sun Mar 10 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.39-6
- Do not pull optional dependencies

* Sat Feb 09 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.39-5
- Run tests in infrastructure

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.39-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 31 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.39-3
- Adapt to new packaging

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.39-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 21 2018 Josh Stone <jistone@redhat.com> - 0.1.39-1
- Update to 0.1.39

* Fri May 11 2018 Josh Stone <jistone@redhat.com> - 0.1.38-1
- Update to 0.1.38

* Thu May 10 2018 Josh Stone <jistone@redhat.com> - 0.1.37-1
- Update to 0.1.37

* Wed Feb 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.36-1
- Update to 0.1.36

* Mon Jan 08 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.35-2
- Rebuild for rust-packaging v5

* Mon Nov 06 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.35-1
- Update to 0.1.35

* Wed Jun 14 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.33-2
- Port to use rust-packaging

* Thu Mar 02 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.33-1
- Initial package