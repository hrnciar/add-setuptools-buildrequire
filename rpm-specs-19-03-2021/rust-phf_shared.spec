# Generated by rust2rpm 13
%bcond_without check
%global debug_package %{nil}

%global crate phf_shared

Name:           rust-%{crate}
Version:        0.8.0
Release:        3%{?dist}
Summary:        Support code shared by PHF libraries

# Upstream license specification: MIT
# https://github.com/sfackler/rust-phf/pull/118
License:        MIT
URL:            https://crates.io/crates/phf_shared
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Support code shared by PHF libraries.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+std-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+std-devel %{_description}

This package contains library source intended for building other packages
which use "std" feature of "%{crate}" crate.

%files       -n %{name}+std-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+unicase-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+unicase-devel %{_description}

This package contains library source intended for building other packages
which use "unicase" feature of "%{crate}" crate.

%files       -n %{name}+unicase-devel
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
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Feb 15 13:48:25 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.8.0-1
- Update to 0.8.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.24-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.24-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun 22 09:36:19 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.7.24-6
- Regenerate

* Thu Mar 14 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.7.24-5
- Update siphasher to 0.3

* Thu Mar 14 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.7.24-4
- Do not pull optional dependencies

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.24-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jan 26 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.7.24-2
- Add unicase feature back

* Tue Jan 08 2019 Josh Stone <jistone@redhat.com> - 0.7.24-1
- Update to 0.7.24

* Fri Nov 09 2018 Josh Stone <jistone@redhat.com> - 0.7.23-2
- Adapt to new packaging

* Sat Sep 08 2018 Josh Stone <jistone@redhat.com> - 0.7.23-1
- Update to 0.7.23

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed May 02 2018 Josh Stone <jistone@redhat.com> - 0.7.22-1
- Update to 0.7.22

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 24 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.7.21-1
- Initial package
