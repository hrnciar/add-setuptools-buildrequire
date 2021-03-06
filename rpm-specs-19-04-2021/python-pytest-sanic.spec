%global pypi_name pytest-sanic

Name:           python-%{pypi_name}
Version:        1.7.0
Release:        1%{?dist}
Summary:        Pytest plugin for Sanic

License:        ASL 2.0
URL:            https://github.com/yunstanford/pytest-sanic
Source0:        %{pypi_source}
BuildArch:      noarch

%description
A pytest plugin for Sanic. It helps you to test your code asynchronously 
very easy testing with async coroutines, common and useful fixtures, 
asynchronous fixture support, test_client/sanic_client and a test_server.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
A pytest plugin for Sanic. It helps you to test your code asynchronously 
very easy testing with async coroutines, common and useful fixtures, 
asynchronous fixture support, test_client/sanic_client and a test_server.

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/pytest_sanic/
%{python3_sitelib}/pytest_sanic-%{version}-py%{python3_version}.egg-info

%changelog
* Sat Feb 27 2021 Fabian Affolter <mail@fabian-affolter.ch> - 1.7.0-1
- Update to new upstream release 1.7.0 (#1933393)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Sep 26 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.6.2-1
- Update to new upstream release 1.6.2 (#1882883)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jun 06 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.6.1-1
- Initial package for Fedora