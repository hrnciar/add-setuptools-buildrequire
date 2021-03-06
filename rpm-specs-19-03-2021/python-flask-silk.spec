%global mod_name	Flask-Silk

Name:		python-flask-silk
Version:	0.2
Release:	14%{?dist}
Summary:	Adds silk icons to your Flask application or module, or extension
# The code is BSD.  The icons are CC-BY-SA.
License:	BSD and CC-BY-SA
URL:		http://github.com/sublee/flask-silk/
Source0:	https://files.pythonhosted.org/packages/source/F/%{mod_name}/%{mod_name}-%{version}.tar.gz
# Fix icon paths
Patch0:         %{name}-icons.patch
# Fix imports.  See
# https://github.com/sublee/flask-silk/commit/3a8166550f9a0ec52edae7bf31d9818c4c15c531
Patch1:         %{name}-import.patch
BuildArch:	noarch
BuildRequires:	python3-devel
BuildRequires:	%{py3_dist flask}
BuildRequires:	%{py3_dist flask-sphinx-themes}
BuildRequires:	%{py3_dist setuptools}
BuildRequires:	%{py3_dist sphinx}

%global _description\
Adds silk icons to your Flask application or module, or extension.

%description %_description

%package -n python3-flask-silk
Summary: %summary
%{?python_provide:%python_provide python3-flask-silk}

%description -n python3-flask-silk %_description

%package docs
Summary:	Documentation for %{name}

%description docs
HTML documentation for %{name}.

%prep
%autosetup -p1 -n %{mod_name}-%{version}

# Remove bundled flask-sphinx-themes
rm -fr docs/_themes

# Remove prebuilt .pyc
find . -name \*.pyc -delete

# The icons should not be executable
chmod a-x flask_silk/icons/*.png

# Fix table percentages that make the icons invisible
sed -i 's/1 99/10 90/' flask_silk/icons/__init__.py

# Fix version number in the documentation
sed -i 's/0\.1\.2/%{version}/' docs/conf.py


%build
%py3_build

# Build the documentation
sphinx-build-%{python3_version} docs html

%install
%py3_install

%check
%{python3} test.py

%files -n python3-flask-silk
%doc README
%license LICENSE
%{python3_sitelib}/flask_silk/
%{python3_sitelib}/*.egg-info/

%files docs
%doc html/*

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Oct  5 2020 Jerry James <loganjerry@gmail.com> - 0.2-13
- Add -icons patch to fix paths to icons
- Add -import patch from upstream

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-13
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hron??ok <mhroncok@redhat.com> - 0.2-11
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hron??ok <mhroncok@redhat.com> - 0.2-9
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hron??ok <mhroncok@redhat.com> - 0.2-8
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 15 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2-5
- Enable python dependency generator

* Mon Jan 14 2019 Miro Hron??ok <mhroncok@redhat.com> - 0.2-4
- Subpackage python2-flask-silk has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hron??ok <mhroncok@redhat.com> - 0.2-2
- Rebuilt for Python 3.7

* Sat Jun  2 2018 Jerry James <loganjerry@gmail.com> - 0.2-1
- Update to latest upstream release, fixes FTBFS (bz 1556177)
- Use license macro
- Build for both python 2 and python 3
- Build documentation
- Add a check script

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Aug 19 2017 Zbigniew J??drzejewski-Szmek <zbyszek@in.waw.pl> - 0.1.2-10
- Python 2 binary package renamed to python2-flask-silk
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-7
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Sep 16 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.1.2-1
- Update to latest upstream release

* Sat Sep 15 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.1.1-5
- Correct upstream url (#839098)
- Update license tag to match package contents (#839098)
- Add LICENSE and test.py files from upstream scm

* Thu Sep 13 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.1.1-4
- Add missing python-setuptools build requires (#839071)

* Fri Aug 17 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.1.1-3
- Update build requires for proper chroot build

* Sun Aug 5 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.1.1-2
- No need to set CFLAGS for noarch (#839071)

* Tue Jul 10 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.1.1-1
- Initial python-flask-silk spec.
