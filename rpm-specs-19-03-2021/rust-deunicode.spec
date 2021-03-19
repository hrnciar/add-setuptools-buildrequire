# Generated by rust2rpm 13
%bcond_without check
%global debug_package %{nil}

%global crate deunicode

Name:           rust-%{crate}
Version:        1.1.1
Release:        4%{?dist}
Summary:        Convert Unicode strings to pure ASCII by intelligently transliterating them

# Upstream license specification: BSD-3-Clause
# https://github.com/kornelski/deunicode/issues/3
License:        BSD
URL:            https://crates.io/crates/deunicode
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Convert Unicode strings to pure ASCII by intelligently transliterating them.
Suppors Emoji and Chinese.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
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
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Apr 23 2020 Josh Stone <jistone@redhat.com> - 1.1.1-1
- Update to 1.1.1

* Mon Feb 24 2020 Josh Stone <jistone@redhat.com> - 1.1.0-1
- Update to 1.1.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 23 11:26:06 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.0-2
- Regenerate

* Fri May 31 11:27:46 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.0-1
- Initial package