%global pypiname lunr

Name:           python-%{pypiname}
Version:        0.5.8
Release:        5%{?dist}
Summary:        A Python implementation of Lunr.js

License:        MIT
URL:            https://github.com/yeraydiazdiaz/lunr.py
Source0:        https://github.com/yeraydiazdiaz/lunr.py/archive/%{version}.tar.gz#/%{pypiname}.py-%{version}.tar.gz

BuildArch:      noarch


%global _description %{expand:
This Python version of Lunr.js aims to bring the simple and powerful full text
search capabilities into Python guaranteeing results as close as the original
implementation as possible.}

%description %_description

%package -n python3-%{pypiname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
%{?python_provide:%python_provide python3-%{pypiname}}

#Some nltk resource is needed to run tests but not available in Fedora
# BuildRequires:  python3-six
# BuildRequires:  python3-future
# BuildRequires:  python3-pytest
# BuildRequires:  python3-pytest-timeout
# BuildRequires:  python3-mock
# BuildRequires:  python3dist(nltk) >= 3.2.5
# BuildRequires:  /usr/bin/coverage

%{?python_extras_subpkg:Recommends:  python3-%{pypiname}+languages}
%{!?python_extras_subpkg:Recommends: python3dist(nltk) >= 3.2.5}

%description -n python3-%{pypiname} %_description

%{?python_extras_subpkg:%python_extras_subpkg -n python3-%{pypiname} -i %{python3_sitelib}/%{pypiname}-*.egg-info languages}


%prep
%autosetup -n %{pypiname}.py-%{version}

%build
%py3_build

%install
%py3_install

%check
#make tests

%files -n python3-%{pypiname}
%license LICENSE
%doc README.md CHANGELOG.md readme.rst docs/
%{python3_sitelib}/%{pypiname}-*.egg-info/
%{python3_sitelib}/%{pypiname}/

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Miro Hron??ok <mhroncok@redhat.com> - 0.5.8-3
- Add lunr[languages] subpackage

* Thu Jun 25 2020 Robin Lee <cheeselee@fedoraproject.org> - 0.5.8-2
- BR python3dist(setuptools)

* Fri Jun 12 2020 Qiyu Yan <yanqiyu01@gmail.com> - 0.5.8-1
- Update to 0.5.8

* Tue May 26 2020 Miro Hron??ok <mhroncok@redhat.com> - 0.5.6-2
- Rebuilt for Python 3.9

* Sun Mar  8 2020 Robin Lee <cheeselee@fedoraproject.org> - 0.5.6-1
- Initial packaging
