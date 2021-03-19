# Generated by rust2rpm 17
%bcond_without check
%global __cargo_skip_build 0

%global crate gitui

Name:           rust-%{crate}
Version:        0.11.0
Release:        4%{?dist}
Summary:        Blazing fast terminal-ui for git

# Upstream license specification: MIT
License:        MIT
URL:            https://crates.io/crates/gitui
Source:         %{crates_source}
# Initial patched metadata
# * Update tui to 0.14, https://github.com/extrawurst/gitui/commit/2481be7a8706c491fca3cc2dfaae5a42ef9b48ac
Patch0:         gitui-fix-metadata.diff

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-packaging

%global _description %{expand:
Blazing fast terminal-ui for git.}

%description %{_description}

%package     -n %{crate}
Summary:        %{summary}
# 0BSD or MIT or ASL 2.0
# ASL 2.0
# BSD
# MIT
# MIT or ASL 2.0
# MIT or ASL 2.0 or zlib
License:        MIT and ASL 2.0 and BSD

%description -n %{crate} %{_description}

%files       -n %{crate}
%license LICENSE.md
%doc README.md THEMES.md CHANGELOG.md
%{_bindir}/gitui

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
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 10 20:05:32 CET 2021 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.11.0-1
- Update tui to 0.14

* Tue Dec 29 14:21:55 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.11.0-2
- Rebuild against libgit2 1.1.x

* Sun Dec 27 14:37:33 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.11.0-1
- Update to 0.11.0

* Sat Aug 29 19:32:52 CEST 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.10.0-1
- Update to 0.10.0

* Sat Aug 29 19:28:07 CEST 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.9.1-1
- Update to 0.9.1

* Tue Aug 18 15:04:08 CEST 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.9.0-1
- Update to 0.9.0

* Sun Aug 16 15:01:29 GMT 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.8.1-4
- Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Josh Stone <jistone@redhat.com> - 0.8.1-1
- Update to 0.8.1

* Mon Jul 06 16:30:46 CEST 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.8.0-1
- Update to 0.8.0

* Mon Jun 15 12:44:06 CEST 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.7.0-1
- Update to 0.7.0

* Wed Jun 10 2020 Josh Stone <jistone@redhat.com> - 0.6.0-1
- Update to 0.6.0

* Mon Jun 01 2020 Josh Stone <jistone@redhat.com> - 0.5.0-1
- Update to 0.5.0

* Thu May 28 16:14:15 CEST 2020 Igor Raits <i.gnatenko.brain@gmail.com> - 0.4.0-1
- Initial package
