# Generated by rust2rpm
%bcond_with check
%global debug_package %{nil}

%global crate quickersort

Name:           rust-%{crate}
Version:        3.0.1
Release:        10%{?dist}
Summary:        Fast sorting compatible with stable Rust

# Upstream license specification: MIT / Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/quickersort
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-packaging
BuildRequires:  (crate(nodrop/default) >= 0.1.0 with crate(nodrop/default) < 0.2.0)
BuildRequires:  (crate(unreachable) >= 1.0.0 with crate(unreachable) < 2.0.0)
%if %{with check}
BuildRequires:  (crate(itertools/default) >= 0.7.0 with crate(itertools/default) < 0.8.0)
BuildRequires:  (crate(num-traits/default) >= 0.1.0 with crate(num-traits/default) < 0.2.0)
BuildRequires:  (crate(rand/default) >= 0.4.0 with crate(rand/default) < 0.5.0)
%endif

%global _description \
Fast sorting compatible with stable Rust.\
Also has (optional) support for\
efficient and robust sorting of floating point numbers.

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE
%doc CHANGELOG.md perf.txt README.md
%{cargo_registry}/%{crate}-%{version}/
%exclude %{cargo_registry}/%{crate}-%{version}/bors.toml

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+assert_working_compare-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+assert_working_compare-devel %{_description}

This package contains library source intended for building other packages
which use "assert_working_compare" feature of "%{crate}" crate.

%files       -n %{name}+assert_working_compare-devel
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
%autosetup -n %{crate}-%{version_no_tilde} -p1
grep -IUlr $'\r' | xargs sed -i 's/\r$//'
%cargo_prep

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Mar 09 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.0.1-6
- Adapt to new packaging

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 28 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.0.1-4
- Rebuild to trigger tests

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 31 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.0.1-1
- Update to 3.0.1

* Mon Jan 08 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.0.0-2
- Rebuild for rust-packaging v5

* Sat Jan 06 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.0.0-1
- Initial package
