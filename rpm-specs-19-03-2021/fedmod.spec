# Based on initial spec generated by pyp2rpm-3.2.3

Name:           fedmod
Version:        0.6.3
Release:        13%{?dist}
Summary:        Utilities for generating & maintaining modulemd files

License:        GPLv2+ and GPLv3+ and MIT
URL:            https://pagure.io/modularity/fedmod
Source0:        %{name}-%{version}.tar.gz
Patch0:         0001-Add-f31-release-dataset-and-change-the-default-from-.patch
Patch1:         0002-Use-https-URLs-for-download.fedoraproject.org.patch
Patch2:         0003-Add-f32-branched-dataset.patch
Patch3:         0004-Mark-f32-as-stable-and-switch-to-f32-dataset-by-defa.patch
Patch4:         0005-Add-f33-release-dataset-and-change-the-default-from-f32-to-f33.patch

BuildArch:      noarch

BuildRequires:  python3-aiohttp
BuildRequires:  python3-attrs
BuildRequires:  python3-click
BuildRequires:  python3-click-completion
BuildRequires:  python3-decorator
BuildRequires:  python3-devel
BuildRequires:  python3-dnf
BuildRequires:  python3-gobject-base
BuildRequires:  python3-koji
BuildRequires:  python3-libmodulemd1 >= 1.6.2
BuildRequires:  python3-lxml
BuildRequires:  python3-pytest
BuildRequires:  python3-PyYAML
BuildRequires:  python3-requests
BuildRequires:  python3-requests-toolbelt
BuildRequires:  python3-setuptools
BuildRequires:  python3-smartcols
BuildRequires:  python3-solv

Requires:       python3-aiohttp
Requires:       python3-attrs
Requires:       python3-click
Requires:       python3-click-completion
Requires:       python3-gobject-base
Requires:       python3-koji
Requires:       python3-libmodulemd1 >= 1.6.2
Requires:       python3-lxml
Requires:       python3-PyYAML
Requires:       python3-requests
Requires:       python3-requests-toolbelt
Requires:       python3-setuptools
Requires:       python3-smartcols
Requires:       python3-solv

%description
fedmod provides tools for converting existing RPMs (most notably metapackages)
into module definitions in Fedora's modulemd format.

%prep
%autosetup -n %{name}-%{version} -p1
# Remove bundled egg-info
rm -rf %{name}.egg-info

%build
%py3_build

%install
%py3_install

