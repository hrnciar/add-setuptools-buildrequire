%global pypi_name case

# docs depend on package sphinx_celery
# https://github.com/celery/sphinx_celery
%global with_docs 0

Name:           python-%{pypi_name}
Version:        1.5.3
Release:        10%{?dist}
Summary:        Python unittest Utilities

License:        BSD
URL:            https://github.com/celery/case
Source0:        https://files.pythonhosted.org/packages/source/c/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
%{summary}.

%package -n     python3-%{pypi_name}
Summary:        Python unittest Utilities
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3-six
Requires:       python3-setuptools >= 0.7
Requires:       python3-nose >= 1.3.7
Requires:       python3-setuptools

BuildRequires:  python3-devel
BuildRequires:  python3-coverage >= 3.0
BuildRequires:  python3-setuptools
BuildRequires:  python3-nose
BuildRequires:  python3-six

%description -n python3-%{pypi_name}
%{summary}.

%if 0%{?with_docs} > 0
%package -n python-%{pypi_name}-doc
Summary:        case documentation
%description -n python-%{pypi_name}-doc
Documentation for case
%endif

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%if 0%{?with_docs} > 0
# generate html docs
sphinx-build docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}
%endif

%install
# Must do the subpackages' install first because the scripts in /usr/bin are
# overwritten with every setup.py install.
%py3_install


%check
%{__python3} setup.py test

%files -n python3-%{pypi_name}
%license LICENSE
%doc docs/templates/readme.txt README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%if 0%{?with_docs} > 0
%files -n python-%{pypi_name}-doc
%doc html
%endif

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon May 25 2020 Miro Hron??ok <mhroncok@redhat.com> - 1.5.3-8
- Rebuilt for Python 3.9

* Sun May 24 2020 Miro Hron??ok <mhroncok@redhat.com> - 1.5.3-7
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan  9 2020 Zbigniew J??drzejewski-Szmek <zbyszek@in.waw.pl> - 1.5.3-5
- Remove dependency on unittest2 (#1789200)

* Thu Oct 03 2019 Miro Hron??ok <mhroncok@redhat.com> - 1.5.3-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hron??ok <mhroncok@redhat.com> - 1.5.3-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 30 2019 Matthias Runge <mrunge@redhat.com> - 1.5.3-1
- drop python2 subpackage

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hron??ok <mhroncok@redhat.com> - 1.5.2-7
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 16 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.5.2-5
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 02 2017 Matthias Runge <mrunge@redhat.com> - 1.5.2-2
- add missing builddeps: python[23]-unittest2, python[23]-nose

* Tue Dec 27 2016 Matthias Runge <mrunge@redhat.com> - 1.5.2-1
- Initial package. (rhbz#1408868)
