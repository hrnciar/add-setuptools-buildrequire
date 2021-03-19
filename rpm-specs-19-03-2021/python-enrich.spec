%global srcname enrich

Name:    python-%{srcname}
Version: 1.2.6
Release: 2%{?dist}
Summary: Enrich adds few missing features to the wonderful rich library

URL:     https://github.com/pycontribs/enrich
Source:  %{pypi_source}
License: MIT

# Removing the --duration-min option from pytest call (not supported in pytest < 6.1)
patch0: 0001-remove-unsuported-pytest-option.patch

BuildArch: noarch

BuildRequires: python3-devel
BuildRequires: python3dist(rich)
BuildRequires: python3dist(setuptools)
BuildRequires: python3dist(setuptools-scm)

# testing requirements
BuildRequires: python3dist(pytest)
BuildRequires: python3dist(pytest-cov)
BuildRequires: python3dist(pytest-mock)
BuildRequires: python3dist(pytest-xdist)

%global _description %{expand:
rich library functionality with a set of changes that were not accepted
to rich itself.
}

%description %{_description}

%package -n python3-%{srcname}
Summary: Enrich adds few missing features to the wonderful rich library

Requires: python3dist(rich)

%py_provides python3-%{srcname}
%description -n python3-%{srcname} %{_description}

%prep
%autosetup -p1 -n %{srcname}-%{version}


%build
%py3_build

%install
%py3_install

%check
PYTHONPATH=src %{python3} -m pytest src/enrich/test -v

%files -n python3-%{srcname}
%license LICENSE
%{python3_sitelib}/enrich/
%{python3_sitelib}/enrich-*.egg-info/

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec 22 2020 Chedi Toueiti <chedi.toueiti@gmail.com> - 1.2.6-1
- Initial commit
