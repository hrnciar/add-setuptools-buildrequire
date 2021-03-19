%global srcname graphql-server
%global pythonicname graphql_server
%global sum GraphQL Server tools for powering your server


Name:           python-%{srcname}
Version:        3.0.0
Release:        4.b3%{?dist}
Summary:        %{sum}

License:        MIT
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        %{pypi_source graphql-server 3.0.0b3}

BuildArch:      noarch

%global _description %{expand:
GraphQL-Server is a base library that serves as a helper for
building GraphQL servers or integrations into existing web frameworks
using GraphQL-Core.}

%description %_description


%package -n python3-%{srcname}
Summary:        %{sum}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%py_provides python3-%{srcname}
%{?python_extras_subpkg:%python_extras_subpkg -n python3-graphql-server -i %{python3_sitelib}/*.egg-info flask webob aiohttp}

%description -n python3-%{srcname} %_description


%prep
%autosetup -n %{srcname}-%{version}b3

# Remove egg files from source
rm -r %{pythonicname}.egg-info


%build
%py3_build


%install
%py3_install


%files -n python3-%{srcname}
%license LICENSE
%doc README.md docs/
%{python3_sitelib}/%{pythonicname}/
%{python3_sitelib}/*.egg-info/


%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-4.b3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Dec 05 2020 Mattia Verga <mattia.verga@protonmail.com> - 3.0.0-3b3
- Update to 3.0.0b3

* Sat Dec 05 2020 Mattia Verga <mattia.verga@protonmail.com> - 3.0.0-2b2
- Do not provide sanic extras - fixes fedora#1901574

* Tue Nov 24 2020 Mattia Verga <mattia.verga@protonmail.com> - 3.0.0-1b2
- Initial packaging
