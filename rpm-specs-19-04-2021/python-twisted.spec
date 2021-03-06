%global pypi_name twisted

%global common_description %{expand:
Twisted is a networking engine written in Python, supporting numerous protocols.
It contains a web server, numerous chat clients, chat servers, mail servers
and more.}

Name:           python-%{pypi_name}
Version:        21.2.0
Release:        2%{?dist}
Summary:        Twisted is a networking engine written in Python

License:        MIT
URL:            http://twistedmatrix.com/
Source0:        %{pypi_source Twisted}
# Import gobject from gi.repository for Python 3
# https://twistedmatrix.com/trac/ticket/9642
Patch1:         0001-Import-gobject-from-gi.repository-in-Python-3.patch

BuildArch:      noarch

%description
%{common_description}

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  gcc
BuildRequires:  python3-devel >= 3.3
BuildRequires:  python3-Cython
BuildRequires:  python3dist(appdirs) >= 1.4
BuildRequires:  python3dist(automat) >= 0.8
BuildRequires:  python3dist(attrs) >= 19.2.0
BuildRequires:  python3dist(bcrypt) >= 3.0.0
BuildRequires:  python3dist(constantly) >= 15.1
BuildRequires:  python3dist(cryptography) >= 2.6
BuildRequires:  (python3dist(h2) >= 3 with python3dist(h2) < 5)
BuildRequires:  python3dist(hyperlink) >= 17.1.1
BuildRequires:  python3dist(idna) >= 2.4
BuildRequires:  python3dist(incremental) >= 16.10.1
BuildRequires:  (python3dist(priority) >= 1.1 with python3dist(priority) < 2)
BuildRequires:  python3dist(pyasn1)
BuildRequires:  python3dist(pyopenssl) >= 16
BuildRequires:  python3dist(pyserial) >= 3
BuildRequires:  python3dist(service-identity) >= 18.1
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(sphinx) >= 1.3.1
BuildRequires:  python3dist(sphinx-rtd-theme)
BuildRequires:  python3dist(zope.interface) >= 4.4.2
BuildRequires:  python3dist(pyhamcrest) >= 1.9

%{?python_extras_subpkg:Recommends:  python3-%{pypi_name}+tls}
%{!?python_extras_subpkg:Recommends: python3dist(service-identity) >= 18.1}

%description -n python3-%{pypi_name}
%{common_description}

%{?python_extras_subpkg:%python_extras_subpkg -n python3-%{pypi_name} -i %{python3_sitelib}/Twisted-%{version}-py%{python3_version}.egg-info tls}

%prep
%autosetup -p1 -n Twisted-%{version}

%build
%py3_build

