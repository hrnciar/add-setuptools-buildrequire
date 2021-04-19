# Generated by rust2rpm 15
%bcond_with check
%global debug_package %{nil}

%global crate url

Name:           rust-%{crate}1
Version:        1.7.2
Release:        5%{?dist}
Summary:        URL library for Rust, based on the WHATWG URL Standard

# Upstream license specification: MIT/Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/url
Source:         %{crates_source}
# Initial patched metadata
# * Exclude CI files, https://github.com/servo/rust-url/pull/467
# * drop optional + unused serde feature (serde < 1 no longer available)
Patch0:         url-fix-metadata.diff

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
URL library for Rust, based on the WHATWG URL Standard.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-MIT LICENSE-APACHE
%doc README.md UPGRADING.md
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+encoding-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+encoding-devel %{_description}

This package contains library source intended for building other packages
which use "encoding" feature of "%{crate}" crate.

%files       -n %{name}+encoding-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+heap_size-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+heap_size-devel %{_description}

This package contains library source intended for building other packages
which use "heap_size" feature of "%{crate}" crate.

%files       -n %{name}+heap_size-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+heapsize-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+heapsize-devel %{_description}

This package contains library source intended for building other packages
which use "heapsize" feature of "%{crate}" crate.

%files       -n %{name}+heapsize-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+query_encoding-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+query_encoding-devel %{_description}

This package contains library source intended for building other packages
which use "query_encoding" feature of "%{crate}" crate.

%files       -n %{name}+query_encoding-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+rustc-serialize-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+rustc-serialize-devel %{_description}

This package contains library source intended for building other packages
which use "rustc-serialize" feature of "%{crate}" crate.

%files       -n %{name}+rustc-serialize-devel
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
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Nov 08 2020 Fabio Valentini <decathorpe@gmail.com> - 1.7.2-4
- Drop optional serde feature that has missing dependencies.

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Aug 25 08:47:13 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.7.2-1
- Initial package