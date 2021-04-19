# Generated by rust2rpm 15
%bcond_without check
%global debug_package %{nil}

%global crate num-complex

Name:           rust-%{crate}
Version:        0.3.1
Release:        2%{?dist}
Summary:        Complex numbers implementation for Rust

# Upstream license specification: MIT OR Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/num-complex
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Complex numbers implementation for Rust.}

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

%package     -n %{name}+libm-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+libm-devel %{_description}

This package contains library source intended for building other packages
which use "libm" feature of "%{crate}" crate.

%files       -n %{name}+libm-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+rand-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+rand-devel %{_description}

This package contains library source intended for building other packages
which use "rand" feature of "%{crate}" crate.

%files       -n %{name}+rand-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+serde-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde-devel %{_description}

This package contains library source intended for building other packages
which use "serde" feature of "%{crate}" crate.

%files       -n %{name}+serde-devel
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
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Nov 04 2020 Fabio Valentini <decathorpe@gmail.com> - 0.3.1-1
- Update to version 0.3.1.
- Fixes RHBZ#1893056

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 26 2020 Josh Stone <jistone@redhat.com> - 0.3.0-1
- Update to 0.3.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 15 2020 Josh Stone <jistone@redhat.com> - 0.2.4-1
- Update to 0.2.4

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun 22 12:53:38 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.3-2
- Regenerate

* Tue Jun 11 2019 Josh Stone <jistone@redhat.com> - 0.2.3-1
- Update to 0.2.3

* Mon Jun 10 2019 Josh Stone <jistone@redhat.com> - 0.2.2-1
- Update to 0.2.2

* Sun Jun 09 15:11:03 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.1-7
- Regenerate

* Sat Mar 16 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.1-6
- Do not pull optional dependencies

* Sat Feb 09 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.1-5
- Run tests in infrastructure

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Nov 10 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.1-3
- Fix description

* Fri Nov 09 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.2.1-2
- Adapt to new packaging

* Tue Oct 09 2018 Josh Stone <jistone@redhat.com> - 0.2.1-1
- Update to 0.2.1

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Josh Stone <jistone@redhat.com> - 0.2.0-1
- Update to 0.2.0

* Thu Mar 08 2018 Josh Stone <jistone@redhat.com> - 0.1.43-1
- Update to 0.1.43

* Thu Feb 08 2018 Josh Stone <jistone@redhat.com> - 0.1.42-2
- Add doc files

* Thu Feb 08 2018 Josh Stone <jistone@redhat.com> - 0.1.42-1
- Update to 0.1.42

* Mon Jan 08 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.41-2
- Rebuild for rust-packaging v5

* Sat Dec 02 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.41-1
- Update to 0.1.41

* Tue Nov 07 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.40-1
- Update to 0.1.40

* Thu Jun 15 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.38-1
- Update to 0.1.38

* Wed Jun 14 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.36-2
- Port to use rust-packaging

* Thu Mar 02 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.36-1
- Initial package