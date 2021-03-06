# Generated by rust2rpm 17
%bcond_without check
%global __cargo_skip_build 0

%global crate diskonaut

Name:           rust-%{crate}
Version:        0.11.0
Release:        3%{?dist}
Summary:        Terminal disk space visual navigator

# Upstream license specification: MIT
License:        MIT
URL:            https://crates.io/crates/diskonaut
Source:         %{crates_source}
# Initial patched metadata
# * no windows dependencies
# * Update jwalk to 0.6, https://github.com/imsnif/diskonaut/pull/83
Patch0:         diskonaut-fix-metadata.diff

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-packaging

%global _description %{expand:
Terminal disk space visual navigator.}

%description %{_description}

%package     -n %{crate}
Summary:        %{summary}
# 0BSD or MIT or ASL 2.0
# BSD
# MIT
# MIT or ASL 2.0
# MIT or zlib or ASL 2.0
License:        MIT and BSD

%description -n %{crate} %{_description}

%files       -n %{crate}
%license LICENSE
%doc README.md CHANGELOG.md
%{_bindir}/diskonaut

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
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 10 20:44:10 CET 2021 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.11.0-2
- Update jwalk to 0.6

* Sun Oct 25 2020 Fabio Valentini <decathorpe@gmail.com> - 0.11.0-1
- Update to version 0.11.0.

* Sat Sep 12 16:09:22 EEST 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.10.0-1
- Update 0.10.0

* Sun Aug 16 15:01:11 GMT 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.9.0-4
- Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 24 13:49:33 EEST 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.9.0-1
- Update 0.9.0

* Thu Jul 09 20:14:20 EEST 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.8.0-1
- Update 0.8.0

* Sun Jul 05 00:25:42 EEST 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.7.0-1
- Update 0.7.0

* Fri Jul 03 10:46:13 EEST 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.6.0-1
- Update 0.6.0

* Sat Jun 27 14:17:05 EEST 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.5.0-1
- Update 0.5.0

* Sun Jun 21 15:24:15 EEST 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.3.0-1
- Update 0.3.0

* Fri Jun 19 00:52:23 EEST 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.2.0-1
- Update 0.2.0

* Thu Jun 18 00:27:52 EEST 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.1.0-1
- Initial package
