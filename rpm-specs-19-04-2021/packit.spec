%global pypi_name packitos
%global real_name packit

Name:           %{real_name}
Version:        0.28.0
Release:        1%{?dist}
Summary:        A tool for integrating upstream projects with Fedora operating system

License:        MIT
URL:            https://github.com/packit/packit
Source0:        %pypi_source
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-click-man
BuildRequires:  python3-GitPython
BuildRequires:  python3-gnupg
BuildRequires:  python3-ogr
BuildRequires:  python3-packaging
BuildRequires:  python3-pyyaml
BuildRequires:  python3-tabulate
BuildRequires:  python3-cccolutils
BuildRequires:  python3-copr
BuildRequires:  python3-koji
BuildRequires:  python3-lazy-object-proxy
BuildRequires:  python3-marshmallow
BuildRequires:  python3-marshmallow-enum
BuildRequires:  rebase-helper
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools-scm)
BuildRequires:  python3dist(setuptools-scm-git-archive)
BuildRequires:  python3-bodhi-client
# new-sources
Requires:       fedpkg
# bumpspec
Requires:       rpmdevtools
Requires:       python3-%{real_name} = %{version}-%{release}

%description
This project provides tooling and automation to integrate upstream open source
projects into Fedora operating system.

%package -n     python3-%{real_name}
Summary:        %{summary}
# See setup.cfg for details
Requires:       python3-koji
%{?python_provide:%python_provide python3-%{real_name}}

%description -n python3-%{real_name}
Python library for Packit,
check out packit package for the executable.


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install
python3 setup.py --command-packages=click_man.commands man_pages --target %{buildroot}%{_mandir}/man1

install -d -m 755 %{buildroot}%{_datadir}/bash-completion/completions
cp files/bash-completion/packit %{buildroot}%{_datadir}/bash-completion/completions/packit

%files
%license LICENSE
%{_bindir}/packit
%{_mandir}/man1/packit*.1*
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/%{real_name}
%{_bindir}/_packitpatch

