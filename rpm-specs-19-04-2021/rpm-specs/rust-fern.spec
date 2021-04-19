# Generated by rust2rpm 16
%bcond_without check
%global debug_package %{nil}

%global crate fern

Name:           rust-%{crate}
Version:        0.6.0
Release:        5%{?dist}
Summary:        Simple, efficient logging

# Upstream license specification: MIT
License:        MIT
URL:            https://crates.io/crates/fern
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Simple, efficient logging.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE
%doc CHANGELOG.md CONTRIBUTING.md README.md
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+chrono-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+chrono-devel %{_description}

This package contains library source intended for building other packages
which use "chrono" feature of "%{crate}" crate.

%files       -n %{name}+chrono-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+colored-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+colored-devel %{_description}

This package contains library source intended for building other packages
which use "colored" feature of "%{crate}" crate.

%files       -n %{name}+colored-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+date-based-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+date-based-devel %{_description}

This package contains library source intended for building other packages
which use "date-based" feature of "%{crate}" crate.

%files       -n %{name}+date-based-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+libc-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+libc-devel %{_description}

This package contains library source intended for building other packages
which use "libc" feature of "%{crate}" crate.

%files       -n %{name}+libc-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+meta-logging-in-format-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+meta-logging-in-format-devel %{_description}

This package contains library source intended for building other packages
which use "meta-logging-in-format" feature of "%{crate}" crate.

%files       -n %{name}+meta-logging-in-format-devel
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
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec 28 13:30:09 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.6.0-4
- Rebuild

* Sat Nov 28 2020 Fabio Valentini <decathorpe@gmail.com> - 0.6.0-3
- Remove features with missing dependencies (reopen, syslog).

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon May 11 08:01:54 CEST 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.6.0-1
- Update to 0.6.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 12 17:38:50 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.5.9-1
- Initial package
