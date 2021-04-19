%bcond_without html_docs
%bcond_without tests

Name:           pipx
Version:        0.16.1.0
Release:        4%{?dist}
Summary:        Install and run Python applications in isolated environments

License:        MIT
URL:            https://pipxproject.github.io/%{name}/
Source0:        https://github.com/pipxproject/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

%if %{with tests}
# Note that upstream uses nox as the test runner, but this is not packaged in
# Fedora. See noxfile.py.
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-cov)
%endif

BuildRequires:  pkgconfig(bash-completion)
%global bashcompdir %(pkg-config --variable=completionsdir bash-completion 2>/dev/null)
%global bashcomproot %(dirname %{bashcompdir} 2>/dev/null)
BuildRequires:  pkgconfig(fish)
%global fishcompdir %(pkg-config --variable=completionsdir fish 2>/dev/null)
%global fishcomproot %(dirname %{fishcompdir} 2>/dev/null)
BuildRequires:  /usr/bin/register-python-argcomplete

%description
%{name} is a tool to help you install and run end-user applications written in
Python. It’s roughly similar to macOS’s brew, JavaScript’s npx, and Linux’s
apt.

It’s closely related to pip. In fact, it uses pip, but is focused on installing
and managing Python packages that can be run from the command line directly as
applications.


%package doc
Summary:        Documentation for %{name}

%if %{with html_docs}
# See noxfile.py
BuildRequires:  python3dist(jinja2)
BuildRequires:  python3dist(mkdocs)
BuildRequires:  python3dist(mkdocs-material)
%endif

%description doc
Documentation for %{name}.


%generate_buildrequires
%pyproject_buildrequires -r


%prep
%autosetup


%build
%pyproject_wheel

