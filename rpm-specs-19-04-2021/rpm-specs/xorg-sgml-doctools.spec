Summary:    X.Org SGML documentation generation tools
Name:       xorg-sgml-doctools
Version:    1.11
Release:    13%{?dist}
License:    MIT
URL:        http://www.x.org

BuildArch:  noarch

Source0:    http://www.x.org/pub/individual/doc/%{name}-%{version}.tar.bz2

BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(xorg-macros) >= 1.8

Requires:   pkgconfig
Requires:   xml-common

%description
This package is required in order to generate the X.Org X11 documentation from
source.

%prep
%setup -q

%build
%configure

%install
%make_install

%files
%doc COPYING ChangeLog
%{_datadir}/sgml
%{_datadir}/pkgconfig/%{name}.pc

%changelog
* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Nov  5 12:31:55 AEST 2020 Peter Hutterer <peter.hutterer@redhat.com> - 1.11-12
- Add BuildRequires for make

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Nov 04 2014 Simone Caronni <negativo17@gmail.com> - 1.11-1
- Update to 1.11.
- Clean up SPEC file, fix rpmlint warnings.

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Sep 14 2011 Mat??j Cepl <mcepl@redhat.com> - 1.10-1
- New upstream release.

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Sep 02 2010 Jason L Tibbitts III <tibbs@math.uh.edu> - 1.5-1
- Address review commentary https://bugzilla.redhat.com/show_bug.cgi?id=226569
- Update to 1.5, solving license issue.  This adds a few new files and requires
  a pkgconfig dependency.
- Add dependency on xml-common to fix unowned directory issue. 
- Remove some bits (buildroot tag and cleaning) no longer required in Fedora.
