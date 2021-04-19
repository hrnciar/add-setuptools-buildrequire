%global pkgname mongoengine
%global sum A Python Document-Object Mapper for working with MongoDB
%global desc MongoEngine is a Document-Object Mapper (think ORM, \
but for document databases) for working with MongoDB \
from Python. It uses a simple declarative API, similar \
to the Django ORM.
 
 
Name: python-mongoengine
Version: 0.23.0
Release: 1%{?dist}
BuildArch: noarch
 
License: MIT
Summary: %{sum}
URL:     http://mongoengine.org/
Source0: %{pypi_source %pkgname}
# pymongo and pymongo-gridfs is needed for the docs
BuildRequires: python3-pymongo
BuildRequires: python3-pymongo-gridfs
BuildRequires: python3-sphinx
BuildRequires: python3-sphinx_rtd_theme
BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3-readthedocs-sphinx-ext
BuildRequires: make
 
 
%description
%{desc}
 
 
%package -n python3-%{pkgname}
Summary: %{sum}
Recommends: python3-blinker
Recommends: python3-pillow
Requires: python3-pymongo
Requires: python3-pymongo-gridfs
 
 
%description -n python3-%{pkgname}
%{desc}
 
 
%package doc
Summary: Documentation for %{name}
BuildArch: noarch
 
 
%description doc
Documentation for %{name}.
 
 
%prep
%setup -q -n %{pkgname}-%{version}
find . -name '*.py' | xargs sed -i '1s|^#!.*|#!%{__python3}|'
 
 
%build
%py3_build
PYTHONPATH=$(pwd) make -C docs SPHINXBUILD=sphinx-build-3 html
rm -f docs/_build/html/.buildinfo
# Don't ship fonts
rm -rf docs/_build/html/_static/font
 
 
%install
%py3_install
 
%files -n python3-%{pkgname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pkgname}
%{python3_sitelib}/%{pkgname}-*.egg-info
 
 
%files doc
%license LICENSE
%doc docs/_build/html
 
 
%changelog
* Sat Apr 3 2021 Eduardo Echeverria <echevemaster@gmail.com> - 0.23.0-1
- Initial packaging

