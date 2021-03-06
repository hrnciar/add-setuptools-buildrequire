# Generated by rust2rpm 16
%bcond_without check
%global debug_package %{nil}

%global crate regex

Name:           rust-%{crate}
Version:        1.4.3
Release:        2%{?dist}
Summary:        Implementation of regular expressions for Rust

# Upstream license specification: MIT OR Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/regex
Source:         %{crates_source}
# Initial patched metadata
# - Bump quickcheck to 0.9 https://github.com/rust-lang/regex/pull/616
# - Bump rand to 0.7
Patch0:         regex-fix-metadata.diff

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Implementation of regular expressions for Rust. This implementation uses finite
automata and guarantees linear time matching on all inputs.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-MIT LICENSE-APACHE
%doc README.md CHANGELOG.md HACKING.md PERFORMANCE.md UNICODE.md
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+aho-corasick-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+aho-corasick-devel %{_description}

This package contains library source intended for building other packages
which use "aho-corasick" feature of "%{crate}" crate.

%files       -n %{name}+aho-corasick-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+memchr-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+memchr-devel %{_description}

This package contains library source intended for building other packages
which use "memchr" feature of "%{crate}" crate.

%files       -n %{name}+memchr-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+pattern-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+pattern-devel %{_description}

This package contains library source intended for building other packages
which use "pattern" feature of "%{crate}" crate.

%files       -n %{name}+pattern-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+perf-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+perf-devel %{_description}

This package contains library source intended for building other packages
which use "perf" feature of "%{crate}" crate.

%files       -n %{name}+perf-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+perf-cache-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+perf-cache-devel %{_description}

This package contains library source intended for building other packages
which use "perf-cache" feature of "%{crate}" crate.

%files       -n %{name}+perf-cache-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+perf-dfa-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+perf-dfa-devel %{_description}

This package contains library source intended for building other packages
which use "perf-dfa" feature of "%{crate}" crate.

%files       -n %{name}+perf-dfa-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+perf-inline-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+perf-inline-devel %{_description}

This package contains library source intended for building other packages
which use "perf-inline" feature of "%{crate}" crate.

%files       -n %{name}+perf-inline-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+perf-literal-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+perf-literal-devel %{_description}

This package contains library source intended for building other packages
which use "perf-literal" feature of "%{crate}" crate.

%files       -n %{name}+perf-literal-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+std-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+std-devel %{_description}

This package contains library source intended for building other packages
which use "std" feature of "%{crate}" crate.

%files       -n %{name}+std-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+thread_local-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+thread_local-devel %{_description}

This package contains library source intended for building other packages
which use "thread_local" feature of "%{crate}" crate.

%files       -n %{name}+thread_local-devel
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

%package     -n %{name}+unstable-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+unstable-devel %{_description}

This package contains library source intended for building other packages
which use "unstable" feature of "%{crate}" crate.

%files       -n %{name}+unstable-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+use_std-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+use_std-devel %{_description}

This package contains library source intended for building other packages
which use "use_std" feature of "%{crate}" crate.

%files       -n %{name}+use_std-devel
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
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Jan 09 2021 Fabio Valentini <decathorpe@gmail.com> - 1.4.3-1
- Update to version 1.4.3.
- Fixes RHBZ#1914360

* Thu Nov 05 2020 Fabio Valentini <decathorpe@gmail.com> - 1.4.2-1
- Update to version 1.4.2.
- Fixes RHBZ#1887233

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri May 29 16:55:48 CEST 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.3.9-1
- Update to 1.3.9

* Fri Apr 17 2020 Josh Stone <jistone@redhat.com> - 1.3.7-1
- Update to 1.3.7

* Thu Mar 26 08:35:59 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.3.6-1
- Update to 1.3.6

* Fri Mar 13 2020 Josh Stone <jistone@redhat.com> - 1.3.5-1
- Update to 1.3.5

