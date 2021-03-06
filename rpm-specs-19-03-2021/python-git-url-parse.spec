%global srcname     git-url-parse
%global setup_flags PBR_VERSION=%{version}

Name:    python-%{srcname}
Version: 1.2.2
Release: 7%{?dist}
Summary: A simple GIT URL parser similar to giturlparse.py
License: MIT

URL:     https://github.com/coala/git-url-parse
Source0: https://pypi.io/packages/source/g/%{srcname}/%{srcname}-%{version}.tar.gz

BuildArch: noarch

BuildRequires: make
BuildRequires: python3-pbr
BuildRequires: python3-devel
BuildRequires: python3-pytest
BuildRequires: python3-sphinx
BuildRequires: python3-pytest-cov

%description
A simple GIT URL parser similar to giturlparse.py

%package -n python-%{srcname}-doc
Summary: %summary

%description -n python-%{srcname}-doc
Documentation for python-git-url-parse

%package -n python3-%{srcname}
Summary: %summary

Recommends: python-%{srcname}-doc

Requires: python3-pbr

%{?python_disable_dependency_generator}
%{?python_provide:%python_provide python3-%{srcname}}
%description -n python3-%{srcname}
A simple GIT URL parser similar to giturlparse.py

%prep
%autosetup -n %{srcname}-%{version}

%build
%{setup_flags} %{py3_build}

# generate html docs
cd doc
PYTHONPATH=.. make html
# remove the sphinx-build leftovers
rm -rf build/html/.{doctrees,buildinfo}

%install
%{setup_flags} %{py3_install}

%check
py.test-3 -vv

%files -n python3-%{srcname}
%license LICENSE
%{python3_sitelib}/giturlparse
%{python3_sitelib}/git_url_parse-%{version}-py%{python3_version}.egg-info

%files -n python-%{srcname}-doc
%license LICENSE
%doc *.rst
%doc doc/build/html

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Chedi Toueiti <chedi.toueiti@gmail.com> - 1.2.2-5
- Replace Python version globs with macros to support python 3.10

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.2.2-4
- Rebuilt for Python 3.9

* Wed Feb 26 2020 Chedi Toueiti <chedi.toueiti@gmail.com> - 1.2.2
- Initial package
