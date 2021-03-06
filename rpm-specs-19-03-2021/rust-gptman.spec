# Generated by rust2rpm 13
%bcond_without check
%global debug_package %{nil}

%global crate gptman

Name:           rust-%{crate}
Version:        0.7.3
Release:        2%{?dist}
Summary:        GPT manager that allows you to copy partitions from one disk to another

# Upstream license specification: MIT or ASL 2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/gptman
Source:         %{crates_source}
# Disable CLI binary; we only ship the library
Patch0:         disable-cli.patch

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
GPT manager that allows you to copy partitions from one disk to another.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE.Apache-2.0 LICENSE.MIT
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

%package     -n %{name}+nix-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+nix-devel %{_description}

This package contains library source intended for building other packages
which use "nix" feature of "%{crate}" crate.

%files       -n %{name}+nix-devel
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
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Dec 23 2020 Benjamin Gilbert <bgilbert@redhat.com> - 0.7.3-1
- New release
- Update license to add ASL 2.0 option
- Build with nix 0.18

* Tue Aug 25 2020 Benjamin Gilbert <bgilbert@redhat.com> - 0.7.0-1
- New release

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 15 2020 Benjamin Gilbert <bgilbert@redhat.com> - 0.6.3-1
- Initial package
