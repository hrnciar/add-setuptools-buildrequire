# Generated by rust2rpm 16
%bcond_without check
%global debug_package %{nil}

%global crate image

Name:           rust-%{crate}
Version:        0.23.14
Release:        1%{?dist}
Summary:        Imaging library written in Rust

# Upstream license specification: MIT
License:        MIT
URL:            https://crates.io/crates/image
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Imaging library written in Rust. Provides basic filters and decoders for the
most common image formats.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE
%doc README.md CHANGES.md
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+benchmarks-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+benchmarks-devel %{_description}

This package contains library source intended for building other packages
which use "benchmarks" feature of "%{crate}" crate.

%files       -n %{name}+benchmarks-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+bmp-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+bmp-devel %{_description}

This package contains library source intended for building other packages
which use "bmp" feature of "%{crate}" crate.

%files       -n %{name}+bmp-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+dds-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+dds-devel %{_description}

This package contains library source intended for building other packages
which use "dds" feature of "%{crate}" crate.

%files       -n %{name}+dds-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+dxt-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+dxt-devel %{_description}

This package contains library source intended for building other packages
which use "dxt" feature of "%{crate}" crate.

%files       -n %{name}+dxt-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+farbfeld-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+farbfeld-devel %{_description}

This package contains library source intended for building other packages
which use "farbfeld" feature of "%{crate}" crate.

%files       -n %{name}+farbfeld-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+gif-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+gif-devel %{_description}

This package contains library source intended for building other packages
which use "gif" feature of "%{crate}" crate.

%files       -n %{name}+gif-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+hdr-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+hdr-devel %{_description}

This package contains library source intended for building other packages
which use "hdr" feature of "%{crate}" crate.

%files       -n %{name}+hdr-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+ico-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+ico-devel %{_description}

This package contains library source intended for building other packages
which use "ico" feature of "%{crate}" crate.

%files       -n %{name}+ico-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+jpeg-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+jpeg-devel %{_description}

This package contains library source intended for building other packages
which use "jpeg" feature of "%{crate}" crate.

%files       -n %{name}+jpeg-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+jpeg_rayon-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+jpeg_rayon-devel %{_description}

This package contains library source intended for building other packages
which use "jpeg_rayon" feature of "%{crate}" crate.

%files       -n %{name}+jpeg_rayon-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+png-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+png-devel %{_description}

This package contains library source intended for building other packages
which use "png" feature of "%{crate}" crate.

%files       -n %{name}+png-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+pnm-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+pnm-devel %{_description}

This package contains library source intended for building other packages
which use "pnm" feature of "%{crate}" crate.

%files       -n %{name}+pnm-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+scoped_threadpool-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+scoped_threadpool-devel %{_description}

This package contains library source intended for building other packages
which use "scoped_threadpool" feature of "%{crate}" crate.

%files       -n %{name}+scoped_threadpool-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+tga-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+tga-devel %{_description}

This package contains library source intended for building other packages
which use "tga" feature of "%{crate}" crate.

%files       -n %{name}+tga-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+tiff-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+tiff-devel %{_description}

This package contains library source intended for building other packages
which use "tiff" feature of "%{crate}" crate.

%files       -n %{name}+tiff-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+webp-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+webp-devel %{_description}

This package contains library source intended for building other packages
which use "webp" feature of "%{crate}" crate.

%files       -n %{name}+webp-devel
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
# Missing test files
%cargo_test -- -- \
    --skip dynimage::test::image_dimensions \
    --skip dynimage::test::open_16bpc_png \
    --skip imageops::sample::tests::resize_transparent_image \
    --skip png::tests::ensure_no_decoder_off_by_one \
    --skip png::tests::underlying_error
%endif

%changelog
* Wed Mar 03 2021 Fabio Valentini <decathorpe@gmail.com> - 0.23.14-1
- Update to version 0.23.14.

* Sun Feb 07 2021 Fabio Valentini <decathorpe@gmail.com> - 0.23.13-1
- Update to version 0.23.13.
- Fixes RHBZ#1925270

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.23.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Nov 19 2020 Fabio Valentini <decathorpe@gmail.com> - 0.23.12-1
- Update to version 0.23.12.
- Fixes RHBZ#1899328

* Sat Nov 07 2020 Fabio Valentini <decathorpe@gmail.com> - 0.23.11-1
- Update to version 0.23.11.
- Fixes RHBZ#1891340

* Mon Oct 19 2020 Fabio Valentini <decathorpe@gmail.com> - 0.23.10-1
- Update to version 0.23.10.

* Wed Sep 16 2020 Fabio Valentini <decathorpe@gmail.com> - 0.23.9-1
- Update to version 0.23.9.

* Wed Jul 29 2020 Josh Stone <jistone@redhat.com> - 0.23.8-1
- Update to 0.23.8

* Tue Jul 14 2020 Josh Stone <jistone@redhat.com> - 0.23.7-1
- Update to 0.23.7

* Fri Jun 26 2020 Josh Stone <jistone@redhat.com> - 0.23.6-1
- Update to 0.23.6

* Thu Jun 11 2020 Josh Stone <jistone@redhat.com> - 0.23.5-1
- Update to 0.23.5

* Tue Apr 21 2020 Josh Stone <jistone@redhat.com> - 0.23.4-1
- Update to 0.23.4

* Wed Apr 08 2020 Josh Stone <jistone@redhat.com> - 0.23.3-1
- Update to 0.23.3

* Tue Mar 17 2020 Josh Stone <jistone@redhat.com> - 0.23.2-1
- Update to 0.23.2

* Tue Mar 10 2020 Josh Stone <jistone@redhat.com> - 0.23.1-1
- Update to 0.23.1

* Mon Mar 02 2020 Josh Stone <jistone@redhat.com> - 0.23.0-2
- Bump to png 0.16

* Mon Feb 17 10:58:48 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.23.0-1
- Update to 0.23.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.22.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 16 2020 Josh Stone <jistone@redhat.com> - 0.22.4-1
- Update to 0.22.4

* Tue Nov 19 2019 Josh Stone <jistone@redhat.com> - 0.22.3-1
- Update to 0.22.3

* Sun Sep 08 16:53:42 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.22.2-1
- Update to 0.22.2

* Sun Sep 01 20:48:08 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.22.1-1
- Update to 0.22.1

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun 22 20:49:22 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.21.2-2
- Regenerate

* Sun Jun 09 17:07:34 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.21.2-1
- Update to 0.21.2

* Mon Apr 15 2019 Josh Stone <jistone@redhat.com> - 0.21.1-1
- Update to 0.21.1

* Fri Mar 15 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.21.0-1
- Initial package
