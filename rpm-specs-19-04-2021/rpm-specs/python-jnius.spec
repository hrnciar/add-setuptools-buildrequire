%global modname jnius
%global srcname py%{modname}
%global sum     Dynamic access to Java classes from Python


Name:           python-%{modname}
Version:        1.3.0
Release:        6%{?dist}
Summary:        %{sum}

License:        MIT
URL:            https://github.com/kivy/%{srcname}
Source0:        %{url}/archive/%{version}.tar.gz#/%{srcname}-%{version}.tar.gz

BuildRequires: make
BuildRequires:  gcc

BuildRequires:  python3-devel
BuildRequires:  python3-Cython
BuildRequires:  python3-six
BuildRequires:  python3-pytest

BuildRequires:  ant
BuildRequires:  java-devel

BuildRequires:  %{_bindir}/sphinx-build-3

# FIXME odd bug with wrong default architecture (i386)
# https://github.com/kivy/pyjnius/issues/307
# https://github.com/kivy/pyjnius/issues/306
ExcludeArch:    i686 ppc64 ppc64le s390x armv7hl aarch64

%description
%{summary}.

%package     -n python3-%{srcname}
Summary:        %{sum}
Requires:       java-headless
Requires:       python3-six
%{?python_provide:%python_provide python3-%{srcname}}
Provides:       python3-%{modname}


%description -n python3-%{srcname}
%{summary}.

%package        doc
Summary:        Documentation files for %{srcname}
BuildArch:      noarch

%description    doc
%{summary}.


%prep
%autosetup -p1 -n %{srcname}-%{version}


%build
%py3_build

make %{_smp_mflags} -C docs SPHINXBUILD='sphinx-build-3 %{_smp_mflags}' html

# build java classes for tests
# there is also Makefile, but it calls python setup.py build_ext --inplace
# together with ant, so we don't use it not to build python bits twice
ant all


%install
%py3_install


%check
pushd tests
export CLASSPATH=../build/test-classes:../build/classes
export JAVA_HOME=%{_prefix}/lib/jvm/java
PYTHONPATH=%{buildroot}%{python3_sitearch} pytest -v
popd


%files -n python3-%{srcname}
%license LICENSE
%doc *.md
%{python3_sitearch}/%{modname}/
%{python3_sitearch}/%{modname}_config.py*
%{python3_sitearch}/%{srcname}-%{version}-py*.egg-info/
%{python3_sitearch}/__pycache__/%{modname}_config.cpython-*.pyc
%exclude %{python3_sitearch}/__pycache__
%exclude %{python3_sitearch}/setup_sdist.py

%files doc
%license LICENSE
%doc docs/build/html/


%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Oct 01 2020 Raphael Groner <raphgro@fedoraproject.org> - 1.3.0-5
- use pytest instead of nose as upstream decided, see changes in Makefile
- skip useless additional setup

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 11 2020 Jiri Vanek <jvanek@redhat.com> - 1.3.0-2
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Sat Jun 06 2020 Raphael Groner <raphgro@fedoraproject.org> - 1.3.0-1
- bump to v1.3.0 

* Sat Jun 06 2020 Raphael Groner <raphgro@fedoraproject.org> - 1.2.0-6
- rebuilt

* Tue May 26 2020 Miro Hron??ok <mhroncok@redhat.com> - 1.2.0-5
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hron??ok <mhroncok@redhat.com> - 1.2.0-3
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hron??ok <mhroncok@redhat.com> - 1.2.0-2
- Rebuilt for Python 3.8

* Mon Jul 29 2019 Raphael Groner <projects.rg@smart.ms> - 1.2.0-1
- new version

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Dec 13 2018 Raphael Groner <projects.rg@smart.ms> - 1.1.4-1
- new version

* Mon Nov 12 2018 Miro Hron??ok <mhroncok@redhat.com> - 1.1.1-7
- Subpackage python2-pyjnius has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Wed Jul 18 2018 Raphael Groner <projects.rg@smart.ms> - 1.1.1-6
- several fixes for Python

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-5
-- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hron??ok <mhroncok@redhat.com> - 1.1.1-4
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Oct 24 2017 Raphael Groner <projects.rg@smart.ms> - 1.1.1-2
- be more precisely about owned files

* Sun Oct 22 2017 Raphael Groner <projects.rg@smart.ms> - 1.1.1-1
- initial
