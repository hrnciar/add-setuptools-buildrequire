Name:           votca-csg
Version:        2021
%global         uversion %version
%global         sover 2021
Release:        1%{?dist}
Summary:        VOTCA coarse-graining engine
License:        ASL 2.0
URL:            http://www.votca.org
Source0:        https://github.com/votca/csg/archive/v%{uversion}.tar.gz#/%{name}-%{uversion}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake3
BuildRequires:  eigen3-devel
BuildRequires:  doxygen
BuildRequires:  boost-devel
BuildRequires:  gromacs-devel
BuildRequires:  hdf5-devel
BuildRequires:  perl-generators
BuildRequires:  votca-tools-devel = %{version}
BuildRequires:  txt2tags

Requires:   %{name}-common = %{version}-%{release}
Requires:   %{name}-libs = %{version}-%{release}
# no more pdf manual
Obsoletes:  votca-csg-doc < 2021

%description
Versatile Object-oriented Toolkit for Coarse-graining Applications (VOTCA) is
a package intended to reduce the amount of routine work when doing systematic
coarse-graining of various systems. The core is written in C++.

This package contains the VOTCA coarse-graining engine.


%package libs
Summary:    Libraries for VOTCA coarse-graining engine

%description libs
Versatile Object-oriented Toolkit for Coarse-graining Applications (VOTCA) is
a package intended to reduce the amount of routine work when doing systematic
coarse-graining of various systems. The core is written in C++.

This package contains libraries for the VOTCA coarse-graining engine.

%package devel
Summary:    Development headers and libraries for VOTCA coarse-graining Engine
Requires:   %{name}-libs = %{version}-%{release}
Requires:   %{name} = %{version}-%{release}
Requires:   votca-tools-devel

%description devel
Versatile Object-oriented Toolkit for Coarse-graining Applications (VOTCA) is
a package intended to reduce the amount of routine work when doing systematic
coarse-graining of various systems. The core is written in C++.

This package contains development headers and libraries for the VOTCA
coarse-graining engine.

%package common
Summary:    Architecture independent data files for VOTCA CSG
BuildArch:  noarch

%description common
Versatile Object-oriented Toolkit for Coarse-graining Applications (VOTCA) is
a package intended to reduce the amount of routine work when doing systematic
coarse-graining of various systems. The core is written in C++.

This package contains architecture independent data files for the VOTCA
coarse-graining engine.

%package bash
Summary:    Bash completion for VOTCA CSG
Requires:   %{name} = %{version}-%{release}
Requires:   bash-completion
BuildArch:  noarch

%description bash
Versatile Object-oriented Toolkit for Coarse-graining Applications (VOTCA) is
a package intended to reduce the amount of routine work when doing systematic
coarse-graining of various systems. The core is written in C++.

This package contains bash completion support for the VOTCA coarse-graining
engine.

%prep
%setup -qn csg-%{uversion}

%build
%{cmake3} -DCMAKE_BUILD_TYPE=Release -DENABLE_TESTING=ON -DBUILD_CSGAPPS=ON
%cmake_build

%install
%cmake_install
# Install bash completion file
mkdir -p %{buildroot}%{_datadir}/bash_completion
mv %{buildroot}%{_datadir}/votca/rc/csg-completion.bash %{buildroot}%{_datadir}/bash_completion/votca

%check
%ctest

%ldconfig_scriptlets libs

%files
%{_bindir}/csg_*
%{_mandir}/man1/csg_*.1.*
%{_mandir}/man7/votca-csg.7.*

%files common
%doc CHANGELOG.rst NOTICE.rst README.rst
%license LICENSE.rst
%{_datadir}/votca

%files libs
%license LICENSE.rst
%{_libdir}/libvotca_csg.so.%{sover}

%files devel
%{_includedir}/votca/csg/
%{_libdir}/libvotca_csg.so
%{_libdir}/cmake/VOTCA_CSG

%files bash
%{_datadir}/bash_completion/votca

