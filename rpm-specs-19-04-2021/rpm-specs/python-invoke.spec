Name:		python-invoke
Version:	1.5.0
Release:	2%{?dist}
Summary:	A Python task execution tool and library
License:	BSD
URL:		http://pyinvoke.org/
Source0:	https://github.com/pyinvoke/invoke/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:		0001-Fallback-to-system-lib-if-vendorized-one-does-not-ex.patch
Patch2:		invoke-1.5.0-pytest-too-recent.patch
BuildArch:	noarch
BuildRequires:	python3-devel
BuildRequires:	%{py3_dist setuptools}
BuildRequires:	%{py3_dist fluidity-sm}
BuildRequires:	%{py3_dist lexicon}
BuildRequires:	%{py3_dist PyYAML}
BuildRequires:	%{py3_dist six}
# For test suite
BuildRequires:	%{py3_dist mock}
BuildRequires:	%{py3_dist pytest}
BuildRequires:	%{py3_dist pytest-relaxed}

%description
Invoke is a Python task execution tool and library, drawing inspiration from
various sources to arrive at a powerful and clean feature set.

%package -n python3-invoke
Summary:	A Python task execution tool and library
%{?python_provide:%python_provide python3-invoke}
Obsoletes:	python2-invoke < 1.2.0-5
Requires:	%{py3_dist fluidity-sm}
Requires:	%{py3_dist lexicon}
Requires:	%{py3_dist PyYAML}
Requires:	%{py3_dist six}

%description -n python3-invoke
Invoke is a Python task execution tool and library, drawing inspiration from
various sources to arrive at a powerful and clean feature set.

%prep
%setup -q -n invoke-%{version}

# Avoid need for bundled libs in test suite
%patch0 -p1

# Handing of stdin in more recent pytest versions breaks runner tests, similar to
# https://github.com/pyinvoke/invoke/issues/530
# Work around this by skipping all affected tests (most of them, unfortunately)
%patch2

# Remove bundled egg-info
rm -fr invoke.egg-info/

