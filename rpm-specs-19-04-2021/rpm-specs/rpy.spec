%global srcname rpy
%global sum Python interface to the R language
%global rver   4.0.4

Name:          rpy
Version:       3.4.2
Release:       3%{?dist}
Summary:       %{sum}
License:       GPLv2+
Url:           https://pypi.python.org/pypi/rpy2
Source:        https://files.pythonhosted.org/packages/source/r/%{srcname}2/%{srcname}2-%{version}.tar.gz

BuildRequires: gcc
BuildRequires: R-devel = %{rver}
BuildRequires: python3-devel
BuildRequires: readline-devel
BuildRequires: python3dist(setuptools)
BuildRequires: python3dist(cffi)
BuildRequires: python3dist(numpy)
BuildRequires: python3dist(pytest)
BuildRequires: python3dist(pandas)

Requires:      python3-%{srcname} = %{version}-%{release}

%description
RPy provides a robust Python interface to the R
programming language.  It can manage all kinds of R objects and can
execute arbitrary R functions. All the errors from the R language are
converted to Python exceptions.

%package -n python3-%{srcname}
Summary:       %{sum}
Requires:      R-core = %{rver}
%if (0%{?fedora} && 0%{?fedora} < 33)
%{?python_provide:%python_provide python3-%{srcname}}
%endif

%description -n python3-%{srcname}
RPy provides a robust Python interface to the R
programming language.  It can manage all kinds of R objects and can
execute arbitrary R functions. All the errors from the R language are
converted to Python exceptions.

%prep
%setup -q -n %{srcname}2-%{version}

%build
# Temporary workaround to fix a bug in R
# see https://stat.ethz.ch/pipermail/r-devel/2016-December/073548.html
export CFLAGS="$RPM_OPT_FLAGS -DHAVE_UINTPTR_T=1"
%py3_build

%install
%py3_install

%check
cd %{srcname}2
# rpy requires to test the installed packages
#PYTHONPATH=%{buildroot}%{python3_sitearch} pytest tests/


%files

