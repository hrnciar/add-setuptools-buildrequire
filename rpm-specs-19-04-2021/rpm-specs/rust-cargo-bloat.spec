# Generated by rust2rpm 13
%bcond_without check
%global __cargo_skip_build 0

%global crate cargo-bloat

Name:           rust-%{crate}
Version:        0.10.0
Release:        3%{?dist}
Summary:        Find out what takes most of the space in your executable

# Upstream license specification: MIT
License:        MIT
URL:            https://crates.io/crates/cargo-bloat
Source:         %{crates_source}
# Initial patched metadata
# * bump pico-args from 0.3 to 0.4
Patch0:         cargo-bloat-fix-metadata.diff
# * port to pico-args 0.4 (handle unused arguments manually)
#   (quick-'n-dirty port, not upstreamable in this form)
Patch1:         0001-qnd-port-to-pico-args-0.4.patch

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-packaging

%global _description %{expand:
Find out what takes most of the space in your executable.}

%description %{_description}

%package     -n %{crate}
Summary:        %{summary}
# Install all deps (without check), grab their licenses and make it simple
# * MIT
# * MIT or ASL 2.0
License:        MIT

%description -n %{crate} %{_description}

%files       -n %{crate}
%license LICENSE
%doc README.md CHANGELOG.md
%{_bindir}/cargo-bloat

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
* Thu Apr 08 2021 Fabio Valentini <decathorpe@gmail.com> - 0.10.0-3
- Bump pico-args from 0.3 to 0.4.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Sep 23 2020 Fabio Valentini <decathorpe@gmail.com> - 0.10.0-1
- Update to version 0.10.0.

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Apr 08 2020 Josh Stone <jistone@redhat.com> - 0.9.3-1
- Update to 0.9.3

* Sat Feb 29 13:43:58 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.9.2-1
- Update to 0.9.2

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun 22 12:12:25 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.7.1-1
- Update to 0.7.1

* Sat Jun 08 11:58:39 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.7.0-1
- Update to 0.7.0

* Sat Jun 01 21:03:33 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6.4-1
- Initial package
