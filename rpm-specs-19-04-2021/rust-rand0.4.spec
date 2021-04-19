# Generated by rust2rpm 13
%bcond_with check
%global debug_package %{nil}

%global crate rand

Name:           rust-%{crate}0.4
Version:        0.4.6
Release:        9%{?dist}
Summary:        Random number generators and other randomness functionality

# Upstream license specification: MIT/Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/rand
Source:         %{crates_source}
# Initial patched metadata
# * Exclude unneeded files
# * Remove fuchsia, sgx, and windows dependencies
Patch0:         rand-fix-metadata.diff

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Random number generators and other randomness functionality.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-MIT LICENSE-APACHE
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

%package     -n %{name}+alloc-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+alloc-devel %{_description}

This package contains library source intended for building other packages
which use "alloc" feature of "%{crate}" crate.

%files       -n %{name}+alloc-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+i128_support-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+i128_support-devel %{_description}

This package contains library source intended for building other packages
which use "i128_support" feature of "%{crate}" crate.

%files       -n %{name}+i128_support-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+libc-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+libc-devel %{_description}

This package contains library source intended for building other packages
which use "libc" feature of "%{crate}" crate.

%files       -n %{name}+libc-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+nightly-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+nightly-devel %{_description}

This package contains library source intended for building other packages
which use "nightly" feature of "%{crate}" crate.

%files       -n %{name}+nightly-devel
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
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Feb 18 03:52:39 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.4.6-7
- Disable tests

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun 22 09:50:01 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.6-4
- Regenerate

* Sat Mar 09 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.6-3
- Adapt to new packaging

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 29 2019 Josh Stone <jistone@redhat.com> - 0.4.6-1
- Update to 0.4.6

* Wed Jan 09 2019 Josh Stone <jistone@redhat.com> - 0.4.5-1
- Update to 0.4.5

* Tue Jan 08 2019 Josh Stone <jistone@redhat.com> - 0.4.4-1
- Update to 0.4.4

* Wed Oct 31 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.3-2
- Adapt to new packaging

* Fri Sep 07 2018 Josh Stone <jistone@redhat.com> - 0.4.3-1
- Update to 0.4.3

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jul 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.2-5
- Trivial fixes in spec

* Tue Feb 20 2018 Josh Stone <jistone@redhat.com> - 0.4.2-4
- Exclude python2 utilities

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 08 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.2-2
- Rebuild for rust-packaging v5

* Sat Jan 06 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.2-1
- Update to 0.4.2

* Sun Dec 31 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.1-1
- Update to 0.4.1

* Tue Nov 07 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.18-1
- Update to 0.3.18

* Fri Oct 27 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.17-1
- Update to 0.3.17

* Wed Jun 14 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.15-3
- Port to use rust-packaging

* Fri Feb 24 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.15-2
- Use rich dependencies

* Sun Feb 12 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.15-1
- Initial package