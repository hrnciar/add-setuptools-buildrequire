# Generated by rust2rpm 17
# * tests depend on unreleased version of glib
%bcond_with check
%global debug_package %{nil}

%global crate zvariant

Name:           rust-%{crate}
Version:        2.5.0
Release:        1%{?dist}
Summary:        D-Bus & GVariant encoding & decoding

# Upstream license specification: MIT
License:        MIT
URL:            https://crates.io/crates/zvariant
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
D-Bus & GVariant encoding & decoding.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

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

%package     -n %{name}+arrayvec-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+arrayvec-devel %{_description}

This package contains library source intended for building other packages
which use "arrayvec" feature of "%{crate}" crate.

%files       -n %{name}+arrayvec-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+enumflags2-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+enumflags2-devel %{_description}

This package contains library source intended for building other packages
which use "enumflags2" feature of "%{crate}" crate.

%files       -n %{name}+enumflags2-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+gvariant-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+gvariant-devel %{_description}

This package contains library source intended for building other packages
which use "gvariant" feature of "%{crate}" crate.

%files       -n %{name}+gvariant-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+ostree-tests-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+ostree-tests-devel %{_description}

This package contains library source intended for building other packages
which use "ostree-tests" feature of "%{crate}" crate.

%files       -n %{name}+ostree-tests-devel
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
* Thu Mar 04 2021 Fabio Valentini <decathorpe@gmail.com> - 2.5.0-1
- Update to version 2.5.0.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan 05 22:19:10 CET 2021 Igor Raits <ignatenkobrain@fedoraproject.org> - 2.4.0-1
- Update to 2.4.0

* Mon Aug 03 00:21:30 +04 2020 Marc-André Lureau <marcandre.lureau@redhat.com> - 2.1.0-1
- Initial package, fixes rhbz#1862947