(
  # Temporary local install
  PYTEMP="${PWD}/%{_vpath_builddir}/pytemp"
  if [ -n "${PYTHONPATH-}" ]; then PYTHONPATH="${PYTHONPATH}:"; fi
  export PYTHONPATH="${PYTHONPATH-}${PYTEMP}"
  if [ -n "${PATH-}" ]; then PATH="${PATH}:"; fi
  export PATH="${PATH}:${PYTEMP}/bin"
  %{__python3} -m pip install --target="${PYTEMP}" \
      --no-deps --use-pep517 --no-build-isolation \
      --disable-pip-version-check --no-clean --progress-bar off --verbose \
      %{_pyproject_wheeldir}/*.whl

%if %{with html_docs}
  # Build the documentation
  %{__python3} scripts/generate_docs.py
  mkdocs build
%endif

  # Generate shell completions. “pipx completions” says:
  # Add the appropriate command to your shell's config file
  # so that it is run on startup. You will likely have to restart
  # or re-login for the autocompletion to start working.
  #
  # bash:
  #     eval "$(register-python-argcomplete pipx)"
  #
  # zsh:
  #     To activate completions for zsh you need to have
  #     bashcompinit enabled in zsh:
  #
  #     autoload -U bashcompinit
  #     bashcompinit
  #
  #     Afterwards you can enable completion for pipx:
  #
  #     eval "$(register-python-argcomplete pipx)"
  #
  # tcsh:
  #     eval `register-python-argcomplete --shell tcsh pipx`
  #
  # fish:
  #     register-python-argcomplete --shell fish pipx | source
  for sh in bash tcsh fish
  do
    register-python-argcomplete --shell "${sh}" %{name} \
        > "%{name}.${sh}"
  done

  rm -rf "${PYTEMP}"
)


%install
%pyproject_install
%pyproject_save_files %{name}

install -p -m 0644 -D -t %{buildroot}%{bashcompdir} %{name}.bash
install -p -m 0644 -D -t %{buildroot}%{fishcompdir} %{name}.fish
# It seems that there is not a reasonable way to install tcsh completions
# system-wide, so we just make the completions file available for interested
# users.
install -p -m 0644 -D %{name}.tcsh \
    %{buildroot}%{_datadir}/%{name}/%{name}-completion.tcsh
# Note that there are no “native” zsh completions, so we do not attempt to
# install anything. This could change if an actual zsh user recommends a
# different plan.


%if %{with tests}
%check
# Most of the tests require network access. We also must skip
# test_run_ensure_null_pythonpath because PYTHONPATH is set in the test
# environment.
%pytest -k "$(
  %{__python3} -c 'from sys import argv
print(" and ".join(f"not test_{x}" for x in argv[1].split()))
' '
cache
existing_symlink_points_to_existing_wrong_location_warning
existing_symlink_points_to_nothing
extra
force_install
include_deps
inject_include_apps
inject_simple
inject_simple_legacy_venv
inject_tricky_character
install_easy_packages
install_local_extra
install_no_packages_found
install_package_specs
install_pip_failure
install_same_package_twice_no_error
install_same_package_twice_no_force
install_suffix
install_tricky_packages
list_legacy_venv
list_package_install
list_suffix
list_suffix_legacy_venv
missing_interpreter
name_tricky_characters
package_determination
package_inject
package_install
path_warning
reinstall
reinstall_all
reinstall_all_legacy_venv
reinstall_all_suffix
reinstall_all_suffix_legacy_venv
reinstall_legacy_venv
reinstall_specifier
reinstall_suffix
reinstall_suffix_legacy_venv
run_script_from_internet
runpip
simple_run
spec
uninstall
uninstall_all
uninstall_all_legacy_venv
uninstall_legacy_venv
uninstall_suffix
uninstall_suffix_legacy_venv
uninstall_with_missing_interpreter
upgrade
upgrade_legacy_venv
upgrade_suffix
upgrade_suffix_legacy_venv

run_ensure_null_pythonpath
')"
%endif


%files -f %{pyproject_files}
%license LICENSE

%{_bindir}/%{name}

# Note that it is standard in Fedora for packages providing shell completions
# to co-own the completions directory in lieu of having a runtime dependency on
# the relevant shell completions package.
%{bashcomproot}
%{fishcomproot}
%{_datadir}/%{name}


%files doc
%license LICENSE
%doc README.md
# Markdown
%doc docs
%if %{with html_docs}
%doc site
%endif


%changelog
* Tue Mar 30 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 0.16.1.0-4
- Use pyproject-rpm-macros for build and install, too
- Drop Fedora 32/33 workarounds since they lack the dependency versions
  required for the current version

* Thu Mar 25 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 0.16.1.0-3
- Improved source URL (better tarball name)

* Tue Mar 16 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 0.16.1.0-2
- Drop python3dist(setuptools) BR, redundant with %%pyproject_buildrequires

* Fri Feb 26 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 0.16.1.0-1
- New version 0.16.1.0

* Tue Feb 16 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 0.16.0.0-1
- New version 0.16.0.0

* Sun Feb 14 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 0.15.6.0-1
- New version 0.15.6.0
- Use GitHub tarball instead of PyPI tarball
- License is now only “MIT” instead of “MIT and BSD”
- Drop obsolete python_provide macro; do not add py_provides, since the package
  is only to support the command-line tool and does not provide a public API
- Use pyproject-rpm-macros for generated BR’s
- Improve description
- Run those few tests that do not require network access
- Drop sed invocation, as there are no longer stray shebangs
- Build HTML documentation and install it in a new -doc subpackage
- Package shell completions

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Oct  5 2020 Martin Jackson <mhjacks@swbell.net> - 0.15.5.1-3
- Add explicit dep on setuptools

* Sat Aug 29 2020 Martin Jackson <mhjacks@swbell.net> - 0.15.5.1-2
- Rebuilding.  Dep is OK on f33.

* Thu Aug 27 2020 Martin Jackson <mhjacks@swbell.net> - 0.15.5.1-1
- Update to upstream release 0.15.5.1

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.15.3.1-2
- Rebuilt for Python 3.9

* Mon May 18 2020 Martin Jackson <mhjacks@swbell.net> - 0.15.3.1-1
- Update to upstream release 0.15.3.1

* Tue Jan 21 2020 Martin Jackson <mhjacks@swbell.net> - 0.15.1.3-1
- Update to upstream release 0.15.1.3

* Sun Jan 12 2020 Martin Jackson <mhjacks@swbell.net> - 0.15.1.2-1
- Update to upstream release 0.15.1.2

* Sat Jan 04 2020 Martin Jackson <mhjacks@swbell.net> - 0.14.0.0-1
- Convert to pipx name
