%global pypi_name jsonfield

Name:           python-%{pypi_name}
Version:        3.1.0
Release:        5%{?dist}
Summary:        A reusable Django field that allows you to store validated JSON in your model
License:        MIT
URL:            https://github.com/rpkilby/jsonfield
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch            

BuildRequires:  sqlite
BuildRequires:  python3-django
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description            
jsonfield is a reusable Django field that allows you to store validated            
JSON in your model. It silently takes care of serialization. To use, simply            
add the field to one of your models.

%package -n python3-%{pypi_name}
Summary: %{summary}

Obsoletes:      python-django-jsonfield < 2.0.2-8
Obsoletes:      python3-django-jsonfield < 2.0.2-8

%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}            
jsonfield is a reusable Django field that allows you to store validated            
JSON in your model. It silently takes care of serialization. To use, simply            
add the field to one of your models.

%prep            
%setup -q -n %{pypi_name}-%{version}

%build            
%py3_build

%install            
%py3_install

%check
PYTHONPATH=%{buildroot}%{python3_sitelib} %{python3} manage.py test

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 08 2020 Luis Bazan <lbazan@fedoraproject.org> - 3.1.0-2
- Rebuid and add obsolete package

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.1.0-2
- Rebuilt for Python 3.9

* Wed Apr 22 2020 Luis Bazan <lbazan@fedoraproject.org> - 3.1.0-1
- Rebuild