%changelog
* Sat Mar 13 2021 Christoph Junghans <junghans@votca.org> - 2021-1
- Version bump to v2021 (bug #1916964)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2021~rc1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2021 Jonathan Wakely <jwakely@redhat.com> - 2021~rc1-2
- Rebuilt for Boost 1.75

* Thu Jan 21 12:41:40 MST 2021 Christoph Junghans <junghans@lanl.gov> - 2021~rc1-1
- Version bump to 2021~rc1 (bug #1916964)

* Tue Jan 12 14:46:09 MST 2021 Christoph Junghans <junghans@lanl.gov> - 1.6.4-1
- Version bump to v1.6.4 (bug #1915545)

* Wed Dec  9 17:14:58 MST 2020 Christoph Junghans <junghans@votca.org> - 1.6.3-1
- Version bump to 1.6.3 (bug #1905832)

* Sat Aug 22 2020 Christoph Junghans <junghans@votca.org> - 1.6.2-1
- Version bump to v1.6.2 (bug #1871344)

* Tue Aug 04 2020 Christoph Junghans <junghans@votca.org> - 1.6.1-5
- Fix out-of-source build on F33 (bug#1865609)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Orion Poplawski <orion@cora.nwra.com> - 1.6.1-2
- Rebuild for hdf5 1.10.6

* Sun Jun 21 2020 Christoph Junghans <junghans@votca.org> - 1.6.1-1
- Version bump to v1.6.1

* Thu May 28 2020 Jonathan Wakely <jwakely@redhat.com> - 1.6-2
- Rebuilt for Boost 1.73

* Sat Apr 18 2020 Christoph Junghans <junghans@votca.org> - 1.6-1
- Version bump to v1.6 (bug #1825473)

* Mon Feb 10 2020 Christoph Junghans <junghans@votca.org> - 1.6~rc2-1
- Version bump to 1.6~rc2
- Drop 473.patch - merged upstream

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-0.3rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Dec 12 2019 Christoph Junghans <junghans@votca.org> - 1.6-0.2rc1
- Added upstream 473.patch to fix 32bit build

* Thu Dec 05 2019 Christoph Junghans <junghans@votca.org> - 1.6-0.1rc1
- Version bump to 1.6_rc1 (bug #1779848)

* Fri Nov 22 2019 Christoph Junghans <junghans@votca.org> - 1.5.1-1
- Version bump to 1.5.1 (bug #1774830)

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-3.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Mar 16 2019 Orion Poplawski <orion@nwra.com> - 1.5-3.1
- Rebuild for hdf5 1.10.5

* Sun Feb 17 2019 Christoph Junghans <junghans@votca.org> - 1.5-3
- Rebuild for gromacs-2019

* Tue Feb 05 2019 Christoph Junghans <junghans@votca.org> - 1.5-2
- Fix cma.py shebang

* Sat Feb 02 2019 Christoph Junghans <junghans@votca.org> - 1.5-1
- Version bump to v1.5

* Tue Jan 29 2019 Jonathan Wakely <jwakely@redhat.com> - 1.4.1-2.1
- Rebuilt for Boost 1.69

* Tue Jan 29 2019 Christoph Junghans <junghans@votca.org> - 1.4.1-2
- Fix FTBFS (bug #1670437)

* Fri Jan 25 2019 Jonathan Wakely <jwakely@redhat.com> - 1.4.1-1.1.4
- Rebuilt for Boost 1.69

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-1.1.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-1.1.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 23 2018 Jonathan Wakely <jwakely@redhat.com> - 1.4.1-1.1.1
- Rebuilt for Boost 1.66

* Sat Dec 30 2017 Christoph Junghans <junghans@votca.org> - 1.4.1-1.1
- Rebuild for gromacs-2018

* Sun Sep 03 2017 Christoph Junghans <junghans@votca.org> - 1.4.1-1
- Update to 1.4.1

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-1.6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-1.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 24 2017 Bj??rn Esser <besser82@fedoraproject.org> - 1.4-1.4
- Rebuilt for Boost 1.64

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-1.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-1.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 Jonathan Wakely <jwakely@redhat.com> - 1.4-1.1
- Rebuilt for Boost 1.63

* Sun Oct 30 2016 Christoph Junghans <junghans@votca.org> - 1.4-1
- Update to 1.4
- Added pdf manual in doc package

* Mon Oct 03 2016 Christoph Junghans <junghans@votca.org> - 1.4-0.2rc1
- fix shebang, bash completion install

* Wed Sep 28 2016 Christoph Junghans <junghans@votca.org> - 1.4-0.1rc1
- Update to 1.4_rc1

* Mon Aug 22 2016 Christoph Junghans <junghans@votca.org> - 1.3.1-1
- Update to 1.3.1
- Drop obsolete patch

* Fri May 20 2016 Jonathan Wakely <jwakely@redhat.com> - 1.3-4
- Rebuilt for linker errors in boost (#1331983)

* Fri Apr 01 2016 Dominik Mierzejewski <rpm@greysector.net> - 1.3-3
- rebuild for gromacs
- fix recent libgromacs_d detection using upstream patch

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jan 24 2016 Thomas Spura <tomspur@fedoraproject.org> - 1.3-2
- Rebuilt for gromacs

* Tue Jan 19 2016 Christoph Junghans <junghans@votca.org> - 1.3-1
- update to 1.3
- cleanup spec

* Mon Nov 09 2015 Thomas Spura <tomspur@fedoraproject.org> - 1.3-0.1.rc1
- update to 1.3_rc1
- cleanup spec

* Thu Sep 03 2015 Jonathan Wakely <jwakely@redhat.com> - 1.2.4-10
- Rebuilt for Boost 1.59

* Sun Aug 30 2015 Thomas Spura <tomspur@fedoraproject.org> - 1.2.4-9
- Add another patch by Christoph Junghans to build with gromacs-5.1

* Fri Aug 28 2015 Jonathan Wakely <jwakely@redhat.com> - 1.2.4-8
- Rebuilt for Boost 1.59

* Fri Aug 21 2015 Thomas Spura <tomspur@fedoraproject.org> - 1.2.4-7
- Add patch by Christoph Junghans to build with gromacs-5.1

* Wed Aug 05 2015 Thomas Spura <tomspur@fedoraproject.org> - 1.2.4-6
- Rebuilt for new boost

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Apr 24 2015 Thomas Spura <tomspur@fedoraproject.org> - 1.2.4-4
- Rebuilt against new gromacs

* Thu Feb 05 2015 Thomas Spura <tomspur@fedoraproject.org> - 1.2.4-3
- Rebuilt for new boost

* Sun Sep  7 2014 Thomas Spura <tomspur@fedoraproject.org> - 1.2.4-2
- correct source url

* Fri Sep 05 2014 Christoph Junghans <junghans@votca.org> - 1.2.4-1
- Update to 1.2.4
- Drop obsolete patch

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 David Tardon <dtardon@redhat.com> - 1.2.3-6
- rebuild for boost 1.55.0

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jul 28 2013 Petr Machata <pmachata@redhat.com> - 1.2.3-4
- Rebuild for boost 1.54.0

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 1.2.3-3
- Perl 5.18 rebuild

* Thu Mar 07 2013 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.2.3-2
- Rebuild for Gromacs 4.6.1.

* Sun Feb 10 2013 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.2.3-1
- Update to 1.2.3.

* Sat Feb 09 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1.2.1-6
- Rebuild for Boost-1.53.0

* Wed Aug 15 2012 Jussi Lehtola <jussilehtola@fedoraproject.org> - 1.2.1-5
- Bump spec due to boost update.

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-3
- Rebuilt for c++ ABI breakage

* Tue Jan 10 2012 Jussi Lehtola <jussilehtola@fedoraproject.org> - 1.2.1-2
- Fix FTBFS on rawhide.

* Wed Nov 23 2011 Jussi Lehtola <jussilehtola@fedoraproject.org> - 1.2.1-1.1
- Bump due to boost update.

* Thu Aug 25 2011 Jussi Lehtola <jussilehtola@fedoraproject.org> - 1.2.1-1
- Update to 1.2.1.

* Sat Jul 23 2011 Jussi Lehtola <jussilehtola@fedoraproject.org> - 1.1-3
- Bump spec due to new boost.

* Thu Apr 07 2011 Jussi Lehtola <jussilehtola@fedoraproject.org> - 1.1-2
- Bump spec due to boost upgrade.

* Mon Feb 21 2011 Jussi Lehtola <jussilehtola@fedoraproject.org> - 1.1-1
- Update to 1.1.

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Feb 06 2011 Thomas Spura <tomspur@fedoraproject.org> - 1.0.1-3
- rebuild for new boost

* Wed Dec 08 2010 Jussi Lehtola <jussilehtola@fedoraproject.org> - 1.0.1-2
- Fix spelling error in Requires of -devel, preserve timestamps upon install.

* Tue Dec 07 2010 Jussi Lehtola <jussilehtola@fedoraproject.org> - 1.0.1-1
- Update to 1.0.1.
- Added bash completion package.

* Thu Nov 25 2010 Jussi Lehtola <jussilehtola@fedoraproject.org> - 1.0-1
- First release.
