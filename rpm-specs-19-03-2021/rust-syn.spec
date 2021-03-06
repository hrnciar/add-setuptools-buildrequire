# Generated by rust2rpm 16
# syn-test-suite is not packaged
%bcond_with check
%global debug_package %{nil}

%global crate syn

Name:           rust-%{crate}
Version:        1.0.60
Release:        1%{?dist}
Summary:        Parser for Rust source code

# Upstream license specification: MIT OR Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/syn
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Parser for Rust source code.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-MIT LICENSE-APACHE
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

%package     -n %{name}+clone-impls-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+clone-impls-devel %{_description}

This package contains library source intended for building other packages
which use "clone-impls" feature of "%{crate}" crate.

%files       -n %{name}+clone-impls-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+derive-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+derive-devel %{_description}

This package contains library source intended for building other packages
which use "derive" feature of "%{crate}" crate.

%files       -n %{name}+derive-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+extra-traits-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+extra-traits-devel %{_description}

This package contains library source intended for building other packages
which use "extra-traits" feature of "%{crate}" crate.

%files       -n %{name}+extra-traits-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+fold-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+fold-devel %{_description}

This package contains library source intended for building other packages
which use "fold" feature of "%{crate}" crate.

%files       -n %{name}+fold-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+full-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+full-devel %{_description}

This package contains library source intended for building other packages
which use "full" feature of "%{crate}" crate.

%files       -n %{name}+full-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+parsing-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+parsing-devel %{_description}

This package contains library source intended for building other packages
which use "parsing" feature of "%{crate}" crate.

%files       -n %{name}+parsing-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+printing-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+printing-devel %{_description}

This package contains library source intended for building other packages
which use "printing" feature of "%{crate}" crate.

%files       -n %{name}+printing-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+proc-macro-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+proc-macro-devel %{_description}

This package contains library source intended for building other packages
which use "proc-macro" feature of "%{crate}" crate.

%files       -n %{name}+proc-macro-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+quote-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+quote-devel %{_description}

This package contains library source intended for building other packages
which use "quote" feature of "%{crate}" crate.

%files       -n %{name}+quote-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+test-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+test-devel %{_description}

This package contains library source intended for building other packages
which use "test" feature of "%{crate}" crate.

%files       -n %{name}+test-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+visit-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+visit-devel %{_description}

This package contains library source intended for building other packages
which use "visit" feature of "%{crate}" crate.

%files       -n %{name}+visit-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+visit-mut-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+visit-mut-devel %{_description}

This package contains library source intended for building other packages
which use "visit-mut" feature of "%{crate}" crate.

%files       -n %{name}+visit-mut-devel
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
* Sat Feb 27 2021 Fabio Valentini <decathorpe@gmail.com> - 1.0.60-1
- Update to version 1.0.60.
- Fixes RHBZ#1919515

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.58-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 11 2021 Fabio Valentini <decathorpe@gmail.com> - 1.0.58-1
- Update to version 1.0.58.
- Fixes RHBZ#1913082

