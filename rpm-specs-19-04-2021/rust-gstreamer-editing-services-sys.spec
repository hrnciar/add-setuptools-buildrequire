# Generated by rust2rpm 13
%bcond_with check
%global debug_package %{nil}

%global crate gstreamer-editing-services-sys

Name:           rust-%{crate}
Version:        0.9.1
Release:        2%{?dist}
Summary:        FFI bindings to libges-1.0

# Upstream license specification: MIT
# https://gitlab.freedesktop.org/gstreamer/gstreamer-rs/merge_requests/255
License:        MIT
URL:            https://crates.io/crates/gstreamer-editing-services-sys
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
These bindings are providing unsafe FFI API that can be used to interface with
GStreamer. Generally they are meant to be used as the building block for
higher-level abstractions like:

Bindings for GStreamer applications and plugins:
• https://gitlab.freedesktop.org/gstreamer/gstreamer-rs

Various GStreamer plugins written in Rust:
• https://gitlab.freedesktop.org/gstreamer/gst-plugins-rs

The bindings are autogenerated with gir based on the GObject-Introspection API
metadata provided by the GStreamer project.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       pkgconfig(gst-editing-services-1.0) >= 1.0

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

%package     -n %{name}+dox-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+dox-devel %{_description}

This package contains library source intended for building other packages
which use "dox" feature of "%{crate}" crate.

%files       -n %{name}+dox-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+v1_10-devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       pkgconfig(gst-editing-services-1.0) >= 1.10

%description -n %{name}+v1_10-devel %{_description}

This package contains library source intended for building other packages
which use "v1_10" feature of "%{crate}" crate.

%files       -n %{name}+v1_10-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+v1_12-devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       pkgconfig(gst-editing-services-1.0) >= 1.12

%description -n %{name}+v1_12-devel %{_description}

This package contains library source intended for building other packages
which use "v1_12" feature of "%{crate}" crate.

%files       -n %{name}+v1_12-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+v1_14-devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       pkgconfig(gst-editing-services-1.0) >= 1.14

%description -n %{name}+v1_14-devel %{_description}

This package contains library source intended for building other packages
which use "v1_14" feature of "%{crate}" crate.

%files       -n %{name}+v1_14-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+v1_16-devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       pkgconfig(gst-editing-services-1.0) >= 1.16

%description -n %{name}+v1_16-devel %{_description}

This package contains library source intended for building other packages
which use "v1_16" feature of "%{crate}" crate.

%files       -n %{name}+v1_16-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+v1_18-devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       pkgconfig(gst-editing-services-1.0) >= 1.18

%description -n %{name}+v1_18-devel %{_description}

This package contains library source intended for building other packages
which use "v1_18" feature of "%{crate}" crate.

%files       -n %{name}+v1_18-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+v1_2-devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       pkgconfig(gst-editing-services-1.0) >= 1.2

%description -n %{name}+v1_2-devel %{_description}

This package contains library source intended for building other packages
which use "v1_2" feature of "%{crate}" crate.

%files       -n %{name}+v1_2-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+v1_4-devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       pkgconfig(gst-editing-services-1.0) >= 1.4

%description -n %{name}+v1_4-devel %{_description}

This package contains library source intended for building other packages
which use "v1_4" feature of "%{crate}" crate.

%files       -n %{name}+v1_4-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+v1_6-devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       pkgconfig(gst-editing-services-1.0) >= 1.6

%description -n %{name}+v1_6-devel %{_description}

This package contains library source intended for building other packages
which use "v1_6" feature of "%{crate}" crate.

%files       -n %{name}+v1_6-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+v1_8-devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       pkgconfig(gst-editing-services-1.0) >= 1.8

%description -n %{name}+v1_8-devel %{_description}

This package contains library source intended for building other packages
which use "v1_8" feature of "%{crate}" crate.

%files       -n %{name}+v1_8-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires
echo 'pkgconfig(gst-editing-services-1.0) >= 1.0'

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Sep 09 2020 Josh Stone <jistone@redhat.com> - 0.9.1-1
- Update to 0.9.1

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 09 2020 Josh Stone <jistone@redhat.com> - 0.9.0-1
- Update to 0.9.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 15 2020 Josh Stone <jistone@redhat.com> - 0.8.1-1
- Update to 0.8.1

* Tue Dec 10 2019 Josh Stone <jistone@redhat.com> - 0.8.0-1
- Update to 0.8.0

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon May 06 11:43:42 EEST 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.7.0-1
- Initial package
