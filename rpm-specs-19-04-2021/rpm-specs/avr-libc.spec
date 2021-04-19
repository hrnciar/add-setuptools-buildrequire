 # FORCE NOARCH
# This package is noarch intentionally, although it supplies binaries,
# as they're not intended for the build platform, but for AVR.
# The related discussion can be found here:
# https://www.redhat.com/archives/fedora-devel-list/2009-February/msg02261.html
%global _binaries_in_noarch_packages_terminate_build 0

Name:           avr-libc
Version:        2.0.0
Release:        11%{?dist}
Summary:        C library for use with GCC on Atmel AVR microcontrollers
License:        BSD
URL:            http://www.nongnu.org/avr-libc/
#Source0:        http://download.savannah.gnu.org/releases/avr-libc/avr-libc-%{version}.tar.bz2
#Source4:        http://distribute.atmel.no/tools/opensource/Atmel-AVR-GNU-Toolchain/3.4.2/avr/avr-patches.tar.gz
# since 3.4.3 atmel no longer distributes patch set, only patched sources in tarball
Source0:        http://distribute.atmel.no/tools/opensource/Atmel-AVR-GNU-Toolchain/3.5.4/avr-libc.tar.bz2#/avr-libc-%{version}+atmel.tar.bz2
Source1:        http://download.savannah.gnu.org/releases/avr-libc/avr-libc-manpages-%{version}.tar.bz2
Source2:        http://download.savannah.gnu.org/releases/avr-libc/avr-libc-user-manual-%{version}.tar.bz2
Source3:        http://download.savannah.gnu.org/releases/avr-libc/avr-libc-user-manual-%{version}.pdf.bz2
Patch0:         avr-libc-1.6.4-documentation.patch
Source5:        http://distribute.atmel.no/tools/opensource/Atmel-AVR-GNU-Toolchain/3.5.4/avr/avr8-headers.zip

BuildRequires:  avr-gcc, autoconf, automake, libtool
BuildRequires: make
BuildArch:      noarch

%description
AVR Libc is a Free Software project whose goal is to provide a high quality C
library for use with GCC on Atmel AVR microcontrollers.

AVR Libc is licensed under a single unified license. This so-called modified
Berkeley license is intented to be compatible with most Free Software licenses
like the GPL, yet impose as little restrictions for the use of the library in
closed-source commercial applications as possible.


%package doc
Summary:        AVR C library docs in html and pdf format
Requires:       %{name} = %{version}-%{release}
Obsoletes:      %{name}-docs < %{version}-%{release}

%description doc
This package contains the AVR C library docs in html and pdf format, the main
package already contains the docs in man-page format (use "avr-man xxxx" to
access these).


%prep
%setup -q -c
# atmel's tarball needs some shuffling to have expected directory layout
# must be done in two steps because of conflicting libc directory
mv libc delete-libc
mv delete-libc/avr-libc/* .
rmdir delete-libc/avr-libc
tar -joxf %SOURCE1
%patch0 -p1 -b .nolatexbatch

I=0
unzip %{SOURCE5} -d avr8-headers
for i in ./avr8-headers/avr/io[0-9a-zA-Z]*.h
do
  cp $i include/avr/ -v
done

# Add html docs
mkdir html
cd html/
tar -jxvf %SOURCE2
cd -

# Add pdf manual
mkdir pdf
cd pdf/
bzip2 -dc %SOURCE3 > avr-libc-user-manual-%{version}.pdf
cd -

for i in doc/api/faq.dox doc/api/overview.dox include/stdio.h include/stdlib.h;
  do
    iconv -f CP1252 -t UTF8 $i > tmp
    mv tmp $i
done
sed -i 's|@DOC_INST_DIR@/man|%{_prefix}/avr/share/man|' scripts/avr-man.in


%build
./bootstrap
# The ps doc ways in at 7Mb versus 2.5 for the pdf and has little added value
./configure --prefix=%{_prefix} --host=avr --build=`./config.guess` #--enable-doc
# don't use %{?_smp_mflags}, it breaks the build
make


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

# put the man-pages in the FHS mandir and gzip them
mkdir -p $RPM_BUILD_ROOT%{_prefix}/avr/share
find man/ -type f -exec gzip {} \;
mv man  $RPM_BUILD_ROOT%{_prefix}/avr/share

# we only want to use %doc with an absolute path to avoid rpmbuild from erasing
# %{_docdir}/%{name}
mv $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version} $RPM_BUILD_ROOT%{_docdir}/%{name}
install -p -m 644 doc/TODO doc/CHANGES.old AUTHORS ChangeLog* LICENSE NEWS \
  pdf/* README $RPM_BUILD_ROOT%{_docdir}/%{name}
mkdir $RPM_BUILD_ROOT%{_docdir}/%{name}/html
cp -ap html/%{name}-user-manual*/* $RPM_BUILD_ROOT%{_docdir}/%{name}/html
chmod -R u=rwX,g=rX,o=rX $RPM_BUILD_ROOT%{_docdir}/%{name}/html

