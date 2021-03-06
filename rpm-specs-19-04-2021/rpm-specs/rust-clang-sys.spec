# Generated by rust2rpm 16
%bcond_without check
%global debug_package %{nil}

%global crate clang-sys

Name:           rust-%{crate}
Version:        1.1.1
Release:        1%{?dist}
Summary:        Rust bindings for libclang

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            https://crates.io/crates/clang-sys
Source:         %{crates_source}
# Initial patched metadata
# * Exclude unneeded files
Patch0:         clang-sys-fix-metadata.diff

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Rust bindings for libclang.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE.txt
%doc README.md CHANGELOG.md
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       clang-devel >= 3.5

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+clang_10_0-devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       clang-devel >= 10.0

%description -n %{name}+clang_10_0-devel %{_description}

This package contains library source intended for building other packages
which use "clang_10_0" feature of "%{crate}" crate.

%files       -n %{name}+clang_10_0-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+clang_11_0-devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       clang-devel >= 11.0

%description -n %{name}+clang_11_0-devel %{_description}

This package contains library source intended for building other packages
which use "clang_11_0" feature of "%{crate}" crate.

%files       -n %{name}+clang_11_0-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+clang_3_5-devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       clang-devel >= 3.5

%description -n %{name}+clang_3_5-devel %{_description}

This package contains library source intended for building other packages
which use "clang_3_5" feature of "%{crate}" crate.

%files       -n %{name}+clang_3_5-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+clang_3_6-devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       clang-devel >= 3.6

%description -n %{name}+clang_3_6-devel %{_description}

This package contains library source intended for building other packages
which use "clang_3_6" feature of "%{crate}" crate.

%files       -n %{name}+clang_3_6-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+clang_3_7-devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       clang-devel >= 3.7

%description -n %{name}+clang_3_7-devel %{_description}

This package contains library source intended for building other packages
which use "clang_3_7" feature of "%{crate}" crate.

%files       -n %{name}+clang_3_7-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+clang_3_8-devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       clang-devel >= 3.8

%description -n %{name}+clang_3_8-devel %{_description}

This package contains library source intended for building other packages
which use "clang_3_8" feature of "%{crate}" crate.

%files       -n %{name}+clang_3_8-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+clang_3_9-devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       clang-devel >= 3.9

%description -n %{name}+clang_3_9-devel %{_description}

This package contains library source intended for building other packages
which use "clang_3_9" feature of "%{crate}" crate.

%files       -n %{name}+clang_3_9-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+clang_4_0-devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       clang-devel >= 4.0

%description -n %{name}+clang_4_0-devel %{_description}

This package contains library source intended for building other packages
which use "clang_4_0" feature of "%{crate}" crate.

%files       -n %{name}+clang_4_0-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+clang_5_0-devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       clang-devel >= 5.0

%description -n %{name}+clang_5_0-devel %{_description}

This package contains library source intended for building other packages
which use "clang_5_0" feature of "%{crate}" crate.

%files       -n %{name}+clang_5_0-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+clang_6_0-devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       clang-devel >= 6.0

%description -n %{name}+clang_6_0-devel %{_description}

This package contains library source intended for building other packages
which use "clang_6_0" feature of "%{crate}" crate.

%files       -n %{name}+clang_6_0-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+clang_7_0-devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       clang-devel >= 7.0

%description -n %{name}+clang_7_0-devel %{_description}

This package contains library source intended for building other packages
which use "clang_7_0" feature of "%{crate}" crate.

%files       -n %{name}+clang_7_0-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+clang_8_0-devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       clang-devel >= 8.0

%description -n %{name}+clang_8_0-devel %{_description}

This package contains library source intended for building other packages
which use "clang_8_0" feature of "%{crate}" crate.

%files       -n %{name}+clang_8_0-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+clang_9_0-devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       clang-devel >= 9.0

%description -n %{name}+clang_9_0-devel %{_description}

This package contains library source intended for building other packages
which use "clang_9_0" feature of "%{crate}" crate.

%files       -n %{name}+clang_9_0-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+libloading-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+libloading-devel %{_description}

This package contains library source intended for building other packages
which use "libloading" feature of "%{crate}" crate.

%files       -n %{name}+libloading-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+runtime-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+runtime-devel %{_description}

This package contains library source intended for building other packages
which use "runtime" feature of "%{crate}" crate.

%files       -n %{name}+runtime-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+static-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+static-devel %{_description}

This package contains library source intended for building other packages
which use "static" feature of "%{crate}" crate.

%files       -n %{name}+static-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires
echo 'clang-devel >= 3.5'

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
* Wed Mar 03 2021 Fabio Valentini <decathorpe@gmail.com> - 1.1.1-1
- Update to version 1.1.1.

* Wed Feb 10 2021 Fabio Valentini <decathorpe@gmail.com> - 1.1.0-1
- Update to version 1.1.0.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Nov 27 2020 Fabio Valentini <decathorpe@gmail.com> - 1.0.3-1
- Update to version 1.0.3.

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.29.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri May 29 2020 Josh Stone <jistone@redhat.com> - 0.29.3-2
- Bump to libloading 0.6

* Wed Apr 01 2020 Josh Stone <jistone@redhat.com> - 0.29.3-1
- Update to 0.29.3

* Wed Mar 11 2020 Josh Stone <jistone@redhat.com> - 0.29.2-2
- Rebuild

* Tue Mar 10 2020 Josh Stone <jistone@redhat.com> - 0.29.2-1
- Update to 0.29.2

* Fri Mar 06 2020 Josh Stone <jistone@redhat.com> - 0.29.1-1
- Update to 0.29.1

* Thu Mar 05 2020 Josh Stone <jistone@redhat.com> - 0.29.0-1
- Update to 0.29.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.28.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Nov 23 2019 Josh Stone <jistone@redhat.com> - 0.28.1-1
- Update to 0.28.1

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.28.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 07 14:21:57 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.28.0-2
- Update glob to 0.3

* Sat Mar 16 2019 Robert-Andr?? Mauchin <zebob.m@gmail.com> - 0.28.0-1
- Update to 0.28.0 (#1678018)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.27.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 22 2019 Josh Stone <jistone@redhat.com> - 0.27.0-1
- Update to 0.27.0

* Mon Jan 07 2019 Josh Stone <jistone@redhat.com> - 0.26.4-1
- Update to 0.26.4

* Wed Nov 14 2018 Josh Stone <jistone@redhat.com> - 0.26.3-1
- Update to 0.26.3

* Sun Nov 04 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.26.2-1
- Update to 0.26.2

* Thu Oct 11 2018 Josh Stone <jistone@redhat.com> - 0.26.1-1
- Update to 0.26.1

* Mon Oct 08 2018 Josh Stone <jistone@redhat.com> - 0.26.0-1
- Update to 0.26.0

* Thu Oct 04 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.24.0-1
- Initial package
