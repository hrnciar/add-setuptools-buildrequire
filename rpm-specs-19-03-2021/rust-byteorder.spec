# Generated by rust2rpm 13
%bcond_without check
%global debug_package %{nil}

%global crate byteorder

Name:           rust-%{crate}
Version:        1.3.4
Release:        3%{?dist}
Summary:        Library for reading/writing numbers in big-endian and little-endian

# Upstream license specification: Unlicense OR MIT
License:        Unlicense or MIT
URL:            https://crates.io/crates/byteorder
Source:         %{crates_source}
# Initial patched metadata
# - Bump quickcheck to 0.9 https://github.com/BurntSushi/byteorder/pull/154
# - Bump rand to 0.7
Patch0:         byteorder-fix-metadata.diff

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Library for reading/writing numbers in big-endian and little-endian.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license COPYING UNLICENSE LICENSE-MIT
%doc README.md CHANGELOG.md
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
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Feb 10 2020 Josh Stone <jistone@redhat.com> - 1.3.4-1
- Update to 1.3.4

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Sep 13 17:57:06 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.3.2-4
- Bump quickcheck to 0.9

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 19 23:11:29 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.3.2-2
- Regenerate

* Sun Jun 09 17:01:45 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.3.2-1
- Update to 1.3.2

* Sun Jun 09 12:28:17 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.3.1-4
- Fix skip_build

* Sat Jun 08 23:51:46 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.3.1-3
- Regenerate

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 23 2019 Josh Stone <jistone@redhat.com> - 1.3.1-1
- Update to 1.3.1

* Sat Jan 19 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.3.0-1
- Update to 1.3.0

* Fri Oct 26 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.2.7-1
- Update to 1.2.7

* Fri Oct 26 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.2.6-2
- Adapt to new packaging

* Thu Aug 30 2018 Josh Stone <jistone@redhat.com> - 1.2.6-1
- Update to 1.2.6

* Tue Jul 31 2018 Josh Stone <jistone@redhat.com> - 1.2.4-1
- Update to 1.2.4

* Sat Jul 28 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.2.3-3
- Rebuild to trigger tests

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon May 14 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.2.3-1
- Update to 1.2.3

* Mon Apr 02 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.2.2-1
- Update to 1.2.2

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 08 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.2.1-3
- Rebuild for rust-packaging v5

* Sun Dec 31 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.2.1-2
- Bump rand to 0.4

* Thu Nov 30 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.2.1-1
- Update to 1.2.1

* Fri Nov 10 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.1.0-1
- Update to 1.1.0

* Fri Jun 16 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.0-1
- Initial package