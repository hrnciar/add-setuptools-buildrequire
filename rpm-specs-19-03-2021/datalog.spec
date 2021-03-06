%{!?luaver: %global luaver %(lua -e "print(string.sub(_VERSION, 5))")}
%global	luapkgdir %{_datadir}/lua/%{luaver}

Name:		datalog
Version:	2.6
Release:	16%{?dist}

Source0:	http://downloads.sourceforge.net/datalog/%{name}-%{version}.tar.gz

URL:		http://sourceforge.net/projects/datalog

Summary:	A Lightweight Deductive Database using Datalog
License:	LGPLv2+
%if 0%{?rhel}
%endif

BuildRequires:	gcc, texinfo, lua-devel > 5.1, readline-devel
BuildRequires: make

%description
This package contains a lightweight deductive database system.
Queries and database updates are expressed using Datalog--a
declarative logic language in which each formula is a function-free
Horn clause, and every variable in the head of a clause must appear in
the body of the clause.  The use of Datalog syntax and an
implementation based on tabling intermediate results, ensures that all
queries terminate.

The components in this package are designed to be small, and usable on
memory constrained devices.  The package includes an interactive
interpreter for Datalog, and the development package has a library
that can be used to embed the interpreter into C programs.

%package devel
Summary: Datalog header file and library
%if 0%{?rhel}
%endif
Requires: datalog = %{version}

%description devel
This package includes the header file and library that can be used to
embed a datalog interpreter into C programs.

%prep
%setup -q

%build
%configure --with-lua --enable-shared --disable-static
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install
mkdir -p %{buildroot}%{luapkgdir}
install -m 644 %{name}.lua %{buildroot}%{luapkgdir}
rm -rf %{buildroot}/%{_libdir}/lib%{name}.la
rm -rf %{buildroot}/%{_datadir}/%{name}
rm -rf %{buildroot}/%{_infodir}/dir

%ldconfig_scriptlets

%files
%doc %{name}.html ChangeLog README COPYING.LIB AUTHORS NEWS
%{_bindir}/%{name}
%{_libdir}/lib%{name}.so.*
%{_infodir}/%{name}.info.*
%{_mandir}/man1/*
%{luapkgdir}/%{name}.lua

%files devel
%{_includedir}/%{name}.h
%{_libdir}/lib%{name}.so

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 24 2019 Bj??rn Esser <besser82@fedoraproject.org> - 2.6-12
- Remove hardcoded gzip suffix from GNU info pages

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.6-11
- Rebuild for readline 8.0

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 21 2018 John D. Ramsdell <ramsdell@mitre.org> - 2.6-8
- Added gcc to BuildRequires in spec file

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Igor Gnatenko <ignatenko@redhat.com> - 2.6-3
- Rebuild for readline 7.x

* Fri Jun 17 2016 John D. Ramsdell <ramsdell@mitre.org> - 2.6-2
- Enabled readline support

* Thu Jun 02 2016 John D. Ramsdell <ramsdell@mitre.org> - 2.6-1
- Made header compilable and documented dl_mark and dl_reset

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Apr 28 2015 John D. Ramsdell <ramsdell@mitre.org> - 2.5-1
- Updated Lua sources to version 5.3.0

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue May 14 2013 Tom Callaway <spot@fedoraproject.org> - 2.4-2
- rebuild for lua 5.2

* Wed Mar 27 2013 John D. Ramsdell <ramsdell@mitre.org> - 2.4-1
- Add support for ARM 64 bit CPU architecture (aarch64)

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Oct 22 2012 John D. Ramsdell <ramsdell@mitre.org> - 2.3-2
- Remove lua(api) requirement

* Thu Jun  7 2012 John D. Ramsdell <ramsdell@mitre.org> - 2.2-4
- Added lua(abi) requirement

* Tue Jun  5 2012 John D. Ramsdell <ramsdell@mitre.org> - 2.2-3
- Removed rm of build root in %%install
- Group field defined only for RHEL
- Removed license field in subpackage devel

* Fri May 25 2012 John D. Ramsdell <ramsdell@mitre.org> - 2.2-2
- Changed %%define to %%global

* Thu Apr 26 2012 John D. Ramsdell <ramsdell@mitre.org> - 2.2-1
- Changed devel requires from libdatalog to datalog

* Sun Apr  8 2012 John D. Ramsdell <ramsdell@mitre.org> - 2.1-1
- Added AUTHORS and NEWS to %%doc

* Thu Jan 26 2012 John D. Ramsdell <ramsdell@mitre.org> - 1.8-2
- Use lua to determine its version number

* Wed Jan 18 2012 John D. Ramsdell <ramsdell@mitre.org> - 1.8-1
- Added a manual page

* Fri Jan 13 2012 John D. Ramsdell <ramsdell@mitre.org> - 1.7-3
- Fix devel license and summary
- chmod 644 on installed datalog.lua

* Wed Oct 12 2011 John D. Ramsdell <ramsdell@mitre.org> - 1.7-2
- Added devel package
- Moved luapkgdir def to top of file
- sf.net --> sourceforge.net
- Removed Packager field
- Removed newline between %%description and text

* Thu Sep 29 2011 John D. Ramsdell <ramsdell@mitre.org> - 1.7-1
- Use installed Lua package and shared libraries

* Tue Sep 20 2011 John D. Ramsdell <ramsdell@mitre.org> - 1.6-2
- Removed devel package

* Sat Aug 6 2011 John D. Ramsdell <ramsdell@mitre.org> - 1.6-1
- Fixed license name by adding version number
- Dropped vendor field
- Switched to standard name for build root
- %%defaddrs now contain four fields
- Removed asterisks in %%files
- Added COPYING.LIB

* Thu Jul 7 2011 John D. Ramsdell <ramsdell@mitre.org> - 1.4-1
- Initial spec release
