# Generated by rust2rpm 13
%bcond_with check
%global debug_package %{nil}

%global crate gtk-source-sys

Name:           rust-%{crate}
Version:        0.10.0
Release:        3%{?dist}
Summary:        FFI bindings to libgtksourceview-3

# Upstream license specification: MIT
License:        MIT
URL:            https://crates.io/crates/gtk-source-sys
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
FFI bindings to libgtksourceview-3.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       pkgconfig(gtksourceview-3.0) >= 3.0

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+dox-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+dox-devel %{_description}

This package contains library source intended for building other packages
which use "dox" feature of "%{crate}" crate.

%files       -n %{name}+dox-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+v3_10-devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       pkgconfig(gtksourceview-3.0) >= 3.10

%description -n %{name}+v3_10-devel %{_description}

This package contains library source intended for building other packages
which use "v3_10" feature of "%{crate}" crate.

%files       -n %{name}+v3_10-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+v3_12-devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       pkgconfig(gtksourceview-3.0) >= 3.12

%description -n %{name}+v3_12-devel %{_description}

This package contains library source intended for building other packages
which use "v3_12" feature of "%{crate}" crate.

%files       -n %{name}+v3_12-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+v3_14-devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       pkgconfig(gtksourceview-3.0) >= 3.14

%description -n %{name}+v3_14-devel %{_description}

This package contains library source intended for building other packages
which use "v3_14" feature of "%{crate}" crate.

%files       -n %{name}+v3_14-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+v3_16-devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       pkgconfig(gtksourceview-3.0) >= 3.16

%description -n %{name}+v3_16-devel %{_description}

This package contains library source intended for building other packages
which use "v3_16" feature of "%{crate}" crate.

%files       -n %{name}+v3_16-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+v3_18-devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       pkgconfig(gtksourceview-3.0) >= 3.18

%description -n %{name}+v3_18-devel %{_description}

This package contains library source intended for building other packages
which use "v3_18" feature of "%{crate}" crate.

%files       -n %{name}+v3_18-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+v3_20-devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       pkgconfig(gtksourceview-3.0) >= 3.20

%description -n %{name}+v3_20-devel %{_description}

This package contains library source intended for building other packages
which use "v3_20" feature of "%{crate}" crate.

%files       -n %{name}+v3_20-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+v3_22-devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       pkgconfig(gtksourceview-3.0) >= 3.22

%description -n %{name}+v3_22-devel %{_description}

This package contains library source intended for building other packages
which use "v3_22" feature of "%{crate}" crate.

%files       -n %{name}+v3_22-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+v3_24-devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       pkgconfig(gtksourceview-3.0) >= 3.24

%description -n %{name}+v3_24-devel %{_description}

This package contains library source intended for building other packages
which use "v3_24" feature of "%{crate}" crate.

%files       -n %{name}+v3_24-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+v3_4-devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       pkgconfig(gtksourceview-3.0) >= 3.4

%description -n %{name}+v3_4-devel %{_description}

This package contains library source intended for building other packages
which use "v3_4" feature of "%{crate}" crate.

%files       -n %{name}+v3_4-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+v3_8-devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       pkgconfig(gtksourceview-3.0) >= 3.8

%description -n %{name}+v3_8-devel %{_description}

This package contains library source intended for building other packages
which use "v3_8" feature of "%{crate}" crate.

%files       -n %{name}+v3_8-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires
echo 'pkgconfig(gtksourceview-3.0) >= 3.0'

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

* Thu Jul 09 2020 Josh Stone <jistone@redhat.com> - 0.10.0-1
- Update to 0.10.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 15 2020 Josh Stone <jistone@redhat.com> - 0.9.1-1
- Update to 0.9.1

* Tue Dec 10 2019 Josh Stone <jistone@redhat.com> - 0.9.0-1
- Update to 0.9.0

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Apr 28 15:41:22 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.8.0-1
- Update to 0.8.0

* Mon Feb 18 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.7.0-1
- Update to 0.7.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Mar 20 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6.0-1
- Update to 0.6.0

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.5.0-1
- Initial package
