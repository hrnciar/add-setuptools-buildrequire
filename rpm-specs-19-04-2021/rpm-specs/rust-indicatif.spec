# Generated by rust2rpm 15
%bcond_without check
%global debug_package %{nil}

%global crate indicatif

Name:           rust-%{crate}
Version:        0.15.0
Release:        3%{?dist}
Summary:        Progress bar and cli reporting library for Rust

# Upstream license specification: MIT
License:        MIT
URL:            https://crates.io/crates/indicatif
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Progress bar and cli reporting library for Rust.}

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

%package     -n %{name}+improved_unicode-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+improved_unicode-devel %{_description}

This package contains library source intended for building other packages
which use "improved_unicode" feature of "%{crate}" crate.

%files       -n %{name}+improved_unicode-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+rayon-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+rayon-devel %{_description}

This package contains library source intended for building other packages
which use "rayon" feature of "%{crate}" crate.

%files       -n %{name}+rayon-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+unicode-segmentation-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+unicode-segmentation-devel %{_description}

This package contains library source intended for building other packages
which use "unicode-segmentation" feature of "%{crate}" crate.

%files       -n %{name}+unicode-segmentation-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+unicode-width-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+unicode-width-devel %{_description}

This package contains library source intended for building other packages
which use "unicode-width" feature of "%{crate}" crate.

%files       -n %{name}+unicode-width-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+with_rayon-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+with_rayon-devel %{_description}

This package contains library source intended for building other packages
which use "with_rayon" feature of "%{crate}" crate.

%files       -n %{name}+with_rayon-devel
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
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 18 06:46:22 CEST 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.15.0-1
- Update to 0.15.0

* Wed Feb 26 2020 Josh Stone <jistone@redhat.com> - 0.14.0-1
- Update to 0.14.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Dec 06 17:29:48 CET 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.13.0-1
- Update to 0.13.0

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jul 21 08:54:40 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.11.0-5
- Regenerate

* Sun Jun 09 14:47:20 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.11.0-4
- Regenerate

* Tue May 07 14:30:02 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.11.0-3
- Update number_prefix to 0.3

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 28 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.11.0-1
- Initial package
