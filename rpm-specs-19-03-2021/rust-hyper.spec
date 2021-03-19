# Generated by rust2rpm 16
# * examples and UI tests are not included in the crate
# * tokio-test in Fedora is too old
%bcond_with check
%global debug_package %{nil}

%global crate hyper

Name:           rust-%{crate}
Version:        0.14.4
Release:        1%{?dist}
Summary:        Fast and correct HTTP library

# Upstream license specification: MIT
License:        MIT
URL:            https://crates.io/crates/hyper
Source:         %{crates_source}
# Initial patched metadata
# * remove nightly-only / internal features
Patch0:         hyper-fix-metadata.diff

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Fast and correct HTTP library.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+client-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+client-devel %{_description}

This package contains library source intended for building other packages
which use "client" feature of "%{crate}" crate.

%files       -n %{name}+client-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+ffi-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+ffi-devel %{_description}

This package contains library source intended for building other packages
which use "ffi" feature of "%{crate}" crate.

%files       -n %{name}+ffi-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+full-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+full-devel %{_description}

This package contains library source intended for building other packages
which use "full" feature of "%{crate}" crate.

%files       -n %{name}+full-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+h2-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+h2-devel %{_description}

This package contains library source intended for building other packages
which use "h2" feature of "%{crate}" crate.

%files       -n %{name}+h2-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+http1-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+http1-devel %{_description}

This package contains library source intended for building other packages
which use "http1" feature of "%{crate}" crate.

%files       -n %{name}+http1-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+http2-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+http2-devel %{_description}

This package contains library source intended for building other packages
which use "http2" feature of "%{crate}" crate.

%files       -n %{name}+http2-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+libc-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+libc-devel %{_description}

This package contains library source intended for building other packages
which use "libc" feature of "%{crate}" crate.

%files       -n %{name}+libc-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+runtime-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+runtime-devel %{_description}

This package contains library source intended for building other packages
which use "runtime" feature of "%{crate}" crate.

%files       -n %{name}+runtime-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+server-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+server-devel %{_description}

This package contains library source intended for building other packages
which use "server" feature of "%{crate}" crate.

%files       -n %{name}+server-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+socket2-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+socket2-devel %{_description}

This package contains library source intended for building other packages
which use "socket2" feature of "%{crate}" crate.

%files       -n %{name}+socket2-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+stream-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+stream-devel %{_description}

This package contains library source intended for building other packages
which use "stream" feature of "%{crate}" crate.

%files       -n %{name}+stream-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+tcp-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+tcp-devel %{_description}

This package contains library source intended for building other packages
which use "tcp" feature of "%{crate}" crate.

%files       -n %{name}+tcp-devel
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
* Sat Mar 06 2021 Fabio Valentini <decathorpe@gmail.com> - 0.14.4-1
- Update to version 0.14.4.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Nov 04 2020 Fabio Valentini <decathorpe@gmail.com> - 0.13.9-1
- Update to version 0.13.9.
- Fixes RHBZ#1893917

* Sun Sep 20 2020 Fabio Valentini <decathorpe@gmail.com> - 0.13.8-1
- Update to version 0.13.8.

* Tue Aug 25 2020 Josh Stone <jistone@redhat.com> - 0.13.7-1
- Update to 0.13.7

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Fabio Valentini <decathorpe@gmail.com> - 0.13.6-2
- Enable running unit tests.

* Sat May 30 2020 Josh Stone <jistone@redhat.com> - 0.13.6-1
- Update to 0.13.6

* Fri Apr 17 2020 Josh Stone <jistone@redhat.com> - 0.13.5-1
- Update to 0.13.5

* Sat Mar 21 07:25:29 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.13.4-1
- Update to 0.13.4

* Wed Mar 04 2020 Josh Stone <jistone@redhat.com> - 0.13.3-1
- Update to 0.13.3

* Tue Feb 11 10:57:12 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.13.2-1
- Update to 0.13.2

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.35-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Nov 23 2019 Josh Stone <jistone@redhat.com> - 0.12.35-1
- Update to 0.12.35

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.32-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jul 13 11:22:33 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.12.32-1
- Update to 0.12.32

* Thu Jun 27 08:14:30 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.12.31-4
- Regenerate

* Fri Jun 21 21:49:45 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.12.30-3
- Update want to 0.2

* Fri Jun 21 18:36:23 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.12.30-2
- Regenerate

* Fri Jun 14 2019 Josh Stone <jistone@redhat.com> - 0.12.30-1
- Update to 0.12.30

* Sun Jun 02 13:53:51 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.12.29-1
- Update to 0.12.29

* Tue Apr 30 08:30:54 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.12.28-1
- Update to 0.12.28

* Sat Apr 13 2019 Josh Stone <jistone@redhat.com> - 0.12.27-1
- Update to 0.12.27

* Wed Apr 10 10:43:57 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.12.26-2
- Drop internal features

* Wed Apr 10 07:37:59 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.12.26-1
- Update to 0.12.26

* Fri Mar 01 2019 Josh Stone <jistone@redhat.com> - 0.12.25-1
- Update to 0.12.25

* Mon Feb 11 2019 Josh Stone <jistone@redhat.com> - 0.12.24-1
- Update to 0.12.24

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 24 2019 Josh Stone <jistone@redhat.com> - 0.12.23-1
- Update to 0.12.23

* Wed Jan 23 2019 Josh Stone <jistone@redhat.com> - 0.12.22-1
- Update to 0.12.22

* Tue Jan 15 2019 Josh Stone <jistone@redhat.com> - 0.12.21-1
- Update to 0.12.21

* Tue Jan 08 2019 Josh Stone <jistone@redhat.com> - 0.12.20-1
- Update to 0.12.20

* Wed Dec 12 2018 Josh Stone <jistone@redhat.com> - 0.12.18-1
- Update to 0.12.18

* Thu Dec 06 2018 Josh Stone <jistone@redhat.com> - 0.12.17-1
- Update to 0.12.17

* Mon Nov 26 2018 Josh Stone <jistone@redhat.com> - 0.12.16-1
- Update to 0.12.16

* Sun Nov 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.12.14-1
- Update to 0.12.14

* Mon Oct 22 2018 Josh Stone <jistone@redhat.com> - 0.12.12-1
- Update to 0.12.12

* Fri Sep 28 2018 Josh Stone <jistone@redhat.com> - 0.12.11-1
- Update to 0.12.11

* Mon Sep 17 2018 Josh Stone <jistone@redhat.com> - 0.12.10-1
- Update to 0.12.10

* Sat Sep 08 2018 Josh Stone <jistone@redhat.com> - 0.12.9-1
- Update to 0.12.9

* Sat Aug 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.12.8-1
- Update to 0.12.8

* Sat Jul 28 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.12.7-2
- Rebuild to trigger tests

* Tue Jul 24 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.12.7-1
- Update to 0.12.7

* Fri Jul 13 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.12.6-1
- Update to 0.12.6

* Wed Jul 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.12.5-1
- Update to 0.12.5

* Sun May 06 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.11.26-1
- Update to 0.11.26

* Thu Apr 05 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.11.25-1
- Update to 0.11.25

* Fri Mar 23 2018 Josh Stone <jistone@redhat.com> - 0.11.24-1
- Update to 0.11.24

* Thu Mar 22 2018 Josh Stone <jistone@redhat.com> - 0.11.23-1
- Update to 0.11.23

* Fri Mar 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.11.22-1
- Initial package
