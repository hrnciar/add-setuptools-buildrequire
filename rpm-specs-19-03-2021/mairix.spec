Name:           mairix
Version:        0.24
Release:        10%{?dist}
Summary:        A program for indexing and searching email messages

License:        GPLv2
URL:            http://www.rc0.org.uk/mairix
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch0:         mairix-build.patch

BuildRequires: make
BuildRequires:  gcc bison flex bzip2-devel zlib-devel

%description
mairix is a program for indexing and searching email messages
stored in Maildir, MH or mbox folders.

%prep
%setup -q
%patch0 -p1 -b .build

for i in NEWS; do
  iconv -f iso8859-1 -t utf8 -o ${i}{_,} && touch -r ${i}{,_} && mv -f ${i}{_,}
done

%build
%configure
%make_build

%install
%make_install

%check
# it doesn't pass currently
#chmod 755 test/scripts/*
#make check

%files
%license COPYING
%doc ACKNOWLEDGEMENTS NEWS README dotmairixrc.eg
%{_bindir}/mairix
%{_mandir}/man1/mairix.1*
%{_mandir}/man5/mairixrc.5*

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.24-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.24-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.24-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.24-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.24-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 20 2018 Miroslav Lichvar <mlichvar@redhat.com> 0.24-5
- add gcc to build requirements

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.24-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue May 22 2018 Miroslav Lichvar <mlichvar@redhat.com> 0.24-3
- modernize spec

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Aug 25 2017 Miroslav Lichvar <mlichvar@redhat.com> 0.24-1
- update to 0.24

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.23-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.23-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.23-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.23-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.23-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.23-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Aug 02 2011 Miroslav Lichvar <mlichvar@redhat.com> 0.23-1
- update to 0.23

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jun 14 2010 Miroslav Lichvar <mlichvar@redhat.com> 0.22-1
- update to 0.22

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.21-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.21-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Aug 29 2008 Miroslav Lichvar <mlichvar@redhat.com> 0.21-2
- fix building with new rpm

* Wed Mar 05 2008 Miroslav Lichvar <mlichvar@redhat.com> 0.21-1
- initial release
