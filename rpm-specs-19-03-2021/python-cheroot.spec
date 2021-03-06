# Created by pyp2rpm-3.2.2
%global pypi_name cheroot
# sphinx-tabs not available in fedora for docs build
%bcond_with docs

Name:           python-%{pypi_name}
Version:        8.5.2
Release:        2%{?dist}
Summary:        Highly-optimized, pure-python HTTP server

License:        BSD
URL:            https://github.com/cherrypy/cheroot
Source0:        %{pypi_source}
BuildArch:      noarch

%description
Cheroot is the high performance, pure Python HTTP server used by CherryPy.Status
The test suite currently relies on pytest. It's being run via Travis
CI.Contribute Cheroot.

%package -n python3-%{pypi_name}
Summary:        %{summary}
Requires:       python3dist(six) >= 1.11
Requires:       python3dist(more-itertools) >= 2.6
Requires:       python3-pyOpenSSL
Requires:       python3dist(jaraco.functools)

BuildRequires:  python3-devel
BuildRequires:  python3-pyOpenSSL
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-cov)
BuildRequires:  python3dist(pytest-mock)
BuildRequires:  python3dist(jaraco.functools)

%if 0%{?el8}
BuildRequires:  python3dist(setuptools-scm)
BuildRequires:  python3dist(more-itertools) >= 2.6
%else
BuildRequires:  python3dist(setuptools-scm-git-archive) >= 1.0
%endif

# testmon is not needed to tests to run successfully
# the f31 version of testmon requires pytest < 4
# which is not in f31
# BuildRequires:  python3dist(pytest-testmon)
BuildRequires:  python3dist(requests)
BuildRequires:  python3dist(requests-unixsocket)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(trustme)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Cheroot is the high performance, pure Python HTTP server used by CherryPy.Status
The test suite currently relies on pytest. It's being run via Travis
CI.Contribute Cheroot.

%if %{with docs}
%package -n python-%{pypi_name}-doc
Summary:        cheroot documentation

BuildRequires:  python3dist(sphinx)
BuildRequires:  python3-sphinx-theme-alabaster
BuildRequires:  python3dist(rst-linker)
BuildRequires:  python3dist(jaraco-packaging)
BuildRequires:  python3dist(docutils)

%description -n python-%{pypi_name}-doc
Documentation for cheroot
%endif

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
# remove backports.functools_lru_cache from setup.cfg. it's a py2 dep
sed -i '/backports.functools_lru_cache/d' setup.cfg

# testmon is not needed to tests to run successfully
# the f31 version of testmon requires pytest < 4
# which is not in f31
sed -i 's/ --testmon//' pytest.ini
sed -i 's/ -n auto//' pytest.ini
sed -i '/pytest-testmon/d' setup.cfg
# trustme is a build-time only dependency
sed -i '/trustme/d' setup.cfg
%if 0%{?el8}
# drop setuptools_scm_git_archive
sed -i '/setuptools_scm_git_archive/d' setup.cfg
%endif

%build
%py3_build
%if %{with docs}
sphinx-build -vvv docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}
%endif

%install
%py3_install

%check
# checks fail currently
# LANG=C.utf-8 %{__python3} -m pytest --ignore=build

%files -n python3-%{pypi_name}
%license LICENSE.md
%doc README.rst
%{_bindir}/cheroot
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%if %{with docs}
%files -n python-%{pypi_name}-doc
%license LICENSE.md
%doc html
%endif

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 8.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan 19 2021 Dan Radez <dradez@redhat.com> - 8.5.2-1
- update to 8.5.2

* Sat Dec 12 2020 Dan Radez <dradez@redhat.com> - 8.5.1-1
- update to 8.5.1

* Mon Dec 07 2020 Ken Dreyer <kdreyer@redhat.com> 8.5.0-1
- Update to 8.5.0 (rhbz#1868629)

* Tue Aug 04 2020 Fabien Boucher <fboucher@redhat.com> - 8.4.2-1
- update to 8.4.2

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 03 2020 Matthias Runge <mrunge@redhat.com> - 8.2.1-3
- skip test and rebuild to fix fail to install for cherrypy

* Tue May 26 2020 Miro Hron??ok <mhroncok@redhat.com> - 8.2.1-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Oct 18 2019 Dan Radez <dradez@redhat.com> - 8.2.1-1
- update to 8.2.1

* Thu Oct 17 2019 Dan Radez <dradez@redhat.com> - 8.2.0-1
- update to 8.2.0

* Fri Oct 11 2019 Dan Radez <dradez@redhat.com> - 8.1.0-1
- update to 8.1.0

* Fri Sep 27 2019 Dan Radez <dradez@redhat.com> - 7.0.0-2
- fixing dep naming issues

* Thu Sep 26 2019 Dan Radez <dradez@redhat.com> - 7.0.0-1
- update to 7.0.0

* Tue Sep 24 2019 Dan Radez <dradez@redhat.com> - 6.5.8-1
- update to 6.5.8

* Wed Aug 21 2019 Miro Hron??ok <mhroncok@redhat.com> - 6.5.6-2
- Rebuilt for Python 3.8

* Mon Aug 19 2019 Dan Radez <dradez@redhat.com> - 6.5.6-1
- update to 6.5.6

* Mon Aug 19 2019 Miro Hron??ok <mhroncok@redhat.com> - 6.5.5-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.5.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 30 2019 Dan Radez <dradez@redhat.com> - 6.5.5-1
- update to 6.5.5
- disable docs build, new dep sphinx-tabs was introduced.

* Tue Apr 09 2019 Dan Radez <dradez@redhat.com> - 6.5.4-2
- enabling docs

* Wed May 02 2018 Dan Radez <dradez@redhat.com> - 6.5.4-1
- Initial package.
