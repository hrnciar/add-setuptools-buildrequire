# Generated by rust2rpm 17
%bcond_without check
%global debug_package %{nil}

%global crate console

Name:           rust-%{crate}
Version:        0.14.0
Release:        2%{?dist}
Summary:        Terminal and console abstraction for Rust

# Upstream license specification: MIT
License:        MIT
URL:            https://crates.io/crates/console
Source:         %{crates_source}
# Initial patched metadata
# * No Windows
Patch0:         console-fix-metadata.diff

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Terminal and console abstraction for Rust.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE
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

%package     -n %{name}+ansi-parsing-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+ansi-parsing-devel %{_description}

This package contains library source intended for building other packages
which use "ansi-parsing" feature of "%{crate}" crate.

%files       -n %{name}+ansi-parsing-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+regex-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+regex-devel %{_description}

This package contains library source intended for building other packages
which use "regex" feature of "%{crate}" crate.

%files       -n %{name}+regex-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+unicode-width-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+unicode-width-devel %{_description}

This package contains library source intended for building other packages
which use "unicode-width" feature of "%{crate}" crate.

%files       -n %{name}+unicode-width-devel
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
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 10 17:45:33 CET 2021 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.14.0-1
- Update to 0.14.0 (Fixes: RHBZ#1910977)

* Sun Oct 25 2020 Fabio Valentini <decathorpe@gmail.com> - 0.13.0-1
- Update to version 0.13.0.

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon May 18 2020 Josh Stone <jistone@redhat.com> - 0.11.3-1
- Update to 0.11.3

* Sat May 02 10:56:03 CEST 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.11.2-1
- Update to 0.11.2

* Mon Apr 27 08:18:46 CEST 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.10.1-1
- Update to 0.10.1

* Mon Mar 23 07:04:01 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.10.0-1
- Update to 0.10.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 27 2020 Josh Stone <jistone@redhat.com> - 0.9.2-1
- Update to 0.9.2

* Fri Dec 06 17:31:03 CET 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.9.1-1
- Update to 0.9.1

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 20 11:03:42 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.7.7-1
- Update to 0.7.7

* Tue Jun 18 23:43:14 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.7.6-1
- Update to 0.7.6

* Sun Jun 09 14:26:32 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.7.5-3
- Regenerate

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 28 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.7.5-1
- Update to 0.7.5

* Thu Dec 20 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6.2-3
- Run tests in infrastructure

* Sat Nov 03 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6.2-2
- Adapt to new packaging

* Tue Sep 11 2018 Josh Stone <jistone@redhat.com> - 0.6.2-1
- Update to 0.6.2

* Mon Sep 03 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6.1-1
- Initial package