# Generated by rust2rpm 13
%bcond_with check
%global debug_package %{nil}

%global crate lru_time_cache

Name:           rust-%{crate}
Version:        0.10.0
Release:        3%{?dist}
Summary:        Implementation of a Least Recently Used caching algorithm

# Upstream license specification: MIT OR BSD-3-Clause
License:        MIT or BSD
URL:            https://crates.io/crates/lru_time_cache
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Implementation of a Least Recently Used caching algorithm in a container which
may be limited by size or time, ordered by most recently seen.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-BSD LICENSE-MIT
%doc README.md CHANGELOG.md
%{cargo_registry}/%{crate}-%{version_no_tilde}/
%exclude %{cargo_registry}/%{crate}-%{version_no_tilde}/appveyor.yml

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+fake_clock-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+fake_clock-devel %{_description}

This package contains library source intended for building other packages
which use "fake_clock" feature of "%{crate}" crate.

%files       -n %{name}+fake_clock-devel
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
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Apr 09 2020 Josh Stone <jistone@redhat.com> - 0.10.0-1
- Update to 0.10.0

* Wed Mar 04 2020 Josh Stone <jistone@redhat.com> - 0.9.0-1
- Update to 0.9.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Mar 16 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.8.1-3
- Do not pull optional dependencies

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 08 2019 Josh Stone <jistone@redhat.com> - 0.8.1-1
- Update to 0.8.1

* Fri Dec 07 2018 Josh Stone <jistone@redhat.com> - 0.8.0-4
- Fix warnings on removed lints

* Fri Nov 09 2018 Josh Stone <jistone@redhat.com> - 0.8.0-3
- Adapt to new packaging

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jul 06 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.8.0-1
- Initial package