%files -n python3-%{srcname}
%doc AUTHORS NEWS PKG-INFO
%license gpl-2.0.txt
%{python3_sitearch}/%{srcname}*
%{python3_sitearch}/_rinterface_cffi_abi.py
%{python3_sitearch}/_rinterface_cffi_api.abi3.so
%{python3_sitearch}/__pycache__/*

%changelog
* Mon Feb 15 2021 Tom Callaway <spot@fedoraproject.org> - 3.4.2-3
- rebuild for R 4.0.4

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 11 2021 Jos?? Matos <jamatos@fedoraproject.org> - 3.4.2-1
- update to 3.4.2

* Sun Jan  3 2021 Jos?? Matos <jamatos@fedoraproject.org> - 3.4.1-1
- update to 3.4.1

* Tue Oct 13 2020 Tom Callaway <spot@fedoraproject.org> - 3.3.6-1
- update to 3.3.6
- R 4.0.3

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.5-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul  8 2020 Jos?? Matos <jamatos@fedoraproject.org> - 3.3.5-1
- update to 3.3.5

* Thu Jun 25 2020 Jos?? Matos <jamatos@fedoraproject.org> - 3.3.4-1
- update to 3.3.4

* Tue Jun 23 2020 Tom Callaway <spot@fedoraproject.org> - 3.3.3-6
- rebuild for R 4.0.2

* Sat Jun 20 2020 Dennis Gilmore <dennis@ausil.us> - 3.3.3-5
- rebuild for R 4.0.1

* Wed Jun 17 2020 Jos?? Matos <jamatos@fedoraproject.org> - 3.3.3-4
- rebuild to pick both python-3.9 and R-4.0

* Wed Jun  3 2020 Tom Callaway <spot@fedoraproject.org> - 3.3.3-3
- rebuild for R 4.0.0

* Tue May 26 2020 Miro Hron??ok <mhroncok@redhat.com> - 3.3.3-2
- Rebuilt for Python 3.9

* Mon May 18 2020 Jos?? Matos <jamatos@fedoraproject.org> - 3.3.3-1
- update to 3.3.3

* Sun Mar 22 2020 Jos?? Matos <jamatos@fedoraproject.org> - 3.2.7-2
- place BuildRequires in canonical form
- remove Requires since they are automatically provided

* Sun Mar 22 2020 Jos?? Matos <jamatos@fedoraproject.org> - 3.2.7-1
- update to 3.2.7

* Tue Mar  3 2020 Tom Callaway <spot@fedoraproject.org> - 3.2.6-2
- rebuild for R 3.6.3

* Sun Feb 23 2020 Jos?? Matos <jamatos@fedoraproject.org> - 3.2.6-1
- update to 3.2.6

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Dec 12 2019 Tom Callaway <spot@fedoraproject.org> - 3.2.2-1
- update to 3.2.2
- package is now arch specific

* Thu Oct 03 2019 Miro Hron??ok <mhroncok@redhat.com> - 3.0.5-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hron??ok <mhroncok@redhat.com> - 3.0.5-4
- Rebuilt for Python 3.8

* Fri Aug 16 2019 Tom Callaway <spot@fedoraproject.org> - 3.0.5-3
- rebuild for R 3.6.1

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 17 2019 Jos?? Matos <jamatos@fedoraproject.org> - 3.0.5-1
- update to 3.0.5

* Thu May 30 2019 Tom Callaway <spot@fedoraproject.org> - 3.0.4-2
- rebuild for R 3.6.0

* Thu May 16 2019 Jos?? Matos <jamatos@fedoraproject.org> - 3.0.4-1
- update to 3.0.4

* Mon May  6 2019 Jos?? Matos <jamatos@fedoraproject.org> - 3.0.3-1
- update to 3.0.3

* Sat May  4 2019 Jos?? Matos <jamatos@fedoraproject.org> - 3.0.2-1
- update to 3.0.2

* Mon Mar 11 2019 Tom Callaway <spot@fedoraproject.org> - 3.0.1-2
- R 3.5.3

* Mon Mar  4 2019 Jos?? Matos <jamatos@fedoraproject.org> - 3.0.1-1
- update to 3.0.1
- rpy >= 3.0.0 requires python3
- add a %%chech section (commented because the tests are not present in the release)

* Wed Feb 27 2019 Jos?? Matos <jamatos@fedoraproject.org> - 3.0.0-1
- update to 3.0.0
- fix the directory ownership
- declare license file

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 17 2019 Tom Callaway <spot@fedoraproject.org> - 2.9.5-1
- update to 2.9.5
- R 3.5.2

* Fri Sep 14 2018 Tom Callaway <spot@fedoraproject.org> - 2.9.4-4
- rebuild for R 3.5.1

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 10 2018 Pete Walter <pwalter@fedoraproject.org> - 2.9.4-2
- Rebuild for ICU 62

* Sat Jun 30 2018 Jos?? Matos <jamatos@fedoraproject.org> - 2.9.4-1
- update to 2.9.4

* Tue Jun 19 2018 Miro Hron??ok <mhroncok@redhat.com> - 2.9.3-2
- Rebuilt for Python 3.7

* Mon May 14 2018 Tom Callaway <spot@fedoraproject.org> - 2.9.3-1
- update to 2.9.3, R 3.5.0

* Mon Apr 30 2018 Pete Walter <pwalter@fedoraproject.org> - 2.9.2-2
- Rebuild for ICU 61.1

* Wed Mar 28 2018 Tom Callaway <spot@fedoraproject.org> - 2.9.2-1
- update to 2.9.2, R 3.4.4

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Dec  4 2017 Tom Callaway <spot@fedoraproject.org> - 2.9.1-1
- update to 2.9.1, rebuild for R 3.4.3

* Thu Nov 30 2017 Pete Walter <pwalter@fedoraproject.org> - 2.9.0-2
- Rebuild for ICU 60.1

* Fri Oct 27 2017 Tom Callaway <spot@fedoraproject.org> - 2.9.0-1
- update to 2.9.0, rebuild for R 3.4.2
- disable python2 support

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jun 30 2017 Tom Callaway <spot@fedoraproject.org> - 2.8.6-1
- update to 2.8.6, rebuild for R 3.4.1

* Mon May 15 2017 Tom Callaway <spot@fedoraproject.org> - 2.8.5-4
- rebuild for R 3.4.0

* Wed Mar  8 2017 Tom Callaway <spot@fedoraproject.org> - 2.8.5-3
- rebuild for R 3.3.3

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Dec 30 2016 Jos?? Matos <jamatos@fedoraproject.org> - 2.8.5-1
- update to 2.8.5
- workaround to fix a bug in R (it fails for 32 bit archs)

* Mon Dec 19 2016 Miro Hron??ok <mhroncok@redhat.com> - 2.8.3-2
- Rebuild for Python 3.6

* Tue Nov  1 2016 Tom Callaway <spot@fedoraproject.org> - 2.8.3-1
- update to 2.8.3
- rebuild for R 3.3.2

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.1-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Jul  6 2016 Tom Callaway <spot@fedoraproject.org> - 2.8.1-2
- rebuild for R 3.3.1

* Thu Jun 16 2016 Jos?? Ab??lio Matos <jamatos@fc.up.pt> - 2.8.1-1
- update to 2.8.1
- adapt the source url to a new scheme

* Tue May 10 2016 Tom Callaway <spot@fedoraproject.org> - 2.7.9-1
- update to 2.7.9, R 3.3.0

* Fri Apr 15 2016 David Tardon <dtardon@redhat.com> - 2.7.8-3
- rebuild for ICU 57.1

* Fri Mar 18 2016 Tom Callaway <spot@fedoraproject.org> - 2.7.8-2
- rebuild for R 3.2.4

* Sun Feb 14 2016 Jos?? Matos <jamatos@fedoraproject.org> - 2.7.8-1
- update to 2.7.8
- modernize python2 and python3 preserving the upgrade path

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Dec 11 2015 Tom Callaway <spot@fedoraproject.org> - 2.7.5-1
- update to 2.7.5

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Wed Oct 28 2015 David Tardon <dtardon@redhat.com> - 2.6.2-2
- rebuild for ICU 56.1

* Fri Aug 14 2015 Tom Callaway <spot@fedoraproject.org> - 2.6.2-1
- update to 2.6.2, R 3.2.2

* Tue Jul 21 2015 Jos?? Matos <jamatos@fedoraproject.org> - 2.6.1-1
- Update to 2.6.1

* Fri Jun 19 2015 Tom Callaway <spot@fedoraproject.org> - 2.6.0-1
- 2.6.0, R 3.2.1

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Apr 30 2015 Tom Callaway <spot@fedoraproject.org> - 2.5.6-4
- R 3.2.0

* Wed Apr 1 2015 Orion Poplawski <orion@cora.nwra.com> - 2.5.6-3
- Fix URL

* Tue Mar 10 2015 Jos?? Matos <jamatos@fedoraproject.org> - 2.5.6-2
- R 3.1.3

* Fri Feb 13 2015 Jos?? Matos <jamatos@fedoraproject.org> - 2.5.6-1
- update to 2.5.6

* Mon Jan 26 2015 David Tardon <dtardon@redhat.com> - 2.5.2-2
- rebuild for ICU 54.1

* Fri Nov 28 2014 Jos?? Matos <jamatos@fedoraproject.org> - 2.5.2-1
- update to 2.5.2

* Fri Nov 14 2014 Jos?? Matos <jamatos@fedoraproject.org> - 2.5.1-1
- update to 2.5.1
- add python3 subpackage

* Sat Nov  1 2014 Tom Callaway <spot@fedoraproject.org> - 2.4.4-1
- update to 2.4.4
- R 3.1.2

* Wed Sep 24 2014 Jos?? Matos <jamatos@fedoraproject.org> - 2.4.3-1
- update to 2.4.3

* Tue Aug 26 2014 David Tardon <dtardon@redhat.com> - 2.4.2-3
- rebuild for ICU 53.1

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Jul 16 2014 Tom Callaway <spot@fedoraproject.org> - 2.4.2-1
- update to 2.4.2
- R 3.1.1

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Apr 21 2014 Tom Callaway <spot@fedoraproject.org> - 2.3.10-1
- update to 2.3.10
- R 3.1.0

* Sun Mar 23 2014 Tom Callaway <spot@fedoraproject.org> - 2.3.9-2
- rebuild for R 3.0.3

* Fri Jan 31 2014 Jos?? Matos <jamatos@fedoraproject.org> - 2.3.9-1
- update to 2.3.9
- prepare the python3 support:
-  add virtual provides for python-rpy
-  change the build requirement from python-devel to python2-devel

* Tue Oct 15 2013 Tom Callaway <spot@fedoraproject.org> - 2.3.8-1
- update to 2.3.8, rebuild for R 3.0.2

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri May 17 2013 Tom Callaway <spot@fedoraproject.org> - 2.3.6-2
- rebuild for R 3.0.1

* Mon May  6 2013 Jos?? Matos <jamatos@fedoraproject.org> - 2.3.6-1
- update to 2.3.6

* Thu Apr 11 2013 Tom Callaway <spot@fedoraproject.org> - 2.3.5-1
- update to 2.3.5, built against R 3.0.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.0-0.2.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Oct 29 2012 Tom Callaway <spot@fedoraproject.org> - 2.3.0-0.1.beta1
- update to 2.3.0beta1

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jul  4 2012 Tom Callaway <spot@fedoraproject.org> - 2.2.6-1
- update to 2.2.6, R 2.15.1

* Sat Mar 31 2012 Tom Callaway <spot@fedoraproject.org> - 2.2.5-1
- update to 2.2.5, R 2.15.0

* Fri Jan  6 2012 Jos?? Matos <jamatos@fedoraproject.org> - 2.2.4-2
- rebuild for R 2.14.1

* Wed Nov  9 2011 Tom Callaway <spot@fedoraproject.org> - 2.2.4-1
- update to 2.2.4
- rebuild for R 2.14.0

* Fri Oct  7 2011 Tom Callaway <spot@fedoraproject.org> - 2.2.3-1
- update to 2.2.3
- rebuild for R 2.13.2

* Mon Jul 11 2011 Tom Callaway <spot@fedoraproject.org> - 2.2.1-2
- add BuildRequires: readline-devel

* Mon Jul 11 2011 Tom Callaway <spot@fedoraproject.org> - 2.2.1-1
- update to 2.2.1, note R at 2.13.1
- spec file modernization

* Fri Apr 15 2011 Michel Salim <salimma@fedoraproject.org> - 2.1.9-4
- Rebuild for R 2.13.0

* Sun Feb 27 2011 Tom Callaway <spot@fedoraproject.org> - 2.1.9-3
- rebuild for R 2.12.2

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Dec 17 2010 Tom Callaway <spot@fedoraproject.org> - 2.1.9-1
- update to 2.1.9

* Wed Oct 20 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 2.1.7-1
- update to 2.1.7

* Mon Jul 26 2010 David Malcolm <dmalcolm@redhat.com> - 2.1.3-3
- generalize reference to 2.6 to 2.? in %%install

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 2.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Tue Jun  1 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 2.1.3-1
- update to 2.1.3

* Fri Apr 23 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 2.1.0-1
- update to 2.1.0

* Thu Apr  8 2010 Jos?? Matos <jamatos@fc.up.pt> - 2.0.8-2
- Rebuild for new numpy.

* Mon Jan 25 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 2.0.8-1
- update to 2.0.8

* Tue Dec 29 2009 Alex Lancaster <alexlan[AT]fedoraproject org> - 2.0.6-7
- Rebuild for new R (2.10.1)

* Thu Nov  5 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 2.0.6-7
- rebuild for R 2.10.0

* Mon Sep 21 2009 Jos?? Matos <jamatos@fc.up.pt> - 2.0.6-6
- require at runtime just R-core

* Mon Aug 24 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 2.0.6-5
- rebuild for R 2.9.2

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jul 10 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 2.0.6-3
- images are only installed incorrectly on 64bit platforms that aren't ia64

* Thu Jul  9 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 2.0.6-1
- rebuild for R 2.9.1
- update to rpy2 2.0.6

* Fri Apr 17 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 2.0.3-2
- rebuild for R 2.9.0

* Fri Mar 20 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 2.0.3-1
- update to rpy2 2.0.3

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Dec 22 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.0.3-6
- rebuild for R 2.8.1

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 1.0.3-5
- Rebuild for Python 2.6

* Sun Oct 26 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.0.3-4
- rebuild against R-2.8.0

* Fri Aug 29 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.0.3-3
- rebuild against R-2.7.2

* Tue Jul  8 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.0.3-2
- rebuild against R 2.7.1

* Wed May 21 2008 Jos?? Matos <jamatos[AT]fc.up.pt> - 1.0.3-1
- Update to 1.0.3
- Backport two patches from upstream (turn off debug and use the lapack version that R was compiled with)

* Tue Apr 29 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.0.2-1
- update to 1.0.2
- R 2.7.0

* Wed Feb 13 2008 Jos?? Matos <jamatos[AT]fc.up.pt> - 1.0.1-5
- BR texinfo -> texinfo-tex

* Wed Feb 13 2008 Jos?? Matos <jamatos[AT]fc.up.pt> - 1.0.1-4
- Rebuild for gcc 4.3

* Fri Feb  8 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.0.1-3
- rebuild for R 2.6.2

* Mon Feb  4 2008 Jos?? Matos <jamatos[AT]fc.up.pt> - 1.0.1-2
- Sometimes _patch_'s guesses are not good enough. Redo patch to setup.py.

* Sun Feb  3 2008 Jos?? Matos <jamatos[AT]fc.up.pt> - 1.0.1-1
- New upstream release.

* Mon Jan  7 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.0-0.7.RC3
- find the moved R headers in their new home (/usr/include/R)

* Mon Jan  7 2008 Alex Lancaster <alexlan[AT]fedoraproject org> - 1.0-0.6.RC3
- BuildRequires: R-devel rather than just R

* Mon Nov 26 2007 Tom "spot" Callaway <tcallawa@redhat.com> - 1.0-0.5.RC3
- really rebuild against R 2.6.1
- versioned buildrequires for R

* Mon Nov 26 2007 Tom "spot" Callaway <tcallawa@redhat.com> - 1.0-0.4.RC3
- rebuild against R 2.6.1

* Mon Oct  8 2007 Jos?? Matos <jamatos[AT]fc.up.pt> - 1.0-0.3.RC3
- Rebuild for R 2.6.0 (really).

* Fri Oct  5 2007 Jos?? Matos <jamatos[AT]fc.up.pt> - 1.0-0.2.RC3
- Rebuild for R version 2.6.

* Wed Aug 29 2007 Jos?? Matos <jamatos[AT]fc.up.pt> - 1.0-0.1.RC3
- New upstream version.
- Change from python-numeric to numpy package.

* Tue Aug 28 2007 Jos?? Matos <jamatos[AT]fc.up.pt> - 0.4.6-18
- License fix, rebuild for devel (F8).

* Fri Jul  6 2007 Tom "spot" Callaway <tcallawa@redhat.com> - 0.4.6-17
- Rebuild to link with R 2.5.1

* Thu Apr 26 2007 Jos?? Matos <jamatos[AT]fc.up.pt> - 0.4.6-16
- Rebuild to link with R 2.5.0

* Thu Dec 21 2006 Tom "spot" Callaway <tcallawa@redhat.com> - 0.4.6-15
- Rebuild for new R-version.

* Tue Dec 12 2006 Jos?? Matos <jamatos[AT]fc.up.pt> - 0.4.6-14
- Rebuild for python 2.5.

* Tue Oct 17 2006 Jos?? Matos <jamatos[AT]fc.up.pt> - 0.4.6-13
- Rebuild for new R-version.

* Thu Sep 14 2006 Jos?? Matos <jamatos[AT]fc.up.pt> - 0.4.6-12
- Rebuild for FC6.

* Sun Jun  4 2006 Jos?? Matos <jamatos[AT]fc.up.pt> - 0.4.6-11
- Rebuild for R-2.3.1

* Wed Apr 26 2006 Jos?? Matos <jamatos[AT]fc.up.pt> - 0.4.6-10
- BuildRequires tetex for "make pdf" (pdftex).

* Wed Apr 26 2006 Jos?? Matos <jamatos[AT]fc.up.pt> - 0.4.6-9
- Fix detection of R version.

* Wed Apr 26 2006 Jos?? Matos <jamatos[AT]fc.up.pt> - 0.4.6-8
- Rebuild for R-2.3.0

* Fri Feb 17 2006 Alex Lancaster <alexl[AT]users.sourceforge.net> - 0.4.6-7
- Build info docs (bz#169002).
- Build pdf and html documentation, clean doc directory. (jamatos)

* Thu Feb 16 2006 Jos?? Matos <jamatos[AT]fc.up.pt> - 0.4.6-6
- Use a fixed value for R version.

* Thu Feb 16 2006 Jos?? Matos <jamatos[AT]fc.up.pt> - 0.4.6-5
- Set explicit dependency on exact version of R used to build the package. (bz#177078)

* Tue Jan  3 2006 Jos?? Matos <jamatos[AT]fc.up.pt> - 0.4.6-4
- Update for R-2.2.1

* Tue Oct 11 2005 Jos?? Matos <jamatos[AT]fc.up.pt> - 0.4.6-3
- Another try to deal with make tag.

* Mon Oct 10 2005 Jos?? Matos <jamatos[AT]fc.up.pt> - 0.4.6-2
- Rebuild for R-2.2.0

* Thu Sep 15 2005 Jos?? Matos <jamatos[AT]fc.up.pt> - 0.4.6-1
- Initial package for Fedora Extras
