Summary: Utilities for use with dual head setups using independent screens
Name: dualscreen-mouse-utils
Version: 0.5
Release: 23%{?dist}
License: GPLv2
URL: http://digamma.cs.unm.edu/trac.dmohr/wiki/DualscreenMouseUtils
Source0: http://dsp.mcbf.net/releases/dualscreen-mouse-utils-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires: libX11-devel
BuildRequires: make

%description
Utilities for use with old-school dual head setups: namely not
twinview / one big desktop, but rather two X screens.

mouse-switchscreen:
  Change the mouse cursor from one screen to the other. Remembers the previous
  mouse position for each screen.

mouse-wrapscreen:
  If you have an xorg.conf where both X screens are "separated" on the X
  coordinates, then the mouse cursor cannot cross. Which is sometimes desired,
  and sometimes not. Using mouse-wrapscreen you can configure them to be
  "uncrossable", and then run it in the background when you do want to be able
  to cross the cursor.

%prep
%setup -q

%build
make CFLAGS="%{optflags}" %{?_smp_mflags}

%install
install -d %{buildroot}%{_bindir}
install -m 755 mouse-wrapscreen mouse-switchscreen %{buildroot}%{_bindir}/

%files 
%doc gpl.txt README
%{_bindir}/*

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Sep 30 2009 Christian Krause <chkr@fedoraproject.org> - 0.5-4
- Correct email address

* Mon Sep 28 2009 Christian Krause <chkr@fedoraproject.org> - 0.5-3
- Fix spelling mistake

* Sun Sep 27 2009 Christian Krause <chkr@fedoraproject.org> - 0.5-2
- Deleting %%buildroot is not necessary in %%install anymore (F10 and greater)
- Remove definition of %%buildroot (not needed for F10 and greater)
- Use rpm macro for optflags now

* Wed Sep 16 2009 Christian Krause <chkr@fedoraproject.org> - 0.5-1
- Initial package

