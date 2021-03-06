# Generated by rust2rpm
# * Tests are run in infrastructure
%bcond_with check
%global debug_package %{nil}

%global crate edit-distance

Name:           rust-%{crate}
Version:        2.1.0
Release:        6%{?dist}
Summary:        Levenshtein edit distance between strings, a measure for similarity

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            https://crates.io/crates/edit-distance
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-packaging
%if %{with check}
BuildRequires:  (crate(quickcheck/default) >= 0.0.0 with crate(quickcheck/default) < 1.0.0)
%endif

%global _description \
Levenshtein edit distance between strings, a measure for similarity.

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
%{cargo_registry}/%{crate}-%{version}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
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
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 04 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.1.0-1
- Update to 2.1.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 30 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.0.1-6
- Adapt to new packaging

* Mon Sep 10 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.0.1-5
- Bump quickcheck to 0.7

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 08 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.0.1-2
- Rebuild for rust-packaging v5

* Thu Jan 04 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.0.1-1
- Update to 2.0.1

* Mon Jan 01 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.0.0-3
- Bump quickcheck to 0.6

* Sat Dec 02 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.0.0-2
- Bump quickcheck to 0.5

* Wed Nov 29 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.0.0-1
- Initial package
