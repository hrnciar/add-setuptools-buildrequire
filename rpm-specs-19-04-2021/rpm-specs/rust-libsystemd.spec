# Generated by rust2rpm 16
%bcond_without check
%global debug_package %{nil}

%global crate libsystemd

Name:           rust-%{crate}
Version:        0.2.1
Release:        5%{?dist}
Summary:        Pure-Rust client library to interact with systemd

# Upstream license specification: MIT/Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/libsystemd
Source:         %{crates_source}
# Initial patched metadata
# * Update hmac to 0.8, sha2 to 0.9: https://github.com/lucab/libsystemd-rs/commit/40470ed
# Update hmac to 0.10: https://github.com/lucab/libsystemd-rs/commit/431d1d5
Patch0:         libsystemd-fix-metadata.diff
Patch0001:      0001-id128-update-to-new-hmac-API.patch

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Pure-Rust client library to interact with systemd.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license COPYRIGHT LICENSE-APACHE-2.0 LICENSE-MIT
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
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Nov 14 2020 Fabio Valentini <decathorpe@gmail.com> - 0.2.1-4
- Bump hmac from 0.8 to 0.10.

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun 21 19:00:16 CEST 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.2.1-2
- Update hmac to 0.8 and sha2 to 0.9

* Thu Apr 30 2020 Robert Fairley <rfairley@redhat.com> - 0.2.1-1
- Update to 0.2.1

* Thu Apr 23 2020 Robert Fairley <rfairley@redhat.com> - 0.2.0-1
- Update to 0.2.0
- Regenerate specfile using rust2rpm 13

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Sep 13 20:57:31 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.1.0-5
- Update quickcheck to 0.9

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 27 17:37:46 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.0-3
- Regenerate

* Mon Jun 10 12:53:00 UTC 2019 Robert Fairley <rfairley@redhat.com> - 0.1.0-2
- Add license files

* Sun Jun 09 18:06:08 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.0-1
- Initial package