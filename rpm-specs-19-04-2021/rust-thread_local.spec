# Generated by rust2rpm 16
%bcond_without check
%global debug_package %{nil}

%global crate thread_local

Name:           rust-%{crate}
Version:        1.1.3
Release:        1%{?dist}
Summary:        Per-object thread-local storage

# Upstream license specification: Apache-2.0/MIT
License:        ASL 2.0 or MIT
URL:            https://crates.io/crates/thread_local
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Per-object thread-local storage.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-APACHE LICENSE-MIT
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

%package     -n %{name}+criterion-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+criterion-devel %{_description}

This package contains library source intended for building other packages
which use "criterion" feature of "%{crate}" crate.

%files       -n %{name}+criterion-devel
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
* Sun Feb 07 2021 Fabio Valentini <decathorpe@gmail.com> - 1.1.3-1
- Update to version 1.1.3.
- Fixes RHBZ#1919457

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Jan 09 2021 Fabio Valentini <decathorpe@gmail.com> - 1.1.0-1
- Update to version 1.1.0.
- Fixes RHBZ#1913996

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 24 2020 Josh Stone <jistone@redhat.com> - 1.0.1-1
- Update to 1.0.1

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 20 11:12:52 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.6-6
- Regenerate

* Sun Jun 09 11:02:42 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.6-5
- Regenerate

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Oct 27 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.6-3
- Adapt to new packaging

* Sun Oct 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.6-2
- Run tests in infrastructure

* Thu Aug 30 2018 Josh Stone <jistone@redhat.com> - 0.3.6-1
- Update to 0.3.6

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 08 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.5-2
- Rebuild for rust-packaging v5

* Mon Dec 11 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.5-1
- Update to 0.3.5

* Thu Nov 30 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.4-2
- Bump lazy_static to 1

* Sat Jul 01 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.4-1
- Update to 0.3.4

* Wed Jun 14 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.3-4
- Bump unreachable dependency to 1.0

* Wed Jun 14 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.3-3
- Port to use rust-packaging

* Fri Feb 24 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.3-2
- Update to 0.3.3

* Fri Feb 24 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.2-2
- Use rich dependencies

* Sat Feb 18 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.2-1
- Initial package
