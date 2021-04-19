# Generated by rust2rpm 16
# * https://github.com/PistonDevelopers/image-gif/issues/51
%bcond_with check
%global debug_package %{nil}

%global crate gif

Name:           rust-%{crate}
Version:        0.11.2
Release:        1%{?dist}
Summary:        GIF de- and encoder

# Upstream license specification: MIT/Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/gif
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
GIF de- and encoder.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-MIT LICENSE-APACHE
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

%package     -n %{name}+raii_no_panic-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+raii_no_panic-devel %{_description}

This package contains library source intended for building other packages
which use "raii_no_panic" feature of "%{crate}" crate.

%files       -n %{name}+raii_no_panic-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+std-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+std-devel %{_description}

This package contains library source intended for building other packages
which use "std" feature of "%{crate}" crate.

%files       -n %{name}+std-devel
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
* Tue Mar 23 2021 Fabio Valentini <decathorpe@gmail.com> - 0.11.2-1
- Update to version 0.11.2.
- Fixes RHBZ#1941772

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Oct 01 2020 Fabio Valentini <decathorpe@gmail.com> - 0.11.1-1
- Update to version 0.11.1.

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Sep 21 08:58:58 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.10.3-1
- Update to 0.10.3

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 23 10:58:48 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.10.2-2
- Regenerate

* Mon Jun 03 2019 Josh Stone <jistone@redhat.com> - 0.10.2-1
- Update to 0.10.2

* Fri Mar 15 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.10.1-1
- Initial package
