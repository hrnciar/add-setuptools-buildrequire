# Generated by rust2rpm 16
%bcond_without check

# Install all deps (without check), grab their licenses and make it simple
# * ASL 2.0
# * ASL 2.0 or MIT
# * BSD
# * ISC
# * MIT
# * MIT or ASL 2.0
# * Unlicense or MIT
# * zlib
# * zlib or ASL 2.0 or MIT
%global binary_license BSD and ASL 2.0 and ISC and MIT and zlib

%global crate rav1e

Name:           rust-%{crate}
Version:        0.4.1
Release:        1%{?dist}
Summary:        Fastest and safest AV1 encoder

# Upstream license specification: BSD-2-Clause
# src/ext/x86/x86inc.asm is under ISC, https://github.com/xiph/rav1e/issues/2181
License:        BSD and ISC
URL:            https://crates.io/crates/rav1e
Source:         %{crates_source}
# Initial patched metadata
# * Remove fuzzing dependencies
Patch0:         rav1e-fix-metadata.diff

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Fastest and safest AV1 encoder.}

%description %{_description}

%if ! %{__cargo_skip_build}
%package     -n %{crate}
Summary:        %{summary}
License:        %{binary_license}

%description -n %{crate} %{_description}

%files       -n %{crate}
%license LICENSE PATENTS
%doc README.md
%{_bindir}/rav1e

%package     -n %{crate}-libs
Summary:        Library files for rav1e
License:        %{binary_license}

%description -n %{crate}-libs
Library files for rav1e, the fastest and safest AV1 encoder.

%files       -n %{crate}-libs
%license LICENSE PATENTS
%{_libdir}/librav1e.so.0*

%package     -n %{crate}-devel
Summary:        Development files for rav1e
Requires:       %{crate}-libs%{?_isa} = %{version}-%{release}

%description -n %{crate}-devel
Development files for rav1e, the fastest and safest AV1 encoder.

%files       -n %{crate}-devel
%{_includedir}/rav1e/
%{_libdir}/librav1e.so
%{_libdir}/pkgconfig/rav1e.pc
%endif

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license PATENTS LICENSE
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

%package     -n %{name}+aom-sys-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+aom-sys-devel %{_description}

This package contains library source intended for building other packages
which use "aom-sys" feature of "%{crate}" crate.

%files       -n %{name}+aom-sys-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+asm-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+asm-devel %{_description}

This package contains library source intended for building other packages
which use "asm" feature of "%{crate}" crate.

%files       -n %{name}+asm-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+av-metrics-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+av-metrics-devel %{_description}

This package contains library source intended for building other packages
which use "av-metrics" feature of "%{crate}" crate.

%files       -n %{name}+av-metrics-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+backtrace-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+backtrace-devel %{_description}

This package contains library source intended for building other packages
which use "backtrace" feature of "%{crate}" crate.

%files       -n %{name}+backtrace-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+bench-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+bench-devel %{_description}

This package contains library source intended for building other packages
which use "bench" feature of "%{crate}" crate.

%files       -n %{name}+bench-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+binaries-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+binaries-devel %{_description}

This package contains library source intended for building other packages
which use "binaries" feature of "%{crate}" crate.

%files       -n %{name}+binaries-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+byteorder-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+byteorder-devel %{_description}

This package contains library source intended for building other packages
which use "byteorder" feature of "%{crate}" crate.

%files       -n %{name}+byteorder-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+capi-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+capi-devel %{_description}

This package contains library source intended for building other packages
which use "capi" feature of "%{crate}" crate.

%files       -n %{name}+capi-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+cc-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+cc-devel %{_description}

This package contains library source intended for building other packages
which use "cc" feature of "%{crate}" crate.

%files       -n %{name}+cc-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+channel-api-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+channel-api-devel %{_description}

This package contains library source intended for building other packages
which use "channel-api" feature of "%{crate}" crate.

%files       -n %{name}+channel-api-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+check_asm-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+check_asm-devel %{_description}

This package contains library source intended for building other packages
which use "check_asm" feature of "%{crate}" crate.

