# EPEL is missing dependencies required for docs and tests
%if 0%{?rhel}
%bcond_with docs
%bcond_with tests
%else
%bcond_without docs
%bcond_without tests
%endif

%global pypi_name TestSlide

Name:           python-%{pypi_name}
Version:        2.6.4
Release:        4%{?dist}
Summary:        A Python test framework

License:        MIT
URL:            https://github.com/facebookincubator/TestSlide
# The PyPI tarball doesn't include tests, so use the original source instead
Source0:        %{url}/archive/%{version}.tar.gz#/%{pypi_name}-%{version}.tar.gz
# PR#271: move dependency management to requirements.txt and requirements-dev.txt
Patch0:         %{url}/commit/9a62c484ca9360ea8dfca82b244589c733182449.patch
# PR#272: requirements: relax dataclasses version dependency
Patch1:         %{url}/commit/f0a82aa1bf93863794e8a9867cb34df14fdf62a4.patch
# PR#273: requirements: allow Pygments 2.2.0 or later
Patch2:         %{url}/commit/fa69263d6eaf07df5090dad4c199d1c6d14abf05.patch
%if 0%{?fedora} < 33
# pygments 2.4.x in F32 does not support ipython code blocks
Patch3:         %{pypi_name}-%{version}-no_ipython.patch
# flake8 fails on testslide directory:
#   testslide/lib.py:19:5: F401 'testslide.mock_callable._CallableMock' imported but unused
#   testslide/lib.py:20:5: F401 'testslide.strict_mock.StrictMock' imported but unused
#   testslide/lib.py:20:5: F401 'testslide.strict_mock._DefaultMagic' imported but unused
# isort does not support --profile option
Patch4:         %{pypi_name}-%{version}-relax_lints.patch
%endif
# PR#297: Use get_typing_hints instead of __annotations__ to resolve types in Python 3.10
Patch5:         %{url}/commit/44990479e035a05fc265e7e88c8a14f5c01590d2.patch
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 38.6
BuildRequires:  sed

%if %{with docs}
# Docs requirements
BuildRequires:  make
BuildRequires:  ncurses
BuildRequires:  python3-ipython
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-kr-theme)
%endif

%if %{with tests}
# Test requirements
BuildRequires:  black
BuildRequires:  make
BuildRequires:  python3dist(coverage)
BuildRequires:  python3dist(flake8)
BuildRequires:  python3dist(isort)
BuildRequires:  python3dist(mypy)
BuildRequires:  python3dist(psutil)
BuildRequires:  python3dist(pygments)
BuildRequires:  python3dist(typeguard)
%endif

%description
A test framework for Python that enable unit testing / TDD / BDD to be
productive and enjoyable.

Its well behaved mocks with thorough API validations catches bugs both
when code is first written or long in the future when it is changed.

The flexibility of using them with existing unittest.TestCase or TestSlide's
own test runner let users get its benefits without requiring refactoring
existing code.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%if 0%{?fedora} < 33 || 0%{?rhel} < 9
%py_provides    python3-%{pypi_name}
%endif

%description -n python3-%{pypi_name}
A test framework for Python that enable unit testing / TDD / BDD to be
productive and enjoyable.

Its well behaved mocks with thorough API validations catches bugs both
when code is first written or long in the future when it is changed.

The flexibility of using them with existing unittest.TestCase or TestSlide's
own test runner let users get its benefits without requiring refactoring
existing code.

%if %{with docs}
%package -n     python3-%{pypi_name}-docs
Summary:        Documentation for python3-%{pypi_name}

%description -n python3-%{pypi_name}-docs
The python3-%{pypi_name}-docs package contains documentation for
python3-%{pypi_name}.
%endif

%prep
%autosetup -n %{pypi_name}-%{version} -p1
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build
%if %{with docs}
make docs V=1
%endif

%install
%py3_install

%if %{with tests}
%check
export PYTHONPATH=%{buildroot}%{python3_sitelib}
make tests V=1
%endif

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{_bindir}/testslide
%{python3_sitelib}/testslide
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%if %{with docs}
%files -n python3-%{pypi_name}-docs
%doc docs/_build/html
%endif

%changelog
* Thu Apr 15 2021 Davide Cavalca <dcavalca@fedoraproject.org> - 2.6.4-4
- Backport PR#297 for Python 3.10 compatibility (#1944109)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.4-3.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 14 2021 Michel Alexandre Salim <salimma@fedoraproject.org> - 2.6.4-2.1
- Fix documentation build and skip some lints on F32 and below

* Tue Jan  5 2021 Davide Cavalca <dcavalca@fedoraproject.org> - 2.6.4-2
- Backport PR#271, PR#272 and PR#273 to adjust requirements for EPEL 8

* Sat Jan  2 2021 Davide Cavalca <dcavalca@fedoraproject.org> - 2.6.4-1
- New upstream release

* Wed Dec 30 2020 Davide Cavalca <dcavalca@fedoraproject.org> - 2.6.3-2
- Build for EPEL 8

* Thu Nov 12 2020 Davide Cavalca <dcavalca@fedoraproject.org> - 2.6.3-1
- New upstream release

* Mon Nov  2 2020 Davide Cavalca <dcavalca@fedoraproject.org> - 2.6.1-3
- Backport PR#260, PR#261, PR#262
- Add py_provides for F32
- Build and package docs
- Run tests

* Tue Oct 27 2020 Davide Cavalca <dcavalca@fb.com> - 2.6.1-2
- Update BuildRequires
- Remove unneeded shebangs
- Drop unnecessary python_provide macro

* Tue Oct 27 2020 Davide Cavalca <dcavalca@fb.com> - 2.6.1-1
- Initial package
- Disable tests and docs for now
