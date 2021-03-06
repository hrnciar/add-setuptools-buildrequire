# Generated by rust2rpm 16
%bcond_without check
%global debug_package %{nil}

%global crate regex-syntax

Name:           rust-%{crate}
Version:        0.6.22
Release:        2%{?dist}
Summary:        Regular expression parser

# Upstream license specification: MIT/Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/regex-syntax
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Regular expression parser.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-MIT LICENSE-APACHE
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+unicode-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+unicode-devel %{_description}

This package contains library source intended for building other packages
which use "unicode" feature of "%{crate}" crate.

%files       -n %{name}+unicode-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+unicode-age-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+unicode-age-devel %{_description}

This package contains library source intended for building other packages
which use "unicode-age" feature of "%{crate}" crate.

%files       -n %{name}+unicode-age-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+unicode-bool-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+unicode-bool-devel %{_description}

This package contains library source intended for building other packages
which use "unicode-bool" feature of "%{crate}" crate.

%files       -n %{name}+unicode-bool-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+unicode-case-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+unicode-case-devel %{_description}

This package contains library source intended for building other packages
which use "unicode-case" feature of "%{crate}" crate.

%files       -n %{name}+unicode-case-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+unicode-gencat-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+unicode-gencat-devel %{_description}

This package contains library source intended for building other packages
which use "unicode-gencat" feature of "%{crate}" crate.

%files       -n %{name}+unicode-gencat-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+unicode-perl-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+unicode-perl-devel %{_description}

This package contains library source intended for building other packages
which use "unicode-perl" feature of "%{crate}" crate.

%files       -n %{name}+unicode-perl-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+unicode-script-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+unicode-script-devel %{_description}

This package contains library source intended for building other packages
which use "unicode-script" feature of "%{crate}" crate.

%files       -n %{name}+unicode-script-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+unicode-segment-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+unicode-segment-devel %{_description}

This package contains library source intended for building other packages
which use "unicode-segment" feature of "%{crate}" crate.

%files       -n %{name}+unicode-segment-devel
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
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Jan 09 2021 Fabio Valentini <decathorpe@gmail.com> - 0.6.22-1
- Update to version 0.6.22.
- Fixes RHBZ#1914361

* Thu Nov 05 2020 Fabio Valentini <decathorpe@gmail.com> - 0.6.21-1
- Update to version 0.6.21.
- Fixes RHBZ#1887234

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri May 29 16:56:02 CEST 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.6.18-1
- Update to 0.6.18

* Fri Mar 13 2020 Josh Stone <jistone@redhat.com> - 0.6.17-1
- Update to 0.6.17

* Tue Mar 03 2020 Josh Stone <jistone@redhat.com> - 0.6.16-1
- Update to 0.6.16

* Mon Mar 02 09:08:42 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.6.15-1
- Update to 0.6.15

* Fri Jan 31 2020 Josh Stone <jistone@redhat.com> - 0.6.14-1
- Update to 0.6.14

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 15 2020 Josh Stone <jistone@redhat.com> - 0.6.13-1
- Update to 0.6.13

* Sun Sep 08 09:34:53 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6.12-1
- Update to 0.6.12

* Sun Aug 04 06:55:50 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6.11-1
- Update to 0.6.11

* Sun Jul 28 21:15:48 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6.10-1
- Update to 0.6.10

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jul 07 15:01:15 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6.8-1
- Update to 0.6.8

* Thu Jun 20 11:07:48 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6.7-2
- Regenerate

* Sun Jun 09 15:17:37 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6.7-1
- Update to 0.6.7

* Sun Jun 09 11:20:40 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6.6-2
- Regenerate

* Tue Apr 02 2019 Josh Stone <jistone@redhat.com> - 0.6.6-1
- Update to 0.6.6

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 28 2019 Josh Stone <jistone@redhat.com> - 0.6.5-1
- Update to 0.6.5

* Mon Dec 03 2018 Josh Stone <jistone@redhat.com> - 0.6.4-1
- Update to 0.6.4

* Sat Nov 10 2018 Josh Stone <jistone@redhat.com> - 0.6.3-1
- Update to 0.6.3

* Sat Oct 27 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6.2-3
- Adapt to new packaging

* Sun Oct 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6.2-2
- Run tests in infrastructure

* Thu Jul 19 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6.2-1
- Update to 0.6.2

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 12 2018 Josh Stone <jistone@redhat.com> - 0.6.1-1
- Update to 0.6.1

* Tue Jun 12 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6.0-1
- Update to 0.6.0

* Tue May 01 2018 Josh Stone <jistone@redhat.com> - 0.5.6-1
- Update to 0.5.6

* Mon Apr 16 2018 Josh Stone <jistone@redhat.com> - 0.5.5-1
- Update to 0.5.5

* Wed Mar 14 2018 Josh Stone <jistone@redhat.com> - 0.5.3-1
- Update to 0.5.3

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 08 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.2-2
- Rebuild for rust-packaging v5

* Sun Dec 31 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.2-1
- Update to 0.4.2

* Sat Dec 02 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.1-3
- Bump quickcheck to 0.5

* Wed Nov 29 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.1-2
- Enable tests

* Wed Jun 14 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.1-1
- Update to 0.4.1

* Wed Jun 14 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.0-3
- Port to use rust-packaging

* Fri Feb 24 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.0-2
- Use rich dependencies

* Sat Feb 18 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.0-1
- Initial package
