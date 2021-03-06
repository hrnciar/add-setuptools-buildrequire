%global srcname gmpy2
%global prerelease b5

Name:           python-%{srcname}
Version:        2.1.0
Release:        0.22%{?prerelease:.%{prerelease}}%{?dist}
Summary:        Python interface to GMP, MPFR, and MPC

License:        LGPLv3+
URL:            https://pypi.python.org/pypi/gmpy2
Source0:        https://github.com/aleaxit/gmpy/archive/%{srcname}-%{version}%{?prerelease}.tar.gz
# Fix build with python 3.10
# https://github.com/aleaxit/gmpy/pull/283
Patch0:         %{name}-python310.patch
# Some tests return different results in python 3.10 due to this change:
# "If object.__ipow__() returns NotImplemented, the operator will correctly
#  fall back to object.__pow__() and object.__rpow__() as expected.
#  https://bugs.python.org/issue38302"
Patch1:         %{name}-pow.patch

BuildRequires:  gcc
BuildRequires:  gmp-devel
BuildRequires:  libmpc-devel
BuildRequires:  make
BuildRequires:  pkgconfig(mpfr)
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist cython}
BuildRequires:  %{py3_dist setuptools}
BuildRequires:  %{py3_dist sphinx}

%global common_desc \
This package contains a C-coded Python extension module that supports \
multiple-precision arithmetic.  It is the successor to the original \
gmpy module.  The gmpy module only supported the GMP multiple-precision \
library.  Gmpy2 adds support for the MPFR (correctly rounded real \
floating-point arithmetic) and MPC (correctly rounded complex \
floating-point arithmetic) libraries.  It also updates the API and \
naming conventions to be more consistent and support the additional \
functionality.

%description
%{common_desc}

%package -n python3-%{srcname}
Summary:        Python 3 interface to GMP, MPFR, and MPC
Provides:       bundled(jquery)

%description -n python3-%{srcname}
%{common_desc}

%prep
%autosetup -N -n gmpy-%{srcname}-%{version}%{?prerelease}
%patch0 -p1
%if 0%{?python3_version_nodots} >= 310
%patch1 -p1
%endif

# Update the sphinx theme name
sed -i "s/'default'/'classic'/" docs/conf.py

# Version 2.1.0b5 still calls itself 2.1.0b1
sed -i "s/b1/b5/" docs/conf.py

# Symbols from the math library are also used
sed -i "s/'mpfr','gmp'/&,'m'/" setup.py

%build
# Do not pass -pthread to the compiler or linker
export CC=gcc
export LDSHARED="gcc -shared"

%py3_build
make -C docs html

%install
%py3_install

%check
export PYTHONPATH=%{buildroot}%{python3_sitearch}
%{python3} test/runtests.py
cd test_cython
%{python3} setup_cython.py build '--executable=%{python3} -s'
%{python3} runtests.py
cd -

%files -n python3-%{srcname}
%license COPYING COPYING.LESSER
%doc docs/_build/html/*
%{python3_sitearch}/%{srcname}*

%changelog
* Tue Mar  9 2021 Jerry James <loganjerry@gmail.com> - 2.1.0-0.22.b5
- Add -pow patch for python 3.10 compatibility (bz 1936947)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-0.21.b5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Nov 13 2020 Jerry James <loganjerry@gmail.com> - 2.1.0-0.20.b5
- Add -python310 patch (bz 1897588)

* Fri Jul 31 2020 Jerry James <loganjerry@gmail.com> - 2.1.0-0.19.b5
- Version 2.1.0 beta5
- Drop all patches

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-0.18.b4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 24 2020 Jerry James <loganjerry@gmail.com> - 2.1.0-0.17.b4
- Add -endian patch to fix s390x problems

* Tue May 26 2020 Miro Hron??ok <mhroncok@redhat.com> - 2.1.0-0.16.b4
- Rebuilt for Python 3.9

* Mon Feb 10 2020 Jerry James <loganjerry@gmail.com> - 2.1.0-0.15.b4
- Version 2.1.0 beta4
- Also run the Cython tests

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-0.14.b3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Dec 11 2019 Jerry James <loganjerry@gmail.com> - 2.1.0-0.13.b3
- Fix overlinking (with libpthread) and underlinking (missing libm)
- Drop unnecessary cython BR

* Wed Oct  9 2019 Jerry James <loganjerry@gmail.com> - 2.1.0-0.12.b3
- Rebuild for mpfr 4

* Mon Sep  2 2019 Jerry James <loganjerry@gmail.com> - 2.1.0-0.11.b3
- Update to beta 3
- Drop upstreamed -qdiv, -no-copy, and -test patches

* Mon Aug 19 2019 Miro Hron??ok <mhroncok@redhat.com> - 2.1.0-0.10.b1
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-0.9.b1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 27 2019 Jerry James <loganjerry@gmail.com> - 2.1.0-0.8.b1
- Add -qdiv, -no-copy, and -test patches to fix the build

* Wed May 22 2019 Jerry James <loganjerry@gmail.com> - 2.1.0-0.8.b1
- Update to beta 1

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-0.7.a4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Nov 15 2018 Jerry James <loganjerry@gmail.com> - 2.1.0-0.6.a4
- Update to alpha 4
- Drop python2 subpackage (bz 1647371)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-0.5.a2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 26 2018 Jerry James <loganjerry@gmail.com> - 2.1.0-0.4.a2
- Take 2 on the -addzero patch

* Tue Jun 26 2018 Jerry James <loganjerry@gmail.com> - 2.1.0-0.3.a2
- Add -addzero patch to fix bogus results in sympy

* Tue Jun 19 2018 Miro Hron??ok <mhroncok@redhat.com> - 2.1.0-0.2.a2
- Rebuilt for Python 3.7

* Sat Jun  2 2018 Jerry James <loganjerry@gmail.com> - 2.1.0-0.1.a2
- Update to alpha version for sagemath 8.2

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hron??ok <mhroncok@redhat.com> - 2.0.8-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.8-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue Jun 28 2016 Jerry James <loganjerry@gmail.com> - 2.0.8-1
- New upstream release
- Drop upstreamed -decref patch

* Fri Mar 25 2016 Jerry James <loganjerry@gmail.com> - 2.0.7-4
- Add -decref patch

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Feb  1 2016 Jerry James <loganjerry@gmail.com> - 2.0.7-2
- Comply with latest python packaging guidelines

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Sat Aug 22 2015 Jerry James <loganjerry@gmail.com> - 2.0.7-1
- New upstream release

* Mon Jul  6 2015 Jerry James <loganjerry@gmail.com> - 2.0.6-1
- New upstream release

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jan 19 2015 Jerry James <loganjerry@gmail.com> - 2.0.5-1
- New upstream release
- Drop patch for 32-bit systems, fixed upstream

* Mon Oct 13 2014 Jerry James <loganjerry@gmail.com> - 2.0.4-1
- New upstream release

* Fri Sep 12 2014 Jerry James <loganjerry@gmail.com> - 2.0.3-2
- BR python2-devel instead of python-devel
- Provide bundled(jquery)

* Fri Sep  5 2014 Jerry James <loganjerry@gmail.com> - 2.0.3-1
- Initial RPM
