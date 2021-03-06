# Arches on which the multilib {sysdefs,types}.h hack is needed:
# (Update libast-wrapper.h when adding archs)

%define multilib_arches %{ix86} ia64 ppc ppc64 s390 s390x x86_64
%define cvs 20080502

Summary:        Library of Assorted Spiffy Things
Name:           libast
Version:        0.7.1
Release:        0.28.%{cvs}cvs%{?dist}
License:        BSD
URL:            http://www.eterm.org/
# Sources are pulled from cvs:
# $ cvs -z3 -d :pserver:anonymous@anoncvs.enlightenment.org:/var/cvs/e \
#      co -d libast-20080502 -D 20080502 eterm/libast
# $ tar czvf libast-20080502.tar.gz libast-20080502
Source:        libast-%{cvs}.tar.gz
Source1:       libast-wrapper.h
BuildRequires: imlib2-devel pcre-devel libXt-devel
BuildRequires: automake autoconf libtool
BuildRequires: make

%description
LibAST is the Library of Assorted Spiffy Things.  It contains various
handy routines and drop-in substitutes for some good-but-non-portable
functions.  It currently has a built-in memory tracking subsystem as
well as some debugging aids and other similar tools.

It's not documented yet, mostly because it's not finished.  Hence the
version number that begins with 0.

%package devel
Summary:  Header files, libraries and development documentation for %{name}
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -q -n %{name}-%{cvs}

%build
./autogen.sh
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} DESTDIR=%{buildroot} install

# Fix multiarch stuff
%ifarch %{multilib_arches}
for header in sysdefs types ; do
    mv %{buildroot}%{_includedir}/%{name}/$header.h \
       %{buildroot}%{_includedir}/%{name}/$header-%{_arch}.h
    %{__install} -m 0644 -c %{SOURCE1} %{buildroot}%{_includedir}/%{name}/$header.h
    %{__sed} -i -e 's/<HEADER>/'$header'/g' %{buildroot}%{_includedir}/%{name}/$header.h
    touch -r ChangeLog %{buildroot}%{_includedir}/%{name}/$header.h
done
%{__sed} -i -e '/^LDFLAGS=/d' %{buildroot}%{_bindir}/%{name}-config
touch -r ChangeLog %{buildroot}%{_bindir}/%{name}-config
%endif

%ldconfig_scriptlets

%files
%doc ChangeLog DESIGN README LICENSE
%{_libdir}/%{name}.so.*

%files devel
%dir %{_includedir}/%{name}
%{_bindir}/%{name}-config
%{_libdir}/%{name}.so
%{_includedir}/%{name}.h
%{_includedir}/%{name}/*.h
%{_datadir}/aclocal/%{name}.m4
%exclude %{_libdir}/*.la
%exclude %{_libdir}/*.a

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-0.28.20080502cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-0.27.20080502cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-0.26.20080502cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-0.25.20080502cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-0.24.20080502cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-0.23.20080502cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-0.22.20080502cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-0.21.20080502cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-0.20.20080502cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-0.19.20080502cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-0.18.20080502cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-0.17.20080502cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-0.16.20080502cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-0.15.20080502cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-0.14.20080502cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-0.13.20080502cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-0.12.20080502cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Feb 10 2012 Petr Pisar <ppisar@redhat.com> - 0.7.1-0.11.20080502cvs
- Rebuild against PCRE 8.30

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-0.10.20080502cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-0.9.20080502cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-0.8.20080502cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-0.7.20080502cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri May  2 2008 Terje R??sten <terje.rosten@ntnu.no> - 0.7.1-0.6.20080502cvs
- Fix source url

* Sat Feb 11 2008 Terje R??sten <terje.rosten@ntnu.no> - 0.7.1-0.5.20060818cvs
- Fix date

* Sat Feb  9 2008 Terje R??sten <terje.rosten@ntnu.no> - 0.7.1-0.4.20060818cvs
- Rebuild

* Sat Jan 20 2008 Terje R??sten <terje.rosten@ntnu.no> - 0.7.1-0.3.20060818cvs
- Fix multiarch stuff
- Some style cleanup

* Tue Aug 28 2007 Terje R??sten <terje.rosten@ntnu.no> - 0.7.1-0.2.20060818cvs
- Rebuild

* Sat Sep  2 2006 Terje R??sten <terje.rosten@ntnu.no> - 0.7.1-0.1.20060818cvs
- 0.7.1 (from CVS)
- LICENCE now included in upstrean package

* Sun Feb 26 2006 Terje R??sten <terje.rosten@ntnu.no> - 0.7-3
- Add LICENSE

* Tue Feb 21 2006 Terje R??sten <terje.rosten@ntnu.no> - 0.7-2
- Fix buildroot var
- Clean buildroot before install
- Remove static libs
- Add imlib2 to buildrequires

* Sun Feb 19 2006 Terje R??sten <terje.rosten@ntnu.no> - 0.7-1
- Initial packaging based on upstream spec file.

