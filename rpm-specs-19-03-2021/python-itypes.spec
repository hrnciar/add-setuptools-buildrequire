%global srcname itypes

Name:           python-%{srcname}
Version:        1.2.0
Release:        2%{?dist}
Summary:        Simple immutable types for python

License:        BSD
URL:            http://github.com/PavanTatikonda/itypes
Source0:        %{pypi_source}
Source1:        %{url}/raw/master/LICENSE.md

BuildArch:      noarch

%global _description %{expand:
%{summary}.}

%description %{_description}

%package     -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description -n python3-%{srcname} %{_description}

Python 3 version.

%prep
%autosetup -n %{srcname}-%{version} -p1
rm -vr *.egg-info
cp -a %{S:1} .

%build
%py3_build

%install
%py3_install

%files -n python3-%{srcname}
%license LICENSE.md
%{python3_sitelib}/itypes.py
%{python3_sitelib}/__pycache__/itypes.*
%{python3_sitelib}/itypes-*.egg-info/

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Dec 12 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.2.0-1
- Update to 1.2.0

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.1.0-2
- Rebuilt for Python 3.9

* Fri Jan 31 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.1.0-1
- Initial package