# despite us being noarch redhat-rpm-config insists on stripping our files
%if %{fedora}0 > 200
%global __os_install_post /usr/lib/rpm/brp-compress
%else
%global __os_install_post /usr/lib/rpm/redhat/brp-compress
%endif


%files
%dir %{_prefix}/avr
%dir %{_prefix}/avr/share
%doc %{_prefix}/avr/share/man
%dir %{_docdir}/%{name}
%doc %{_docdir}/%{name}/AUTHORS
%doc %{_docdir}/%{name}/C*
%doc %{_docdir}/%{name}/LICENSE
%doc %{_docdir}/%{name}/NEWS
%doc %{_docdir}/%{name}/README
%doc %{_docdir}/%{name}/TODO
%doc %{_docdir}/%{name}/examples
%{_prefix}/avr/include
%{_prefix}/avr/lib
%{_bindir}/avr-man

%files doc
%doc %{_docdir}/%{name}/html
%doc %{_docdir}/%{name}/%{name}*.pdf

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Nov 10 2020 Michal Hlavinka <mhlavink@redhat.com> - 2.0.0-10
- rebuild for avr-gcc 10.2.0

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Nov 13 2016 Michal Hlavinka <mhlavink@redhat.com> - 2.0.0-2
- rebuild with new avr-gcc

* Sun Nov 13 2016 Michal Hlavinka <mhlavink@redhat.com> - 2.0.0-1
- updated to 2.0.0

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Dec 01 2015 Michal Hlavinka <mhlavink@redhat.com> - 1.8.0-11
- bump release for rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 09 2014 Michal Hlavinka <mhlavink@redhat.com> - 1.8.0-9
- fix FTBFS (#1105987)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Aug 08 2013 Michal Hlavinka <mhlavink@redhat.com> - 1.8.0-7
- use unversioned docdir (#993677)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jun 25 2013 Michal Hlavinka <mhlavink@redhat.com> - 1.8.0-5
- use more atmel's patches to support more MCUs (#972384)

* Wed Mar 27 2013 Michal Hlavinka <mhlavink@redhat.com> - 1.8.0-4
- fix aarch64 support (#925065)

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Dec 04 2012 Michal Hlavinka <mhlavink@redhat.com> - 1.8.0-2
- fix avr-libc-docs -> avr-libc-doc transition (#883339)

* Thu Nov 15 2012 Michal Hlavinka <mhlavink@redhat.com> - 1.8.0-1
- updated to 1.8.0

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jan 3 2012 Thibault North <tnorth@fedoraproject.org> 1.7.1-3
- Build docs with doxygen

* Wed Dec 7 2011 Thibault North <tnorth@fedoraproject.org> 1.7.1-2
- Add html and pdf docs

* Sat Oct 15 2011 Thibault North <tnorth@fedoraproject.org> 1.7.1-1
- New upstream release
- Fix PSTR definition BZ#737449
- Remove docs for now as they don't compile properly (sorry)

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 11 2010 Thibault North <tnorth@fedoraproject DOT org> 1.7.0-1
- Version 1.7.0

* Fri Mar 12 2010 Thibault North <tnorth AT fedoraproject DOT org> 1.6.8-1
- New upstream release. Fixes in power.h for 8-bits AVR

* Mon Nov 30 2009 Thibault North <tnorth AT fedoraproject DOT org> 1.6.5-2
- Rebuild with new avr-gcc

* Wed Nov 25 2009 Thibault North <tnorth AT fedoraproject DOT org> 1.6.5-1
- Updated to 1.6.7 

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue May 26 2009 Michael Schwendt <mschwendt@fedoraproject.org> - 1.6.4-4
- Fix unowned versioned documentation directory (#473625).

* Sat Apr 18 2009 Milos Jakubicek <xjakub@fi.muni.cz> - 1.6.4-3
- Fix FTBFS: force noarch (see comment in the top of the spec file).

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Feb 19 2009 Thibault North <tnorth AT fedoraproject DOT org> 1.6.4-1
- New upstream release
- Patches update

* Tue Jul 17 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1.4.6-4
- Gzip manpages
- Make manpages %%doc
- Install -docs documentation in same dir as the main package docs
- Change License field from GPL to BSD (oops)

* Sun Jun 10 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1.4.6-3
- Move man pages to /usr/avr/share/man

* Fri May 25 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1.4.6-2
- Add patch from Trond Danielsen (trond.danielsen@gmail.com) to fix pdf doc
  generation
- Put html and pdf docs in a seperate -docs subpackage

* Thu May 24 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1.4.6-1
- Initial Fedora package
