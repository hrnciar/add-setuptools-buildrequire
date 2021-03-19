# Generated by rust2rpm 16
%bcond_without check
%global debug_package %{nil}

%global crate config

Name:           rust-%{crate}
Version:        0.10.1
Release:        5%{?dist}
Summary:        Layered configuration system for Rust applications

# Upstream license specification: MIT/Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/config
Source:         %{crates_source}
# Initial patched metadata
# * serde-hjson is not packaged
# * Update float-cmp to 0.6, https://github.com/mehcode/config-rs/pull/131
# * Update rust-ini to 0.15, https://github.com/mehcode/config-rs/pull/152
# * Bump rust-ini to 0.16
Patch0:         config-fix-metadata.diff
# adapt to small API changes between rust-ini 0.13 and 0.15
Patch1:         00-port-to-ini-0.15.patch
# adapt to error message change in recent toml
Patch2:         01-adapt-toml-error-message.patch

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Layered configuration system for Rust applications.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-MIT LICENSE-APACHE
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

%package     -n %{name}+ini-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+ini-devel %{_description}

This package contains library source intended for building other packages
which use "ini" feature of "%{crate}" crate.

%files       -n %{name}+ini-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+json-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+json-devel %{_description}

This package contains library source intended for building other packages
which use "json" feature of "%{crate}" crate.

%files       -n %{name}+json-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+rust-ini-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+rust-ini-devel %{_description}

This package contains library source intended for building other packages
which use "rust-ini" feature of "%{crate}" crate.

%files       -n %{name}+rust-ini-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+serde_json-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde_json-devel %{_description}

This package contains library source intended for building other packages
which use "serde_json" feature of "%{crate}" crate.

%files       -n %{name}+serde_json-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+toml-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+toml-devel %{_description}

This package contains library source intended for building other packages
which use "toml" feature of "%{crate}" crate.

%files       -n %{name}+toml-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+yaml-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+yaml-devel %{_description}

This package contains library source intended for building other packages
which use "yaml" feature of "%{crate}" crate.

%files       -n %{name}+yaml-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+yaml-rust-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+yaml-rust-devel %{_description}

This package contains library source intended for building other packages
which use "yaml-rust" feature of "%{crate}" crate.

%files       -n %{name}+yaml-rust-devel
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
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov 23 2020 Fabio Valentini <decathorpe@gmail.com> - 0.10.1-4
- Bump rust-ini to 0.16.

* Mon Sep 28 2020 Fabio Valentini <decathorpe@gmail.com> - 0.10.1-3
- Bump rust-ini to 0.15.

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Feb 23 10:48:06 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.10.1-1
- Update to 0.10.1

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 09 2019 Josh Stone <jistone@redhat.com> - 0.9.3-1
- Update to 0.9.3

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 08 2019 Josh Stone <jistone@redhat.com> - 0.9.2-1
- Update to 0.9.2

* Tue Nov 13 2018 Josh Stone <jistone@redhat.com> - 0.9.1-3
- Adapt to new packaging

* Sun Oct 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.9.1-2
- Run tests in infrastructure
- Bump rust-ini to 0.13

* Thu Sep 27 2018 Josh Stone <jistone@redhat.com> - 0.9.1-1
- Update to 0.9.1

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jul 06 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.9.0-1
- Initial package
