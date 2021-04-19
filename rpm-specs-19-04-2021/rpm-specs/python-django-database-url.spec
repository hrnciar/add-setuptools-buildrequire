%global srcname dj_database_url

Name:           python-django-database-url
Version:        0.5.0
Release:        11%{?dist}
Summary:        Use Database URLs in your Django Application
License:        BSD
URL:            https://github.com/kennethreitz/dj-database-url
Source0:        https://github.com/kennethreitz/dj-database-url/archive/v%{version}.tar.gz#/dj-database-url-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%global _description\
This simple Django utility allows you to utilize the 12factor inspired\
DATABASE_URL environment variable to configure your Django application.

%description %_description

%package -n python3-django-database-url
Summary:        %summary
Requires:       python3-django
Obsoletes:      python-django-database-url < 0.4.2-4
Obsoletes:      python2-django-database-url < 0.4.2-4
%{?python_provide:%python_provide python3-django-database-url}

%description -n python3-django-database-url %_description
This simple Django utility allows you to utilize the 12factor inspired
DATABASE_URL environment variable to configure your Django application.

%prep
%autosetup -n dj-database-url-%{version}

%build
%py3_build

%install
%py3_install

%check
%{__python3} test_dj_database_url.py

%files -n python3-django-database-url
%doc README.rst
%license LICENSE
%{python3_sitelib}/%{srcname}.py*
%{python3_sitelib}/__pycache__/%{srcname}.cpython-*.py*
%{python3_sitelib}/%{srcname}-%{version}-py*.egg-info

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.5.0-9
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.0-7
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.0-6
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.5.0-2
- Rebuilt for Python 3.7

* Tue Mar 06 2018 Juan Orti Alcaine <jorti@fedoraproject.org> - 0.5.0-1
- New version 0.5.0

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Feb 05 2018 Juan Orti Alcaine <jorti@fedoraproject.org> - 0.4.2-4
- Remove Python2 subpackage

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jul 01 2017 Juan Orti Alcaine <jorti@fedoraproject.org> - 0.4.2-2
- Python3 changes

* Sun Feb 26 2017 Juan Orti Alcaine <jorti@fedoraproject.org> - 0.4.2-1
- Version 0.4.2

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.4.0-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Juan Orti Alcaine <jorti@fedoraproject.org> - 0.4.0-1
- Version 0.4.0

* Wed Nov 18 2015 Juan Orti Alcaine <jorti@fedoraproject.org> - 0.3.0-7
- Use python_provide macro
- Substitute some commands with macros

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Apr 09 2015 Juan Orti Alcaine <jorti@fedoraproject.org> - 0.3.0-4
- Use license macro

* Thu Dec 11 2014 Juan Orti <jorti@fedoraproject.org> - 0.3.0-3
- Add Python3 support
- Change Source0 to GitHub
- Run tests

* Wed Dec 03 2014 Juan Orti <jorti@fedoraproject.org> - 0.3.0-2
- Spec file cleanup

* Mon May 26 2014 Didier Fabert <didier.fabert@gmail.com> 0.3.0-1
- Initial RPM release
