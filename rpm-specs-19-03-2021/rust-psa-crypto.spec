%bcond_without check
%global debug_package %{nil}

%global crate psa-crypto

Name:           rust-%{crate}
Version:        0.7.0
Release:        1%{?dist}
Summary:        Wrapper around the PSA Cryptography API

License:        ASL 2.0
URL:            https://crates.io/crates/psa-crypto
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Wrapper around the PSA Cryptography API.}

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

%package     -n %{name}+interface-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+interface-devel %{_description}

This package contains library source intended for building other packages
which use "interface" feature of "%{crate}" crate.

%files       -n %{name}+interface-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+no-std-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+no-std-devel %{_description}

This package contains library source intended for building other packages
which use "no-std" feature of "%{crate}" crate.

%files       -n %{name}+no-std-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+operations-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+operations-devel %{_description}

This package contains library source intended for building other packages
which use "operations" feature of "%{crate}" crate.

%files       -n %{name}+operations-devel
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
%cargo_test -- -- --test-threads=1
%endif

%changelog
* Mon Feb 15 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 0.7.0-1
- Update to 0.7.0

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Oct 21 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 0.6.0-1
- Update to 0.6.0

* Tue Sep 08 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 0.5.1-1
- Update to 0.5.1

* Tue Aug 25 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 0.5.0-1
- Update to 0.5.0

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 16 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 0.3.0-1
- Initial package
