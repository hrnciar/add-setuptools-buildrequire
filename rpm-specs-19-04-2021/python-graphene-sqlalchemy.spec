%global srcname graphene-sqlalchemy
%global pythonicname graphene_sqlalchemy
%global sum Graphene SQLAlchemy integration


Name:           python-%{srcname}
Version:        2.3.0
Release:        2%{?dist}
Summary:        %{sum}

License:        BSD
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        %{pypi_source}
# License text is not provided within Pypi sources
Source1:        LICENSE

BuildArch:      noarch

%global _description %{expand:
A SQLAlchemy integration for Graphene.}

%description %_description


%package -n python3-%{srcname}
Summary:        %{sum}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%py_provides python3-%{srcname}

%description -n python3-%{srcname} %_description


%prep
%autosetup -n %{srcname}-%{version}

cp %{SOURCE1} .

# Remove egg files from source
rm -r %{pythonicname}.egg-info


%build
%py3_build


%install
%py3_install


%files -n python3-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pythonicname}/
%{python3_sitelib}/*.egg-info/


%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Nov 22 2020 Mattia Verga <mattia.verga@protonmail.com> - 2.3.0-1
- Initial packaging
