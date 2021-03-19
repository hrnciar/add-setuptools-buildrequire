# Generated by rust2rpm 13
%bcond_with check
%global debug_package %{nil}

%global crate cairo-rs

Name:           rust-%{crate}
Version:        0.9.1
Release:        3%{?dist}
Summary:        Rust bindings for the Cairo library

# Upstream license specification: MIT
License:        MIT
URL:            https://crates.io/crates/cairo-rs
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Rust bindings for the Cairo library.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license COPYRIGHT LICENSE
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

%package     -n %{name}+dox-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+dox-devel %{_description}

This package contains library source intended for building other packages
which use "dox" feature of "%{crate}" crate.

%files       -n %{name}+dox-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+embed-lgpl-docs-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+embed-lgpl-docs-devel %{_description}

This package contains library source intended for building other packages
which use "embed-lgpl-docs" feature of "%{crate}" crate.

%files       -n %{name}+embed-lgpl-docs-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+freetype-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+freetype-devel %{_description}

This package contains library source intended for building other packages
which use "freetype" feature of "%{crate}" crate.

%files       -n %{name}+freetype-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+glib-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+glib-devel %{_description}

This package contains library source intended for building other packages
which use "glib" feature of "%{crate}" crate.

%files       -n %{name}+glib-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+glib-sys-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+glib-sys-devel %{_description}

This package contains library source intended for building other packages
which use "glib-sys" feature of "%{crate}" crate.

%files       -n %{name}+glib-sys-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+gobject-sys-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+gobject-sys-devel %{_description}

This package contains library source intended for building other packages
which use "gobject-sys" feature of "%{crate}" crate.

%files       -n %{name}+gobject-sys-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+gtk-rs-lgpl-docs-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+gtk-rs-lgpl-docs-devel %{_description}

This package contains library source intended for building other packages
which use "gtk-rs-lgpl-docs" feature of "%{crate}" crate.

%files       -n %{name}+gtk-rs-lgpl-docs-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+pdf-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+pdf-devel %{_description}

This package contains library source intended for building other packages
which use "pdf" feature of "%{crate}" crate.

%files       -n %{name}+pdf-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+png-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+png-devel %{_description}

This package contains library source intended for building other packages
which use "png" feature of "%{crate}" crate.

%files       -n %{name}+png-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+ps-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+ps-devel %{_description}

This package contains library source intended for building other packages
which use "ps" feature of "%{crate}" crate.

%files       -n %{name}+ps-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+purge-lgpl-docs-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+purge-lgpl-docs-devel %{_description}

This package contains library source intended for building other packages
which use "purge-lgpl-docs" feature of "%{crate}" crate.

%files       -n %{name}+purge-lgpl-docs-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+script-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+script-devel %{_description}

This package contains library source intended for building other packages
which use "script" feature of "%{crate}" crate.

%files       -n %{name}+script-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+svg-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+svg-devel %{_description}

This package contains library source intended for building other packages
which use "svg" feature of "%{crate}" crate.

%files       -n %{name}+svg-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+use_glib-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+use_glib-devel %{_description}

This package contains library source intended for building other packages
which use "use_glib" feature of "%{crate}" crate.

%files       -n %{name}+use_glib-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+v1_14-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+v1_14-devel %{_description}

This package contains library source intended for building other packages
which use "v1_14" feature of "%{crate}" crate.

%files       -n %{name}+v1_14-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+v1_16-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+v1_16-devel %{_description}

This package contains library source intended for building other packages
which use "v1_16" feature of "%{crate}" crate.

%files       -n %{name}+v1_16-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+xcb-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+xcb-devel %{_description}

This package contains library source intended for building other packages
which use "xcb" feature of "%{crate}" crate.

%files       -n %{name}+xcb-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+xlib-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+xlib-devel %{_description}

This package contains library source intended for building other packages
which use "xlib" feature of "%{crate}" crate.

%files       -n %{name}+xlib-devel
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
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Josh Stone <jistone@redhat.com> - 0.9.1-1
- Update to 0.9.1

* Thu Feb 20 2020 Josh Stone <jistone@redhat.com> - 0.8.1-1
- Update to 0.8.1

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 15 2020 Josh Stone <jistone@redhat.com> - 0.8.0-1
- Update to 0.8.0

* Tue Dec 10 2019 Josh Stone <jistone@redhat.com> - 0.7.1-1
- Update to 0.7.1

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Apr 28 14:38:36 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6.0-1
- Update to 0.6.0

* Mon Feb 18 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.5.0-1
- Update to 0.5.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 22 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.1-1
- Update to 0.4.1

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 08 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.0-2
- Rebuild for rust-packaging v5

* Sat Jan 06 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.0-1
- Initial package
