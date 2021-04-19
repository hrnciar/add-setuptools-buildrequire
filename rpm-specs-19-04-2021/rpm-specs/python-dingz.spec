%global pypi_name dingz

Name:           python-%{pypi_name}
Version:        0.3.0
Release:        2%{?dist}
Summary:        Python API client for interacting with dingz devices

License:        ASL 2.0
URL:            https://github.com/home-assistant-ecosystem/python-dingz
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
Asynchronous Python API client for interacting with dingz devices.

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Asynchronous Python API client for interacting with dingz devices.

%package -n %{pypi_name}
Summary:        CLI tool to interact with dingz devices

Requires:       python3-%{pypi_name} = %{?epoch:%{epoch}:}%{version}-%{release}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n %{pypi_name}
CLI tool to interact with dingz devices.

%prep
%autosetup -n %{name}-%{version}

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.rst
%license LICENSE
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/python_%{pypi_name}*.egg-info/

%files -n %{pypi_name}
%{_bindir}/%{pypi_name}

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Nov 13 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.0-1
- Add CLI tool
- Update to latest upstream release 0.3.0

* Sun Nov 08 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.0-1
- Initial package for Fedora
