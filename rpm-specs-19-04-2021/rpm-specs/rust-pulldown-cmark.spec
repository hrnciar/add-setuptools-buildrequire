# Generated by rust2rpm 16
%bcond_without check

%global crate pulldown-cmark

Name:           rust-%{crate}
Version:        0.8.0
Release:        2%{?dist}
Summary:        Pull parser for CommonMark

# Upstream license specification: MIT
License:        MIT
URL:            https://crates.io/crates/pulldown-cmark
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Pull parser for CommonMark.}

%description %{_description}

%if ! %{__cargo_skip_build}
%package     -n %{crate}
Summary:        %{summary}

%description -n %{crate} %{_description}

%files       -n %{crate}
%license LICENSE
%doc README.md CONTRIBUTING.md
%{_bindir}/pulldown-cmark
%endif

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE
%doc README.md CONTRIBUTING.md
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+gen-tests-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+gen-tests-devel %{_description}

This package contains library source intended for building other packages
which use "gen-tests" feature of "%{crate}" crate.

%files       -n %{name}+gen-tests-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+getopts-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+getopts-devel %{_description}

This package contains library source intended for building other packages
which use "getopts" feature of "%{crate}" crate.

%files       -n %{name}+getopts-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+simd-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+simd-devel %{_description}

This package contains library source intended for building other packages
which use "simd" feature of "%{crate}" crate.

%files       -n %{name}+simd-devel
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
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Dec 25 11:19:56 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.8.0-1
- Update to 0.8.0

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Josh Stone <jistone@redhat.com> - 0.7.2-1
- Update to 0.7.2

* Thu May 07 2020 Josh Stone <jistone@redhat.com> - 0.7.1-1
- Update to 0.7.1

* Sat Feb 22 19:29:22 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.7.0-1
- Update to 0.7.0

* Sat Feb 15 16:29:57 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.6.1-3
- Update html5ever to 0.25

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 19 2019 Josh Stone <jistone@redhat.com> - 0.6.1-1
- Update to 0.6.1

* Fri Sep 13 18:40:36 CEST 2019 Robert-Andr?? Mauchin <zebob.m@gmail.com> - 0.6.0-1
- Update to 0.6.0

* Sun Jul 28 18:31:45 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.5.3-1
- Update to 0.5.3

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun 22 20:31:59 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.5.2-2
- Regenerate

* Fri May 31 15:34:29 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.5.2-1
- Update to 0.5.2

* Tue May 14 15:27:10 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.5.1-1
- Update to 0.5.1

* Tue Apr 16 2019 Josh Stone <jistone@redhat.com> - 0.4.1-1
- Update to 0.4.1

* Thu Apr 04 07:55:23 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.0-1
- Update to 0.4.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 21 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.2-1
- Update to 0.1.2

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 08 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.0-2
- Rebuild for rust-packaging v5

* Mon Nov 13 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.0-1
- Initial package
