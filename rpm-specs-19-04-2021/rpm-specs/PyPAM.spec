Summary:        PAM bindings for Python
Name:           PyPAM
Version:        0.5.0
Release:        48%{?dist}
# Note that the upstream site is dead.
Source0:        http://www.pangalactic.org/PyPAM/%{name}-%{version}.tar.gz
Url:            http://www.pangalactic.org/PyPAM
Patch0:         PyPAM-dlopen.patch
Patch1:         PyPAM-0.5.0-dealloc.patch
Patch2:         PyPAM-0.5.0-nofree.patch
Patch3:         PyPAM-0.5.0-memory-errors.patch
Patch4:         PyPAM-0.5.0-return-value.patch
Patch5:         PyPAM-python3-support.patch
License:        LGPLv2
BuildRequires:  pam-devel
BuildRequires:  gcc
%filter_provides_in %{python3_sitearch}/PAM*.so$
%filter_setup

%global _description\
PAM (Pluggable Authentication Module) bindings for Python.

%description %_description

%package -n python3-PyPAM
Summary:        PAM bindings for Python 3
BuildRequires:  python3-devel

%description -n python3-PyPAM
PAM (Pluggable Authentication Module) bindings for Python 3.

%prep
%setup -q
%patch0 -p1 -b .dlopen
%patch1 -p1 -b .dealloc
%patch2 -p1 -b .nofree
%patch3 -p1 -b .memory
%patch4 -p1 -b .retval
%patch5 -p0 -b .python3
# remove prebuild rpm and others binaries
rm -rf build dist

%build
%set_build_flags
CFLAGS="$CFLAGS -fno-strict-aliasing" %{__python3} setup.py build

%install
%{__python3} setup.py install --root=$RPM_BUILD_ROOT

# Make sure we don't include binary files in the docs
chmod 644 examples/pamtest.py
rm -f examples/pamexample

%check
PYTHONPATH=build/lib.linux-`uname -m`-%{python3_version}/ %{__python3} tests/PamTest.py

%files -n python3-PyPAM
%{python3_sitearch}/PAM*.so
%{python3_sitearch}/*.egg-info
%license COPYING
%doc AUTHORS NEWS README ChangeLog INSTALL
%doc examples

%changelog
* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-48
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.5.0-46
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-45
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.0-44
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 15 2019 Miroslav Suchý <msuchy@redhat.com> 0.5.0-42
- simplify spec
- fix build issue

* Fri Jul 12 2019 Miroslav Suchý <msuchy@redhat.com> 0.5.0-41
- stop building python2 bindings

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.5.0-38
- Rebuilt for Python 3.7

* Sat May 05 2018 Miro Hrončok <mhroncok@redhat.com> - 0.5.0-37
- Update Python macros to new packaging standards
  (See https://fedoraproject.org/wiki/Changes/Avoid_usr_bin_python_in_RPM_Build)

* Mon Feb 19 2018 Miroslav Suchý <msuchy@redhat.com> 0.5.0-36
- add gcc as buildrequires

* Wed Feb 07 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.5.0-35
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Aug 21 2017 Miroslav Suchý <msuchy@redhat.com> 0.5.0-33
- remove obsoleted parts of spec

* Sun Aug 20 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.5.0-32
- Add Provides for the old name without %%_isa

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.5.0-31
- Python 2 binary package renamed to python2-pypam
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 07 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.5.0-28
- Rebuild due to bug in RPM (RHBZ #1468476)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec 22 2016 Miro Hrončok <mhroncok@redhat.com> - 0.5.0-26
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-25
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-23
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jun 24 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 0.5.0-20
- Add Python 3 support.

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon May  7 2012 Tomáš Mráz <tmraz@redhat.com> - 0.5.0-15
- fix one more memory leak

* Mon May  7 2012 Tomáš Mráz <tmraz@redhat.com> - 0.5.0-14
- always return the error code in exceptions (#819244)

* Fri May  4 2012 Tomáš Mráz <tmraz@redhat.com> - 0.5.0-13
- fix memory manipulation errors (leaks, doublefree CVE-2012-1502)

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 23 2011 Miroslav Suchý <msuchy@redhat.com> 0.5.0-10
- 679714 - deallocate the conversation response only in case of error

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jan 19 2011 Miroslav Suchý <msuchy@redhat.com> 0.5.0-9
- 658955 - fix two bugs in the PAM object deallocation
- add -fno-strict-aliasing to CFLAGS

* Thu Aug 05 2010 Miroslav Suchý <msuchy@redhat.com> 0.5.0-7
- 612998 - PyPAM do not work with python3 (msuchy@redhat.com)

* Thu Aug 05 2010 Miroslav Suchý <msuchy@redhat.com> 0.5.0-6
- 612998 - fix condition for BR (msuchy@redhat.com)

* Thu Aug 05 2010 Miroslav Suchý <msuchy@redhat.com> 0.5.0-5
- 612998 - return back BR for python

* Thu Aug 05 2010 Miroslav Suchý <msuchy@redhat.com> 0.5.0-4
- 612998 - remove binaries. Just in case
- 612998 - filter provide PAMmodule.so()(64bit)
- 612998 - do not use INSTALLED_FILES feature, and enumerate files manualy
- 612998 - use %%{__python} in %%build section
- 612998 - fix buildrequires for PyPAM
- 612998 - add macros for rhel5

* Fri Jul 09 2010 Miroslav Suchý <msuchy@redhat.com> 0.5.0-3
- rebuild 

* Fri Jul 09 2010 Miroslav Suchý <msuchy@redhat.com> 0.5.0-2
- rebase PyPAM-dlopen.patch to latest source

* Fri Jul 09 2010 Miroslav Suchý <msuchy@redhat.com> 0.5.0-1
- rebase to PyPAM 0.5.0

* Fri Mar 06 2009 Devan Goodwin <dgoodwin@redhat.com> 0.4.2-26
- Fix bad patch whitespace.

* Fri Feb 27 2009 Dennis Gilmore 0.4.2-25
- rebuild to pick up ppc ppc64 ia64 arches

* Fri Feb 27 2009 Devan Goodwin <dgoodwin@redhat.com> 0.4.2-23
- Rebuild for new rel-eng tools.

* Fri May 16 2008 Michael Mraka <michael.mraka@redhat.com> 0.4.2-20
- fixed file ownership

* Tue Jun 22 2004 Mihai Ibanescu <misa@redhat.com> 0.4.2-5
- Rebuilt

* Fri Jul 11 2003 Mihai Ibanescu <misa@redhat.com>
- Adapted the original rpm to build with python 2.2
