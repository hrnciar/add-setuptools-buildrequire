%global pypi_name restfly

Name:           python-%{pypi_name}
Version:        1.3.5
Release:        3%{?dist}
Summary:        Library to make API wrappers creation easier

License:        MIT
URL:            https://github.com/stevemcgrath/restfly
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
RESTfly is a framework for building libraries to easily interact with RESTful
APIs.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  %py3_dist setuptools
BuildRequires:  %py3_dist requests
BuildRequires:  %py3_dist pytest
BuildRequires:  %py3_dist pytest-cov
BuildRequires:  %py3_dist pytest-vcr
BuildRequires:  %py3_dist pytest-datafiles
BuildRequires:  %py3_dist python-box
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
RESTfly is a framework for building libraries to easily interact with RESTful
APIs.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%pytest -v tests

%files -n python3-%{pypi_name}
%doc README.rst
%license LICENSE
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py*.egg-info/

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Dec 16 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.3.5-2
- Update macros

* Sun Aug 09 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.3.5-1
- Update to new upstream release 1.3.5 (#1858206)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 17 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.3.4-1
- Update to new upstream release 1.3.4 (#1858206)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.1.1-2
- Rebuilt for Python 3.9

* Thu Mar 19 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.1.1-1
- Initial package for Fedora
