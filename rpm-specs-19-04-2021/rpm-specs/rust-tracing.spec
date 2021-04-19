# Generated by rust2rpm 16
%bcond_without check
%global debug_package %{nil}

%global crate tracing

Name:           rust-%{crate}
Version:        0.1.25
Release:        1%{?dist}
Summary:        Application-level tracing for Rust

# Upstream license specification: MIT
License:        MIT
URL:            https://crates.io/crates/tracing
Source:         %{crates_source}
# Initial patched metadata
# * No wasm deps
Patch0:         tracing-fix-metadata.diff

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Application-level tracing for Rust.}

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

%package     -n %{name}+async-await-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+async-await-devel %{_description}

This package contains library source intended for building other packages
which use "async-await" feature of "%{crate}" crate.

%files       -n %{name}+async-await-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+attributes-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+attributes-devel %{_description}

This package contains library source intended for building other packages
which use "attributes" feature of "%{crate}" crate.

%files       -n %{name}+attributes-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+log-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+log-devel %{_description}

This package contains library source intended for building other packages
which use "log" feature of "%{crate}" crate.

%files       -n %{name}+log-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+log-always-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+log-always-devel %{_description}

This package contains library source intended for building other packages
which use "log-always" feature of "%{crate}" crate.

%files       -n %{name}+log-always-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+max_level_debug-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+max_level_debug-devel %{_description}

This package contains library source intended for building other packages
which use "max_level_debug" feature of "%{crate}" crate.

%files       -n %{name}+max_level_debug-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+max_level_error-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+max_level_error-devel %{_description}

This package contains library source intended for building other packages
which use "max_level_error" feature of "%{crate}" crate.

%files       -n %{name}+max_level_error-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+max_level_info-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+max_level_info-devel %{_description}

This package contains library source intended for building other packages
which use "max_level_info" feature of "%{crate}" crate.

%files       -n %{name}+max_level_info-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+max_level_off-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+max_level_off-devel %{_description}

This package contains library source intended for building other packages
which use "max_level_off" feature of "%{crate}" crate.

%files       -n %{name}+max_level_off-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+max_level_trace-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+max_level_trace-devel %{_description}

This package contains library source intended for building other packages
which use "max_level_trace" feature of "%{crate}" crate.

%files       -n %{name}+max_level_trace-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+max_level_warn-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+max_level_warn-devel %{_description}

This package contains library source intended for building other packages
which use "max_level_warn" feature of "%{crate}" crate.

%files       -n %{name}+max_level_warn-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+release_max_level_debug-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+release_max_level_debug-devel %{_description}

This package contains library source intended for building other packages
which use "release_max_level_debug" feature of "%{crate}" crate.

%files       -n %{name}+release_max_level_debug-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+release_max_level_error-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+release_max_level_error-devel %{_description}

This package contains library source intended for building other packages
which use "release_max_level_error" feature of "%{crate}" crate.

%files       -n %{name}+release_max_level_error-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+release_max_level_info-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+release_max_level_info-devel %{_description}

This package contains library source intended for building other packages
which use "release_max_level_info" feature of "%{crate}" crate.

%files       -n %{name}+release_max_level_info-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+release_max_level_off-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+release_max_level_off-devel %{_description}

This package contains library source intended for building other packages
which use "release_max_level_off" feature of "%{crate}" crate.

%files       -n %{name}+release_max_level_off-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+release_max_level_trace-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+release_max_level_trace-devel %{_description}

This package contains library source intended for building other packages
which use "release_max_level_trace" feature of "%{crate}" crate.

%files       -n %{name}+release_max_level_trace-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+release_max_level_warn-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+release_max_level_warn-devel %{_description}

This package contains library source intended for building other packages
which use "release_max_level_warn" feature of "%{crate}" crate.

%files       -n %{name}+release_max_level_warn-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+std-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+std-devel %{_description}

This package contains library source intended for building other packages
which use "std" feature of "%{crate}" crate.

%files       -n %{name}+std-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+tracing-attributes-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+tracing-attributes-devel %{_description}

This package contains library source intended for building other packages
which use "tracing-attributes" feature of "%{crate}" crate.

%files       -n %{name}+tracing-attributes-devel
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
* Sat Feb 27 2021 Fabio Valentini <decathorpe@gmail.com> - 0.1.25-1
- Update to version 0.1.25.

* Sun Feb 07 2021 Fabio Valentini <decathorpe@gmail.com> - 0.1.23-1
- Update to version 0.1.23.
- Fixes RHBZ#1925331

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Nov 27 2020 Fabio Valentini <decathorpe@gmail.com> - 0.1.22-1
- Update to version 0.1.22.
- Fixes RHBZ#1900911

* Thu Oct 01 2020 Fabio Valentini <decathorpe@gmail.com> - 0.1.21-1
- Update to version 0.1.21.

* Tue Aug 25 2020 Josh Stone <jistone@redhat.com> - 0.1.19-1
- Update to 0.1.19

* Thu Jul 23 2020 Josh Stone <jistone@redhat.com> - 0.1.17-1
- Initial package
