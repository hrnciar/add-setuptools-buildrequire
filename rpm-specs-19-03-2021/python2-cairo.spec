Name: python2-cairo
Version: 1.18.2
Release: 8%{?dist}
Summary: Python 2 bindings for the cairo library

License: MPLv1.1 or LGPLv2
URL: http://cairographics.org/pycairo
Source0: https://github.com/pygobject/pycairo/releases/download/v%{version}/pycairo-%{version}.tar.gz

# This package has a FESCo exception to use Python 2, for GIMP
# https://pagure.io/fesco/issue/2238

BuildRequires: cairo-devel
BuildRequires: gcc
BuildRequires: pkgconfig
BuildRequires: python2-devel
BuildRequires: python2-setuptools

%{?python_provide:%python_provide python2-cairo}
# Renamed in F27
Obsoletes: pycairo < 1.15.2
Provides: pycairo = %{version}-%{release}
Provides: pycairo%{?_isa} = %{version}-%{release}

%description
Python 2 bindings for the cairo library.

%package devel
Summary: Libraries and headers for python2-cairo
Requires: python2-cairo%{?_isa} = %{version}-%{release}
Requires: python2-devel
# Renamed in F27
Obsoletes: pycairo-devel < 1.15.2
Provides: pycairo-devel = %{version}-%{release}
Provides: pycairo-devel%{?_isa} = %{version}-%{release}

%description devel
This package contains files required to build wrappers for cairo add-on
libraries so that they interoperate with python2-cairo.

%prep
%autosetup -p1 -n pycairo-%{version}

%build
%py2_build

%install
%py2_install

# No python2-pytest, no %%check

%files
%license COPYING*
%{python2_sitearch}/cairo/
%{python2_sitearch}/pycairo*.egg-info

%files devel
%dir %{_includedir}/pycairo
%{_includedir}/pycairo/pycairo.h
%{_libdir}/pkgconfig/pycairo.pc

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Nov  4 2020 Miro Hrončok <mhroncok@redhat.com> - 1.18.2-7
- Split python2-cairo to a separate component

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri May 22 2020 Miro Hrončok <mhroncok@redhat.com> - 1.18.2-5
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 06 2019 Petr Viktorin <pviktori@redhat.com> - 1.18.2-3
- Build require python-setuptools

* Tue Oct 29 2019 Petr Viktorin <pviktori@redhat.com> - 1.18.2-2
- Do not run tests on Python 2

* Thu Oct 24 2019 Kalev Lember <klember@redhat.com> - 1.18.2-1
- Update to 1.18.2

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.18.1-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Thu Aug 15 2019 Miro Hrončok <mhroncok@redhat.com> - 1.18.1-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 24 2019 Kalev Lember <klember@redhat.com> - 1.18.1-1
- Update to 1.18.1

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Nov 14 2018 Kalev Lember <klember@redhat.com> - 1.18.0-1
- Update to 1.18.0

* Thu Sep 27 2018 Owen Taylor <otaylor@redhat.com> - 1.17.1-3
- Disable xpyb support - this is only for Python2, and was originally added
  for qtile, which uses Python3 now.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 11 2018 Kalev Lember <klember@redhat.com> - 1.17.1-1
- Update to 1.17.1

* Fri Jun 15 2018 Miro Hrončok <mhroncok@redhat.com> - 1.16.3-2
- Rebuilt for Python 3.7

* Mon Mar 19 2018 Kalev Lember <klember@redhat.com> - 1.16.3-1
- Update to 1.16.3

* Tue Feb 06 2018 Kalev Lember <klember@redhat.com> - 1.16.1-1
- Update to 1.16.1

* Mon Feb 05 2018 Kalev Lember <klember@redhat.com> - 1.16.0-1
- Update to 1.16.0

* Mon Feb 05 2018 Kalev Lember <klember@redhat.com> - 1.15.6-1
- Update to 1.15.6

* Fri Dec 01 2017 Kalev Lember <klember@redhat.com> - 1.15.4-1
- Update to 1.15.4

* Wed Sep 20 2017 Kalev Lember <klember@redhat.com> - 1.15.3-1
- Update to 1.15.3