# default configuration files
install -d -m 755 %{buildroot}%{_sysconfdir}/fedmod
install -m 644 config/*.yaml %{buildroot}%{_sysconfdir}/fedmod/

# shell completion
for shell_path in \
        bash:%{_datadir}/bash-completion/completions/fedmod \
        zsh:%{_datadir}/zsh/vendor-completions/_fedmod \
        fish:%{_datadir}/fish/vendor_completions.d/fedmod.fish; do
    shell="${shell_path%%:*}"
    path="${shell_path#*:}"
    dir="${path%/*}"

    install -d "%{buildroot}${dir}"

    _FEDMOD_COMPLETE=source-"$shell" %{__python3} \
        -c "import sys; sys.argv[0] = 'fedmod'; from _fedmod import cli; cli.run()" \
        > "%{buildroot}${path}"
done

%check
if ! %{__python3} -m pytest -v -m "not needs_metadata"; then
    exitcode=$?
    if [ $exitcode -eq 4 ]; then
        echo Skipping test-suite.
    else
        exit $exitcode
    fi
fi


%files
%doc
%license LICENSE
%{_bindir}/fedmod
%dir %{_sysconfdir}/fedmod
%config(noreplace) %{_sysconfdir}/fedmod/*.yaml
%{python3_sitelib}/_fedmod
%{python3_sitelib}/%{name}-%{version}-py%{python3_version}.egg-info
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/fedmod
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/vendor-completions
%{_datadir}/zsh/vendor-completions/_fedmod
%dir %{_datadir}/fish
%dir %{_datadir}/fish/vendor_completions.d
%{_datadir}/fish/vendor_completions.d/fedmod.fish

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Nov 04 2020 Petr Šabata <contyk@redhat.com> - 0.6.3-12
- Add f33 release dataset and change the default from f32 to f33
- Thanks to Kalev Lamber

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon May 25 2020 Miro Hrončok <mhroncok@redhat.com> - 0.6.3-10
- Rebuilt for Python 3.9

* Tue Apr 28 2020 Kalev Lember <klember@redhat.com> - 0.6.3-9
- Mark f32 as stable and switch to f32 dataset by default

* Tue Apr 07 2020 Kalev Lember <klember@redhat.com> - 0.6.3-8
- Add f32 branched dataset

* Wed Feb 05 2020 Kalev Lember <klember@redhat.com> - 0.6.3-7
- Add f31 release dataset and change the default from f30 to f31

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.6.3-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.6.3-4
- Rebuilt for Python 3.8

* Wed Jul 31 2019 Stephen Gallagher <sgallagh@redhat.com> - 0.6.3-3
- Fix libmodulemd dependency

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 27 2019 Nils Philippsen <nils@redhat.com> 0.6.3-1
- Update version metadata for release 0.6.3 (nils@redhat.com)
- Add f30 release dataset and change the default from f29 to f30
  (klember@redhat.com)

* Tue Mar 12 2019 Nils Philippsen <nils@redhat.com> 0.6.2-1
- Update version metadata for release 0.6.2 (nils@redhat.com)
- repo2module: allow feeding from existing modulemd (nils@redhat.com)
- repo2module: set NSVC, default profile from API pkg (or default)
  (nils@redhat.com)
- add ModuleFromRepoGenerator and repo2module command (nils@redhat.com)
- parse_dataset_name(): cope with 'architectures' missing (nils@redhat.com)
- add reading list of packages from a repository (nils@redhat.com)
- allow writing caches silently (nils@redhat.com)
- DistroPaths: work with local repositories (nils@redhat.com)
- cope with non-x86_64 multilib (nils@redhat.com)
- add script to generate compat arch configuration (nils@redhat.com)
- _depchase: don't hardcode x86_64 (nils@redhat.com)
- fix summarize_modules() called from outside CLI (nils@redhat.com)
- fix typo (nils@redhat.com)

* Mon Mar 04 2019 Nils Philippsen <nils@redhat.com> 0.6.1-1
- Update version metadata for release 0.6.1 (nils@redhat.com)
- cope with click < 7.0 (nils@redhat.com)

* Mon Mar 04 2019 Nils Philippsen <nils@redhat.com> 0.6.0-1
- Update version metadata for release 0.6.0 (nils@redhat.com)
- add get-modulemds command (nils@redhat.com)
- --show-property: allow using globs (nils@redhat.com)
- summarize-modules: allow reordering default properties (nils@redhat.com)
- add ModuleProperty.__repr__() (nils@redhat.com)
- tack MBS build info onto retrieved module objects (nils@redhat.com)
- summarize-modules: allow showing additional properties (nils@redhat.com)
- summarize-modules: use more intuitive option variable names (nils@redhat.com)
- use consistent names for module summarizing tests (nils@redhat.com)
- deprecate 'summarize-module' command name and options (nils@redhat.com)
- summarize-module: update help texts (nils@redhat.com)
- report on found modules and builds if verbose (nils@redhat.com)
- fix loglevel options (nils@redhat.com)
- lint: don't superfluously declare command name (nils@redhat.com)
- use command names consistently for CLI functions (nils@redhat.com)
- fix import order (nils@redhat.com)

* Tue Feb 26 2019 Nils Philippsen <nils@redhat.com> 0.5.0-1
- Update version metadata for release 0.5.0 (nils@redhat.com)
- only print summary if builds are found (nils@redhat.com)
- filter module builds by platform stream (nils@redhat.com)
- config: expand platform module stream name template (nils@redhat.com)
- add platform module configuration (nils@redhat.com)
- summarize-module: optionally access MBS (nils@redhat.com)
- bump copyright years (nils@redhat.com)
- add enumerate_module_defaults() methods (nils@redhat.com)
- optimize requesting builds if latest and no filters (nils@redhat.com)
- simplify iterating over module stream builds (nils@redhat.com)
- implement filtering module builds by NSVC (nils@redhat.com)
- implement filtering module names (nils@redhat.com)
- Source.enumerate_module_builds(): add `latest` parameter (nils@redhat.com)
- RPMRepoDataSource: implement enumerate_module_builds() (nils@redhat.com)
- RPMRepoDataSource: make API match Source interface (nils@redhat.com)
- rename RPMRepositorySource -> RPMRepoDataSource (nils@redhat.com)
- collect_pages(): introduce `limit` parameter (nils@redhat.com)
- collect_pages(): retrieve pages concurrently (nils@redhat.com)
- retry(): catch timeout errors (nils@redhat.com)
- retry(): put growing sleeps between attempts (nils@redhat.com)
- move code out of else branch in try...except (nils@redhat.com)
- only gather sibling builds if `latest` is set (nils@redhat.com)
- use MBS results-per-page setting (nils@redhat.com)
- avoid nested function (nils@redhat.com)
- don't use hardcoded MBS and Pagure connectors (nils@redhat.com)
- add --source option and evaluate it (nils@redhat.com)
- add runtime configuration (nils@redhat.com)
- add Source.from_type() factory (nils@redhat.com)
- add config needed to access build systems directly (nils@redhat.com)
- add BuildSystemSource (nils@redhat.com)
- add RPMRepositorySource (nils@redhat.com)
- add core Source class (nils@redhat.com)
- define Pagure and MBS API consumers (nils@redhat.com)
- add async REST API consumer (nils@redhat.com)
- repodata: cache merged modulemds (nils@redhat.com)
- repodata: distinguish between JSON and YAML caches (nils@redhat.com)
- summarize-module: ignore versions in tests (nils@redhat.com)
- set default dataset in Fedora configuration (nils@redhat.com)
- cope with un- rather than wrongly defined dataset (nils@redhat.com)
- move dataset functions to util (nils@redhat.com)
- move dict helper functions and classes into util (nils@redhat.com)
- split out application setup from CLI toplevel function (nils@redhat.com)
- add --debug option (nils@redhat.com)
- lint: use not implicitly casting YAML loader (nils@redhat.com)
- augment PyYAML to not implicitly type-cast scalars (nils@redhat.com)
- make util a package (nils@redhat.com)

* Tue Feb 05 2019 Nils Philippsen <nils@redhat.com> 0.4.6-1
- Update version metadata for release 0.4.6 (nils@redhat.com)
- Fix buildorder for generated flatpak modulemd (otaylor@fishsoup.net)

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 21 2019 Nils Philippsen <nils@redhat.com> 0.4.5-1
- Update version metadata for release 0.4.5 (nils@redhat.com)
- fix typo (nils@redhat.com)
- Change rationale from "Runtime dependencies" to "Runtime dependency"
  (otaylor@fishsoup.net)
- Clean up generated Flatpak modulemd (otaylor@fishsoup.net)
- rpm2flatpak: Handle manifests with 'id' rather than 'app-id'
  (otaylor@fishsoup.net)
- rpm2flatpak: Add 'platform' as a dependency (otaylor@fishsoup.net)
- rpm2flatpak: add a --flatpak-common option (otaylor@fishsoup.net)

* Wed Jan 16 2019 Nils Philippsen <nils@redhat.com> 0.4.4-1
- Update version metadata for release 0.4.4 (nils@redhat.com)
- access default-architecture via template expansion (nils@redhat.com)
- log and re-raise unhandled exceptions (nils@redhat.com)
- dataset: cope with dashes in release name (nils@redhat.com)

* Thu Dec 20 2018 Nils Philippsen <nils@redhat.com> 0.4.3-1
- Update version metadata for release 0.4.3 (nils@redhat.com)
- remove obsolete test files (nils@redhat.com)
- flatpak generator: move test files out of source (nils@redhat.com)
- rpm2flatpak: Add an option to initialize from the Flathub manifest
  (otaylor@fishsoup.net)
- flatpak_generator.py: Use a literal string for finish-args
  (otaylor@fishsoup.net)
- add missing blank lines after imports (nils@redhat.com)
- flake8: use 'google' import order style (nils@redhat.com)
- define application name for flake8 (nils@redhat.com)
- summarizer: improve how GErrors are wrapped (nils@redhat.com)
- summarizer: better handling of local yaml files (rdossant@redhat.com)
- mention rebasing (nils@redhat.com)
- add contributing section (nils@redhat.com)
- mention summarize-module (nils@redhat.com)
- summarizer: replace assert by exception (rdossant@redhat.com)
- summarizer: read metadata from url in cmdline (rdossant@redhat.com)
- summarizer: update method documentation (rdossant@redhat.com)
- summarizer: add glob pattern matching for filtering (nils@redhat.com)
- summarizer: ignore cached metadata when given a yaml (rdossant@redhat.com)
- flake8: only flag lines longer than 100 characters (nils@redhat.com)
- summarize-module: add modular dependency info (rdossant@redhat.com)
- summarize-module: add version and context to output (rdossant@redhat.com)
- Flatten the module profiles lookup dict (rdossant@redhat.com)
- summarize-module: make shallow copy of lookup dicts (rdossant@redhat.com)
- summarize-module: mark print_summary as internal (rdossant@redhat.com)
- Revert "repodata: make get_dataset public" (rdossant@redhat.com)
- download further metadata from redirected URLs (nils@redhat.com)
- always access local paths via repo_paths object (nils@redhat.com)
- split _download_metadata_files() chunks visually (nils@redhat.com)
- move repo <-> metadata logic into RepoPaths (nils@redhat.com)
- pep8: don't use bare 'except' (nils@redhat.com)
- pep8: fix over-/underindentation (nils@redhat.com)
- pep8: fix too long lines (nils@redhat.com)
- pep8: fix number of blank lines between items (nils@redhat.com)
- pep8: remove stray commas from single element sets (nils@redhat.com)
- pep8: fix whitespace errors (nils@redhat.com)
- pep8: ignore E402 around gi.require_version() lines (nils@redhat.com)
- pep8: separate import groups (nils@redhat.com)
- pep8: reorder imports (nils@redhat.com)
- pep8: remove unused imports (nils@redhat.com)
- summarize_modules: use spec.v2.yaml for tests (nils@redhat.com)
- module-summarizer: add tests (rdossant@redhat.com)
- Add tool for displaying summary of modules (rdossant@redhat.com)
- fetchrepodata: make merge_modules public (rdossant@redhat.com)
- repodata: make get_dataset public (rdossant@redhat.com)
- Add lookup for default stream and profiles (rdossant@redhat.com)
- Add lookup for module profiles in cached data (rdossant@redhat.com)
- Use new ImprovedModule available in libmodulemd (rdossant@redhat.com)

* Fri Nov 16 2018 Nils Philippsen <nils@redhat.com> 0.4.2-1
- Update version metadata for release 0.4.2 (nils@redhat.com)
- add shell completion for dataset names (nils@redhat.com)
- install shell completion files (nils@redhat.com)
- add basic command line completion functionality (nils@redhat.com)
- add comment about 'virtualenv' option (nils@redhat.com)
- fix Fedora Rawhide URLs (nils@redhat.com)
- fix Fedora architectures (nils@redhat.com)
- fix using plain strings as baseurl (nils@redhat.com)
- cope with missing default architecture, assume x86_64 (nils@redhat.com)
- cope with dataset regex not defining $releasever (nils@redhat.com)
- derive 'rawhide' release from fedora-base (nils@redhat.com)

* Tue Nov 13 2018 Nils Philippsen <nils@redhat.com> 0.4.1-1
- Update version metadata for release 0.4.1 (nils@redhat.com)
- only optionally require koji (nils@redhat.com)

* Fri Nov 09 2018 Nils Philippsen <nils@redhat.com> 0.4.0-1
- Update version metadata for release 0.4.0 (nils@redhat.com)
- add BR: python3-{decorator,dnf} for tests (nils@redhat.com)
- don't install test suite (nils@redhat.com)
- don't mention metalink in configuration files (nils@redhat.com)
- let Config.clear() clean out pre-processed helper dicts (nils@redhat.com)
- config: honor all configuration directories (nils@redhat.com)
- ship configuration files (nils@redhat.com)
- use configured instead of hardcoded repositories (nils@redhat.com)
- add and verify configuration for source repositories (nils@redhat.com)
- add releases dict containing expanded configuration (nils@redhat.com)
- lint: add default for --min-level (nils@redhat.com)
- use command option defaults from configuration (nils@redhat.com)
- add first round of configuration files (nils@redhat.com)
- add basic configuration framework (nils@redhat.com)
- cope with faulty or missing content length (nils@redhat.com)
- provide information about unexpected exceptions (nils@redhat.com)
- lint: understand booleans as scalar values (nils@redhat.com)
- require minimum pytest version (nils@redhat.com)
- run (standalone) tests as check (nils@redhat.com)
- update dependencies (nils@redhat.com)
- move Python sources back to toplevel (nils@redhat.com)
- require PyGObject and koji Python packages (nils@redhat.com)
- merge relevant parts of src/README.md (nils@redhat.com)
- update the README (nils@redhat.com)
- mark tests that need metadata present (nils@redhat.com)
- test_cli_ux: cope with missing metadata cache (nils@redhat.com)

* Tue Sep 25 2018 Nils Philippsen <nils@redhat.com> 0.3.1-1
- Update version metadata for release 0.3.1 (nils@redhat.com)
- use summary and description of first package (nils@redhat.com)

* Mon Sep 17 2018 Nils Philippsen <nils@redhat.com> 0.3.0-1
- Update version metadata for release 0.3.0 (nils@redhat.com)
- test that wrong data types in filter block get flagged (nils@redhat.com)
- test that wrong data types in api block get flagged (nils@redhat.com)
- test that wrong data types in profiles block get flagged (nils@redhat.com)
- test that non-scalar values in references get flagged (nils@redhat.com)
- test that unknown reference keys get flagged (nils@redhat.com)
- lint: cope gracefully with non-dict references block (nils@redhat.com)
- test that non-dict references block gets flagged (nils@redhat.com)
- test that non-dict xmd block gets flagged (nils@redhat.com)
- test that missing platform dependencies are flagged (nils@redhat.com)
- lint: warn about missing dependencies block (nils@redhat.com)
- test that a missing dependencies block gets flagged (nils@redhat.com)
- pytest: filter more deprecation warnings caused by koji (nils@redhat.com)
- test that items from infrastructure are flagged (nils@redhat.com)
- avoid other warnings when importing Modulemd (nils@redhat.com)
- make @linting_fails preserve method signatures (nils@redhat.com)
- refactor @linting_fails (nils@redhat.com)
- test license blocks that are unknown or not lists (nils@redhat.com)
- test license blocks that aren't dicts (nils@redhat.com)
- test summaries that are more than one sentence (nils@redhat.com)
- test non-Unicode and non-YAML documents (nils@redhat.com)
- test non-scalar license values (nils@redhat.com)
- test missing licenses, licenses.module blocks (nils@redhat.com)
- lint: fix lint_licenses_scalar() (nils@redhat.com)
- test dependencies blocks of the wrong version (nils@redhat.com)
- lint: check that a v1 dependencies block is a dict (nils@redhat.com)
- test for trailing periods in summary, description (nils@redhat.com)
- include all levels when linting by default (nils@redhat.com)
- lint: better cope with missing description (nils@redhat.com)
- test for missing summary and description (nils@redhat.com)
- test for wrong or missing document versions (nils@redhat.com)
- add class for generic modulemd tests (nils@redhat.com)
- add and use linting_fails decorator (nils@redhat.com)
- lint: test missing document element (nils@redhat.com)
- add basic harness to test linting (nils@redhat.com)
- require pytest for testing (nils@redhat.com)
- lint: update copyright year (nils@redhat.com)
- lint: update v1_dependencies_buildrequires_dict docstring (nils@redhat.com)
- lint: cope with modulemd v1/v2 dependencies blocks (nils@redhat.com)
- lint: accept modulemd v2 documents (nils@redhat.com)
- lint: add missing blank line before class (nils@redhat.com)
- lint: update linked anchors (nils@redhat.com)
- add period to sentence ends (nils@redhat.com)
- Fix error message when container.yaml exists (otaylor@fishsoup.net)
- pytest: filter deprecation warnings caused by koji (nils@redhat.com)
- avoid warning when importing Modulemd (nils@redhat.com)
- change back out of temporary directory after test (nils@redhat.com)
- tests: make check for Python 2 setuptools fuzzier (nils@redhat.com)

* Thu Sep 06 2018 Nils Philippsen <nils@redhat.com> 0.2.3-1
- Update version metadata for release 0.2.3 (nils@redhat.com)
- Default to the f29 dataset (otaylor@fishsoup.net)
- Flatpak: Base runtime and package branches off of the current dataset
  (otaylor@fishsoup.net)
- Add a f29 release version (otaylor@fishsoup.net)
- Add a rawhide release version (otaylor@fishsoup.net)
- Allow for multiple release versions, and add a --dataset argument
  (otaylor@fishsoup.net)
- Add F28 modular updates repo (otaylor@fishsoup.net)
- Fix usage of attrs (otaylor@fishsoup.net)

* Thu Aug 09 2018 Nils Philippsen <nils@redhat.com> 0.2.2-1
- Update version metadata for release 0.2.2 (nils@redhat.com)
- fix modulemd dependencies (nils@redhat.com)

* Thu Aug 09 2018 Nils Philippsen <nils@redhat.com> 0.2.1-1
- Update version metadata for release 0.2.1 (nils@redhat.com)
- For Flatpaks, default components to the F28 branch (otaylor@fishsoup.net)
- rpm2flatpak: reference the master stream, not the stable stream
  (otaylor@fishsoup.net)
- Fix libmodulemd usage for changes in libmodulemd-1.5 (otaylor@fishsoup.net)

* Tue Aug 07 2018 Nils Philippsen <nils@redhat.com> 0.2-1
- Update version metadata for release 0.2 (nils@redhat.com)
- ignore untracked files for releases (nils@redhat.com)
- reset release when tagging (nils@redhat.com)
- fix typo (nils@redhat.com)
- Add flatpak-report command (otaylor@fishsoup.net)
- Add rpm2flatpak (otaylor@fishsoup.net)
- Factor out a rpm_name_only utility functio (otaylor@fishsoup.net)

* Fri May 25 2018 Karsten Hopp <karsten@redhat.com> 0.1-2
- update License tag for package review add %%license (karsten@redhat.com)
- add changelog (karsten@redhat.com)
- Update version metadata for release 0.1 (karsten@redhat.com)
- _depchase: Remove some stray assignments (otaylor@fishsoup.net)
- add mapping package/module for dependencies (karsten@redhat.com)
- Enable the Fedora updates repository (otaylor@fishsoup.net)
- depchase: Handle duplicate packages in the pool (otaylor@fishsoup.net)
- Fix problem resolving relative paths to updates repo (otaylor@fishsoup.net)
- Use RPM metadata as the basis for summary and description
  (otaylor@fishsoup.net)
- Use a cache for dependency details (otaylor@fishsoup.net)
- update maintainer (karsten@redhat.com)
- disable updates for now, move that to a new issue (karsten@redhat.com)
- break out unrelated commit (karsten@redhat.com)
- add module updates (karsten@redhat.com)
- libmodulemd fixes (karsten@redhat.com)
- Use libmodulemd instead of modulemd (otaylor@fishsoup.net)

* Fri May 25 2018 Karsten Hopp <karsten@redhat.com>
- update License tag for package review add %%license (karsten@redhat.com)
- add changelog (karsten@redhat.com)
- Update version metadata for release 0.1 (karsten@redhat.com)
- _depchase: Remove some stray assignments (otaylor@fishsoup.net)
- add mapping package/module for dependencies (karsten@redhat.com)
- Enable the Fedora updates repository (otaylor@fishsoup.net)
- depchase: Handle duplicate packages in the pool (otaylor@fishsoup.net)
- Fix problem resolving relative paths to updates repo (otaylor@fishsoup.net)
- Use RPM metadata as the basis for summary and description
  (otaylor@fishsoup.net)
- Use a cache for dependency details (otaylor@fishsoup.net)
- update maintainer (karsten@redhat.com)
- disable updates for now, move that to a new issue (karsten@redhat.com)
- break out unrelated commit (karsten@redhat.com)
- add module updates (karsten@redhat.com)
- libmodulemd fixes (karsten@redhat.com)
- Use libmodulemd instead of modulemd (otaylor@fishsoup.net)

* Fri May 25 2018 Karsten Hopp <karsten@redhat.com>
- Update version metadata for release 0.1 (karsten@redhat.com)
- _depchase: Remove some stray assignments (otaylor@fishsoup.net)
- add mapping package/module for dependencies (karsten@redhat.com)
- Enable the Fedora updates repository (otaylor@fishsoup.net)
- depchase: Handle duplicate packages in the pool (otaylor@fishsoup.net)
- Fix problem resolving relative paths to updates repo (otaylor@fishsoup.net)
- Use RPM metadata as the basis for summary and description
  (otaylor@fishsoup.net)
- Use a cache for dependency details (otaylor@fishsoup.net)
- update maintainer (karsten@redhat.com)
- disable updates for now, move that to a new issue (karsten@redhat.com)
- break out unrelated commit (karsten@redhat.com)
- add module updates (karsten@redhat.com)
- libmodulemd fixes (karsten@redhat.com)
- Use libmodulemd instead of modulemd (otaylor@fishsoup.net)

* Thu Apr 05 2018 Karsten Hopp <karsten@redhat.com> 0.0.10-1
- Update version metadata for release 0.0.10 (karsten@redhat.com)
- Strip down module generation (otaylor@fishsoup.net)
- Comment out references to updates repo (otaylor@fishsoup.net)
- Move from F27 to F28 (otaylor@fishsoup.net)
- Remove special handling of fedora-release (otaylor@fishsoup.net)
- Remove references to bootstrap module (otaylor@fishsoup.net)
- Move gzip import into the right file (otaylor@fishsoup.net)
- When tracking package dependencies, look at pre-requires, not just normal
  reqs (otaylor@fishsoup.net)
- add PyYAML dependency to spec file (nils@redhat.com)
- allow marking blocks as "explicitly empty" (nils@redhat.com)
- don't trip over 'filter: ~' (nils@redhat.com)
- improve wording in some detailed descriptions (nils@redhat.com)
- fix grammar (nils@redhat.com)
- check that filter/rpms exists before accessing it (nils@redhat.com)
- check for optional dependencies/(build)requires (nils@redhat.com)
- fix some method/prerequisite names (nils@redhat.com)
- fix PyYAML dependency (nils@redhat.com)
- we don't really support UTF-16 at the moment (nils@redhat.com)
- return a non-zero exit code on warnings, errors (nils@redhat.com)
- add checks for optional blocks (nils@redhat.com)
- load and process the file in linter methods (nils@redhat.com)
- allow empty guidelines link (nils@redhat.com)
- add @prerequisite_for decorator (nils@redhat.com)
- add @option decorator (nils@redhat.com)
- add license blurb (nils@redhat.com)
- more comments (nils@redhat.com)
- check types of content components' metadata (nils@redhat.com)
- check components (nils@redhat.com)
- check filters (nils@redhat.com)
- check the API (nils@redhat.com)
- add check_is_list() and use it (nils@redhat.com)
- check the profiles (nils@redhat.com)
- check the references (nils@redhat.com)
- check that all license elements are scalars (nils@redhat.com)
- check that all license blocks are lists in one go (nils@redhat.com)
- warn about unknown license keys/blocks (nils@redhat.com)
- let check_is_(dict|scalar) accept multiple values (nils@redhat.com)
- make assertion errors more informative (nils@redhat.com)
- assert that every linter method has a docstring (nils@redhat.com)
- check that a potential 'xmd' block is a dict (nils@redhat.com)
- don't use modulemd for linting (nils@redhat.com)
- add check_is_dict() and use it (nils@redhat.com)
- add check_is_scalar() method and use it (nils@redhat.com)
- add checks for the dependencies block (nils@redhat.com)
- flag fields which should be set during build (nils@redhat.com)
- mention recognized license keys (nils@redhat.com)
- format guideline blurbs and problem details better (nils@redhat.com)
- use click.Choice for validating --min-level (nils@redhat.com)
- add --min-level option (nils@redhat.com)
- use check*() methods rather than assert (nils@redhat.com)
- add prerequisite decorator (nils@redhat.com)
- check that description exists (nils@redhat.com)
- add license block checks (nils@redhat.com)
- load raw YAML dict for low-level checks (nils@redhat.com)
- reformat output a little (nils@redhat.com)
- add detail decorator (nils@redhat.com)
- execute linter methods in order of their definition (nils@redhat.com)
- check if description ends in a period (nils@redhat.com)
- add 'lint' command (nils@redhat.com)
- don't import from __future__ (nils@redhat.com)

* Thu Apr 05 2018 Karsten Hopp <karsten@redhat.com> - 0.0.10-1
- update for F28 (Owen Taylor)
- look at pre-reqs for package dependencies, too (Owen Taylor)

* Wed Dec 06 2017 Nick Coghlan <ncoghlan@gmail.com> 0.0.9-1
- Update version metadata for release 0.0.9 (ncoghlan@gmail.com)
- Issue #28: Remove dependency on DNF (ncoghlan@gmail.com)
- Add docs for 'resolve-deps --json' (ncoghlan@gmail.com)
- Add a basic 'resolve-deps --json' test case (ncoghlan@gmail.com)
- Keep function signature compatible (ncoghlan@gmail.com)
- Report lists to handle ambiguous deps (ncoghlan@gmail.com)
- resolve-deps: Add a --json flag to get full output in JSON form
  (otaylor@fishsoup.net)
- Separate metadata fetching to its own file (ncoghlan@gmail.com)
- README: Document srpm-of-rpm command (crobinso@redhat.com)
- cli: add rpms-from-srpm command (crobinso@redhat.com)
- depchase: Handle epoch packages in get_rpms_for_srpms (crobinso@redhat.com)
- depchase: Drop unnecessary archful lookup for get_rpms_for_srpms
  (crobinso@redhat.com)
- depchase: Fix get_rpms_for_srpms lookup mapping (crobinso@redhat.com)
- cli: print sorted output (crobinso@redhat.com)
- Issue #57: Cache metadata lookup tables (ncoghlan@gmail.com)
- Issue #34: Improve handling of duplicate components (ncoghlan@gmail.com)
- Issue #49: Migrate CLI processing to click (ncoghlan@gmail.com)

* Wed Nov 22 2017 Adam Samalik <asamalik@redhat.com> 0.0.8-1
- Update version metadata for release 0.0.8 (asamalik@redhat.com)
- add smartcols and solv dependencies to spec (asamalik@redhat.com)
- Issue #52: Handle missing metadata (ncoghlan@gmail.com)
- Add basic test file descriptions (ncoghlan@gmail.com)
- Clarify repoquery subcommand docs (ncoghlan@gmail.com)
- Tidy up whitespace in test file (ncoghlan@gmail.com)

* Fri Nov 10 2017 Adam Samalik <asamalik@redhat.com> 0.0.7-1
- Update version metadata for release 0.0.7 (asamalik@redhat.com)
- add srpm-of-rpm functionality (asamalik@redhat.com)

* Tue Nov 07 2017 Adam Samalik <asamalik@redhat.com> 0.0.6-1
- Update version metadata for release 0.0.6 (asamalik@redhat.com)
- workaround for https://pagure.io/pagure/issue/2751 (asamalik@redhat.com)
- add user docs (asamalik@redhat.com)
- add tests for module repoquery (asamalik@redhat.com)
- use forward lookup table for modules (asamalik@redhat.com)
- implement repoquery-like commands (asamalik@redhat.com)
- Remove dependency-reports-scripts cross-reference (ncoghlan@gmail.com)
- Fix COPR package name (ncoghlan@redhat.com)
- Add release publication docs (ncoghlan@gmail.com)

* Thu Nov 02 2017 Nick Coghlan <ncoghlan@gmail.com> 0.0.5-1
- Update version metadata for release 0.0.5 (ncoghlan@gmail.com)
- Put requirements before description (ncoghlan@gmail.com)

* Thu Nov 02 2017 Nick Coghlan <ncoghlan@gmail.com> 0.0.4-1
- new package built with tito

* Wed Nov 01 2017 mockbuilder - 0.0.2-1
- Initial package.
