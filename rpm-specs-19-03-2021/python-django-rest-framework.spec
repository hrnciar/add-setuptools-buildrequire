%global pypi_name djangorestframework

Name:           python-django-rest-framework
Version:        3.12.2
Release:        1%{?dist}
Summary:        Web APIs for Django, made easy

License:        BSD
URL:            http://www.django-rest-framework.org
Source0:        https://github.com/encode/django-rest-framework/archive/%{version}.tar.gz#/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
Django REST framework is a powerful and flexible toolkit that makes it easy
to build Web APIs.

Some reasons you might want to use REST framework:

* The Web browsable API is a huge usability win for your developers.
* Authentication policies including OAuth1a and OAuth2 out of the box.
* Serialization that supports both ORM and non-ORM data sources.
* Customizable all the way down - just use regular function-based views if
  you don't need the more powerful features.
* Extensive documentation, and great community support.


%package -n python3-django-rest-framework
Summary:        Web APIs for Django, made easy
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-django-rest-framework}

Obsoletes: python2-django-rest-framework < 3.7.7-2
Obsoletes: python-django-rest-framework < 3.7.7-2

%description -n python3-django-rest-framework
Django REST framework is a powerful and flexible toolkit that makes it easy
to build Web APIs.

Some reasons you might want to use REST framework:

* The Web browsable API is a huge usability win for your developers.
* Authentication policies including OAuth1a and OAuth2 out of the box.
* Serialization that supports both ORM and non-ORM data sources.
* Customizable all the way down - just use regular function-based views if
  you don't need the more powerful features.
* Extensive documentation, and great community support.


%prep
%autosetup -n django-rest-framework-%{version}

echo "recursive-include rest_framework/locale *.mo" >> MANIFEST.in

# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

# remove .po files
find . -name *.po -exec rm -f '{}' \;

%build
%py3_build

%install
%py3_install

%find_lang django

%files -n python3-django-rest-framework -f django.lang

%license
%{python3_sitelib}/rest_framework/__pycache__
%dir %{python3_sitelib}/rest_framework/
%{python3_sitelib}/rest_framework/authtoken
%dir %{python3_sitelib}/rest_framework/locale
%dir %{python3_sitelib}/rest_framework/locale/??/
%dir %{python3_sitelib}/rest_framework/locale/??/LC_MESSAGES
%dir %{python3_sitelib}/rest_framework/locale/??_??/
%dir %{python3_sitelib}/rest_framework/locale/??_??/LC_MESSAGES
%{python3_sitelib}/rest_framework/management
%{python3_sitelib}/rest_framework/schemas
%{python3_sitelib}/rest_framework/static
%{python3_sitelib}/rest_framework/templates
%{python3_sitelib}/rest_framework/templatetags
%{python3_sitelib}/rest_framework/utils
%{python3_sitelib}/rest_framework/*.py*
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Mon Feb 01 2021 Matthias Runge <mrunge@redhat.com> - 3.12.2-1
- rebase to 3.12.2 (rbz#1866277)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec 07 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 3.11.0-5
- Drop duplicated Requires

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hron??ok <mhroncok@redhat.com> - 3.11.0-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 03 2020 Matthias Runge <mrunge@redhat.com> - 3.11.0
- update to 3.11.0 (rhbz#1782883)

* Thu Sep 05 2019 Matthias Runge <mrunge@redhat.com> - 3.10.3
- update to 3.10.3 (rhbz#1742938)

* Mon Aug 19 2019 Miro Hron??ok <mhroncok@redhat.com> - 3.9.4-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jul 04 2019 Matthias Runge <mrunge@redhat.com> - 3.9.4-1
- update to 3.9.4 (rhbz#1684922)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Sep 04 2018 Matthias Runge <mrunge@redhat.com> - 3.8.2-1
- update to 3.8.2 (rhbz#156705)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hron??ok <mhroncok@redhat.com> - 3.8.1-2
- Rebuilt for Python 3.7

* Thu Apr 05 2018 Matthias Runge <mrunge@redhat.com> - 3.8.1-1
- update to 3.8.1 (rhbz#1528477)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 30 2018 Matthias Runge <mrunge@redhat.com> - 3.7.7-2
- drop Python2 subpackage for https://fedoraproject.org/wiki/Changes/Django20

* Wed Jan 24 2018 Matthias Runge <mrunge@redhat.com> - 3.7.7-1
- rebase to 3.7.7

* Thu Dec 21 2017 Matthias Runge <mrunge@redhat.com> - 3.7.4-1
- update to 3.7.4 (rhbz#1528080)

* Tue Nov 07 2017 Matthias Runge <mrunge@redhat.com> - 3.7.3-1
- update to 3.7.3 (rhbz#1387806)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hron??ok <mhroncok@redhat.com> - 3.5.2-2
- Rebuild for Python 3.6

* Wed Nov 02 2016 Matthias Runge <mrunge@redhat.com> - 3.5.2-1
- update to 3.5.2 (rhbz#1387806)

* Fri Oct 21 2016 Matthias Runge <mrunge@redhat.com> - 3.5.0-1
- update to 3.5.0
- modernize spec file

* Thu Sep 22 2016 Matthias Runge <mrunge@redhat.com> - 3.4.7-1
- update to 3.4.7 (rhbz#1317496)

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.2-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 18 2016 Matthias Runge <mrunge@redhat.com> - 3.3.2-3
- Fix python3 conditionals (rhbz#1399432)
- provide proper python2 and python3 packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 27 2016 Matthias Runge <mrunge@redhat.com> - 3.3.2-1
- update to 3.3.2 (rhbz#1301379)

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue May 05 2015 Matthias Runge <mrunge@redhat.com> - 3.1.1-3
- handle locales better (rhbz#1197605)

* Tue May 05 2015 Matthias Runge <mrunge@redhat.com> - 3.1.1-2
- add python-setuptools to BR

* Tue May 05 2015 Matthias Runge <mrunge@redhat.com> - 3.1.1-1
- update to 3.1.1
- add python3 subpackage

* Fri Feb 27 2015 Matthias Runge <mrunge@redhat.com> - 3.0.5-1
- Initial package. (rhbz#1197605)
