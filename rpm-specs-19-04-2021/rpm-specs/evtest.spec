Name:           evtest
Version:        1.34
Release:        5%{?dist}
Summary:        Event device test program

License:        GPLv2+
URL:            http://cgit.freedesktop.org/evtest/
Source0:        http://cgit.freedesktop.org/evtest/snapshot/%{name}-%{version}.tar.bz2

BuildRequires:  automake gcc make
BuildRequires:  asciidoc xmlto libxml2-devel

%description
%{name} is a simple utility to query information about input devices
and watch the event stream generated by input devices.

%prep
%setup -q

%build
autoreconf -v --install --force || exit 1
%configure
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

%files
%{_bindir}/%{name}
%doc COPYING
%{_mandir}/man1/evtest.1*

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.34-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec 01 2020 Peter Hutterer <peter.hutterer@redhat.com> 1.34-4
- Add make to BuildRequires

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.34-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.34-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 05 2019 Peter Hutterer <peter.hutterer@redhat.com> 1.34-1
- evtest 1.34

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.33-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.33-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.33-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Feb 19 2018 Peter Hutterer <peter.hutterer@redhat.com> 1.33-7
- Add BR for gcc

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.33-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.33-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.33-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.33-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.33-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 28 2016 Peter Hutterer <peter.hutterer@redhat.com>
- remove unnecessary defattr

* Thu Jul 23 2015 Peter Hutterer <peter.hutterer@redhat.com> 1.33-1
- evtest 1.33

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.32-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.32-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Aug 08 2014 Peter Hutterer <peter.hutterer@redhat.com> 1.32-1
- evtest 1.32

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.31-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Aug 22 2013 Peter Hutterer <peter.hutterer@redhat.com> 1.31-1
- evtest 1.31
- upstream dropped evtest-capture, use evemu instead

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.30-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Mar 26 2013 Peter Hutterer <peter.hutterer@redhat.com> 1.30-4
- force autoreconf

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.30-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.30-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Apr 27 2012 Peter Hutterer <peter.hutterer@redhat.com> 1.30-1
- evtest 1.30

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.29-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Sep 05 2011 Peter Hutterer <peter.hutterer@redhat.com> 1.29-1
- evtest 1.29

* Wed Jun 01 2011 Peter Hutterer <peter.hutterer@redhat.com> 1.28-1
- evtest 1.28

* Tue Mar 22 2011 Peter Hutterer <peter.hutterer@redhat.com> 1.27-1
- evtest 1.27

* Sat Feb 19 2011 Peter Hutterer <peter.hutterer@redhat.com> 1.26-3
- Change URL and Source, evtest is on fdo proper now.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.26-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Apr 22 2010 Peter Hutterer <peter.hutterer@redhat.com> 1.26-1
- evtest 1.26

* Thu Dec 03 2009 Peter Hutterer <peter.hutterer@redhat.com> 1.25-1
- evtest 1.25 (includes evtest-capture)

* Wed Nov 11 2009 Peter Hutterer <peter.hutterer@redhat.com> 1.24-1
- evtest 1.24

* Wed Oct 21 2009 Peter Hutterer <peter.hutterer@redhat.com> 1.23-1
- Initial package
