# Generated by rust2rpm 17
# * Missing dev-dependency pprof
%bcond_with check

%global crate handlebars

Name:           rust-%{crate}
Version:        3.5.3
Release:        1%{?dist}
Summary:        Handlebars templating implemented in Rust

# Upstream license specification: MIT
License:        MIT
URL:            https://crates.io/crates/handlebars
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Handlebars templating implemented in Rust.}

%description %{_description}

%if ! %{__cargo_skip_build}
%package     -n %{crate}
Summary:        %{summary}
# ASL 2.0 or Boost
# MIT
# MIT or ASL 2.0
# Unlicense or MIT
License:        MIT and (ASL 2.0 or Boost)

%description -n %{crate} %{_description}

%files       -n %{crate}
%license LICENSE
%doc README.md CHANGELOG.md
%{_bindir}/handlebars-cli
%endif

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

%package     -n %{name}+dir_source-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+dir_source-devel %{_description}

This package contains library source intended for building other packages
which use "dir_source" feature of "%{crate}" crate.

%files       -n %{name}+dir_source-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+no_logging-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+no_logging-devel %{_description}

This package contains library source intended for building other packages
which use "no_logging" feature of "%{crate}" crate.

%files       -n %{name}+no_logging-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+walkdir-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+walkdir-devel %{_description}

This package contains library source intended for building other packages
which use "walkdir" feature of "%{crate}" crate.

%files       -n %{name}+walkdir-devel
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
* Tue Feb 23 2021 Fabio Valentini <decathorpe@gmail.com> - 3.5.3-1
- Update to version 3.5.3.
- Fixes RHBZ#1931089

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec 29 17:04:49 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 3.5.2-1
- Update to 3.5.2 (Fixes: RHBZ#1911452)

* Sat Nov 28 2020 Fabio Valentini <decathorpe@gmail.com> - 3.5.1-2
- Drop features with missing dependencies (rhai).

* Mon Oct 26 2020 Fabio Valentini <decathorpe@gmail.com> - 3.5.1-1
- Update to version 3.5.1.

* Wed Jul 29 2020 Josh Stone <jistone@redhat.com> - 3.3.0-1
- Update to 3.3.0

* Fri Jul 10 2020 Josh Stone <jistone@redhat.com> - 3.2.1-1
- Update to 3.2.1

* Tue Jun 02 16:30:52 CEST 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 3.1.0-1
- Update to 3.1.0

* Thu Feb 13 2020 Josh Stone <jistone@redhat.com> - 3.0.1-1
- Update to 3.0.1

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 19 09:44:23 CET 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.0.2-1
- Update to 2.0.2

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 19 23:39:17 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.1.0-1
- Downgrade to 1.1.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Dec 15 2018 Josh Stone <jistone@redhat.com> - 1.2.0-1
- Update to 1.2.0

* Sat Nov 10 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.1.0-1
- Update to 1.1.0

* Thu Oct 04 2018 Josh Stone <jistone@redhat.com> - 1.0.5-1
- Update to 1.0.5

* Fri Sep 28 2018 Josh Stone <jistone@redhat.com> - 1.0.4-1
- Update to 1.0.4

* Sat Sep 08 2018 Josh Stone <jistone@redhat.com> - 1.0.3-1
- Update to 1.0.3

* Wed Jul 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.0-1
- Update to 1.0.0

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.32.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.32.4-1
- Update to 0.32.4

* Mon Mar 12 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.32.0-1
- Update to 0.32.0

* Sat Feb 10 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.31.0-1
- Update to 0.31.0

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.30.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Feb 01 2018 Josh Stone <jistone@redhat.com> - 0.30.1-1
- Update to 0.30.1

* Mon Jan 22 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.30.0-1
- Update to 0.30.0

* Mon Jan 08 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.29.1-3
- Rebuild for rust-packaging v5

* Thu Nov 30 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.29.1-2
- Bump lazy_static to 1

* Tue Nov 14 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.29.1-1
- Update to 0.29.1

* Thu Jul 06 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.27.0-1
- Initial package
