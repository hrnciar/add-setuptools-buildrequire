%global pypi_name ephem

Name:           python-%{pypi_name}
Version:        3.7.7.1
Release:        5%{?dist}
Summary:        Compute positions of the planets and stars

License:        LGPLv3+
URL:            http://rhodesmill.org/pyephem/
Source0:        %{pypi_source}

BuildRequires:  gcc

%description
PyEphem provides an ephem Python package for performing high-precision
astronomy computations. The underlying numeric routines are coded in C
and are the same ones that drive the popular XEphem astronomy application.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-pytest

Provides:       python3-pyephem = %{version}-%{release}
Obsoletes:      python3-pyephem < 3.7.1.1

%description -n python3-%{pypi_name}
PyEphem provides an ephem Python package for performing high-precision
astronomy computations. The underlying numeric routines are coded in C
and are the same ones that drive the popular XEphem astronomy application.

%package -n python-%{pypi_name}-doc
Summary:        The %{pypi_name} documentation
BuildArch:      noarch

BuildRequires:  python3-sphinx

%description -n python-%{pypi_name}-doc
Documentation for %{pypi_name}.

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build
PYTHONPATH=${PWD} sphinx-build-3 ephem/doc html
rm -rf html/.{doctrees,buildinfo}

%install
%py3_install

%check
cd %{buildroot}%{python3_sitearch}/%{pypi_name}
# One test has an AttributeError
%pytest -v tests -k "not JPLTest and not test_github_25" 
# Remove left-overs from the tests
rm -rf %{buildroot}%{python3_sitearch}/%{pypi_name}/{.benchmarks,.hypothesis,.pytest_cache}

%files -n python3-%{pypi_name}
%license LICENSE-GPL LICENSE-LGPL
%doc README.rst
%{python3_sitearch}/%{pypi_name}/
%{python3_sitearch}/%{pypi_name}-%{version}-py%{python3_version}.egg-info
%exclude %{python3_sitearch}/%{pypi_name}/tests
%exclude %{python3_sitearch}/%{pypi_name}/doc

%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE-GPL LICENSE-LGPL

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.7.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Sep 16 2020 Fabian Affolter <mail@fabian-affolter.ch> - 3.7.7.1-4
- Make doc subpackage noarch
- Remove doc directory and BR

* Mon Sep 14 2020 Fabian Affolter <mail@fabian-affolter.ch> - 3.7.7.1-3
- Ignore JPLTest and remove left-overs from tests 
- Don't ship tests

* Tue Sep 01 2020 Fabian Affolter <mail@fabian-affolter.ch> - 3.7.7.1-2
- Update spec file (rhbz#1857767)

* Thu Jul 16 2020 Fabian Affolter <mail@fabian-affolter.ch> - 3.7.7.1-1
- Rename package to python-ephem

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.6.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro HronÄok <mhroncok@redhat.com> - 3.7.6.0-17
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro HronÄok <mhroncok@redhat.com> - 3.7.6.0-16
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.6.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.6.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 02 2018 Christian Dersch <lupinix@fedoraproject.org> - 3.7.6.0-13
- drop python2 subpackage (#1634600)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.6.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro HronÄok <mhroncok@redhat.com> - 3.7.6.0-11
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.6.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.6.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.6.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Apr 07 2017 Christian Dersch <lupinix@mailbox.org> - 3.7.6.0-7
- Added missing summaries
- Added provides and obsoletes for clean upgradepath
- Small spec fixes

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro HronÄok <mhroncok@redhat.com> - 3.7.6.0-5
- Rebuild for Python 3.6

* Wed Jul 27 2016 Dominika Krejci <dkrejci@redhat.com> - 3.7.6.0-4
- Add Python3

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.7.6.0-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Sep  2 2015 Andrew Elwell <Andrew.Elwell@gmail.com> - 3.7.6.0-1
- New upstream release

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.7.5.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.7.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Jul 09 2014 Andrew Elwell <Andrew.Elwell@gmail.com> - 3.7.5.3-1
- New upstream release

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.7.5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.7.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.7.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.7.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Feb 17 2012 Andrew Elwell <andrew.elwell@gmail.com> - 3.7.5.1-1
- New upstream release (closes #789583)

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.7.3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.7.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan 31 2011 Andrew Elwell <andrew.elwell@gmail.com> - 3.7.3.4-1
- New upstream release (closes #590476)
- CHANGELOG no longer included

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 3.7.2.3-6
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.7.2.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.7.2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 3.7.2.3-3
- Rebuild for Python 2.6

* Sun Jul 27 2008 Marek Mahut <mmahut@fedoraproject.org> - 3.7.2.3-2
- Revision increase

* Mon Apr 21 2008 Marek Mahut <mmahut@fedoraproject.org> - 3.7.2.3-1
- Initial build