* Thu Sep 14 2017 Kalev Lember <klember@redhat.com> - 1.15.2-1
- Update to 1.15.2
- Switch to new upstream at https://github.com/pygobject/pycairo
- Switch to distutils build system
- Tighten subpackage deps with the _isa macro
- Rename Python 2 package to python2-cairo
- Enable Python 3 support

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.0-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Aug 23 2015 Kalev Lember <klember@redhat.com> - 1.10.0-3
- Use license macro for license files

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Nov 15 2014 David Tardon <dtardon@redhat.com> - 1.10.0-1
- "new" upstream release

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.10-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.10-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 21 2014 Jakub Čajka <jcajka@redhat.com> - 1.8.10-10
- Resolves: #1079673 - Fixed build dependencies and enabled tests on ppc

* Tue May 20 2014 Dan Horák <dan[at]danny.cz> - 1.8.10-9
- disable tests on big endians (#1079673)

* Thu Feb 27 2014 Peter Robinson <pbrobinson@fedoraproject.org> 1.8.10-8
- Enable xcb and xpyb (RHBZ 1045725, 1005447)
- Spec cleanups
- Run check

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Feb 19 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 1.8.10-4
- Revert illegal package rename so it properly builds
- spec file cleanup

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Sep 21 2010 Matthew Barnes <mbarnes@redhat.com> - 1.8.10-1
- Update to 1.8.10
- Rename the package to python-cairo.

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 1.8.8-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Fri Sep 18 2009 Matthew Barnes <mbarnes@redhat.com> - 1.8.8-1
- Update to 1.8.8

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jun 29 2009 Matthew Barnes <mbarnes@redhat.com> - 1.8.6-1
- Update to 1.8.6

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jan 16 2009 Matthew Barnes <mbarnes@redhat.com> - 1.8.2-1
- Update to 1.8.2

* Tue Dec 16 2008 Matthew Barnes <mbarnes@redhat.com> - 1.8.0-1
- Update to 1.8.0

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 1.4.12-5
- Rebuild for Python 2.6

* Fri Aug 29 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.4.12-4
- fix license tag

* Wed May 07 2008 Matthew Barnes <mbarnes@redhat.com> - 1.4.12-3
- Add more documentation files to the package (RH bug #445519).

* Sun Feb 17 2008 Matthew Barnes <mbarnes@redhat.com> - 1.4.12-2.fc9
- Rebuild with GCC 4.3

* Thu Dec 13 2007 Matthew Barnes <mbarnes@redhat.com> - 1.4.12-1.fc9
- Update to 1.4.12
- Bump cairo requirement to 1.4.12.

* Wed Oct 10 2007 Matthew Barnes <mbarnes@redhat.com> - 1.4.0-2.fc7
- Rebuild

* Thu Mar 15 2007 Matthew Barnes <mbarnes@redhat.com> - 1.4.0-1.fc7
- Update to 1.4.0

* Mon Feb 05 2007 Matthew Barnes <mbarnes@redhat.com> - 1.2.6-3.fc7
- Incorporate suggestions from package review (RH bug #226329).

* Thu Dec  7 2006 Jeremy Katz <katzj@redhat.com> - 1.2.6-2
- rebuild against python 2.5

* Tue Nov 28 2006 Matthew Barnes <mbarnes@redhat.com> - 1.2.6-1.fc7
- Update to 1.2.6
- Clean up the spec file.

* Sun Oct 15 2006 Matthew Barnes <mbarnes@redhat.com> - 1.2.2-1
- Update to 1.2.2

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 1.2.0-1.1
- rebuild

* Wed Jul 05 2006 John (J5) Palmieri <johnp@redhat.com> - 1.2.0-1
- Update to upstream 1.2.0

* Mon Jul  3 2006 Jeremy Katz <katzj@redhat.com> - 1.0.2-3
- require new enough cairo (#197457)

* Mon Jun 05 2006 John (J5) Palmieri <johnp@redhat.com> - 1.0.2-2
- add pkgconfig BR

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 1.0.2-1.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 1.0.2-1.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Wed Oct 26 2005 John (J5) Palmieri <johnp@redhat.com> - 1.0.2-1
- Updated to latest and push into rawhide

* Fri Dec 10 2004 Kristian Høgsberg <krh@redhat.com> - 0.1.3-1
- Add python-devel build requires.

* Wed Nov 24 2004  <jrb@redhat.com> - 
- Initial build.
