# Generated by rust2rpm 13
%bcond_without check

%global crate comrak

Name:           rust-%{crate}
Version:        0.8.2
Release:        3%{?dist}
Summary:        100% CommonMark-compatible GitHub Flavored Markdown parser and formatter

# Upstream license specification: BSD-2-Clause
License:        BSD
URL:            https://crates.io/crates/comrak
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
100% CommonMark-compatible GitHub Flavored Markdown parser and formatter.}

%description %{_description}

%if ! %{__cargo_skip_build}
%package     -n %{crate}
Summary:        %{summary}
# * ASL 2.0 or MIT
# * MIT
# * MIT or ASL 2.0
# * Unlicense or MIT
License:        BSD and MIT

%description -n %{crate} %{_description}

%files       -n %{crate}
%license COPYING
%doc README.md changelog.txt
%{_bindir}/comrak
%endif

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license COPYING
%doc README.md changelog.txt
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+clap-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+clap-devel %{_description}

This package contains library source intended for building other packages
which use "clap" feature of "%{crate}" crate.

%files       -n %{name}+clap-devel
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
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec 28 13:28:40 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.8.2-2
- Rebuild

* Tue Oct 20 2020 Fabio Valentini <decathorpe@gmail.com> - 0.8.2-1
- Update to version 0.8.2.

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Josh Stone <jistone@redhat.com> - 0.7.1-1
- Update to 0.7.1

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 15 2020 Josh Stone <jistone@redhat.com> - 0.7.0-1
- Update to 0.7.0

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 07 07:21:17 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6.2-1
- Update to 0.6.2

* Mon May 06 08:10:52 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6.1-1
- Initial package