%files -n python3-%{real_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/*

%changelog
* Wed Mar 31 2021 Packit Service <user-cont-team+packit-service@redhat.com> - 0.28.0-1
- Remove the no-op `--dry-run` option.
- Handle `centos-stream` targets as `centos-stream-8`, in order to help with the name change in Copr.
- `fmf_url` and `fmf_ref` can be used in a job's `metadata` to specify an external repository and reference to be used to test the package.
- Introduce a `fedora-latest` alias for the latest _branched_ version of Fedora Linux.
- Add a top-level option `-c, --config` to specify a custom path for the package configuration (aka `packit.yaml`).
- Source-git: enable using CentOS Stream 9 dist-git as a source.
- Source-git: rename the subdirectory to store downstream packaging files from `fedora` to the more general `.distro`.
- Source-git: fix creating source-git repositories when Git is configured to call the default branch something other then `master`.


* Thu Mar 18 2021 Packit Service <user-cont-team+packit-service@redhat.com> - 0.27.0-1
- (Source-git) Several improvements of history linearization.
- (Source-git) Detect identical patches in propose-downstream.
- (Source-git) Patches in a spec file are added after the first empty line below the last Patch/Source.
- Fetch all sources defined in packit.yaml.
- New option to sync only specfile from downstream.

* Thu Mar 04 2021 Packit Service <user-cont-team+packit-service@redhat.com> - 0.26.0-1
- Fix construction of the Koji tag for epel branches when running `packit create-update`. ([#1122](https://github.com/packit/packit/pull/1122))
- `create-update` now also shows a message about Bodhi requiring the password. ([#1127](https://github.com/packit/packit/pull/1127))
- `packit init` correctly picks up sources from CentOS and fetches specfile from CentOS dist-git. ([#1106](https://github.com/packit/packit/pull/1106))
- Fix translating of the target aliases by treating the highest pending version in Bodhi as `rawhide`. ([#1114](https://github.com/packit/packit/pull/1114))
- The format of Packit logs is unified for all log levels. ([#1119](https://github.com/packit/packit/pull/1119))
- There is a new configuration option `sources` which enables to define sources to override their URLs in specfile.
  You can read more about this in [our documentation](https://packit.dev/docs/configuration/#sources). ([#1131](https://github.com/packit/packit/pull/1131))

* Fri Feb 12 2021 Matej Mužila <mmuzila@redhat.com> - 0.25.0-1
- `propose-update` command now respects requested dist-git branches. ([#1094](https://github.com/packit/packit/pull/1094))
- Improve the way how patches are added to spec file. ([#1100](https://github.com/packit/packit/pull/1100))
- `--koji-target` option of the `build` command now accepts aliases. ([#1052](https://github.com/packit/packit/pull/1052))
- `propose-downstream` on source-git repositories now always uses `--local-content`. ([#1093](https://github.com/packit/packit/pull/1093))
- Don't behave as if `ref` would be always a branch. ([#1089](https://github.com/packit/packit/pull/1089))
- Detect a name of the default branch of a repository instead of assuming it to be called `master`. ([#1074](https://github.com/packit/packit/pull/1074))

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.24.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 21 2021 Packit Service <user-cont-team+packit-service@redhat.com> - 0.24.0-1
- No user-facing changes done in this release.

* Thu Jan 07 2021 Packit Service <user-cont-team+packit-service@redhat.com> - 0.23.0-1
- The `propose-update` has been renamed to `propose-downstream`; `propose-update` is now deprecated
  to unify the naming between CLI and service. ([@jpopelka](https://github.com/jpopelka), [#1065](https://github.com/packit-service/packit/pull/1065))
- Our README has been cleaned and simplified. ([@ChainYo](https://github.com/ChainYo), [#1058](https://github.com/packit-service/packit/pull/1058))
- The :champagne: comment with the installation instructions has been disabled by default. ([@mfocko](https://github.com/mfocko), [#1057](https://github.com/packit-service/packit/pull/1057))
  - More information can be found in [our documentation](https://packit.dev/docs/configuration/#notifications).
- Packit is being prepared to be released in EPEL 8 so it can be consumed in RHEL and CentOS Stream. ([@nforro](https://github.com/nforro), [#1055](https://github.com/packit-service/packit/pull/1055))

* Thu Dec 10 2020 Packit Service <user-cont-team+packit-service@redhat.com> - 0.22.0-1
- `packit init` introduces the `--upstream-url` option. When specified,
  `init` also sets up a source-git repository next to creating a configuration file.
- Don't rewrite macros when setting release and version in spec file.
- Fix generation of Copr settings URL for groups.
- Improve processing of the version when proposing a Fedora update.

* Wed Nov 25 2020 Packit Service <user-cont-team+packit-service@redhat.com> - 0.21.0-1
- pre-commit autoupdate (Jiri Popelka)
- 0.21.0 release (Release bot)
- parsing git remote URL: inform what's happening... (Tomas Tomecek)
- Revert "Allow recursive search for specfile in repository" (Matej Focko)
- Regenerate test_data for recursive (Matej Focko)
- Allow recursive search for specfile in repository (Matej Focko)
- cli.copr-build: replace / with - (Tomas Tomecek)
- copr, log CoprException.result when creating repo fails (Tomas Tomecek)
- Delete recipe-tests.yaml (Jiri Popelka)
- Add build to default jobs (lbarcziova)
- Add test case for Upstream._fix_spec_source() (Nikola Forró)
- Fix SpecFile.get_source() (Nikola Forró)

* Fri Nov 13 2020 Packit Service <user-cont-team+packit-service@redhat.com> - 0.20.0-1
- new upstream release: 0.20.0

* Thu Oct 29 2020 Packit Service <user-cont-team+packit-service@redhat.com> - 0.19.0-1
- new upstream release: 0.19.0

* Thu Oct 15 2020 Packit Service <user-cont-team+packit-service@redhat.com> - 0.18.0-1
- new upstream release: 0.18.0

* Thu Oct 01 2020 Packit Service <user-cont-team+packit-service@redhat.com> - 0.17.0-1
- new upstream release: 0.17.0

* Thu Sep 03 2020 rebase-helper <rebase-helper@localhost.local> - 0.16.0-1
- new upstream release: 0.16.0

* Thu Aug 20 2020 Packit Service <user-cont-team+packit-service@redhat.com> - 0.15.0-1
- new upstream release: 0.15.0

* Tue Jul 28 2020 Jiri Popelka <jpopelka@redhat.com> - 0.14.0-1
- new upstream release: 0.14.0

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 16 2020 Hunor Csomortáni <csomh@redhat.com> - 0.13.1-1
- new upstream release: 0.13.1

* Thu Jul 09 2020 Packit Service <user-cont-team+packit-service@redhat.com> - 0.13.0-1
- new upstream release: 0.13.0

* Wed Jun 24 2020 lbarcziova <lbarczio@redhat.com> - 0.12.0-1
- new upstream release: 0.12.0

* Thu Jun 11 2020 Jan Sakalos <sakalosj@gmail.com> - 0.11.1-1
- new upstream release: 0.11.1

* Thu May 28 2020 Miro Hrončok <mhroncok@redhat.com> - 0.11.0-2
- Rebuilt for Python 3.9

* Thu May 28 2020 Tomas Tomecek <ttomecek@redhat.com> - 0.11.0-1
- new upstream release: 0.11.0

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.10.1-2
- Rebuilt for Python 3.9

* Thu Apr 16 2020 Jiri Popelka <jpopelka@redhat.com> - 0.10.1-1
- new upstream release: 0.10.1

* Tue Apr 14 2020 Jiri Popelka <jpopelka@redhat.com> - 0.10.0-1
- new upstream release: 0.10.0

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Oct 21 2019 Frantisek Lachman <flachman@redhat.com> - 0.7.1-1
- new upstream release: 0.7.1

* Fri Oct 04 2019 Frantisek Lachman <flachman@redhat.com> - 0.7.0-1
- new upstream release: 0.7.0

* Thu Sep 12 2019 Jiri Popelka <jpopelka@redhat.com> - 0.6.1-1
- new upstream release: 0.6.1

* Tue Sep 10 2019 Tomas Tomecek <ttomecek@redhat.com> - 0.6.0-1
- new upstream release: 0.6.0

* Mon Aug 26 2019 Tomas Tomecek <ttomecek@redhat.com> - 0.5.1-1
- new upstream release: 0.5.1

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.0-2
- Rebuilt for Python 3.8

* Fri Aug 02 2019 Packit Service - 0.5.0-1
- new upstream release: 0.5.0

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 28 2019 Jiri Popelka <jpopelka@redhat.com> - 0.4.2-1
- New upstream release

* Sat May 18 2019 Jiri Popelka <jpopelka@redhat.com> - 0.4.1-1
- Patch release

* Wed May 15 2019 Jiri Popelka <jpopelka@redhat.com> - 0.4.0-1
- New upstream release: 0.4.0
- Build man pages since F30

* Thu Apr 11 2019 Jiri Popelka <jpopelka@redhat.com> - 0.3.0-2
- click-man needs more BuildRequires

* Wed Apr 10 2019 Tomas Tomecek <ttomecek@redhat.com> - 0.3.0-1
- New upstream release: 0.3.0

* Fri Mar 29 2019 Jiri Popelka <jpopelka@redhat.com> - 0.2.0-2
- man pages

* Tue Mar 19 2019 Tomas Tomecek <ttomecek@redhat.com> - 0.2.0-1
- New upstream release 0.2.0

* Thu Mar 14 2019 Frantisek Lachman <flachman@redhat.com> - 0.1.0-1
- New upstream release 0.1.0

* Mon Mar 04 2019 Frantisek Lachman <flachman@redhat.com> - 0.0.1-1
- Initial package.
