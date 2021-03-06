# Generated by rust2rpm
%bcond_with check
%global debug_package %{nil}

%global crate google-drive3-fork

Name:           rust-%{crate}
Version:        1.0.10
Release:        9%{?dist}
Summary:        Fork of Sebastian Thiel's complete library to interact with drive (protocol v3)

License:        MIT
URL:            https://crates.io/crates/google-drive3-fork
Source:         %{crates_source}
# Initial patched metadata
# * Bump url to 1
# * hyper-rustls → hyper-native-tls
Patch0:         google-drive3-fork-fix-metadata.diff

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-packaging
BuildRequires:  (crate(hyper/default) >= 0.10.0 with crate(hyper/default) < 0.11.0)
BuildRequires:  (crate(mime/default) >= 0.2.0 with crate(mime/default) < 0.3.0)
BuildRequires:  (crate(serde/default) >= 1.0.0 with crate(serde/default) < 2.0.0)
BuildRequires:  (crate(serde_derive/default) >= 1.0.0 with crate(serde_derive/default) < 2.0.0)
BuildRequires:  (crate(serde_json/default) >= 1.0.0 with crate(serde_json/default) < 2.0.0)
BuildRequires:  (crate(url/default) >= 1.0.0 with crate(url/default) < 2.0.0)
BuildRequires:  (crate(yup-oauth2/default) >= 1.0.0 with crate(yup-oauth2/default) < 2.0.0)
%if %{with check}
BuildRequires:  (crate(hyper-native-tls/default) >= 0.3.0 with crate(hyper-native-tls/default) < 0.4.0)
%endif

%global _description \
A fork of Sebastian Thiel's complete library to interact with drive (protocol\
v3).

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE.md
%doc README.md
%{cargo_registry}/%{crate}-%{version}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep
# Fix everything hard
find -type f -exec sed -r -i \
  -e "s/&url::form_urlencoded::serialize\(([^)]+)\)/url::form_urlencoded::Serializer::new(String::new()).extend_pairs(\1).finish().as_str()/" \
  -e "s/(extern crate hyper)_rustls/\1_native_tls/;s/hyper_rustls::TlsClient::new\(\)/hyper_native_tls::NativeTlsClient::new().unwrap()/" \
  -e "s/(extern crate google_drive3)( as drive3)/\1_fork\2/" \
  "{}" \+

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.10-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.10-8
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Nov 27 2018 Josh Stone <jistone@redhat.com> - 1.0.10-3
- Adapt to new packaging

* Thu Oct 11 2018 Josh Stone <jistone@redhat.com> - 1.0.10-2
- Bump to hyper-native-tls 0.3

* Thu Jul 26 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.10-1
- Initial package
