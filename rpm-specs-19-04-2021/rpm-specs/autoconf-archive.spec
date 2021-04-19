Name:           autoconf-archive
Version:        2021.02.19
Release:        1%{?dist}
Summary:        The Autoconf Macro Archive
License:        GPLv3+ with exceptions
URL:            https://www.gnu.org/software/autoconf-archive/
Source0:        https://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.xz
Source1:        https://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.xz.sig
# gpg --keyserver pool.sks-keyservers.net --recv-keys 1A4F63A13A4649B632F65EE141BC28FE99089D72
# gpg --export --export-options export-minimal 1A4F63A13A4649B632F65EE141BC28FE99089D72 > gpgkey-1A4F63A13A4649B632F65EE141BC28FE99089D72.gpg
Source2:        gpgkey-1A4F63A13A4649B632F65EE141BC28FE99089D72.gpg
BuildArch:      noarch
BuildRequires:  gnupg2
BuildRequires:  make
Requires:       autoconf

%description
The GNU Autoconf Archive is a collection of more than 450 macros for
GNU Autoconf that have been contributed as free software by friendly
supporters of the cause from all over the Internet.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build
%configure
%make_build

%install
%make_install
# remove dir file which will be generated by /sbin/install-info
rm -frv %{buildroot}%{_infodir}/dir
# document files are installed another location
rm -frv %{buildroot}%{_datadir}/doc/%{name}

%files
%doc AUTHORS NEWS README TODO
%license COPYING*
%{_datadir}/aclocal/*.m4
%{_infodir}/autoconf-archive.info*

%changelog
* Fri Feb 19 2021 David King <amigadave@amigadave.com> - 2021.02.19-1
- Update to 2021.02.19 (#1930679)
- Verify GPG signature of sources

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2019.01.06-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2019.01.06-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2019.01.06-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2019.01.06-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Mar  7 2019 Tim Landscheidt <tim@tim-landscheidt.de> - 2019.01.06-3
- Remove obsolete requirements for post/preun scriptlets

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2019.01.06-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 11 2019 David King <amigadave@amigadave.com> - 2019.01.06-1
- Update to 2019.01.06

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2018.03.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 14 2018 David King <amigadave@amigadave.com> - 2018.03.13-1
- Update to 2018.03.13 (#1555090)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2017.09.28-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Sep 30 2017 David King <amigadave@amigadave.com> - 2017.09.28-1
- Update to 2017.09.28 (#1496786)

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2017.03.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Mar 22 2017 David King <amigadave@amigadave.com> - 2016.09.16-3
- Update to 2017.03.21 (#1434626)

* Tue Mar 14 2017 Igor Gnatenko <ignatenko@redhat.com> - 2016.09.16-3
- Backport patch to fix broken AX_PYTHON_DEVEL (py3.6+)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2016.09.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Sep 16 2016 David King <amigadave@amigadave.com> - 2016.09.16-1
- Update to 2016.09.16 (#1376791)

* Mon Mar 21 2016 David King <amigadave@amigadave.com> - 2016.03.20-1
- Update to 2016.03.20 (#1319533)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2015.09.25-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Sep 25 2015 David King <amigadave@amigadave.com> - 2015.09.25-1
- Update to 2015.09.25 (#1266490)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2015.02.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Feb 24 2015 David King <amigadave@amigadave.com> - 2015.02.24-1
- Update to 2015.02.24
- Use license macro for COPYING*

* Mon Feb 09 2015 Christopher Meng <rpm@cicku.me> - 2015.02.04-1
- Update to 2015.02.04

* Thu Sep 18 2014 Christopher Meng <rpm@cicku.me> - 2014.02.28-1
- Update to 2014.02.28

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2012.09.08-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2012.09.08-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2012.09.08-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Sep 10 2012 Takanori MATSUURA <t.matsuu@gmail.com> - 2012.09.08-1
- update to 2012.09.08

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2012.04.07-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Apr  8 2012 Takanori MATSUURA <t.matsuu@gmail.com> - 2012.04.07-1
- update to 2012.04.07

* Thu Jan  5 2012 Takanori MATSUURA <t.matsuu@gmail.com> - 2011.12.21-1
- update to 2011.12.21

* Sat Nov 19 2011 Takanori MATSUURA <t.matsuu@gmail.com> - 2011.09.17-1
- update to 2011.09.17

* Fri Aug  5 2011 Takanori MATSUURA <t.matsuu@gmail.com> - 2011.07.17-1
- update to 2011.07.17

* Thu May 26 2011 Takanori MATSUURA <t.matsuu@gmail.com> - 2011.04.12-1
- initial release

* Fri May  6 2011 Takanori MATSUURA <t.matsuu@gmail.com> - 2011.04.12-0
- update to 2011.04.12

* Fri Mar 25 2011 Takanori MATSUURA <t.matsuu@gmail.com> - 2011.03.17-0
- update to 2011.03.17

* Tue Jan 11 2011 Takanori MATSUURA <t.matsuu@gmail.com> - 2011.01.02-0
- update to 2011.01.02

* Fri Dec 17 2010 Takanori MATSUURA <t.matsuu@gmail.com> - 2010.10.26-0
- initial build
