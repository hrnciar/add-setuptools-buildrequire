# Generated by rust2rpm 16
%bcond_without check
%global debug_package %{nil}

%global crate minify-html

Name:           rust-%{crate}
Version:        0.3.10
Release:        3%{?dist}
Summary:        Fast and smart HTML + JS minifier

# Upstream license specification: MIT
License:        MIT
URL:            https://crates.io/crates/minify-html
Source:         %{crates_source}
# Initial patched metadata
# * Strip unwanted dependencies
Patch0:         minify-html-fix-metadata.diff

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Fast and smart HTML + JS minifier.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE
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
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec 28 11:31:10 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.3.10-2
- No JS dependencies

* Fri Dec 25 10:52:30 CET 2020 Igor Raits <igor.raits@gmail.com> - 0.3.10-1
- Initial package