%files       -n %{name}+check_asm-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+clap-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+clap-devel %{_description}

This package contains library source intended for building other packages
which use "clap" feature of "%{crate}" crate.

%files       -n %{name}+clap-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+console-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+console-devel %{_description}

This package contains library source intended for building other packages
which use "console" feature of "%{crate}" crate.

%files       -n %{name}+console-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+crossbeam-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+crossbeam-devel %{_description}

This package contains library source intended for building other packages
which use "crossbeam" feature of "%{crate}" crate.

%files       -n %{name}+crossbeam-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+dav1d-sys-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+dav1d-sys-devel %{_description}

This package contains library source intended for building other packages
which use "dav1d-sys" feature of "%{crate}" crate.

%files       -n %{name}+dav1d-sys-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+decode_test-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+decode_test-devel %{_description}

This package contains library source intended for building other packages
which use "decode_test" feature of "%{crate}" crate.

%files       -n %{name}+decode_test-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+decode_test_dav1d-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+decode_test_dav1d-devel %{_description}

This package contains library source intended for building other packages
which use "decode_test_dav1d" feature of "%{crate}" crate.

%files       -n %{name}+decode_test_dav1d-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+desync_finder-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+desync_finder-devel %{_description}

This package contains library source intended for building other packages
which use "desync_finder" feature of "%{crate}" crate.

%files       -n %{name}+desync_finder-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+dump_ivf-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+dump_ivf-devel %{_description}

This package contains library source intended for building other packages
which use "dump_ivf" feature of "%{crate}" crate.

%files       -n %{name}+dump_ivf-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+dump_lookahead_data-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+dump_lookahead_data-devel %{_description}

This package contains library source intended for building other packages
which use "dump_lookahead_data" feature of "%{crate}" crate.

%files       -n %{name}+dump_lookahead_data-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+fern-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+fern-devel %{_description}

This package contains library source intended for building other packages
which use "fern" feature of "%{crate}" crate.

%files       -n %{name}+fern-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+image-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+image-devel %{_description}

This package contains library source intended for building other packages
which use "image" feature of "%{crate}" crate.

%files       -n %{name}+image-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+ivf-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+ivf-devel %{_description}

This package contains library source intended for building other packages
which use "ivf" feature of "%{crate}" crate.

%files       -n %{name}+ivf-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+nasm-rs-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+nasm-rs-devel %{_description}

This package contains library source intended for building other packages
which use "nasm-rs" feature of "%{crate}" crate.

%files       -n %{name}+nasm-rs-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+quick_test-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+quick_test-devel %{_description}

This package contains library source intended for building other packages
which use "quick_test" feature of "%{crate}" crate.

%files       -n %{name}+quick_test-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+regex-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+regex-devel %{_description}

This package contains library source intended for building other packages
which use "regex" feature of "%{crate}" crate.

%files       -n %{name}+regex-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+scan_fmt-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+scan_fmt-devel %{_description}

This package contains library source intended for building other packages
which use "scan_fmt" feature of "%{crate}" crate.

%files       -n %{name}+scan_fmt-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+scenechange-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+scenechange-devel %{_description}

This package contains library source intended for building other packages
which use "scenechange" feature of "%{crate}" crate.

%files       -n %{name}+scenechange-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+serde-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde-devel %{_description}

This package contains library source intended for building other packages
which use "serde" feature of "%{crate}" crate.

%files       -n %{name}+serde-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+serialize-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serialize-devel %{_description}

This package contains library source intended for building other packages
which use "serialize" feature of "%{crate}" crate.

%files       -n %{name}+serialize-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+signal-hook-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+signal-hook-devel %{_description}

This package contains library source intended for building other packages
which use "signal-hook" feature of "%{crate}" crate.

%files       -n %{name}+signal-hook-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+signal_support-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+signal_support-devel %{_description}

This package contains library source intended for building other packages
which use "signal_support" feature of "%{crate}" crate.

%files       -n %{name}+signal_support-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+toml-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+toml-devel %{_description}