* Fri Jan 31 2020 Josh Stone <jistone@redhat.com> - 1.3.4-1
- Update to 1.3.4

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 24 2020 Josh Stone <jistone@redhat.com> - 1.3.3-1
- Update to 1.3.3

* Wed Jan 15 2020 Josh Stone <jistone@redhat.com> - 1.3.2-1
- Update to 1.3.2

* Fri Sep 13 21:47:27 CEST 2019 Robert-Andr?? Mauchin <zebob.m@gmail.com> - 1.3.1-1
- Update to 1.3.1
- Bump quickcheck to 0.9
- Bump rand to 0.7

* Sun Aug 04 06:54:20 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.2.1-1
- Update to 1.2.1

* Sun Jul 28 21:14:41 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.2.0-1
- Update to 1.2.0

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jul 07 15:01:03 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.1.9-1
- Update to 1.1.9

* Sat Jul 06 11:19:59 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.1.8-1
- Update to 1.1.8

* Thu Jun 20 09:20:14 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.1.7-2
- Regenerate

* Sun Jun 09 15:15:29 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.1.7-1
- Update to 1.1.7

* Sun Jun 09 10:24:45 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.1.6-2
- Regenerate

* Tue Apr 16 2019 Josh Stone <jistone@redhat.com> - 1.1.6-1
- Update to 1.1.6

* Wed Apr 03 2019 Josh Stone <jistone@redhat.com> - 1.1.5-1
- Update to 1.1.5

* Thu Feb 28 2019 Josh Stone <jistone@redhat.com> - 1.1.2-1
- Update to 1.1.2

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Dec 03 2018 Josh Stone <jistone@redhat.com> - 1.1.0-1
- Update to 1.1.0

* Sat Nov 10 2018 Josh Stone <jistone@redhat.com> - 1.0.6-1
- Update to 1.0.6

* Sat Oct 27 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.5-3
- Adapt to new packaging

* Sun Oct 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.5-2
- Exclude more unneeded files

* Fri Sep 07 2018 Josh Stone <jistone@redhat.com> - 1.0.5-1
- Update to 1.0.5

* Thu Aug 30 2018 Josh Stone <jistone@redhat.com> - 1.0.4-1
- Update to 1.0.4

* Sat Jul 28 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.2-5
- Rebuild to run tests

* Mon Jul 23 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.2-4
- Rebuild to trigger tests

* Fri Jul 20 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.2-3
- Rebuild to trigger tests

* Fri Jul 20 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.2-2
- Rebuild

* Thu Jul 19 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.2-1
- Update to 1.0.2

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 20 2018 Josh Stone <jistone@redhat.com> - 1.0.1-1
- Update to 1.0.1

* Tue Jun 12 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.0-1
- Update to 1.0.0

* Tue May 01 2018 Josh Stone <jistone@redhat.com> - 0.2.11-1
- Update to 0.2.11

* Fri Mar 16 2018 Josh Stone <jistone@redhat.com> - 0.2.10-1
- Update to 0.2.10

* Wed Mar 14 2018 Josh Stone <jistone@redhat.com> - 0.2.9-1
- Update to 0.2.9

* Fri Feb 09 2018 Josh Stone <jistone@redhat.com> - 0.2.6-1
- Update to 0.2.6

* Mon Jan 08 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.5-2
- Rebuild for rust-packaging v5

* Sun Dec 31 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.5-1
- Update to 0.2.5

* Sat Dec 02 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.3-3
- Bump quickcheck to 0.5

* Thu Nov 30 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.3-2
- Bump lazy_static to 1

* Thu Nov 30 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.3-1
- Update to 0.2.3

* Wed Nov 08 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.2-2
- Bump memchr to 2

* Wed Jun 14 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.2-1
- Update to 0.2.2

* Wed Jun 14 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.1-2
- Port to use rust-packaging

* Sat Feb 25 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.1-1
- Initial package
