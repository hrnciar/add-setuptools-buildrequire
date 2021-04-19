# Generated by rust2rpm 16
# * rspec is not packaged
%bcond_with check
%global debug_package %{nil}

%global crate colored

Name:           rust-%{crate}
Version:        2.0.0
Release:        2%{?dist}
Summary:        Most simple way to add colors in your terminal

# Upstream license specification: MPL-2.0
License:        MPLv2.0
URL:            https://crates.io/crates/colored
Source:         %{crates_source}
# Initial patched metadata
# * No windows
Patch0:         colored-fix-metadata.diff

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Most simple way to add colors in your terminal.}

%description %{_description}

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

%package     -n %{name}+no-color-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+no-color-devel %{_description}

This package contains library source intended for building other packages
which use "no-color" feature of "%{crate}" crate.

%files       -n %{name}+no-color-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
find -type f -executable -exec chmod -v -x '{}' +
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
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov 30 2020 Fabio Valentini <decathorpe@gmail.com> - 2.0.0-1
- Update to version 2.0.0.
- Fixes RHBZ#1856656

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Feb 24 07:03:52 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.9.3-1
- Update to 1.9.3

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 15 2020 Josh Stone <jistone@redhat.com> - 1.9.2-1
- Update to 1.9.2

* Sat Nov 23 2019 Josh Stone <jistone@redhat.com> - 1.9.0-1
- Update to 1.9.0

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 21 22:27:36 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.8.0-3
- Regenerate

* Sun Jun 09 15:37:55 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.8.0-2
- Regenerate

* Thu May 02 2019 Josh Stone <jistone@redhat.com> - 1.8.0-1
- Update to 1.8.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 28 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.7.0-1
- Initial package
