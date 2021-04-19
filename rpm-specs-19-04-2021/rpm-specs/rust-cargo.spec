# Generated by rust2rpm 16
# Tests are too much environment dependent
%bcond_with check
%global debug_package %{nil}

# We ship it as part of rust.src
%global __cargo_is_bin() false

%global crate cargo

Name:           rust-%{crate}
Version:        0.51.0
Release:        1%{?dist}
Summary:        Package manager for Rust

# Upstream license specification: MIT OR Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/cargo
Source:         %{crates_source}
# Initial patched metadata
# * Bump crates-io from 0.31.1 to 0.32
# * No windows/macos
# * No rustc-workspace-hack
# * No vendored OpenSSL
Patch0:         cargo-fix-metadata.diff
# * include function that was added in crates-io 0.31.1 after 0.32.0
# https://github.com/rust-lang/cargo/issues/8914
Patch1:         01-fix-for-crates-io-0.32.patch

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging
%if %{with check}
BuildRequires:  git-core
%endif

%global _description %{expand:
Package manager for Rust.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-APACHE LICENSE-MIT
%doc CHANGELOG.md CONTRIBUTING.md README.md src/doc
%{cargo_registry}/%{crate}-%{version_no_tilde}/
%exclude %{cargo_registry}/%{crate}-%{version_no_tilde}/{.github,azure-pipelines.yml,ci,etc,publish.py}

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+deny-warnings-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+deny-warnings-devel %{_description}

This package contains library source intended for building other packages
which use "deny-warnings" feature of "%{crate}" crate.

%files       -n %{name}+deny-warnings-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+openssl-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+openssl-devel %{_description}

This package contains library source intended for building other packages
which use "openssl" feature of "%{crate}" crate.

%files       -n %{name}+openssl-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+pretty-env-logger-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+pretty-env-logger-devel %{_description}

This package contains library source intended for building other packages
which use "pretty-env-logger" feature of "%{crate}" crate.

%files       -n %{name}+pretty-env-logger-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+pretty_env_logger-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+pretty_env_logger-devel %{_description}

This package contains library source intended for building other packages
which use "pretty_env_logger" feature of "%{crate}" crate.

%files       -n %{name}+pretty_env_logger-devel
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
* Mon Mar 29 2021 Fabio Valentini <decathorpe@gmail.com> - 0.51.0-1
- Update to version 0.51.0.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.49.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec 28 13:27:54 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.49.0-2
- Rebuild

* Sun Nov 29 2020 Fabio Valentini <decathorpe@gmail.com> - 0.49.0-1
- Update to version 0.49.0.
- Fixes RHBZ#1858031

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.45.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 19 2020 Josh Stone <jistone@redhat.com> - 0.45.1-1
- Update to 0.45.1

* Fri Jun 05 2020 Josh Stone <jistone@redhat.com> - 0.45.0-1
- Update to 0.45.0

* Thu May 21 2020 Josh Stone <jistone@redhat.com> - 0.44.1-2
- Bump to im-rc 15

* Thu May 07 2020 Josh Stone <jistone@redhat.com> - 0.44.1-1
- Update to 0.44.1

* Thu Apr 23 2020 Josh Stone <jistone@redhat.com> - 0.44.0-1
- Update to 0.44.0

* Thu Mar 19 12:38:02 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.43.1-2
- Update git2 dependencies

* Tue Mar 17 2020 Josh Stone <jistone@redhat.com> - 0.43.1-1
- Update to 0.43.1

* Thu Mar 12 2020 Josh Stone <jistone@redhat.com> - 0.43.0-1
- Update to 0.43.0

* Thu Mar 05 2020 Josh Stone <jistone@redhat.com> - 0.42.0-3
- Bump to rustfix 0.5

* Tue Mar 03 2020 Josh Stone <jistone@redhat.com> - 0.42.0-2
- Bump git2 dependencies

* Mon Mar 02 2020 Josh Stone <jistone@redhat.com> - 0.42.0-1
- Update to 0.42.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.40.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Dec 07 2019 Josh Stone <jistone@redhat.com> - 0.40.0-1
- Update to 0.40.0

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.36.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 07 2019 Josh Stone <jistone@redhat.com> - 0.36.0-1
- Update to 0.36.0

* Wed Apr 03 2019 Josh Stone <jistone@redhat.com> - 0.32.0-4
- Bump git2 and git2-curl dependencies

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.32.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Dec 15 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.32.0-2
- Bump crossbeam-utils to 0.6

* Thu Dec 06 2018 Josh Stone <jistone@redhat.com> - 0.32.0-1
- Update to 0.32.0

* Sat Nov 17 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.31.0-1
- Update to 0.31.0

* Tue Nov 13 2018 Josh Stone <jistone@redhat.com> - 0.30.0-2
- Adapt to new packaging

* Mon Sep 10 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.29.0-2
- Switch to crossbeam-utils

* Sat Aug 04 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.29.0-1
- Update to 0.29.0

* Sun Jul 22 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.28.0-1
- Initial package
