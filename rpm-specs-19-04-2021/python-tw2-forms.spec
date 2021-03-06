%global modname tw2.forms

Name:           python-tw2-forms
Version:        2.2.6
Release:        8%{?dist}
Summary:        Forms for ToscaWidgets2

License:        MIT
URL:            http://toscawidgets.org
Source0:        https://pypi.python.org/packages/source/t/%{modname}/%{modname}-%{version}.tar.gz
BuildArch:      noarch

# For building, generally
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-webob >= 0.9.7
BuildRequires:  python3-tw2-core >= 2.1.4
BuildRequires:  python3-paste-deploy

# Specifically for the test suite
BuildRequires:  python3-nose
BuildRequires:  python3-coverage
BuildRequires:  python3-formencode
BuildRequires:  python3-webtest
BuildRequires:  python3-sieve >= 0.1.9

# Templating languages for the test suite
BuildRequires:  python3-mako
BuildRequires:  python3-genshi
BuildRequires:  python3-chameleon
BuildRequires:  python3-kajiki
BuildRequires:  python3-jinja2

# Runtime requirements

%global _description\
ToscaWidgets is a web widget toolkit for Python to aid in the creation,\
packaging and distribution of common view elements normally used in the web.\
\
tw2.forms contains the basic form widgets.

%description %_description

%package -n python3-tw2-forms
Summary: Forms for ToscaWidgets2
Requires: python3-tw2-core >= 2.1.4

%description -n python3-tw2-forms
ToscaWidgets is a web widget toolkit for Python to aid in the creation,
packaging and distribution of common view elements normally used in the web.

This package contains the basic form widgets build for python3.


%prep
%setup -q -n %{modname}-%{version}


%build
%{__python3} setup.py build


%install
%{__python3} setup.py install --skip-build \
    --install-data=%{_datadir} --root %{buildroot}


%check
PYTHONPATH=$(pwd) %{__python3} setup.py test


%files -n python3-tw2-forms
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/tw2/forms
%{python3_sitelib}/%{modname}-%{version}*

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hron??ok <mhroncok@redhat.com> - 2.2.6-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hron??ok <mhroncok@redhat.com> - 2.2.6-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Thu Aug 29 2019 J??n ONDREJ (SAL) <ondrejj(at)salstar.sk> - 2.2.6-3
- Revmoved python3 support

* Thu Aug 29 2019 J??n ONDREJ (SAL) <ondrejj(at)salstar.sk> - 2.2.6-2
- Updated source URL (https)
- Versioned provides for python2 package

* Mon Aug 26 2019 J??n ONDREJ (SAL) <ondrejj(at)salstar.sk> - 2.2.6-1
- Update to upstream

* Mon Aug 19 2019 Miro Hron??ok <mhroncok@redhat.com> - 2.2.3-14
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hron??ok <mhroncok@redhat.com> - 2.2.3-10
- Rebuilt for Python 3.7

* Wed Feb 28 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.2.3-9
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Aug 19 2017 Zbigniew J??drzejewski-Szmek <zbyszek@in.waw.pl> - 2.2.3-7
- Python 2 binary package renamed to python2-tw2-forms
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hron??ok <mhroncok@redhat.com> - 2.2.3-4
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.3-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan  7 2016 Toshio Kuratomi <toshio@fedoraproject.org> - 2.2.3-1
- Update to upstream 2.2.3
- Add a python3 subpackage

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.4.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.4.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Apr 28 2014 Ralph Bean <rbean@redhat.com> - 2.1.4.1-7
- Try to fix deps busted by releng.

* Mon Apr 28 2014 Ralph Bean <rbean@redhat.com> - 2.1.4.1-6
- Backported patch to fix buttons.

* Tue Aug 06 2013 Ralph Bean <rbean@redhat.com> - 2.1.4.1-5
- Temporarily disable test suite until the 2.2 release.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild
- Disable tests for epel7.

* Thu Feb 28 2013 Ralph Bean <rbean@redhat.com> - 2.1.4.1-3
- Rename Jinja2 to jinja2 for el6.

* Wed Feb 27 2013 Ralph Bean <rbean@redhat.com> - 2.1.4.1-2
- Renamed README from .txt to .rst.

* Fri Feb 22 2013 Ralph Bean <rbean@redhat.com> - 2.1.4.1-1
- Latest upstream.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 07 2012 Ralph Bean <rbean@redhat.com> - 2.0.2-3
- More explicit directory ownership.

* Mon Apr 30 2012 Ralph Bean <rbean@redhat.com> - 2.0.2-2
- Removed clean section
- Removed defattr in files section
- Removed unnecessary references to buildroot

* Wed Apr 11 2012 Ralph Bean <rbean@redhat.com> - 2.0.2-1
- Update for latest tw2.forms release.
- Fixes rpmlint errors.  Execution bit in templates, wat?
- Added dist macro to release field.
- Added awk line to make sure pkg_resources picks up the right WebOb on el6

* Thu Apr 05 2012 Ralph Bean <rbean@redhat.com> - 2.0.1-1
- Update for latest tw2.forms release.

* Thu Jun 16 2011 Luke Macken <lmacken@redhat.com> - 2.0-0.1.b4
- Initial package
