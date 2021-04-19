# Generated by rust2rpm 13
%bcond_without check
%global __cargo_skip_build 0

%global crate pretty-git-prompt

Name:           rust-%{crate}
Version:        0.2.1
Release:        7%{?dist}
Summary:        Your current git repository information inside a beautiful shell prompt

# Upstream license specification: MIT
License:        MIT
URL:            https://crates.io/crates/pretty-git-prompt
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-packaging

%global _description %{expand:
Your current git repository information inside a beautiful shell prompt.}

%description %{_description}

%package     -n %{crate}
Summary:        %{summary}
# MIT
# MIT or ASL 2.0
# MIT or ASL 2.0 or zlib
License:        MIT

%description -n %{crate} %{_description}

%files       -n %{crate}
%license LICENSE
%doc README.md
%doc files
%{_bindir}/pretty-git-prompt

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
# https://github.com/tomastomecek/pretty-git-prompt/issues/35
%cargo_test || :
%endif

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec 29 14:21:55 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.2.1-6
- Rebuild against libgit2 1.1.x

* Mon Dec 28 13:31:52 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.2.1-5
- Rebuild

* Sun Aug 16 15:01:38 GMT 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.2.1-4
- Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Apr 15 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.2.1-2
- Rebuild for libgit2 1.0.0

* Wed Apr 08 2020 Josh Stone <jistone@redhat.com> - 0.2.1-1
- Update to 0.2.1

* Thu Mar 19 11:41:19 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.2.0-14
- Update git2 to 0.14

* Wed Mar 04 2020 Josh Stone <jistone@redhat.com> - 0.2.0-13
- Bump git2 to 0.12

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jul 14 12:10:39 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.0-10
- Regenerate

* Fri Jun 07 2019 Josh Stone <jistone@redhat.com> - 0.2.0-9
- Bump git2 to 0.9

* Tue Apr 02 2019 Josh Stone <jistone@redhat.com> - 0.2.0-8
- Bump git2 to 0.8

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Aug 10 2018 Josh Stone <jistone@redhat.com> - 0.2.0-6
- Rebuild with fixed rust-libgit2-sys-0.7.7

* Fri Aug 10 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.0-5
- Rebuild for libgit2 0.27.x

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Mar 12 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.0-3
- Bump git2 to 0.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 28 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.0-1
- Initial package