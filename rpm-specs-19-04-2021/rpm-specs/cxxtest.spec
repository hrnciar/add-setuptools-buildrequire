Name:           cxxtest
Version:        4.4
Release:        23%{?dist}
Summary:        A JUnit-like testing framework for C++

License:        LGPLv3
URL:            https://cxxtest.com
Source0:        https://github.com/CxxTest/%{name}/releases/download/%{version}/%{name}-%{version}.tar.gz
Patch0:         %{name}-shebang.patch
# adapt helper script doc/include_anchors.py to work with Python 3
Patch1:         %{name}-include-anchors.patch

BuildArch:      noarch

BuildRequires:  asciidoc >= 8.5.0
BuildRequires:  dblatex
BuildRequires:  python3-devel
BuildRequires:  texlive-multirow
BuildRequires:  texlive-upquote
BuildRequires: make

# the --fog-parser option requires 'ply'
Requires:       python3-ply

%description
CxxTest is a unit testing framework for C++ that is similar in spirit to
JUnit, CppUnit, and xUnit. CxxTest is easy to use because it does not require
precompiling a CxxTest testing library, it employs no advanced features of
C++ (e.g. RTTI) and it supports a very flexible form of test discovery.


%package doc
Summary:        Documentation on how to use CxxTest
Requires:       %{name} = %{version}-%{release}

%description doc
This package contains the documentation on how to use CxxTest.
It also provides code examples.


%prep
%autosetup -p1

rm -f doc/images/icons/README
# remove Windows-related stuff
rm -rf sample/msvc/
rm -f sample/Makefile.bcc32
# remove Python 2 sources
rm -rf python/cxxtest/

find . -name ".cvsignore" -delete
sed -i "s|^PY = python$|PY = %{__python3}|" doc/Makefile


%build
cd python
CFLAGS="%{optflags}" %{__python3} setup.py build

# create pkgconfig file
cd ..
cat <<EOF >%{name}.pc
prefix=%{_prefix}
exec_prefix=%{_prefix}
includedir=%{_includedir}/%{name}

Name: %{name}
Description: A JUnit-like testing framework for C++
Version: %{version}
Cflags: -I\${includedir}
EOF

cd doc

# script to create asciidoc file for manpage of cxxtestgen
cat <<EOF >create_manpage.py
import sys
sys.path.insert(0, '../python/python3')
import cxxtest
cxxtest.create_manpage()
EOF

# create manpage
%{__python3} create_manpage.py
a2x -f manpage cxxtestgen.1.txt

# build documentation in PDF and HTML format (requires asciidoc >= 8.5.0)
make pdf html


%install
mkdir -p %{buildroot}%{_includedir}/cxxtest
install -D -p -m 644 cxxtest/* %{buildroot}%{_includedir}/cxxtest
install -D -p -m 644 %{name}.pc %{buildroot}%{_datadir}/pkgconfig/%{name}.pc
cd python
%{__python3} setup.py install --skip-build --root %{buildroot}

%if 0%{?rhel} == 6
# add symlink present in previous release of cxxtest
ln -s %{_bindir}/cxxtestgen %{buildroot}%{_bindir}/cxxtestgen.py
%endif

cd ..
install -D -p -m 644 doc/cxxtestgen.1 %{buildroot}%{_mandir}/man1/cxxtestgen.1


%files
%doc COPYING README Versions
%{_bindir}/cxxtestgen*
%{_includedir}/%{name}/
%{_datadir}/pkgconfig/%{name}.pc
%{_mandir}/man1/cxxtestgen.1*
%{python3_sitelib}/%{name}/
%{python3_sitelib}/%{name}-*.egg-info


%files doc
%doc doc/guide.pdf doc/guide.html doc/images/
%doc sample/


%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.4-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.4-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hron??ok <mhroncok@redhat.com> - 4.4-21
- Rebuilt for Python 3.9

* Tue Mar 03 2020 Martin Gieseking <martin.gieseking@uos.de> - 4.4-20
- Dropped Python 2 dependencies and references.
- Added patch to make helper script doc/include_anchors.py work with Python 3

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.4-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hron??ok <mhroncok@redhat.com> - 4.4-18
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hron??ok <mhroncok@redhat.com> - 4.4-17
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Martin Gieseking <martin.gieseking@uos.de> - 4.4-14
- Fixed Python shebang cxxtest.
- Ensure proper call of Python 2 in doc/Makefile.

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Miro Hron??ok <mhroncok@redhat.com> - 4.4-12
- Rebuilt for Python 3.7

* Fri Jun 29 2018 Martin Gieseking <martin.gieseking@uos.de> - 4.4-11
- - Added missing build dependency texlive-upquote required as of f29 to build the PDF manual.

* Tue Jun 19 2018 Miro Hron??ok <mhroncok@redhat.com> - 4.4-10
- Rebuilt for Python 3.7

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hron??ok <mhroncok@redhat.com> - 4.4-6
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Mar 02 2016 Martin Gieseking <martin.gieseking@uos.de> 4.4-4
- Switched package to Python 3.
- Added dependency on ply to enable command-line option --fog-parser.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Sep 18 2014 Martin Gieseking <martin.gieseking@uos.de> 4.4-1
- updated to release 4.4

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Petr Pisar <ppisar@redhat.com> - 4.3-3
- Perl 5.18 rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 22 2013 Martin Gieseking <martin.gieseking@uos.de> 4.3-1
- updated to release 4.3

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 4.2.1-2
- Perl 5.18 rebuild

* Fri Apr 12 2013 Martin Gieseking <martin.gieseking@uos.de> 4.2.1-1
- updated to release 4.2.1 which fixes the license information in the source headers

* Wed Mar 20 2013 Martin Gieseking <martin.gieseking@uos.de> 4.2-1
- updated to release 4.2
- changed license to LGPLv3 as intended by upstream

* Fri Mar 15 2013 Martin Gieseking <martin.gieseking@uos.de> 4.1-4
- dropped generation of EPUB manual since it can't be build on koji

* Fri Mar 15 2013 Martin Gieseking <martin.gieseking@uos.de> 4.1-3
- added local pkgconfig file
- added documentation in HTML and EPUB format

* Tue Feb 05 2013 Martin Gieseking <martin.gieseking@uos.de> 4.1-2
- removed broken HTML documentation as it requires a more recent asciidoc (>= 8.5.0)
- build and add the PDF manual to the doc package
- addded symlink cxxtestgen.py to stay compatible with previous package (< f19 only)

* Wed Jan 23 2013 Martin Gieseking <martin.gieseking@uos.de> 4.1-1
- updated to release 4.1
- removed old EPEL stuff

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.10.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.10.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Dec 19 2011 Martin Gieseking <martin.gieseking@uos.de> - 3.10.1-5
- Fixed https://bugzilla.redhat.com/show_bug.cgi?id=768869

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.10.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Aug 05 2009 Martin Gieseking <martin.gieseking@uos.de> - 3.10.1-3
- added exclude tags in files section

* Tue Aug 04 2009 Martin Gieseking <martin.gieseking@uos.de> - 3.10.1-2
- moved headers from devel to main package
- added BuildRequires to avoid build problems
- dropped Requires tag
- cxxtest include directory now explicitely listed in files section

* Tue Aug 04 2009 Martin Gieseking <martin.gieseking@uos.de> - 3.10.1-1
- initial release
