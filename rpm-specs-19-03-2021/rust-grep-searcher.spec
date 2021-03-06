# Generated by rust2rpm 16
%bcond_without check
%global debug_package %{nil}

%global crate grep-searcher

Name:           rust-%{crate}
Version:        0.1.7
Release:        4%{?dist}
Summary:        Fast line oriented regex searching as a library

# Upstream license specification: Unlicense/MIT
License:        Unlicense or MIT
URL:            https://crates.io/crates/grep-searcher
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Fast line oriented regex searching as a library.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license UNLICENSE LICENSE-MIT
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
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Nov 20 2020 Fabio Valentini <decathorpe@gmail.com> - 0.1.7-3
- Remove features with broken dependencies.

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Mar 17 16:29:36 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.1.7-1
- Update to 0.1.7

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Sep 13 17:38:25 CEST 2019 Robert-Andr?? Mauchin <zebob.m@gmail.com> - 0.1.6-2
- Bump bytecount to 0.6

* Sun Sep 08 09:25:37 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.6-1
- Update to 0.1.6

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 27 07:42:50 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.5-1
- Update to 0.1.5

* Thu Jun 20 16:44:14 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.4-3
- Regenerate

* Sun Jun 09 10:15:52 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.4-2
- Regenerate

* Tue Apr 16 12:01:31 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.4-1
- Update to 0.1.4

* Sun Feb 10 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.3-1
- Update to 0.1.3

* Sun Feb 10 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.2-1
- Update to 0.1.2

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Nov 27 2018 Josh Stone <jistone@redhat.com> - 0.1.1-4
- Bump to memmap 0.7

* Sun Oct 28 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.1-3
- Adapt to new packaging

* Sun Oct 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.1-2
- Run tests in infrastructure

* Sat Sep 08 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.1-1
- Initial package
