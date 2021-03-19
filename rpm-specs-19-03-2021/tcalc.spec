Name:		tcalc
Version:	2.1
Release:	13%{?dist}
Summary:	The terminal calculator

License:	GPLv3+
URL:		http://sites.google.com/site/mohammedisam2000/home/projects
Source0:	http://sites.google.com/site/mohammedisam2000/home/projects/%{name}-%{version}.tar.gz

BuildRequires: make
BuildRequires: gcc

%description
The terminal calculator is a small and helpful program to help users of the
GNU/Linux terminal do calculations simply and quickly. The formula to be
calculated can be fed to tcalc through the command line. Alternatively, tcalc
can be run with no formula and then the free mode is started, in which the 
calculator will wait for user input, do the necessary calculations and print 
out the result, and the cycle will repeat until the user enters 'q' or 'quit'.
Support for reading formulas from text files is under way.

The calculator works with the decimal, hexadecimal, octal, and binary number
systems. It automatically identifies hex numbers if entered with a preceding 
"0x" or "0X", octal by preceding the number with a zero, binaries by 
preceding the number with 'b' and decimals by absence of all of the above. 
Alternatively, the user can indicate the type of input by setting the 'format' 
argument.


%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

install -m 0644 -p -D info/tcalc.info* %{buildroot}%{_infodir}/tcalc.info

%files
%{_bindir}/*
%{_mandir}/man1/*
%{_infodir}/*
%{_docdir}/tcalc

#%%doc AUTHORS README COPYING ChangeLog test test2

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Mar 08 2020 Mohammed Isam <mohammed_isam1984@yahoo.com> 2.1-11
- Bugfixes

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 20 2018 Mohammed Isam <mohammed_isam1984@yahoo.com> 2.1-7
- Added BuildRequires: gcc

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Sep 10 2016 Mohammed Isam <mohammed_isam1984@yahoo.com> 2.1-1
- Fixed a bug in number conversion function
- Deciml outputs both signed and unsigned

* Sun Nov 29 2015 Mohammed Isam <mohammed_isam1984@yahoo.com> 2.0-1
- Added Factorial function
- Expanded Table option (Added: from, to, step)
- Improved Custom file reading
- Added Bitwise op support (partial)
- Corrected precendence in calculations

* Mon Oct 12 2015 Mohammed Isam <mohammed_isam1984@yahoo.com> 1.5-1
- Fixed cusom_func.c
- Added calc.c
- Added memory checking and fixed the division function

* Sun Nov 30 2014 Mohammed Isam <mohammed_isam1984@yahoo.com> 1.4-1
- Added '-table' option to print multiplication tables
- Added handling for input redirection from command line

* Wed Nov 12 2014 Mohammed Isam <mohammed_isam1984@yahoo.com> 1.3-1
- Fixed file reading function

* Tue Nov 11 2014 Mohammed Isam <mohammed_isam1984@yahoo.com> 1.2-1
- Corrected ltmain version & duplicate file in spec
- Added support for custom function definitions
- Partial support for reading files

* Fri Nov 07 2014 Mohammed Isam <mohammed_isam1984@yahoo.com> 1.1-1
- Corrected spelling errors in spec file
- Added support for math library functions

* Fri Nov 07 2014 Mohammed Isam <mohammed_isam1984@yahoo.com> 1.0-1
- First release
