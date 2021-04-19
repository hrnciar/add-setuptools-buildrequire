# Generated by rust2rpm 13
# Disable the check as it has loop dependency on other rust-netlink-* packages.
%bcond_with check
%global debug_package %{nil}

%global crate rtnetlink

Name:           rust-%{crate}
Version:        0.5.0
Release:        2%{?dist}
Summary:        Manipulate linux networking resources via netlink

# Upstream license specification: MIT
# Pull request https://github.com/little-dude/netlink/pull/96 will
# include LICENSE file in crate
License:        MIT
URL:            https://crates.io/crates/rtnetlink
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Manipulate linux networking resources via netlink.}

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
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Oct 10 2020 Gris Ge <fge@redhat.com> - 0.5.0-1
- Upgrade to 0.5.0

* Wed Aug 26 2020 Gris Ge <fge@redhat.com> - 0.4.0-1
- Upgrade to 0.4.0

* Tue Jul 07 16:24:32 CST 2020 Gris Ge <cnfourt@gmail.com> - 0.3.0-1
- Initial package
