Summary:	Parser Generator with Java Extension
Name:		byaccj
Version:	1.15
Release:	25%{?dist}
License:	Public Domain
URL:		http://byaccj.sourceforge.net/

Source0:	http://sourceforge.net/projects/byaccj/files/byaccj/1.15/byaccj1.15_src.tar.gz

BuildRequires:  gcc
BuildRequires:  make

%description
BYACC/J is an extension of the Berkeley v 1.8 YACC-compatible 
parser generator. Standard YACC takes a YACC source file, and 
generates one or more C files from it, which if compiled properly, 
will produce a LALR-grammar parser. This is useful for expression 
parsing, interactive command parsing, and file reading. Many 
megabytes of YACC code have been written over the years.
This is the standard YACC tool that is in use every day to produce 
C/C++ parsers. I have added a "-J" flag which will cause BYACC to 
generate Java source code, instead. So there finally is a YACC for 
Java now! 

%prep
%setup -q -n %{name}%{version}
chmod -c -x src/* docs/*
sed -i -e 's|-arch i386 -isysroot /Developer/SDKs/MacOSX10.4u.sdk -mmacosx-version-min=10.4|$(LDFLAGS)|g' src/Makefile


%build
pushd src
%make_build yacc CFLAGS="%{optflags}" LDFLAGS="$RPM_LD_FLAGS"
popd

%install
install -d -m 755 %{buildroot}%{_bindir}
install -p -m 755 src/yacc %{buildroot}%{_bindir}/%{name}

%files
%doc docs/* src/README
%{_bindir}/%{name}

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.15-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Nov 25 2020 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.15-24
- Use make_build RPM macro to comply with packaging guidelines

* Wed Nov 25 2020 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.15-23
- Respect system-wide linker flags during build

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0:1.15-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0:1.15-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0:1.15-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0:1.15-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0:1.15-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0:1.15-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Sep 22 2017 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.15-16
- Cleanup spec file

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0:1.15-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0:1.15-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0:1.15-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0:1.15-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 23 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.15-11
- Don't install bogus manpage

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.15-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.15-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.15-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Jul 26 2013 Ville Skyttä <ville.skytta@iki.fi> - 0:1.15-7
- Simplify installation of docs.
- Drop executable bits from sources and docs.

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.15-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.15-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 26 2012 Alexander Kurtakov <akurtako@redhat.com> - 0:1.15-4
- Fix build.

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Sep 06 2011 Luis Bazan <bazanluis20@gmail.com> 0:1.15-2
- New Release

* Thu Aug 25 2011 Luis Bazan <bazanluis20@gmail.com> 0:1.15-1
- Update to 1.15

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.14-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.14-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun May 10 2009 Ville Skyttä <ville.skytta@iki.fi> - 0:1.14-4
- Build with %%{optflags} (#500022).

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Jul  9 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0:1.14-2
- drop repotag

* Sat Feb 9 2008 Devrim GUNDUZ <devrim@commandprompt.com> - 0:1.14-1jpp.1
- Update to 1.14
- Cosmetic cleanup in spec

* Tue Mar 06 2007 Vivek Lakshmanan <vivekl@redhat.com> - 0:1.11-2jpp.2.fc7
- First build in fedora after passing review

* Thu Feb 15 2007 Tania Bento <tbento@redhat.com> - 0:1.11-2jpp.1
- Fixed the %%Release tag.
- Changed the %%License tag.
- Fixed the %%BuildRoot tag.
- Removed the %%Vendor tag.
- Removed the %%Distribution tag.
- Removed the %%BuildRequires: gcc and make tags as these d not need to be
listed.
- Removed "%%define section free".
- Added "sed -i 's/\r//g docs/tf.y' to fix a warning generated by
rpmlint.
- Fixed the %%Source0 tag.
- Changed the %%Group tag.
- Installed man pages in proper directory. 

* Wed Jan 04 2006 Fernando Nasser <fnasser@redhat.com> - 0:1.11-2jpp
- First JPP 1.7 build

* Wed Nov 16 2005 Ralph Apel <r.apel at r-apel.de> - 0:1.11-1jpp
- First JPackage release