* Sat Jan 02 11:59:43 CET 2021 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.0.57-1
- Update to 1.0.57 (Fixes: RHBZ#1911944)

* Sun Dec 27 09:12:10 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.0.56-1
- Update to 1.0.56

* Mon Dec 07 2020 Fabio Valentini <decathorpe@gmail.com> - 1.0.54-1
- Update to version 1.0.54.
- Fixes RHBZ#1905236

* Mon Nov 30 2020 Fabio Valentini <decathorpe@gmail.com> - 1.0.53-1
- Update to version 1.0.53.
- Fixes RHBZ#1902587

* Fri Nov 27 2020 Fabio Valentini <decathorpe@gmail.com> - 1.0.52-1
- Update to version 1.0.52.
- Fixes RHBZ#1900286

* Wed Nov  4 2020 Fabio Valentini <decathorpe@gmail.com> - 1.0.48-1
- Update to version 1.0.48.
- Fixes RHBZ#1889099

* Sun Oct 11 2020 Fabio Valentini <decathorpe@gmail.com> - 1.0.44-1
- Update to version 1.0.44.

* Thu Oct 01 2020 Fabio Valentini <decathorpe@gmail.com> - 1.0.42-1
- Update to version 1.0.42.

* Wed Sep 23 2020 Fabio Valentini <decathorpe@gmail.com> - 1.0.41-1
- Update to version 1.0.41.

* Wed Sep 09 2020 Josh Stone <jistone@redhat.com> - 1.0.40-1
- Update to 1.0.40

* Sat Aug 22 2020 Josh Stone <jistone@redhat.com> - 1.0.39-1
- Update to 1.0.39

* Wed Aug 05 2020 Josh Stone <jistone@redhat.com> - 1.0.38-1
- Update to 1.0.38

* Tue Aug 04 2020 Josh Stone <jistone@redhat.com> - 1.0.37-1
- Update to 1.0.37

* Wed Jul 29 2020 Josh Stone <jistone@redhat.com> - 1.0.36-1
- Update to 1.0.36

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.35-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 20 2020 Josh Stone <jistone@redhat.com> - 1.0.35-1
- Update to 1.0.35

* Tue Jul 14 2020 Josh Stone <jistone@redhat.com> - 1.0.34-1
- Update to 1.0.34

* Fri Jul 10 2020 Josh Stone <jistone@redhat.com> - 1.0.33-1
- Update to 1.0.33

* Sun Jun 21 09:00:38 CEST 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.0.32-1
- Update to 1.0.32

* Thu Jun 11 2020 Josh Stone <jistone@redhat.com> - 1.0.31-1
- Update to 1.0.31

* Mon Jun 01 14:03:32 CEST 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.0.30-1
- Update to 1.0.30

* Sun May 31 10:18:29 CEST 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.0.29-1
- Update to 1.0.29

* Tue May 26 2020 Josh Stone <jistone@redhat.com> - 1.0.27-1
- Update to 1.0.27

* Tue May 26 2020 Josh Stone <jistone@redhat.com> - 1.0.26-1
- Update to 1.0.26

* Mon May 25 05:52:38 CEST 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.0.24-1
- Update to 1.0.24

* Thu May 21 2020 Josh Stone <jistone@redhat.com> - 1.0.23-1
- Update to 1.0.23

* Sat May 16 19:35:22 CEST 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.0.22-1
- Update to 1.0.22

* Wed May 13 2020 Josh Stone <jistone@redhat.com> - 1.0.21-1
- Update to 1.0.21

* Tue May 12 2020 Josh Stone <jistone@redhat.com> - 1.0.20-1
- Update to 1.0.20

* Wed May 06 2020 Josh Stone <jistone@redhat.com> - 1.0.19-1
- Update to 1.0.19

* Fri Apr 24 06:17:20 CEST 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.0.18-1
- Update to 1.0.18

* Sat Mar 21 07:25:37 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.0.17-1
- Update to 1.0.17

* Mon Feb 24 2020 Josh Stone <jistone@redhat.com> - 1.0.16-1
- Update to 1.0.16

* Fri Feb 21 2020 Josh Stone <jistone@redhat.com> - 1.0.15-1
- Update to 1.0.15

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 27 2020 Josh Stone <jistone@redhat.com> - 1.0.14-1
- Update to 1.0.14

* Wed Jan 15 2020 Josh Stone <jistone@redhat.com> - 1.0.13-1
- Update to 1.0.13

* Sun Dec 01 10:21:44 CET 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.11-1
- Update to 1.0.11

* Tue Nov 19 2019 Josh Stone <jistone@redhat.com> - 1.0.8-1
- Update to 1.0.8

* Sat Aug 31 19:38:13 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.5-1
- Update to 1.0.5

* Sun Aug 18 15:59:32 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.3-1
- Update to 1.0.3

* Sun Aug 18 10:52:14 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.15.44-1
- Update to 0.15.44

* Sun Jul 28 18:13:11 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.15.42-1
- Update to 0.15.42

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.39-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 30 12:07:39 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.15.39-1
- Update to 0.15.39

* Mon Jun 24 21:34:53 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.15.38-1
- Update to 0.15.38

* Sat Jun 22 11:18:33 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.15.37-1
- Update to 0.15.37

* Thu Jun 20 11:47:49 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.15.36-2
- Regenerate

* Fri Jun 14 2019 Josh Stone <jistone@redhat.com> - 0.15.36-1
- Update to 0.15.36

* Sun Jun 09 11:27:25 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.15.35-1
- Update to 0.15.35

* Thu May 09 08:26:56 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.15.34-1
- Update to 0.15.34

* Tue Apr 30 08:41:55 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.15.33-1
- Update to 0.15.33

* Wed Apr 17 2019 Josh Stone <jistone@redhat.com> - 0.15.32-1
- Update to 0.15.32

* Mon Apr 15 2019 Josh Stone <jistone@redhat.com> - 0.15.31-1
- Update to 0.15.31

* Tue Apr 02 2019 Josh Stone <jistone@redhat.com> - 0.15.30-1
- Update to 0.15.30

* Wed Mar 13 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.15.29-1
- Update to 0.15.29

* Fri Mar 08 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.15.28-1
- Update to 0.15.28

* Fri Mar 01 2019 Josh Stone <jistone@redhat.com> - 0.15.27-1
- Update to 0.15.27

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.26-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 17 2019 Josh Stone <jistone@redhat.com> - 0.15.26-1
- Update to 0.15.26

* Mon Jan 14 2019 Josh Stone <jistone@redhat.com> - 0.15.25-1
- Update to 0.15.25

* Tue Jan 08 2019 Josh Stone <jistone@redhat.com> - 0.15.24-1
- Update to 0.15.24

* Mon Nov 26 2018 Josh Stone <jistone@redhat.com> - 0.15.22-1
- Update to 0.15.22

* Fri Nov 16 2018 Josh Stone <jistone@redhat.com> - 0.15.21-1
- Update to 0.15.21

* Tue Nov 13 2018 Josh Stone <jistone@redhat.com> - 0.15.20-1
- Update to 0.15.20

* Fri Nov 02 2018 Josh Stone <jistone@redhat.com> - 0.15.18-1
- Update to 0.15.18

* Mon Oct 29 2018 Josh Stone <jistone@redhat.com> - 0.15.15-1
- Update to 0.15.15

* Fri Oct 26 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.15.14-2
- Adapt to new packaging

* Fri Oct 26 2018 Josh Stone <jistone@redhat.com> - 0.15.14-1
- Update to 0.15.14

* Mon Oct 22 2018 Josh Stone <jistone@redhat.com> - 0.15.13-1
- Update to 0.15.13

* Mon Oct 15 2018 Josh Stone <jistone@redhat.com> - 0.15.11-1
- Update to 0.15.11

* Mon Oct 08 2018 Josh Stone <jistone@redhat.com> - 0.15.9-1
- Update to 0.15.9

* Wed Oct 03 2018 Josh Stone <jistone@redhat.com> - 0.15.8-1
- Update to 0.15.8

* Mon Oct 01 2018 Josh Stone <jistone@redhat.com> - 0.15.7-1
- Update to 0.15.7

* Fri Sep 28 2018 Josh Stone <jistone@redhat.com> - 0.15.6-1
- Update to 0.15.6

* Wed Sep 12 2018 Josh Stone <jistone@redhat.com> - 0.15.4-1
- Update to 0.15.4

* Tue Sep 11 2018 Josh Stone <jistone@redhat.com> - 0.15.3-1
- Update to 0.15.3

* Sat Sep 08 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.15.1-1
- Update to 0.15.1

* Mon Aug 13 2018 Josh Stone <jistone@redhat.com> - 0.14.8-1
- Update to 0.14.8

* Sat Aug 04 2018 Josh Stone <jistone@redhat.com> - 0.14.7-1
- Update to 0.14.7

* Thu Aug 02 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.14.6-1
- Update to 0.14.6

* Mon Jul 23 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.14.5-1
- Update to 0.14.5

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jul 01 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.14.4-1
- Update to 0.14.4

* Thu Jun 21 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.14.2-1
- Update to 0.14.2

* Sun May 20 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.13.11-1
- Update to 0.13.11

* Mon May 14 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.13.10-1
- Update to 0.13.10

* Sat May 12 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.13.9-1
- Update to 0.13.9

* Sat May 12 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.13.8-1
- Update to 0.13.8

* Sun May 06 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.13.7-1
- Update to 0.13.7

* Sat May 05 2018 Josh Stone <jistone@redhat.com> - 0.13.5-1
- Update to 0.13.5

* Wed May 02 2018 Josh Stone <jistone@redhat.com> - 0.13.4-1
- Update to 0.13.4

* Tue Apr 17 2018 Josh Stone <jistone@redhat.com> - 0.13.1-1
- Update to 0.13.1

* Wed Mar 28 2018 Josh Stone <jistone@redhat.com> - 0.12.15-1
- Update to 0.12.15

* Fri Mar 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.12.14-1
- Update to 0.12.14

* Thu Mar 08 2018 Josh Stone <jistone@redhat.com> - 0.12.13-1
- Update to 0.12.13

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 08 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.11.11-2
- Rebuild for rust-packaging v5

* Thu Jun 15 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.11.11-1
- Update to 0.11.11

* Wed Jun 14 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.11.9-2
- Port to use rust-packaging

* Tue Mar 07 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.11.9-1
- Update to 0.11.9

* Tue Feb 28 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.11.8-1
- Update to 0.11.8

* Mon Feb 27 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.11.7-1
- Update to 0.11.7

* Fri Feb 24 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.11.6-1
- Update to 0.11.6

* Sat Feb 18 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.11.4-1
- Initial package
