# Generated by rust2rpm 16
%bcond_without check
%global debug_package %{nil}

%global crate v_frame

Name:           rust-%{crate}
Version:        0.1.0
Release:        2%{?dist}
Summary:        Video Frame data structures, part of rav1e

# Upstream license specification: BSD-2-Clause
# https://github.com/xiph/rav1e/issues/2610
License:        BSD
URL:            https://crates.io/crates/v_frame
Source:         %{crates_source}
# Initial patched metadata
# - Bump noop_proc_macro to 0.3.0 (already upstream)
Patch0:         v_frame-fix-metadata.diff

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Video Frame data structures, part of rav1e.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
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
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Dec 10 08:55:10 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.1.0-1
- Initial package