# Remove bundled libs, import will fallback to system provided libs
rm -rvf invoke/vendor/*

%build
%py3_build

%install
%py3_install

# Backwards compatible links
ln -s inv %{buildroot}%{_bindir}/inv3
ln -s invoke %{buildroot}%{_bindir}/invoke3

%check
PYTHONDONTWRITEBYTECODE=1 \
PYTHONPATH=%{buildroot}%{python3_sitelib} \
pytest-3

%files -n python3-invoke
%license LICENSE
%doc README.rst
%{_bindir}/inv
%{_bindir}/inv3
%{_bindir}/invoke
%{_bindir}/invoke3
%{python3_sitelib}/invoke/
%{python3_sitelib}/invoke-%{version}-*.egg-info/

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Dec 31 2020 Paul Howarth <paul@city-fan.org> - 1.5.0-1
- Update to 1.5.0
  - Allow any string-compatible object to be passed to 'Context.cd', enabling
    use of (for example) 'pathlib.Path' instances (GH#454, GH#577, GH#583,
    GH#607, GH#681)
  - Don't silently discard help text for task arguments whose names happen to
    contain underscores (GH#409, GH#580, GH#611)
  - Don't silently ignore task help specifiers that don't actually map to the
    decorated task's arguments (e.g. '@task(help={"foo": "help for foo"})'
    wrapping a task without a 'foo' argument) (GH#398, GH#580, GH#611)
  - Allow subcollections to act as the default 'tasks' of their parent
    collections (via the new 'default' kwarg to
    '~invoke.collection.Collection.add_collection'); this means that
    non-trivial task trees can specify, e.g. "use my test subcollection's
    default task as the global default task" and similar (GH#197)
  - Enhanced test coverage in a handful of modules whose coverage was under 90%%
  - '~invoke.context.MockContext' now populates its 'NotImplementedError'
    exception instances (typically raised when a command is executed that had
    no pre-prepared result) with the command string that triggered them; this
    makes it much easier to tell what exactly in a test caused the error
  - '~invoke.context.MockContext' now accepts a few quality-of-life shortcuts
    as keys and values in its 'run'/'sudo' arguments:
    - Keys may be compiled regular expression objects, as well as strings, and
      will match any calls whose commands match the regex
    - Values may be 'True' or 'False' as shorthand for otherwise empty
      '~invoke.runners.Result' objects with exit codes of '0' or '1'
      respectively
    - Values may also be strings, as shorthand for otherwise empty
      '~invoke.runners.Result' objects with those strings given as the 'stdout'
      argument
  - Add a new 'repeat' kwarg to '~invoke.context.MockContext' which, when True
    (default: False) causes stored results for its methods to be yielded
    repeatedly instead of consumed (GH#441)
  - Immutable iterable result values handed to '~invoke.context.MockContext'
    would yield errors (due to the use of 'pop()'); the offending logic has
    been retooled to be more iterator-focused and now works for tuples and etc.
  - Update the testing documentation a bit: cleaned up existing examples and
    added new sections for the other updates in the 1.5 release
  - Automatically populate the 'command' attribute of '~invoke.runners.Result'
    objects returned by '~invoke.context.MockContext' methods, with the command
    string triggering that result; previously, users had to do this by hand or
    otherwise suffered inaccurate result objects (GH#700)
  - Upgrade '~invoke.context.MockContext' to wrap its methods in 'Mock' objects
    if the '(unittest.)mock' library is importable; this makes testing
    Invoke-using codebases even easier

* Thu Jul 30 2020 Paul Howarth <paul@city-fan.org> - 1.4.1-4
- Use new-style dependencies, fixes FTBFS due to conflicting pytest requirements

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun May 24 2020 Miro Hrončok <mhroncok@redhat.com> - 1.4.1-2
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Paul Howarth <paul@city-fan.org> - 1.4.1-1
- Update to 1.4.1 (#1796269)
  - Explicitly strip out '__pycache__' (and for good measure, '.py[co]', which
    previously we only stripped from the 'tests/' folder) in our 'MANIFEST.in',
    since at least some earlier releases erroneously included such (GH#586)
  - Fix an issue with '~invoke.run' and friends having intermittent problems at
    exit time (symptom was typically about the exit code value being 'None'
    instead of an integer; often with an exception trace) (GH#660)
  - Close pseudoterminals opened by the '~invoke.runners.Local' class during
    'run(..., pty=True)'; previously, these were only closed incidentally at
    process shutdown, causing file descriptor leakage in long-running processes
    (GH#518)

* Sun Jan  5 2020 Paul Howarth <paul@city-fan.org> - 1.4.0-1
- Update to 1.4.0 (#1787868)
  - A corner case in #~invoke.context.Context.run# caused overridden streams to
    be unused if those streams were also set to be hidden, e.g.
    'run(command, hide=True, out_stream=StringIO())' would result in no writes
    to the 'StringIO' object (GH#637); this has been fixed - hiding for a given
    stream is now ignored if that stream has been set to some non-'None' (and
    in the case of 'in_stream', non-'False') value.
  - As part of feature work on GH#682, we noticed that the
    '~invoke.runners.Result' return value from '~invoke.context.Context.run'
    was inconsistent between dry-run and regular modes; for example, the
    dry-run version of the object lacked updated values for 'hide', 'encoding'
    and 'env' - this has been fixed
  - Add asynchronous behavior to '~invoke.runners.Runner.run' (GH#194, GH#682):
    - Basic asynchronicity, where the method returns as soon as the subprocess
      has started running, and that return value is an object with methods
      allowing access to the final result
    - "Disowning" subprocesses entirely, which not only returns immediately but
      also omits background threading, allowing the subprocesses to outlive
      Invoke's own process
    See the updated API docs for the '~invoke.runners.Runner' for details on
    the new 'asynchronous' and 'disown' kwargs enabling this behavior
  - Never accompanied the top-level singleton '~invoke.run' (which simply wraps
    an anonymous '~invoke.context.Context's 'run' method) with its logical
    sibling, '~invoke.sudo' - this has been remedied

* Thu Dec 12 2019 Paul Howarth <paul@city-fan.org> - 1.3.0-2
- Run (most of) the test suite
- Cosmetic spec changes

* Mon Oct 07 2019 Othman Madjoudj <athmane@fedoraproject.org> - 1.3.0-1
- Update to 1.3.0 (rhbz #1742597)

* Tue Sep 24 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.0-5
- Drop python2-invoke (#1741008)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.0-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jul 11 2019 Othman Madjoudj <athmane@fedoraproject.org> - 1.2.0-2
- Disable tests temporary

* Sat Mar 30 2019 Athmane Madjoudj <athmane@fedoraproject.org> - 1.2.0-1
- Update to 1.2.0 (rhbz #1600756)
- Remove upstreamed patches
- Add patch for bypass vendorized libs

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-2
- Rebuilt for Python 3.7

* Fri May 11 2018 Athmane Madjoudj <athmane@fedoraproject.org> - 1.0.0-1
- Update to 1.0.0 (rhbz #1576807)
- Add patch to fix the testsuite and enable it

* Tue May 01 2018 Athmane Madjoudj <athmane@fedoraproject.org> - 0.23.0-1
- Update to 0.23.0 (rhbz #)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.22.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 31 2018 Athmane Madjoudj <athmane@fedoraproject.org> - 0.22.1-1
- Update to 0.22.1 (rhbz #1539963)

* Wed Sep 20 2017 Athmane Madjoudj <athmane@fedoraproject.org> - 0.21.0-1
- Update to 0.21.0 (rhbz #1493323)

* Sat Aug 19 2017 Athmane Madjoudj <athmane@fedoraproject.org> - 0.20.4-2
- Use python versioned pkg in reqs/BR when possible

* Sat Aug 19 2017 Athmane Madjoudj <athmane@fedoraproject.org> - 0.20.4-1
- Update to 0.20.4 (rhbz #1481475)

* Sat Jul 29 2017 Athmane Madjoudj <athmane@fedoraproject.org> - 0.20.1-1
- Update to 0.20.1

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.19.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jul 02 2017 Athmane Madjoudj <athmane@fedoraproject.org> - 0.19.0-1
- Update to 0.19.0

* Fri May 26 2017 Athmane Madjoudj <athmane@fedoraproject.org> - 0.17.0-1
- Update to 0.17.0

* Sat Apr 22 2017 Athmane Madjoudj <athmane@fedoraproject.org> - 0.16.3-1
- Update to 0.16.3
- Remove upstreamed patch

* Sat Feb 18 2017 Athmane Madjoudj <athmane@fedoraproject.org> - 0.15.0-2
- Fix Deps/BR, remove -spec until unretired

* Sat Feb 18 2017 Athmane Madjoudj <athmane@fedoraproject.org> - 0.15.0-1
- Update to 0.15.0
- Rework unbundling part

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.14.0-2
- Rebuild for Python 3.6

* Sun Dec 11 2016 Athmane Madjoudj <athmane@fedoraproject.org> - 0.14.0-1
- Update to 0.14.0

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13.0-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue Jun 28 2016 Athmane Madjoudj <athmane@fedoraproject.org> - 0.13.0-2
- Remove retired deps

* Tue Jun 28 2016 Athmane Madjoudj <athmane@fedoraproject.org> - 0.13.0-1
- Update to 0.13.0
- Revamp the spec

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-6
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jan 11 2015 Athmane Madjoudj <athmane@fedoraproject.org> - 0.9.0-4
- Update deps

* Mon Dec 01 2014 Athmane Madjoudj <athmane@fedoraproject.org> - 0.9.0-3
- Update BR
- Minor fixes in files and install sections.

* Sat Nov 29 2014 Athmane Madjoudj <athmane@fedoraproject.org> - 0.9.0-2
- Remove bundled libs.
- Remove .egg-info dir
- Restrict files section
- Add some build options

* Fri Nov 14 2014 Athmane Madjoudj <athmane@fedoraproject.org> - 0.9.0-1
- Initial spec

