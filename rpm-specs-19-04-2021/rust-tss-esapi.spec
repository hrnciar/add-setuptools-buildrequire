# * Requires TPM server running
%bcond_with check
%global debug_package %{nil}

%global crate tss-esapi

Name:           rust-%{crate}
Version:        5.0.1
Release:        1%{?dist}
Summary:        Rust-native wrapper around TSS 2.0 Enhanced System API

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            https://crates.io/crates/tss-esapi
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging
BuildRequires:  pkgconfig(tss2-esys) >= 2.3.3
BuildRequires:  pkgconfig(tss2-mu) >= 2.3.3
BuildRequires:  pkgconfig(tss2-tctildr) >= 2.3.3

%global _description %{expand:
Rust-native wrapper around TSS 2.0 Enhanced System API.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       pkgconfig(tss2-esys) >= 2.3.3
Requires:       pkgconfig(tss2-mu) >= 2.3.3
Requires:       pkgconfig(tss2-tctildr) >= 2.3.3

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

%package     -n %{name}+generate-bindings-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+generate-bindings-devel %{_description}

This package contains library source intended for building other packages
which use "generate-bindings" feature of "%{crate}" crate.

%files       -n %{name}+generate-bindings-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires -a
echo 'pkgconfig(tss2-esys) >= 2.3.3'
echo 'pkgconfig(tss2-mu) >= 2.3.3'
echo 'pkgconfig(tss2-tctildr) >= 2.3.3'

%build
%cargo_build -a

%install
%cargo_install -a

%if %{with check}
%check
%cargo_test -a
%endif

%changelog
* Mon Apr 05 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 5.0.1-1
- Update to 5.0.1

* Tue Mar 23 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 5.0.0-2
- Update to 5.0.0 stable release

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.10~alpha.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 20 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 4.0.10~alpha.2-1
- Update to 4.0.10-alpha.2

* Fri Nov 27 2020 Fabio Valentini <decathorpe@gmail.com> - 4.0.10~alpha.1-2
- Bump bindgen to 0.56.

* Tue Nov 24 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 4.0.10~alpha.1-1
- Update to 4.0.10~alpha.1

* Wed Sep 16 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 4.0.9~alpha.1-1
- Update to 4.0.9~alpha.1

* Mon Sep 14 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 4.0.8~alpha.1-1
- Update to 4.0.8~alpha.1

* Wed Aug  5 2020 Peter Robinson <pbrobinson@fedoraproject.org> 4.0.6~alpha.1-1
- Update to 4.0.6~alpha.1

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.5~alpha.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 15 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 4.0.5~alpha.1-1
- Update to 4.0.5~alpha.1

* Wed Jun 17 2020 Igor Raits <i.gnatenko.brain@gmail.com> - 4.0.3~alpha.1-1
- Initial package
