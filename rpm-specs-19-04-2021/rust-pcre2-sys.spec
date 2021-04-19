# Generated by rust2rpm 13
%bcond_without check
%global debug_package %{nil}

%global crate pcre2-sys

Name:           rust-%{crate}
Version:        0.2.5
Release:        2%{?dist}
Summary:        Low level bindings to PCRE2

# Upstream license specification: Unlicense/MIT
License:        Unlicense or MIT
URL:            https://crates.io/crates/pcre2-sys
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Low level bindings to PCRE2.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       pkgconfig(libpcre2-8)

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license UNLICENSE LICENSE-MIT COPYING
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
rm -vrf pcre2
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires
echo 'pkgconfig(libpcre2-8)'

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Sep 16 2020 Fabio Valentini <decathorpe@gmail.com> - 0.2.5-1
- Update to version 0.2.5.

* Wed Aug 26 2020 Josh Stone <jistone@redhat.com> - 0.2.4-1
- Update to 0.2.4

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 27 08:55:35 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.2-2
- Regenerate

* Sun Jun 09 15:19:59 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.2-1
- Update to 0.2.2

* Sun Jun 09 11:33:02 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.1-2
- Regenerate

* Tue Apr 30 08:43:36 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.1-1
- Update to 0.2.1

* Tue Apr 16 2019 Josh Stone <jistone@redhat.com> - 0.2.0-1
- Update to 0.2.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Oct 28 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.1-3
- Adapt to new packaging

* Sun Oct 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.1-2
- Run tests in infrastructure

* Sat Sep 08 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.1-1
- Initial package
