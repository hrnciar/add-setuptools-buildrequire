# https://github.com/ValvePython/vdf/issues/33
%if 0%{?f32}
%bcond_with tests
%else
%bcond_without tests
%endif

%global pypi_name vdf

Name:       python-%{pypi_name}
Version:    3.3
Release:    3%{?dist}
Summary:    Package for working with Valve's text and binary KeyValue format
BuildArch:  noarch

License:    MIT
URL:        https://github.com/ValvePython/vdf
Source0:    %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz

BuildRequires: python3-devel
BuildRequires: python3dist(setuptools)
BuildRequires: python3dist(mock)
BuildRequires: python3dist(pytest-cov) >= 2.7.0
BuildRequires: python3dist(pytest)

%global _description %{expand:
Pure python module for (de)serialization to and from VDF that works just like
json.}

%description %{_description}


%package -n python3-%{pypi_name}
Summary:    %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name} %{_description}


%prep
%autosetup -n %{pypi_name}-%{version} -p1


%build
%py3_build


%install
%py3_install


%if %{with tests}
%check
%{python3} -m pytest -v
%endif


%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}*.egg-info


%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Jan 23 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 3.3-2
- build: polish to conform Fedora guidelines

* Wed Sep 16 2020 gasinvein <gasinvein@gmail.com> - 3.3-0.1
- Initial package
