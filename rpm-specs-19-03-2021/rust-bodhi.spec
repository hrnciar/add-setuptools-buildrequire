# Generated by rust2rpm 16
%bcond_without check
%global debug_package %{nil}

%global crate bodhi

Name:           rust-%{crate}
Version:        1.0.3
Release:        1%{?dist}
Summary:        Bodhi REST API client

# Upstream license specification: MIT OR Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/bodhi
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Bodhi REST API client.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-APACHE LICENSE-MIT
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

%package     -n %{name}+data-tests-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+data-tests-devel %{_description}

This package contains library source intended for building other packages
which use "data-tests" feature of "%{crate}" crate.

%files       -n %{name}+data-tests-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+debug-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+debug-devel %{_description}

This package contains library source intended for building other packages
which use "debug" feature of "%{crate}" crate.

%files       -n %{name}+debug-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+offline-tests-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+offline-tests-devel %{_description}

This package contains library source intended for building other packages
which use "offline-tests" feature of "%{crate}" crate.

%files       -n %{name}+offline-tests-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+online-tests-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+online-tests-devel %{_description}

This package contains library source intended for building other packages
which use "online-tests" feature of "%{crate}" crate.

%files       -n %{name}+online-tests-devel
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
* Mon Mar 08 2021 Fabio Valentini <decathorpe@gmail.com> - 1.0.3-1
- Update to version 1.0.3.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec 15 2020 Fabio Valentini <decathorpe@gmail.com> - 1.0.1-1
- Update to version 1.0.1.

* Tue Nov 03 2020 Fabio Valentini <decathorpe@gmail.com> - 0.6.4-1
- Update to version 0.6.4.

* Fri Aug 28 2020 Fabio Valentini <decathorpe@gmail.com> - 0.6.2-1
- Update to version 0.6.2.

* Sun Aug 16 2020 Fabio Valentini <decathorpe@gmail.com> - 0.6.1-1
- Update to version 0.6.1.

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Fabio Valentini <decathorpe@gmail.com> - 0.6.0-1
- Update to version 0.6.0.

* Wed May 20 13:12:51 CEST 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.5.10-1
- Update to 0.5.10

* Wed Mar 25 19:49:29 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.5.9-1
- Update to 0.5.9

* Fri Mar 20 2020 Fabio Valentini <decathorpe@gmail.com> - 0.5.8-1
- Update to version 0.5.8.

* Thu Mar 05 2020 Fabio Valentini <decathorpe@gmail.com> - 0.5.7-1
- Update to version 0.5.7.

* Sat Feb 29 2020 Fabio Valentini <decathorpe@gmail.com> - 0.5.6-1
- Update to version 0.5.6.

* Sun Feb 16 2020 Fabio Valentini <decathorpe@gmail.com> - 0.5.5-1
- Update to version 0.5.5.

* Mon Feb 10 2020 Fabio Valentini <decathorpe@gmail.com> - 0.5.4-1
- Initial package
