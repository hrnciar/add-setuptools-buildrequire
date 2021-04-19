# Generated by rust2rpm 13
# We don't want to package conduit
%bcond_with check
%global debug_package %{nil}

%global crate git2-curl

Name:           rust-%{crate}
Version:        0.14.1
Release:        2%{?dist}
Summary:        Backend for an HTTP transport in libgit2 powered by libcurl

# Upstream license specification: MIT/Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/git2-curl
Source:         %{crates_source}
# Initial patched metadata
# * No zlib-ng feature
Patch0:         git2-curl-fix-metadata.diff

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Backend for an HTTP transport in libgit2 powered by libcurl.
Intended to be used with the git2 crate.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-MIT LICENSE-APACHE
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
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Aug 20 2020 Josh Stone <jistone@redhat.com> - 0.14.1-1
- Update to 0.14.1

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Mar 19 11:04:04 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.14.0-1
- Update to 0.14.0

* Tue Mar 03 2020 Josh Stone <jistone@redhat.com> - 0.13.0-1
- Update to 0.13.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Dec 25 18:11:49 CET 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.12.0-1
- Update to 0.12.0

* Sat Dec 07 2019 Josh Stone <jistone@redhat.com> - 0.11.0-1
- Update to 0.11.0

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 07 2019 Josh Stone <jistone@redhat.com> - 0.10.0-1
- Update to 0.10.0

* Sun Feb 10 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.9.0-1
- Update to 0.9.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Nov 12 2018 Josh Stone <jistone@redhat.com> - 0.8.2-2
- Adapt to new packaging

* Thu Oct 11 2018 Josh Stone <jistone@redhat.com> - 0.8.2-1
- Update to 0.8.2

* Sun Jul 22 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.8.1-1
- Initial package