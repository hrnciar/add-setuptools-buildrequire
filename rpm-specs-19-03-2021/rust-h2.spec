# Generated by rust2rpm 16
# * rustls stuff is not packaged
%bcond_with check
%global debug_package %{nil}

%global crate h2

Name:           rust-%{crate}
Version:        0.3.1
Release:        1%{?dist}
Summary:        HTTP/2.0 client and server

# Upstream license specification: MIT
License:        MIT
URL:            https://crates.io/crates/h2
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
HTTP/2.0 client and server.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE
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

%package     -n %{name}+stream-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+stream-devel %{_description}

This package contains library source intended for building other packages
which use "stream" feature of "%{crate}" crate.

%files       -n %{name}+stream-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+unstable-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+unstable-devel %{_description}

This package contains library source intended for building other packages
which use "unstable" feature of "%{crate}" crate.

%files       -n %{name}+unstable-devel
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
* Sat Mar 06 2021 Fabio Valentini <decathorpe@gmail.com> - 0.3.1-1
- Update to version 0.3.1.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Nov 12 2020 Fabio Valentini <decathorpe@gmail.com> - 0.2.7-1
- Update to version 0.2.7.
- Fixes RHBZ#1891035

* Tue Aug 25 2020 Josh Stone <jistone@redhat.com> - 0.2.6-1
- Update to 0.2.6

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu May 14 19:53:31 CEST 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.2.5-1
- Update to 0.2.5

* Wed Mar 25 20:09:18 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.2.3-1
- Update to 0.2.3

* Wed Mar 04 2020 Josh Stone <jistone@redhat.com> - 0.2.2-1
- Update to 0.2.2

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Dec 14 16:52:35 CET 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.1-1
- Update to 0.2.1

* Sat Nov 23 2019 Josh Stone <jistone@redhat.com> - 0.1.26-1
- Update to 0.1.26

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.25-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 30 12:10:18 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.25-1
- Update to 0.1.25

* Tue Jun 18 08:24:55 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.24-1
- Update to 0.1.24

* Wed Jun 05 17:48:13 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.23-1
- Update to 0.1.23

* Mon Jun 03 2019 Josh Stone <jistone@redhat.com> - 0.1.22-1
- Update to 0.1.22

* Fri May 31 16:01:11 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.21-1
- Update to 0.1.21

* Wed Apr 10 07:39:15 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.18-1
- Update to 0.1.18

* Wed Mar 13 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.17-1
- Update to 0.1.17

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 24 2019 Josh Stone <jistone@redhat.com> - 0.1.16-1
- Update to 0.1.16

* Mon Jan 14 2019 Josh Stone <jistone@redhat.com> - 0.1.15-1
- Update to 0.1.15

* Thu Dec 06 2018 Josh Stone <jistone@redhat.com> - 0.1.14-1
- Update to 0.1.14

* Mon Nov 12 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.13-2
- Adapt to new packaging

* Mon Oct 22 2018 Josh Stone <jistone@redhat.com> - 0.1.13-1
- Update to 0.1.13

* Thu Aug 09 2018 Josh Stone <jistone@redhat.com> - 0.1.12-1
- Update to 0.1.12

* Sat Aug 04 2018 Josh Stone <jistone@redhat.com> - 0.1.11-1
- Update to 0.1.11

* Wed Jul 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.10-1
- Initial package