This package contains library source intended for building other packages
which use "toml" feature of "%{crate}" crate.

%files       -n %{name}+toml-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+tracing-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+tracing-devel %{_description}

This package contains library source intended for building other packages
which use "tracing" feature of "%{crate}" crate.

%files       -n %{name}+tracing-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+unstable-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+unstable-devel %{_description}

This package contains library source intended for building other packages
which use "unstable" feature of "%{crate}" crate.

%files       -n %{name}+unstable-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+wasm-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+wasm-devel %{_description}

This package contains library source intended for building other packages
which use "wasm" feature of "%{crate}" crate.

%files       -n %{name}+wasm-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+wasm-bindgen-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+wasm-bindgen-devel %{_description}

This package contains library source intended for building other packages
which use "wasm-bindgen" feature of "%{crate}" crate.

%files       -n %{name}+wasm-bindgen-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+y4m-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+y4m-devel %{_description}

This package contains library source intended for building other packages
which use "y4m" feature of "%{crate}" crate.

%files       -n %{name}+y4m-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%generate_buildrequires
# We need optional dependencies for cargo-c to build
%cargo_generate_buildrequires -a
echo "cargo-c"

%build
%cargo_build
cargo cbuild --release \
    --destdir=%{buildroot} \
    --prefix=%{_prefix} \
    --libdir=%{_libdir} \
    --includedir=%{_includedir} \
    --pkgconfigdir=%{_libdir}/pkgconfig

%install
%cargo_install
cargo cinstall --release \
    --destdir=%{buildroot} \
    --prefix=%{_prefix} \
    --libdir=%{_libdir} \
    --includedir=%{_includedir} \
    --pkgconfigdir=%{_libdir}/pkgconfig
rm -v %{buildroot}%{_libdir}/librav1e.a

%if %{with check}
%check
# FIXME: doctests fail to compile on aarch64
# FIXME: transform::test::roundtrips_u8 fails on aarch64 since 0.3.4
%ifarch aarch64
%cargo_test -- --lib -- --skip transform::test::roundtrips_u8
%else
%cargo_test
%endif
%endif

%changelog
* Wed Apr  7 17:07:05 CEST 2021 Robert-Andr?? Mauchin <zebob.m@gmail.com> - 0.4.1-1
- Update to 0.4.1
- Close: rhbz#1915864

* Mon Mar 29 16:18:27 CEST 2021 Robert-Andr?? Mauchin <zebob.m@gmail.com> - 0.4.0-1
- Update to 0.4.0
- Close: rhbz#1915864

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0~alpha-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec 28 13:32:03 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.4.0~alpha-0.2
- Rebuild

* Wed Dec 09 15:17:53 CET 2020 Robert-Andr?? Mauchin <zebob.m@gmail.com> - 0.4.0~alpha-0.1
- Update to 0.4.0~alpha

* Sun Dec 06 04:37:40 CET 2020 Robert-Andr?? Mauchin <zebob.m@gmail.com> - 0.3.4-3
- Rebuild with new cargo-c to fix pkgconfig includedir
- Fix: rhbz#1902211

* Tue Oct 20 2020 Fabio Valentini <decathorpe@gmail.com> - 0.3.4-2
- Temporarily skip some broken tests on aarch64.

* Tue Oct 20 2020 Fabio Valentini <decathorpe@gmail.com> - 0.3.4-1
- Update to version 0.3.4.

* Wed Aug 26 2020 Josh Stone <jistone@redhat.com> - 0.3.3-3
- Bump paste to 1.0

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 11 2020 Josh Stone <jistone@redhat.com> - 0.3.3-1
- Update to 0.3.3

* Mon Mar 09 17:45:25 CET 2020 Robert-Andr?? Mauchin <zebob.m@gmail.com> - 0.3.1-2
- Fix pkgconfig prefix path

* Thu Feb 20 21:15:47 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.3.1-1
- Update to 0.3.1

* Tue Feb 11 01:28:07 CET 2020 Robert-Andr?? Mauchin <zebob.m@gmail.com> - 0.3.0-1
- Initial package