%install
# no-manual-page-for-binary
mkdir -p %{buildroot}%{_mandir}/man1/
for s in conch core mail; do
cp -a docs/$s/man/*.1 %{buildroot}%{_mandir}/man1/
done

%py3_install

# Packages that install arch-independent twisted plugins install here.
# https://bugzilla.redhat.com/show_bug.cgi?id=1252140
mkdir -p %{buildroot}%{python3_sitelib}/twisted/plugins

# Move and symlink python3 scripts
# no-manual-page-for-binary: man page is trial and twistd
mv %{buildroot}%{_bindir}/trial %{buildroot}%{_bindir}/trial-%{python3_version}
ln -s ./trial-%{python3_version} %{buildroot}%{_bindir}/trial-3
ln -s ./trial-%{python3_version} %{buildroot}%{_bindir}/trial

mv %{buildroot}%{_bindir}/twistd %{buildroot}%{_bindir}/twistd-%{python3_version}
ln -s ./twistd-%{python3_version} %{buildroot}%{_bindir}/twistd-3
ln -s ./twistd-%{python3_version} %{buildroot}%{_bindir}/twistd

# ambiguous shebangs
pathfix.py -pn -i %{__python3} %{buildroot}%{python3_sitelib}


%check
# can't get this to work within the buildroot yet due to multicast
# https://twistedmatrix.com/trac/ticket/7494
PATH=%{buildroot}%{_bindir}:$PATH PYTHONPATH=%{buildroot}%{python3_sitearch} %{buildroot}%{_bindir}/trial twisted ||:


%files -n python3-twisted
%doc NEWS.rst README.rst
%license LICENSE
%{_bindir}/trial-3*
%{_bindir}/twistd-3*
%{python3_sitelib}/twisted/
%{python3_sitelib}/Twisted-%{version}-py%{python3_version}.egg-info
%{_bindir}/cftp
%{_bindir}/ckeygen
%{_bindir}/conch
%{_bindir}/mailmail
%{_bindir}/pyhtmlizer
%{_bindir}/tkconch
%{_bindir}/trial
%{_bindir}/twist
%{_bindir}/twistd
%{_mandir}/man1/cftp.1*
%{_mandir}/man1/ckeygen.1*
%{_mandir}/man1/conch.1*
%{_mandir}/man1/mailmail.1*
%{_mandir}/man1/pyhtmlizer.1*
%{_mandir}/man1/tkconch.1*
%{_mandir}/man1/trial.1*
%{_mandir}/man1/twistd.1*


%changelog
* Fri Mar 05 2021 Miro Hron??ok <mhroncok@redhat.com> - 21.2.0-2
- Reintroduce twisted[tls] subpackage
- Fixes: rhbz#1935872
- Fixes: rhbz#1935873
- Fixes: rhbz#1935869
- Fixes: rhbz#1935870
- Fixes: rhbz#1935871

* Fri Mar  5 09:54:54 CET 2021 Robert-Andr?? Mauchin <zebob.m@gmail.com> - 21.2.0-1
- Update to 21.2.0

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Dec 20 2020 Robert-Andr?? Mauchin <zebob.m@gmail.com> - 20.3.0-4
- Bump h2 dependency
- Fix: rhbz#1909413

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Miro Hron??ok <mhroncok@redhat.com> - 20.3.0-2
- Add twisted[tls] subpackage

* Thu Jun 18 05:29:03 CEST 2020 Robert-Andr?? Mauchin <zebob.m@gmail.com> - 20.3.0-1
- Update to 20.3.0

* Sun May 24 2020 Miro Hron??ok <mhroncok@redhat.com> - 19.10.0-3
- Rebuilt for Python 3.9

* Tue Mar 17 16:31:05 CET 2020 Robert-Andr?? Mauchin <zebob.m@gmail.com> - 19.10.0-2
- Security fix for CVE-2020-10108 (#1813439, #1813441)
- Security fix for CVE-2020-10109 (#1813447, #1813449)

* Tue Mar 17 15:15:48 CET 2020 Robert-Andr?? Mauchin <zebob.m@gmail.com> - 19.10.0-1
- Update to 19.10.0
- Revert removal of %%{python3_sitelib}/twisted/plugins/

* Sun Oct 13 23:35:33 CEST 2019 Robert-Andr?? Mauchin <zebob.m@gmail.com> - 19.7.0-2
- Drop Python 2 support (#1761204)

* Mon Sep 16 2019 Jeremy Cline <jcline@redhat.com> - 19.7.0-1
- Update to 19.7.0

* Tue Sep 03 2019 Miro Hron??ok <mhroncok@redhat.com> - 19.2.1-6
- Stop running Python 2 tests at build time, reduce the build dependencies

* Sat Aug 17 2019 Miro Hron??ok <mhroncok@redhat.com> - 19.2.1-5
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 19.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 09 2019 Miro Hron??ok <mhroncok@redhat.com> - 19.2.1-3
- Security fix for CVE-2019-12855 (Check certificates for XMPP TLS) (#1728206) (#1728207)

* Wed Jul 03 2019 Miro Hron??ok <mhroncok@redhat.com> - 19.2.1-2
- Rebuilt to update automatic Python dependencies

* Sun Jun 09 18:40:31 CEST 2019 Robert-Andr?? Mauchin <zebob.m@gmail.com> - 19.2.1-1
- Release 19.2.1

* Wed May 22 18:26:29 CEST 2019 Robert-Andr?? Mauchin <zebob.m@gmail.com> - 19.2.0-3
- Add patch to import gobject from gi.repository for Python 3
- Fix #1712748

* Tue May 14 16:00:42 CEST 2019 Robert-Andr?? Mauchin <zebob.m@gmail.com> - 19.2.0-2
- Add patch regenerating raiser.c to use with Python 3.8a4
- Fix #11709817

* Wed Apr 10 17:38:50 CET 2019 Robert-Andr?? Mauchin <zebob.m@gmail.com> - 19.2.0-1
- Release 19.2.0 (#1698490)

* Thu Mar 07 2019 Robert-Andr?? Mauchin <zebob.m@gmail.com> - 18.9.0-1
- Release 18.9.0
- Run tests

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 18.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Oct 22 2018 Miro Hron??ok <mhroncok@redhat.com> - 18.7.0-3
- Recommend pythonX-service-identity

* Sat Jul 21 2018 Robert-Andr?? Mauchin <zebob.m@gmail.com> - 18.7.0-2
- Remove erroneous symlink to binaries

* Sun Jul 15 2018 Robert-Andr?? Mauchin <zebob.m@gmail.com> - 18.7.0-1
- Update to 18.7.0

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 18.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Robert-Andr?? Mauchin <zebob.m@gmail.com> - 18.4.0-1
- Update to 18.4.0
- Default binaries to Python 3
- Drop old Obsoletes/Provides
- Refresh BR
- Remove useless macros
- Use python_enable_dependency_generator

* Mon Jun 18 2018 Miro Hron??ok <mhroncok@redhat.com> - 16.4.1-11
- Rebuilt for Python 3.7

* Wed May 23 2018 Miro Hron??ok <mhroncok@redhat.com> - 16.4.1-10
- Fix ambiguous shebangs

* Fri Apr 27 2018 Petr Viktorin <pviktori@redhat.com> - 16.4.1-9
- No longer require python-crypto

* Mon Mar 26 2018 Iryna Shcherbina <ishcherb@redhat.com> - 16.4.1-8
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 16.4.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Sep 29 2017 Troy Dawson <tdawson@redhat.com> - 16.4.1-6
- Cleanup spec file conditionals

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 16.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 16.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 16.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Dec 13 2016 Stratakis Charalampos <cstratak@redhat.com> - 16.4.1-2
- rebuilt

* Wed Oct 26 2016 Jonathan Steffan <jsteffan@fedoraproject.org> - 16.4.1-1
- Update to 16.4.1

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 16.3.0-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri Jul 8 2016 Jonathan Steffan <jsteffan@fedoraproject.org> - 16.3.0-1
- Update to 16.3.0
- mahole, tap2deb, tap2rpm are removed upstream

* Sun Jun 26 2016 Jonathan Steffan <jsteffan@fedoraproject.org> - 16.2.0-2
- Add rpmlint notes
- Fix unneeded py3 conditional for py2 script chmod

* Sun Jun 26 2016 Jonathan Steffan <jsteffan@fedoraproject.org> - 16.2.0-1
- Update to 16.2.0
- Update upstream source location

* Thu Jun  2 2016 Ha??kel Gu??mar <hguemar@fedoraproject.org> - 16.1.1-3
- Drop tkinter dependency (only required for tkconch)
- Use python3 conditionals
- Move BR under the proper subpackage

* Tue May 10 2016 Petr Viktorin <pviktori@redhat.com> - 16.1.1-2
- Update to better conform to Python packaging guidelines

* Thu May 05 2016 Julien Enselme <jujens@jujens.eu> - 16.1.1-1
- Update to 16.1.1 (#1287381)

* Thu Mar 10 2016 Julien Enselme <jujens@jujens.eu> - 15.5.0-2
- Add python3 support

* Thu Mar 10 2016 Julien Enselme <jujens@jujens.eu> - 15.5.0-1
- Update to 15.5.0 (#1287381)
- Use new python macros
- Remove deprecated %%clean section

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 15.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Nov 27 2015 Tom Prince <tom.prince@twistedmatrix.com> - 15.4.0-2
- Add arch-independent plugin directory to package. (RHBZ#1252140)

* Thu Oct 29 2015 Tom Prince <tom.prince@twistedmatrix.com> - 15.4.0-1
- Update to 15.4.0
- Include test certificates.

* Mon Jul 20 2015 Jonathan Steffan <jsteffan@fedoraproject.org> - 15.2.1-1
- Update to 15.2.1

* Sat May 09 2015 Jonathan Steffan <jsteffan@fedoraproject.org> - 15.1.0-1
- Update to 15.1.0 (RHBZ#1187921,RHBZ#1192707)
- Require python-service-identity (RHBZ#1119067)
- Obsolete python-twisted-core-doc (RHBZ#1187025)

* Sat Nov 22 2014 Jonathan Steffan <jsteffan@fedoraproject.org> - 14.0.2-1
- Update to 14.0.2 (RHBZ#1143002)

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 14.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Jonathan Steffan <jsteffan@fedoraproject.org> - 14.0.0-1
- Update to 14.0.0
- Ship Twisted as a fully featured package without subpackages on the advice
  of upstream and to mirror what pypi provides
- Explictly build for python2 with new macros

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 12.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 12.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 12.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Sep 03 2012 Julian Sikorski <belegdol@fedoraproject.org> - 12.2.0-1
- Updated to 12.2.0

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 12.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jun 17 2012 Julian Sikorski <belegdol@fedoraproject.org> - 12.1.0-1
- Updated to 12.1.0

* Sun Feb 12 2012 Julian Sikorski <belegdol@fedoraproject.org> - 12.0.0-1
- Updated to 12.0.0

* Sat Jan 07 2012 Julian Sikorski <belegdol@fedoraproject.org> - 11.1.0-2
- Rebuilt for gcc-4.7

* Fri Nov 18 2011 Julian Sikorski <belegdol@fedoraproject.org> - 11.1.0-1
- Updated to 11.1.0
- Dropped obsolete Group, Buildroot, %%clean and %%defattr

* Sat Apr 30 2011 Julian Sikorski <belegdol@fedoraproject.org> - 11.0.0-1
- Updated to 11.0.0
- Added comment on how to obtain the PKG-INFO file

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 10.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jan 15 2011 Julian Sikorski <belegdol@fedoraproject.org> - 10.2.0-1
- Updated to 10.2.0

* Mon Nov 08 2010 Julian Sikorski <belegdol@fedoraproject.org> - 10.1.0-3
- Use python_sitelib instead of python-sitearch
- The aforementioned macros are defined in Fedora 13 and above

* Sun Nov 07 2010 Julian Sikorski <belegdol@fedoraproject.org> - 10.1.0-2
- Added egg-info file

* Tue Sep 21 2010 Julian Sikorski <belegdol@fedoraproject.org> - 10.1.0-1
- Updated to 10.1.0
- Switched to macros for versioned dependencies

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Dec 29 2008 Matthias Saou <http://freshrpms.net/> 8.2.0-1
- Update to 8.2.0.
- Change back spec cosmetic details from Paul's to Thomas' preference.

* Wed Jul 16 2008 Matthias Saou <http://freshrpms.net/> 8.1.0-2
- Update to 8.1.0.
- Minor spec file cleanups.
- Merge back changes from Paul Howarth.

* Wed May 21 2008 Thomas Vander Stichele <thomas at apestaart dot org>
- 2.5.0-1
- update to 2.5.0 release (only the umbrella package was missing)

* Tue Jan 16 2007 Thomas Vander Stichele <thomas at apestaart dot org>
- 2.4.0-3
- list packages in README.fedora

* Wed Jan 03 2007 Thomas Vander Stichele <thomas at apestaart dot org>
- 2.4.0-2
- add a README.fedora
- made noarch, since it doesn't actually install any python twisted/ module
  code
- fixed provides/obsoletes

* Wed Jun 07 2006 Thomas Vander Stichele <thomas at apestaart dot org>
- 2.4.0-1
- this is now a pure umbrella package

* Mon Oct 10 2005 Jeff Pitman <symbiont+pyvault@berlios.de> 2.1.0-1
- upstream release

* Tue Aug 23 2005 Jeff Pitman <symbiont+pyvault@berlios.de> 2.0.1-1
- upstream release

* Mon Apr 04 2005 Jeff Pitman <symbiont+pyvault@berlios.de> 2.0.0-2
- add zsh support

* Fri Mar 25 2005 Jeff Pitman <symbiont+pyvault@berlios.de> 2.0.0-1
- final release

* Thu Mar 17 2005 Jeff Pitman <symbiont+pyvault@berlios.de> 2.0.0-0.2.a3
- dropped web2

* Wed Mar 16 2005 Jeff Pitman <symbiont+pyvault@berlios.de> 2.0.0-0.1.a3
- upstream release

* Sat Mar 12 2005 Jeff Pitman <symbiont+pyvault@berlios.de> 2.0.0-0.1.a2
- new prerelease; FE versioning

* Mon Feb 07 2005 Jeff Pitman <symbiont+pyvault@berlios.de> 2.0.0a1-1
- prep for split

* Fri Aug 20 2004 Jeff Pitman <symbiont+pyvault@berlios.de> 1.3.0-1
- new version

* Mon Apr 19 2004 Jeff Pitman <symbiont+pyvault@berlios.de> 1.2.0-3
- vaultize

* Mon Apr 12 2004 Jeff Pitman <symbiont+pyvault@berlios.de> 1.2.0-2
- require pyOpenSSL, SOAPpy, openssh-clients, crypto, dia so trial can run

