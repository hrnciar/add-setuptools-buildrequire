# Generated by rust2rpm 16
%bcond_without check
%global debug_package %{nil}

%global crate uuid

Name:           rust-%{crate}
Version:        0.8.2
Release:        2%{?dist}
Summary:        Library to generate and parse UUIDs

# Upstream license specification: Apache-2.0 OR MIT
License:        ASL 2.0 or MIT
URL:            https://crates.io/crates/uuid
Source:         %{crates_source}
# Initial patched metadata
# * No windows
Patch0:         uuid-fix-metadata.diff

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Library to generate and parse UUIDs.}

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

%package     -n %{name}+getrandom-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+getrandom-devel %{_description}

This package contains library source intended for building other packages
which use "getrandom" feature of "%{crate}" crate.

%files       -n %{name}+getrandom-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+md5-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+md5-devel %{_description}

This package contains library source intended for building other packages
which use "md5" feature of "%{crate}" crate.

%files       -n %{name}+md5-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+serde-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde-devel %{_description}

This package contains library source intended for building other packages
which use "serde" feature of "%{crate}" crate.

%files       -n %{name}+serde-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+sha1-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+sha1-devel %{_description}

This package contains library source intended for building other packages
which use "sha1" feature of "%{crate}" crate.

%files       -n %{name}+sha1-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+slog-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+slog-devel %{_description}

This package contains library source intended for building other packages
which use "slog" feature of "%{crate}" crate.

%files       -n %{name}+slog-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+std-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+std-devel %{_description}

This package contains library source intended for building other packages
which use "std" feature of "%{crate}" crate.

%files       -n %{name}+std-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+v1-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+v1-devel %{_description}

This package contains library source intended for building other packages
which use "v1" feature of "%{crate}" crate.

%files       -n %{name}+v1-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+v3-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+v3-devel %{_description}

This package contains library source intended for building other packages
which use "v3" feature of "%{crate}" crate.

%files       -n %{name}+v3-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+v4-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+v4-devel %{_description}

This package contains library source intended for building other packages
which use "v4" feature of "%{crate}" crate.

%files       -n %{name}+v4-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+v5-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+v5-devel %{_description}

This package contains library source intended for building other packages
which use "v5" feature of "%{crate}" crate.

%files       -n %{name}+v5-devel
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
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 11 2021 Fabio Valentini <decathorpe@gmail.com> - 0.8.2-1
- Update to version 0.8.2.
- Fixes RHBZ#1914753

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 16 2020 Josh Stone <jistone@redhat.com> - 0.8.1-2
- Bump to md5 0.7

* Thu Jan 16 2020 Josh Stone <jistone@redhat.com> - 0.8.1-1
- Update to 0.8.1

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun 22 10:18:57 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.7.4-2
- Regenerate

* Fri Mar 29 15:50:41 CET 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.7.4-1
- Update to 0.7.4

* Mon Mar 25 08:29:16 CET 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.7.3-1
- Update to 0.7.3

* Sun Mar 10 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.7.2-3
- Do not pull optional dependencies

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 29 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.7.2-1
- Update to 0.7.2

* Tue Dec 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.7.1-3
- Bump rand, md5 to 0.6

* Sat Dec 08 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.7.1-2
- Run tests in infrastructure

* Tue Nov 20 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.7.1-1
- Update to 0.7.1

* Fri Nov 02 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6.5-3
- Adapt to new packaging

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri May 25 2018 Josh Stone <jistone@redhat.com> - 0.6.5-1
- Update to 0.6.5

* Thu May 24 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6.4-1
- Update to 0.6.4

* Thu Apr 26 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6.3-1
- Update to 0.6.3

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 08 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.5.1-4
- Rebuild for rust-packaging v5

* Sun Jan 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.5.1-3
- Add implicit cargo features

* Sun Dec 31 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.5.1-2
- Bump rand to 0.4
- Bump sha1 to 0.4

* Sat Dec 02 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.5.1-1
- Initial package
