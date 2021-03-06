# Generated by rust2rpm 16
%bcond_without check
%global __cargo_skip_build 0

%global crate silver

Name:           rust-%{crate}
Version:        1.1.0
Release:        14%{?dist}
Summary:        Cross-shell customizable powerline-like prompt with icons

# Upstream license specification: Unlicense
License:        Unlicense
URL:            https://crates.io/crates/silver
Source:         %{crates_source}
# Initial patched metadata
# * No Windows
# * Update git2 to 0.13, https://github.com/reujab/silver/pull/29
# * Bump to hostname 0.3, humantime 2, https://github.com/reujab/silver/pull/24
# * Drop yaml feature from clap, https://github.com/reujab/silver/pull/24
# * Update users to 0.10, https://github.com/reujab/silver/pull/32
# * Update rust-ini to 0.15, https://github.com/reujab/silver/commit/276ad67
# * Bump rust-ini to 0.16
Patch0:         silver-fix-metadata.diff
Patch1:         0001-Bump-hostname-dependency.patch
Patch2:         0002-Bump-rust-ini-dependency.patch

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-packaging

%global _description %{expand:
Cross-shell customizable powerline-like prompt with icons.}

%description %{_description}

%package     -n %{crate}
Summary:        %{summary}
# MIT
# MIT or ASL 2.0
# MIT or ASL 2.0 or zlib
License:        Unlicense and MIT

%description -n %{crate} %{_description}

%files       -n %{crate}
%license unlicense
%doc readme.md
%{_bindir}/silver

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
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec 29 14:21:55 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.1.0-13
- Rebuild against libgit2 1.1.x

* Mon Dec 28 13:32:34 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.1.0-12
- Rebuild

* Mon Nov 23 2020 Fabio Valentini <decathorpe@gmail.com> - 1.1.0-11
- Bump to rust-ini 0.16.

* Tue Sep 29 2020 Fabio Valentini <decathorpe@gmail.com> - 1.1.0-10
- Port to rust-ini 0.15.

* Sun Aug 16 15:01:43 GMT 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.1.0-9
- Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri May 22 11:37:37 CEST 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.1.0-7
- Update users to 0.10

* Wed Apr 15 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.1.0-6
- Rebuild for libgit2 1.0.0

* Thu Mar 19 11:11:28 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.1.0-5
- Update git2 to 0.13

* Tue Mar 03 2020 Josh Stone <jistone@redhat.com> - 1.1.0-4
- Bump to git2 0.12
- Bump to hostname 0.3
- Bump to humantime 2

* Sun Feb 02 20:23:45 CET 2020 Robert-Andr?? Mauchin <zebob.m@gmail.com> - 1.1.0-3
- Bump git2 to 0.11

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Sep 12 08:25:53 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.1.0-1
- Update to 1.1.0

* Sun Sep 01 20:42:10 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.8-1
- Update to 1.0.8

* Sun Jul 28 15:47:34 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.7-4
- Regenerate

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 07 2019 Josh Stone <jistone@redhat.com> - 1.0.7-2
- Bump git2 to 0.9

* Thu May 09 2019 Josh Stone <jistone@redhat.com> - 1.0.7-1
- Update to 1.0.7

* Fri Apr 26 20:18:32 CEST 2019 Robert-Andr?? Mauchin <zebob.m@gmail.com> - 1.0.5-1
- Initial package
