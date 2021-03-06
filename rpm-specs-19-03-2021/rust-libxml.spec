# Generated by rust2rpm 16
# https://github.com/KWARC/rust-libxml/issues/73
%if 0%{?__isa_bits} == 64
%bcond_without check
%else
%bcond_with check
%endif
%global debug_package %{nil}

%global crate libxml

Name:           rust-%{crate}
Version:        0.2.16
Release:        1%{?dist}
Summary:        Rust wrapper for libxml2

# Upstream license specification: MIT
License:        MIT
URL:            https://crates.io/crates/libxml
Source:         %{crates_source}
# Initial patched metadata
# * No macos deps
# * No windows deps
Patch0:         libxml-fix-metadata.diff

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Rust wrapper for libxml2 - the XML C parser and toolkit developed for the Gnome
project.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       pkgconfig(libxml-2.0)

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

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires
echo 'pkgconfig(libxml-2.0)'

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
* Mon Feb 15 2021 Fabio Valentini <decathorpe@gmail.com> - 0.2.16-1
- Update to version 0.2.16.
- Fixes RHBZ#1922874

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Oct 01 2020 Fabio Valentini <decathorpe@gmail.com> - 0.2.15-1
- Update to version 0.2.15.

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 12 16:35:46 CEST 2020 Igor Raits <i.gnatenko.brain@gmail.com> - 0.2.14-1
- Initial package
