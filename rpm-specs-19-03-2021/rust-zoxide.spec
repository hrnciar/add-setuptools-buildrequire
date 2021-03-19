# Generated by rust2rpm 17
%bcond_without check
%global __cargo_skip_build 0

%global crate zoxide

Name:           rust-%{crate}
Version:        0.5.0
Release:        2%{?dist}
Summary:        Faster way to navigate your filesystem

# Upstream license specification: MIT
License:        MIT
URL:            https://crates.io/crates/zoxide
Source:         %{crates_source}
# Initial patched metadata
# * Update dirs-next to 2, upstreamed
Patch0:         zoxide-fix-metadata.diff

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-packaging

%global _description %{expand:
Faster way to navigate your filesystem.}

%description %{_description}

%package     -n %{crate}
Summary:        %{summary}
# CC0
# MIT
# MIT or ASL 2.0
# Unlicense or MIT
License:        MIT and CC0
# For interactive mode
Recommends:     fzf

%description -n %{crate} %{_description}

%files       -n %{crate}
%license LICENSE
%doc README.md CHANGELOG.md
%{_bindir}/zoxide

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires
%if %{with check}
echo '/usr/bin/bash'
echo '/usr/bin/fish'
echo '/usr/bin/shellcheck'
echo '/usr/bin/xonsh'
echo '/usr/bin/zsh'
%endif

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test -- -- --skip shell::tests::test_pwsh --skip shell::tests::test_shfmt_bash --skip shell::tests::test_shfmt_posix
%endif

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec 29 17:14:03 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.5.0-1
- Update to 0.5.0 (Fixes: RHBZ#1893357)

* Mon Dec 28 13:34:03 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.4.3-2
- Rebuild

* Wed Aug 26 2020 Josh Stone <jistone@redhat.com> - 0.4.3-1
- Update to 0.4.3

* Sun Aug 16 15:02:00 GMT 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.4.1-4
- Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun 07 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.4.1-2
- Recommends: fzf

* Mon May 25 07:37:22 CEST 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.4.1-1
- Update to 0.4.1

* Thu May 14 15:19:09 CEST 2020 Igor Raits <i.gnatenko.brain@gmail.com> - 0.4.0-1
- Initial package
