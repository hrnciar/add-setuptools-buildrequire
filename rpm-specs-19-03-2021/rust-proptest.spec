# Generated by rust2rpm 16
%bcond_without check
%global debug_package %{nil}

%global crate proptest

Name:           rust-%{crate}
Version:        0.10.1
Release:        3%{?dist}
Summary:        Hypothesis-like property-based testing and shrinking

# Upstream license specification: MIT/Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/proptest
Source:         %{crates_source}
# Initial patched metadata
# * TODO: Send PR, Exclude unneeded files
Patch0:         proptest-fix-metadata.diff

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Hypothesis-like property-based testing and shrinking.}

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

%package     -n %{name}+atomic64bit-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+atomic64bit-devel %{_description}

This package contains library source intended for building other packages
which use "atomic64bit" feature of "%{crate}" crate.

%files       -n %{name}+atomic64bit-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+bit-set-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+bit-set-devel %{_description}

This package contains library source intended for building other packages
which use "bit-set" feature of "%{crate}" crate.

%files       -n %{name}+bit-set-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+break-dead-code-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+break-dead-code-devel %{_description}

This package contains library source intended for building other packages
which use "break-dead-code" feature of "%{crate}" crate.

%files       -n %{name}+break-dead-code-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+default-code-coverage-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-code-coverage-devel %{_description}

This package contains library source intended for building other packages
which use "default-code-coverage" feature of "%{crate}" crate.

%files       -n %{name}+default-code-coverage-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+fork-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+fork-devel %{_description}

This package contains library source intended for building other packages
which use "fork" feature of "%{crate}" crate.

%files       -n %{name}+fork-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+lazy_static-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+lazy_static-devel %{_description}

This package contains library source intended for building other packages
which use "lazy_static" feature of "%{crate}" crate.

%files       -n %{name}+lazy_static-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+quick-error-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+quick-error-devel %{_description}

This package contains library source intended for building other packages
which use "quick-error" feature of "%{crate}" crate.

%files       -n %{name}+quick-error-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+regex-syntax-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+regex-syntax-devel %{_description}

This package contains library source intended for building other packages
which use "regex-syntax" feature of "%{crate}" crate.

%files       -n %{name}+regex-syntax-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+rusty-fork-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+rusty-fork-devel %{_description}

This package contains library source intended for building other packages
which use "rusty-fork" feature of "%{crate}" crate.

%files       -n %{name}+rusty-fork-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+std-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+std-devel %{_description}

This package contains library source intended for building other packages
which use "std" feature of "%{crate}" crate.

%files       -n %{name}+std-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+tempfile-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+tempfile-devel %{_description}

This package contains library source intended for building other packages
which use "tempfile" feature of "%{crate}" crate.

%files       -n %{name}+tempfile-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+timeout-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+timeout-devel %{_description}

This package contains library source intended for building other packages
which use "timeout" feature of "%{crate}" crate.

%files       -n %{name}+timeout-devel
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

# building tests takes too much memory for 32-bit arches
%if %{with check} && %{?__isa_bits}%{?!__isa_bits:0} >= 64
%check
%cargo_test
%endif

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Dec 11 2020 Fabio Valentini <decathorpe@gmail.com> - 0.10.1-2
- Remove hardware-rng feature (missing dependency: x86).

* Fri Sep 25 2020 Fabio Valentini <decathorpe@gmail.com> - 0.10.1-1
- Update to version 0.10.1.

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Apr 15 2020 Josh Stone <jistone@redhat.com> - 0.9.6-1
- Update to 0.9.6

* Tue Feb 11 2020 Josh Stone <jistone@redhat.com> - 0.9.5-3
- Disable testing on 32-bit arches.

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Josh Stone <jistone@redhat.com> - 0.9.5-1
- Update to 0.9.5

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 27 17:17:22 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.9.4-2
- Regenerate

* Sun Jun 09 13:43:04 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.9.4-1
- Update to 0.9.4

* Mon Apr 29 07:08:16 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.9.3-1
- Update to 0.9.3

* Sat Apr 27 12:08:50 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.9.2-1
- Update to 0.9.2

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Dec 15 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.8.7-4
- Bump rand to 0.6

* Sun Dec 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.8.7-3
- Rebuild

* Sun Dec 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.8.7-2
- Run tests in infrastructure

* Sun Dec 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.8.7-1
- Initial package
