%{?python_enable_dependency_generator}
%global modname okaara
%global rel 1

# -- headers ------------------------------------------------------------------

Name:           python-okaara
Version:        1.0.37
Release:        16%{?dist}
Summary:        Python command line utilities

License:        GPLv2
URL:            https://github.com/jdob/okaara
Source0:        https://github.com/jdob/%{modname}/archive/python-%{modname}-%{version}-%{rel}.tar.gz

BuildArch:      noarch

%description
Python library to facilitate the creation of command-line interfaces.

%package -n python3-%{modname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-babel
BuildRequires:  python3-nose
BuildRequires:  python3-future
BuildRequires:  python3-mock
%{?python_provide:%python_provide python3-%{modname}}

%description -n python3-%{modname}
Python library to facilitate the creation of command-line interfaces.


%prep
%autosetup -n %{modname}-%{name}-%{version}-%{rel}

# -- build --------------------------------------------------------------------

%build
%py3_build

mkdir -p po/build
for lang in `ls po/*.po` ; do
    echo $lang;
    lang=`basename $lang .po`;
    mkdir -p po/build/$lang/LC_MESSAGES/;
    %{__python3} setup.py compile_catalog -i po/$lang.po \
        -o po/build/$lang/LC_MESSAGES/okaara.mo;
done

# -- install ------------------------------------------------------------------

%install
# Python setup
%py3_install

mkdir -p $RPM_BUILD_ROOT/%{_datadir}/locale/
cp -R po/build/* $RPM_BUILD_ROOT/%{_datadir}/locale/
%find_lang okaara

# -- check --------------------------------------------------------------------

%check
nosetests-%{python3_version}

# -- files --------------------------------------------------------------------

%files -f %{modname}.lang -n python3-%{modname}
%license LICENSE
%{python3_sitelib}/%{modname}/
%{python3_sitelib}/%{modname}*.egg-info

# -- changelog ----------------------------------------------------------------

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.37-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.37-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hron??ok <mhroncok@redhat.com> - 1.0.37-14
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.37-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hron??ok <mhroncok@redhat.com> - 1.0.37-12
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hron??ok <mhroncok@redhat.com> - 1.0.37-11
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.37-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.37-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 04 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.37-8
- Enable python dependency generator

* Fri Jan 04 2019 Miro Hron??ok <mhroncok@redhat.com> - 1.0.37-7
- Python 2 package removed

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.37-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hron??ok <mhroncok@redhat.com> - 1.0.37-5
- Rebuilt for Python 3.7

* Mon Feb 12 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.0.37-4
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.37-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.37-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Mar 14 2017 Iryna Shcherbina <ishcherb@redhat.com> - 1.0.37-1
- Update to version 1.0.37 and add a Python 3 subpackage

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.32-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.32-6
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.32-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.32-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.32-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Jan 31 2014 Alex Wood <awood@redhat.com> 1.0.32-2
- Add BuildRequires on pytz

* Fri Jan 31 2014 Alex Wood <awood@redhat.com> 1.0.32-1
- Update to latest version

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.21-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu May 23 2013 Jay Dobies <jason.dobies@redhat.com> 1.0.32-1
- Added empty strings as a possibility for optional parse methods
  (jason.dobies@redhat.com)
- Added copyright information (jason.dobies@redhat.com)

* Wed May 22 2013 Jay Dobies <jason.dobies@redhat.com> 1.0.31-1
- Renamed non-negative int parser (jason.dobies@redhat.com)
- Added base set of parsers (jason.dobies@redhat.com)
- Header standardization (jason.dobies@redhat.com)
- Updated sample (jason.dobies@redhat.com)

* Thu Feb 14 2013 Jay Dobies <jason.dobies@redhat.com> 1.0.30-1
- Various clean up (jason.dobies@redhat.com)

* Thu Feb 14 2013 Jay Dobies <jason.dobies@redhat.com> 1.0.29-1
- Fixed deadlock when the threaded spinner times out (jason.dobies@redhat.com)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.21-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jan 08 2013 Jay Dobies <jason.dobies@redhat.com> 1.0.28-1
- Added support for telling the user if an unexpected option was specified
  (jason.dobies@redhat.com)
- Remove Pulp references (jason.dobies@redhat.com)
- Fixed class formatting (jason.dobies@redhat.com)

* Thu Dec 06 2012 Jay Dobies <jason.dobies@redhat.com> 1.0.27-1
- The full path to the section isn't known, so the usage was misleading since
  it was missing the parent sections. The change for now is to simply not
  include the path to the section and just inform the user of the
  section/command relationship. (jason.dobies@redhat.com)
- Fix to find closest match in the event a nested command is not found to make
  sure the cloest matching subsection is returned (jason.dobies@redhat.com)
- Reorganized code for pip standards (jason.dobies@redhat.com)
- Clean up for handling of argument - prefixes (jason.dobies@redhat.com)

* Fri Aug 24 2012 Jay Dobies <jason.dobies@redhat.com> 1.0.26-1
- Added syntactic sugar methods to the CLI (jason.dobies@redhat.com)
- Added keyword property to the Option class (jason.dobies@redhat.com)

* Fri Aug 24 2012 Jay Dobies <jason.dobies@redhat.com> 1.0.25-1
- fixing a bug where an Exception instance was assumed to have an attribute not
  present in python <2.5, and that attribute was assumed to have a non-
  guaranteed value. (mhrivnak@redhat.com)
- Add i18n support. (jbowes@repl.ca)
- Fixed incorrect package_dir after moving setup.py to root
  (jason.dobies@redhat.com)
- add some more info to setup.py (jbowes@repl.ca)
- spec: nosetests can run from the toplevel src dir (jbowes@repl.ca)
- Move setup.py to the toplevel (jbowes@repl.ca)
- Added column alignment capabilities (jason.dobies@redhat.com)

* Thu Jul 26 2012 Jay Dobies <jason.dobies@redhat.com> 1.0.24-1
- Added interruptable handling to prompt_password (jason.dobies@redhat.com)
- Changed table and col width to be non-instance to make life a whole lot
  easier (jason.dobies@redhat.com)
- Entirely restructured table handling with a pre-parse step
  (jason.dobies@redhat.com)
- Changed table_width and col_width to be stored as instance variables
  (jason.dobies@redhat.com)
- Removed pointless layer between table and its config
  (jason.dobies@redhat.com)

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jul 19 2012 Jay Dobies <jason.dobies@redhat.com> 1.0.23-1
- Added ability to remove a command from the root CLI (jason.dobies@redhat.com)

* Wed Jul 18 2012 Jay Dobies <jason.dobies@redhat.com> 1.0.22-1
- converted to new-style classes so they are easier to subclass.
  (mhrivnak@redhat.com)
- Validate and parse functions are no longer applied to options for which the
  user did not supply any input. (mhrivnak@redhat.com)
 Added built in validate and parse functions on options
  (jason.dobies@redhat.com)
- Some refactoring to support subclasses better (jason.dobies@redhat.com)
- Added color support (naturally) (jason.dobies@redhat.com)

* Mon Jul 09 2012 Jay Dobies <jason.dobies@redhat.com> 1.0.21-1
- Make sure src is in the python path so tests can run
  (jason.dobies@redhat.com)

* Sun Jul 08 2012 Jay Dobies <jason.dobies@redhat.com> 1.0.20-1
- Removing the explicit python version requirement since it's not needed on
  Fedora (might still be needed on RHEL5). (jason.dobies@redhat.com)
- Added %%check section and %%files change for fedora packaging
  (jason.dobies@redhat.com)

* Wed May 23 2012 Jay Dobies <jason.dobies@redhat.com> 1.0.19-1
- Changed RPM macro to adhere to Fedora packaging standards
  (jason.dobies@redhat.com)
- Work on the shell user docs (jason.dobies@redhat.com)
- Corrected incorrect docstrings (jason.dobies@redhat.com)
- More advanced usage for CLIs (jason.dobies@redhat.com)
- Significant work towards the CLI documentation (jason.dobies@redhat.com)

* Fri May 18 2012 Jay Dobies <jason.dobies@redhat.com> 1.0.18-1
- Minor spec tweaks for Fedora packaging guidelines (jason.dobies@redhat.com)
- Added license copy and inclusion in the RPM (jason.dobies@redhat.com)
- Added ability to configure text to automatically prefix command option
  descriptions based on their required attribute (jason.dobies@redhat.com)

* Fri May 11 2012 Jay Dobies <jason.dobies@redhat.com> 1.0.17-1
- Source file header clean up

* Fri May 11 2012 Jay Dobies <jason.dobies@redhat.com> 1.0.16-1
- Corrections to the spec for fedora guidelines (jason.dobies@redhat.com)
- Cleanup of spec whitespace (jason.dobies@redhat.com)

* Fri May 04 2012 Jay Dobies <jason.dobies@redhat.com> 1.0.15-1
- Renamed spec as per fedora packaging conventions (jason.dobies@redhat.com)

* Wed Apr 04 2012 Jay Dobies <jason.dobies@redhat.com> 1.0.14-1
- Added create methods to CLI itself and default exit code for commands
  (jason.dobies@redhat.com)
- Sort sections/commands alphabetically by name on usage. Not perfect and
  eventually make customizable, but this works for now.
  (jason.dobies@redhat.com)
- Added exit code as the return value for CLI.run (jason.dobies@redhat.com)
- Added optional command description that is only displayed in the usage output
  (jason.dobies@redhat.com)
- Added syntactic sugar methods for create to section and command
  (jason.dobies@redhat.com)

* Wed Mar 28 2012 Jay Dobies <jason.dobies@redhat.com> 1.0.13-1
- Added add/find command to root of the CLI (jason.dobies@redhat.com)
- Fixed bar rendering when prompt auto_wrap is enabled and the user supplies a
  multi-line message (jason.dobies@redhat.com)
- Refactoring to support better OO principles and make usage more flexible in
  subclasses (jason.dobies@redhat.com)

* Fri Mar 16 2012 Jay Dobies <jason.dobies@redhat.com> 1.0.12-1
- Added support for default values on options (jason.dobies@redhat.com)

* Tue Mar 13 2012 Jay Dobies <jason.dobies@redhat.com> 1.0.11-1
- Required check needs to run across all options, even those in groups
  (jason.dobies@redhat.com)
- Made option group output closer to OptionParser (jason.dobies@redhat.com)
- Added support for option groups (jason.dobies@redhat.com)
- Added in required/optional argument separation (totally gonna rip this out in
  a few minutes, but committing for archive purposes) (jason.dobies@redhat.com)
- This isn't the right place for that annotation (jason.dobies@redhat.com)

* Wed Mar 07 2012 Jay Dobies <jason.dobies@redhat.com> 1.0.10-1
- Added parser implementation for common scenarios (jason.dobies@redhat.com)
- Upped docs version to match RPM version (jason.dobies@redhat.com)
- Max width calculation needs to take the color characters into account
  (jason.dobies@redhat.com)

* Fri Mar 02 2012 Jay Dobies <jason.dobies@redhat.com> 1.0.9-1
- Added optional color for cli map output (jason.dobies@redhat.com)
- Hardened color command to handle None as the color (jason.dobies@redhat.com)

* Fri Mar 02 2012 Jay Dobies <jason.dobies@redhat.com> 1.0.8-1
- Fixed infinite loop in small circumstances when remaining_line_indent is used
  (jason.dobies@redhat.com)
- Helps if you actually retain a handle to the parser (jason.dobies@redhat.com)
- Added timeout to threaded spinner (jason.dobies@redhat.com)
- Added ability to delete spinners/bars after they are finished
  (jason.dobies@redhat.com)
- Cleaned up the CLI map output (jason.dobies@redhat.com)
- Import clean up (jason.dobies@redhat.com)
- Cleaned up --help output (jason.dobies@redhat.com)

* Wed Feb 29 2012 Jay Dobies <jason.dobies@redhat.com> 1.0.7-1
- Fixed for 2.4 compatibility (jason.dobies@redhat.com)

* Wed Feb 29 2012 Jay Dobies <jason.dobies@redhat.com> 1.0.6-1
- new package built with tito

* Mon Feb 27 2012 Jay Dobies <jason.dobies@redhat.com> 1.0.5-1
- Added remove section/command methods (jason.dobies@redhat.com)

* Mon Feb 27 2012 Jay Dobies <jason.dobies@redhat.com> 1.0.4-1
- Added ThreadedSpinner class (jason.dobies@redhat.com)
- Added message support to Spinner (jason.dobies@redhat.com)
- Added parser override ability to bypass okaara abstraction. Added parser skip
  if no options are provided. (jason.dobies@redhat.com)
- kwargs passed to commands have the -- stripped. Added support for aliases in
  options. Added support for multiple values per option. Cleaned up usage
  message for invalid arguments. (jason.dobies@redhat.com)
- Max was doing alpha comparison instead of length (jason.dobies@redhat.com)
- Played with alignment in cli usage (jason.dobies@redhat.com)
- Abort-related fixes (jason.dobies@redhat.com)
- Fixed first pass logic on wrapping (jason.dobies@redhat.com)
- Don't strip off leading whitespace from the first line while wrapping; it's
  probably intended. After that, we can't really guarantee much
  (jason.dobies@redhat.com)
- Tweaked usage to be light years better (jason.dobies@redhat.com)
- Fixed usage output (jason.dobies@redhat.com)
- Corrected logic for prompt number (jason.dobies@redhat.com)
- Exposed find_section functionality in the CLI itself.
  (jason.dobies@redhat.com)
- No longer log non-tagged calls; it's too damn noisy (jason.dobies@redhat.com)
- Added tag support for progress bar and spinner (jason.dobies@redhat.com)
- Fix for the case where the progress bar's message wraps
  (jason.dobies@redhat.com)
- Call the content's __str__ in case the user is sloppy
  (jason.dobies@redhat.com)
- Made wrap functionality smart enough to not split words if possible
  (jason.dobies@redhat.com)
- Made wrap a first-class function and added center as an argument to write
  (jason.dobies@redhat.com)
- Added color to the progress widgets (jason.dobies@redhat.com)
- Syntax cleanup for 2.4 (jason.dobies@redhat.com)
- Small prompt clarifications (jason.dobies@redhat.com)
- Changed publish to use rsync to make it quicker (jason.dobies@redhat.com)
- Added better test example (jason.dobies@redhat.com)

* Mon Feb 06 2012 Jay Dobies <jason.dobies@redhat.com> 1.0.3-1
- Added download links (jason.dobies@redhat.com)
- Added publish target (jason.dobies@redhat.com)
- Make the build noarch (jason.dobies@redhat.com)

* Mon Feb 06 2012 Jay Dobies <jason.dobies@redhat.com> 1.0.2-1
- Flushed out some unit tests (jason.dobies@redhat.com)
- Fixed typo (jason.dobies@redhat.com)
- Added interrupt simulation to the Script (jason.dobies@redhat.com)
- Ignoring PyCharm files and generated coverage reports
  (jason.dobies@redhat.com)
- Updated documentation for new approach to testing with prompts
  (jason.dobies@redhat.com)
- Added framework for shell documentation (jason.dobies@redhat.com)
- Tweaked testability classes (jason.dobies@redhat.com)
- Added prompt usage and examples (jason.dobies@redhat.com)
- These look better prefaced with get_ (jason.dobies@redhat.com)
- Added tag support for writes as well. Added utility methods to retrieve tags.
  (jason.dobies@redhat.com)
- Moved interruptable functionality to read method (jason.dobies@redhat.com)
- Added progress module usage documentation (jason.dobies@redhat.com)
- Use terminal size if not specified (jason.dobies@redhat.com)
- Overview page documentation (jason.dobies@redhat.com)
- Added shortcut to wrap from write() and terminal size calculation
  (jason.dobies@redhat.com)
- Updated copyright date and version (jason.dobies@redhat.com)
- Fixed documentation for ABORT (jason.dobies@redhat.com)
- More sphinx clean up (jason.dobies@redhat.com)
- Added wrapped iterator support to progress bar (jason.dobies@redhat.com)
- Migrated comments to rest syntax (jason.dobies@redhat.com)
- Updated docstrings for rest format (jason.dobies@redhat.com)
- Restructured docs index (jason.dobies@redhat.com)
- Removed generated docs from sphinx directory (jason.dobies@redhat.com)
- Initial implementation of sphinx documentation (jason.dobies@redhat.com)
- Fixed issue with usage rendering for sections (jason.dobies@redhat.com)
- Propagate flags to recursive call (jason.dobies@redhat.com)
- Module level docs (jason.dobies@redhat.com)
- Changed in place rendering technique to not use save/reset since it's not
  overly supported. (jason.dobies@redhat.com)
- Added spinner implementation (jason.dobies@redhat.com)
- Initial revision of the progress bar (jason.dobies@redhat.com)
- Added save/reset position calls (jason.dobies@redhat.com)
- Reworked clear behavior and added move command (jason.dobies@redhat.com)
- Added clear method and reordered file (jason.dobies@redhat.com)
- Added instance-level color disabling (jason.dobies@redhat.com)
- Changed default behavior to interruptable (jason.dobies@redhat.com)
- Added safe_start ability and enhanced rendering capabilities
  (jason.dobies@redhat.com)
- Added logic to calculate centering text (jason.dobies@redhat.com)
- Added auto-wrapping (jason.dobies@redhat.com)
- Added more colors (jason.dobies@redhat.com)
- Added first sample shell and made some fixes accordingly
  (jason.dobies@redhat.com)
- Continuing on prompt unit tests (jason.dobies@redhat.com)
