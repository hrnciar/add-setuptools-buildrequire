# Generated by rust2rpm
# * Tests are run in infrastructure
%bcond_with check
%global debug_package %{nil}

%global crate heapsize

Name:           rust-%{crate}
Version:        0.4.2
Release:        11%{?dist}
Summary:        Infrastructure for measuring the total runtime size of an object on the heap

# Upstream license specification: MIT/Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/heapsize
Source0:        https://crates.io/api/v1/crates/%{crate}/%{version}/download#/%{crate}-%{version}.crate
# Initial patched metadata
# * No Windows
# * Exclude CI files, https://github.com/servo/heapsize/pull/101
Patch0:         heapsize-fix-metadata.diff

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-packaging

%global _description \
Infrastructure for measuring the total runtime size of an object on the heap.

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
%{cargo_registry}/%{crate}-%{version}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+unstable-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+unstable-devel %{_description}

This package contains library source intended for building other packages
which use "unstable" feature of "%{crate}" crate.

%files       -n %{name}+unstable-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test -f flexible-tests
%endif

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Oct 27 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.2-6
- Adapt to new packaging

* Sun Oct 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.2-5
- Run tests in infrastructure

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 23 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.2-3
- Adopt to new macro

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 29 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.2-1
- Update to 0.4.2

* Mon Jan 08 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.1-2
- Rebuild for rust-packaging v5

* Mon Nov 06 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.1-1
- Update to 0.4.1

* Thu Jun 15 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.0-1
- Update to 0.4.0

* Wed Jun 14 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.9-2
- Port to use rust-packaging

* Thu Mar 30 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.9-1
- Initial package
