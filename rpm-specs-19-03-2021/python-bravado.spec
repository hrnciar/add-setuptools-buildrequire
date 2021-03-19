%global pypi_name bravado

Name:           python-%{pypi_name}
Version:        11.0.2
Release:        2%{?dist}
Summary:        Library for accessing Swagger-enabled API's

License:        BSD
URL:            https://github.com/Yelp/bravado
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
Bravado is a Yelp maintained fork of digium/swagger-py for use with
OpenAPI Specification version 2.0 (previously known as Swagger).


%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Bravado is a Yelp maintained fork of digium/swagger-py for use with
OpenAPI Specification version 2.0 (previously known as Swagger).


%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 11.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Nov 18 2020 Nils Philippsen <nils@redhat.com> - 11.0.2-1
- Version 11.0.2

* Tue Sep 08 2020 Aurelien Bompard <abompard@fedoraproject.org> - 10.6.2-1
- Initial package.
