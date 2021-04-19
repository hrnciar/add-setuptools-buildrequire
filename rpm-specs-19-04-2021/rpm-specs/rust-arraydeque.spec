# Generated by rust2rpm 16
%bcond_without check
%global debug_package %{nil}

%global crate arraydeque

Name:           rust-%{crate}
Version:        0.4.5
Release:        7%{?dist}
Summary:        Ring buffer with a fixed capacity, which can be stored on the stack

# Upstream license specification: MIT/Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/arraydeque
Source:         %{crates_source}
# Initial patched metadata
# * Bump generic-array to 0.14
Patch0:         arraydeque-fix-metadata.diff

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Ring buffer with a fixed capacity, which can be stored on the stack.}

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

%package     -n %{name}+generic-array-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+generic-array-devel %{_description}

This package contains library source intended for building other packages
which use "generic-array" feature of "%{crate}" crate.

%files       -n %{name}+generic-array-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+std-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+std-devel %{_description}

This package contains library source intended for building other packages
which use "std" feature of "%{crate}" crate.

%files       -n %{name}+std-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+use_generic_array-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+use_generic_array-devel %{_description}

This package contains library source intended for building other packages
which use "use_generic_array" feature of "%{crate}" crate.

%files       -n %{name}+use_generic_array-devel
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
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Nov 20 2020 Fabio Valentini <decathorpe@gmail.com> - 0.4.5-6
- Bump generic-array to 0.14

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Feb 20 2020 Josh Stone <jistone@redhat.com> - 0.4.5-4
- Bump generic-array to 0.13

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Mar 24 19:59:23 CET 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.5-1
- Update to 0.4.5

* Wed Mar 20 15:06:35 CET 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.4-1
- Initial package
