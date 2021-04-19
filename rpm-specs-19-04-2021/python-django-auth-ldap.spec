%if 0%{?rhel}
# RHEL does not ship openldap-server :(
%bcond_with check
%else
%bcond_without check
%endif

%global srcname django-auth-ldap

Name:           python-%{srcname}
Version:        2.2.0
Release:        2%{?dist}
Summary:        Django LDAP authentication backend

License:        BSD
URL:            https://pypi.org/project/django-auth-ldap
Source:         %{pypi_source}

BuildArch:      noarch

%description
%{summary}.

%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
%if %{with check}
BuildRequires:  python3dist(django) >= 1.1
BuildRequires:  python3dist(python-ldap) >= 3.1
BuildRequires:  /usr/bin/ldapadd
BuildRequires:  /usr/sbin/slapd
BuildRequires:  python3dist(mock)
%endif

%description -n python3-%{srcname}
%{summary}.

%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%if %{with check}
%check
%python3 -m django test --settings tests.settings
%endif

%files -n python3-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/django_auth_ldap-*.egg-info/
%{python3_sitelib}/django_auth_ldap/

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Dec 11 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 2.2.0-1
- Initial package
