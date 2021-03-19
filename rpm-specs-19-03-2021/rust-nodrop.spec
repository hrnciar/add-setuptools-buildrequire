# Generated by rust2rpm 16
%bcond_without check
%global debug_package %{nil}

%global crate nodrop

Name:           rust-%{crate}
Version:        0.1.14
Release:        6%{?dist}
Summary:        Wrapper type to inhibit drop (destructor)

# Upstream license specification: MIT/Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/nodrop
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Wrapper type to inhibit drop (destructor).
***Deprecated: Use ManuallyDrop or
MaybeUninit instead!***.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-MIT LICENSE-APACHE
%doc README.rst
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

%package     -n %{name}+use_needs_drop-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+use_needs_drop-devel %{_description}

This package contains library source intended for building other packages
which use "use_needs_drop" feature of "%{crate}" crate.

%files       -n %{name}+use_needs_drop-devel
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
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.14-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Dec 12 2020 Fabio Valentini <decathorpe@gmail.com> - 0.1.14-5
- Remove features with missing dependencies (nodrop-union).

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.14-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 19 2019 Josh Stone <jistone@redhat.com> - 0.1.14-1
- Update to 0.1.14

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 19 23:30:49 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.13-3
- Regenerate

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Nov 13 2018 Josh Stone <jistone@redhat.com> - 0.1.13-1
- Update to 0.1.13

* Sat Oct 27 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.12-6
- Adapt to new packaging

* Sun Oct 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.12-5
- Run tests in infrastructure

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 08 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.12-2
- Rebuild for rust-packaging v5

* Sun Dec 03 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.12-1
- Initial package
