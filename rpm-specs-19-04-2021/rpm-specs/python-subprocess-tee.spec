%global srcname subprocess-tee

Name:    python-%{srcname}
Version: 0.2.0
Release: 2%{?dist}
Summary: A subprocess.run that works like tee, being able to display output in real time while still capturing it

URL:     https://github.com/pycontribs/subprocess-tee
Source:  %{pypi_source}
License: MIT

# The following patches are related to the upstream bug
# https://github.com/pycontribs/subprocess-tee/issues/19
# as of the time of this release the current version of pytest in f33 is 6.0, so some
# modification had to be made to enable the tests and only the tests.

# Removing the --duration-min option from pytest call (not supported in pytest < 6.1)
patch0: 0001-remove-unsuported-pytest-option.patch
# Removing some test type annotation present only in pytest >= 6.1
patch1: 0002-remove-pytest-type-annotation.patch

BuildArch: noarch

BuildRequires: python3-devel
BuildRequires: python3dist(rich)
BuildRequires: python3dist(enrich)
BuildRequires: python3dist(setuptools)
BuildRequires: python3dist(setuptools-scm)

# testing requirements
BuildRequires: python3dist(pytest)
BuildRequires: python3dist(pytest-cov)
BuildRequires: python3dist(pytest-mock)
BuildRequires: python3dist(pytest-xdist)

%global _description %{expand:
This package provides an drop-in alternative to subprocess.run that captures
the output while still printing it in real time, just the way tee does.
}

%description %{_description}

%package -n python3-%{srcname}
Summary: A subprocess.run that works like tee, being able to display output in real time while still capturing it

Requires: python3dist(rich)
Requires: python3dist(enrich)

%py_provides python3-%{srcname}
%description -n python3-%{srcname} %{_description}

%prep
%autosetup -p1 -n %{srcname}-%{version}


%build
%py3_build

%install
%py3_install

%check
%{python3} -m pytest lib/subprocess_tee/test -v

%files -n python3-%{srcname}
%license LICENSE
%{python3_sitelib}/subprocess_tee/
%{python3_sitelib}//subprocess_tee-*.egg-info/

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 03 2021 Chedi Toueiti <chedi.toueiti@gmail.com> - 0.2.0-1
- Update to version 0.2.0

* Wed Nov 25 2020 Chedi Toueiti <chedi.toueiti@gmail.com> - 0.1.5-1
- Initial commit
