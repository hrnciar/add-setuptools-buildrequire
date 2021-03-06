# Generated by rust2rpm 13
%bcond_without check

%global crate gcsf

Name:           rust-%{crate}
Version:        0.1.28
Release:        4%{?dist}
Summary:        Filesystem based on Google Drive

# Upstream license specification: MIT
License:        MIT
URL:            https://crates.io/crates/gcsf
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Filesystem based on Google Drive.}

%description %{_description}

%if ! %{__cargo_skip_build}
%package     -n %{crate}
Summary:        %{summary}

%description -n %{crate} %{_description}

%files       -n %{crate}
%license LICENSE
%doc README.md sample_config.toml gcsf.service
%{_bindir}/gcsf
%endif

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
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.28-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec 28 13:30:30 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.1.28-3
- Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.28-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Apr 14 2020 Josh Stone <jistone@redhat.com> - 0.1.28-1
- Update to 0.1.28

* Thu Apr 09 2020 Josh Stone <jistone@redhat.com> - 0.1.26-1
- Update to 0.1.26

* Wed Mar 04 2020 Josh Stone <jistone@redhat.com> - 0.1.25-4
- Bump to config 0.10, lru_time_cache 0.9, pretty_env_logger 0.4

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.25-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.25-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Feb 21 2019 Josh Stone <jistone@redhat.com> - 0.1.25-1
- Update to 0.1.25

* Sun Feb 10 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.24-1
- Update to 0.1.24

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Nov 27 2018 Josh Stone <jistone@redhat.com> - 0.1.18-2
- Adapt to new packaging

* Thu Oct 11 2018 Josh Stone <jistone@redhat.com> - 0.1.18-1
- Update to 0.1.18

* Sat Aug 04 2018 Josh Stone <jistone@redhat.com> - 0.1.17-1
- Update to 0.1.17

* Tue Jul 31 2018 Florian Weimer <fweimer@redhat.com> - 0.1.16-2
- Rebuild with fixed binutils

* Sat Jul 28 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.16-1
- Update to 0.1.16

* Thu Jul 26 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.15-1
- Initial package
