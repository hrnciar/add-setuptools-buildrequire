Name:           openscap
Version:        1.3.4
Release:        4%{?dist}
Epoch:          1
Summary:        Set of open source libraries enabling integration of the SCAP line of standards
License:        LGPLv2+
URL:            http://www.open-scap.org/
Source0:        https://github.com/OpenSCAP/%{name}/releases/download/%{version}/%{name}-%{version}.tar.gz
Patch1:         openscap-1.3.5-plug-memory-leak-PR_1616.patch
Patch2:         openscap-1.3.5-coverity1-PR_1617.patch
Patch3:         openscap-1.3.5-coverity2-PR_1620.patch
Patch4:         openscap-1.3.5-yamlfilecontent-fix-field-names-PR_1619.patch
BuildRequires: make
BuildRequires:  cmake >= 2.6
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  swig libxml2-devel libxslt-devel perl-generators perl-XML-Parser
BuildRequires:  rpm-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  pcre-devel
BuildRequires:  libacl-devel
BuildRequires:  libselinux-devel
BuildRequires:  libcap-devel
BuildRequires:  libblkid-devel
BuildRequires:  bzip2-devel
BuildRequires:  asciidoc
BuildRequires:  openldap-devel
BuildRequires:  glib2-devel
BuildRequires:  dbus-devel
BuildRequires:  libyaml-devel
%if %{?_with_check:1}%{!?_with_check:0}
BuildRequires:  perl-XML-XPath
BuildRequires:  bzip2
%endif
Requires:       bash
Requires:       bzip2-libs
Requires:       dbus
Requires:       glib2
Requires:       libacl
Requires:       libblkid
Requires:       libcap
Requires:       libselinux
Requires:       openldap
Requires:       popt
# Fedora has procps-ng, which provides procps
Requires:       procps

%description
OpenSCAP is a set of open source libraries providing an easier path
for integration of the SCAP line of standards. SCAP is a line of standards
managed by NIST with the goal of providing a standard language
for the expression of Computer Network Defense related information.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       libxml2-devel
Requires:       pkgconfig
BuildRequires:  doxygen

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        python3
Summary:        Python 3 bindings for %{name}
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}
BuildRequires:  python3-devel

%description    python3
The %{name}-python3 package contains the bindings so that %{name}
libraries can be used by python3.

%package        scanner
Summary:        OpenSCAP Scanner Tool (oscap)
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       libcurl >= 7.12.0
BuildRequires:  libcurl-devel >= 7.12.0

%description    scanner
The %{name}-scanner package contains oscap command-line tool. The oscap
is configuration and vulnerability scanner, capable of performing
compliance checking using SCAP content.

%package        utils
Summary:        OpenSCAP Utilities
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       rpmdevtools rpm-build
Requires:       %{name}-scanner%{?_isa} = %{epoch}:%{version}-%{release}

%description    utils
The %{name}-utils package contains command-line tools build on top
of OpenSCAP library. Historically, openscap-utils included oscap
tool which is now separated to %{name}-scanner sub-package.

%package        engine-sce
Summary:        Script Check Engine plug-in for OpenSCAP
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}

%description    engine-sce
The Script Check Engine is non-standard extension to SCAP protocol. This
engine allows content authors to avoid OVAL language and write their assessment
commands using a scripting language (Bash, Perl, Python, Ruby, ...).

%package        engine-sce-devel
Summary:        Development files for %{name}-engine-sce
Requires:       %{name}-devel%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       %{name}-engine-sce%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       pkgconfig

%description    engine-sce-devel
The %{name}-engine-sce-devel package contains libraries and header files
for developing applications that use %{name}-engine-sce.

%package        containers
Summary:        Utils for scanning containers
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       %{name}-scanner
BuildArch:      noarch

%description    containers
Tool for scanning Atomic containers.

%prep
%autosetup -p1

%build
# gconf is a legacy system not used any more, and it blocks testing of oscap-anaconda-addon
# as gconf is no longer part of the installation medium
%cmake \
    -DENABLE_PERL=OFF \
    -DENABLE_DOCS=ON \
    -DOPENSCAP_PROBE_UNIX_GCONF=OFF \
    -DGCONF_LIBRARY=
%cmake_build
make docs

%check
%if %{?_with_check:1}%{!?_with_check:0}
ctest -V %{?_smp_mflags}
%endif

%install
%cmake_install

find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

# fix python shebangs
pathfix.py -i %{__python3} -p -n $RPM_BUILD_ROOT%{_bindir}/scap-as-rpm

%ldconfig_scriptlets

%files
%doc AUTHORS NEWS README.md
%license COPYING
%doc %{_pkgdocdir}/manual/
%dir %{_datadir}/openscap
%dir %{_datadir}/openscap/schemas
%dir %{_datadir}/openscap/xsl
%dir %{_datadir}/openscap/cpe
%{_libdir}/libopenscap.so.*
%{_datadir}/openscap/schemas/*
%{_datadir}/openscap/xsl/*
%{_datadir}/openscap/cpe/*

%files python3
%{python3_sitearch}/*

%files devel
%doc %{_pkgdocdir}/html/
%{_libdir}/libopenscap.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/openscap
%exclude %{_includedir}/openscap/sce_engine_api.h

%files engine-sce-devel
%{_libdir}/libopenscap_sce.so
%{_includedir}/openscap/sce_engine_api.h

%files scanner
%{_mandir}/man8/oscap.8*
%{_bindir}/oscap
%{_bindir}/oscap-chroot
%{_sysconfdir}/bash_completion.d

%files utils
%doc docs/oscap-scan.cron
%{_mandir}/man8/*
%exclude %{_mandir}/man8/oscap.8*
%exclude %{_mandir}/man8/oscap-docker.8*
%{_bindir}/*
%exclude %{_bindir}/oscap
%exclude %{_bindir}/oscap-docker
%exclude %{_bindir}/oscap-chroot

%files engine-sce
%{_libdir}/libopenscap_sce.so.*

%files containers
%{_bindir}/oscap-docker
%{_mandir}/man8/oscap-docker.8*
%{python3_sitelib}/oscap_docker_python/*
%{_bindir}/oscap-podman
%{_mandir}/man8/oscap-podman.8*

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.3.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Dec 09 2020 Jan ??ern?? <jcerny@redhat.com> - 1:1.3.4-3
- Remove dependency on GConf2
- Update cmake command

* Tue Nov 03 2020 Evgenii Kolesnikov <ekolesni@redhat.com> - 1.3.4-2
- Fix problems uncovered by the Coverity Scan
- Fix field names handling in yamlfilecontent probe

* Wed Oct 07 2020 Evgenii Kolesnikov <ekolesni@redhat.com> - 1:1.3.4-1
- Upgrade to the latest upstream release

* Thu Aug 27 2020 Jan ??ern?? <jcerny@redhat.com> - 1:1.3.3-6
- Disabled the gconf probe, and removed the gconf dependency.
  gconf is a legacy system not used any more, and it blocks testing of oscap-anaconda-addon
  as gconf is no longer part of the installation medium for Fedora 32

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.3.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 14 2020 Tom Stellard <tstellar@redhat.com> - 1:1.3.3-4
- Update spec file to use new cmake macros
- https://fedoraproject.org/wiki/Changes/CMake_to_do_out-of-source_builds

* Tue May 26 2020 Miro Hron??ok <mhroncok@redhat.com> - 1:1.3.3-3
- Rebuilt for Python 3.9

* Mon May 04 2020 Jan ??ern?? <jcerny@redhat.com> - 1:1.3.3-2
- Add libyaml-devel as a dependency to enable yamlfilecontent probe

* Thu Apr 30 2020 Jan ??ern?? <jcerny@redhat.com> - 1:1.3.3-1
- Upgrade to the latest upstream release

* Thu Apr 09 2020 Mat??j T???? <matyc@redhat.com> - 1:1.3.2-5
- Made the spec file requirements section copy-paste of the RHEL8 section.
- Cleaned the spec file up from ancient obsoletes.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 27 2020 Jan ??ern?? <jcerny@redhat.com> - 1:1.3.2-3
- Fix duplicate global variables (RHBZ#1793914)

* Wed Jan 15 2020 Jan ??ern?? <jcerny@redhat.com> - 1:1.3.2-2
- Do not use C++ keyword operator as a function parameter name

* Tue Jan 14 2020 Jan ??ern?? <jcerny@redhat.com> - 1:1.3.2-1
- Upgrade to the latest upstream release

* Thu Oct 03 2019 Miro Hron??ok <mhroncok@redhat.com> - 1:1.3.1-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hron??ok <mhroncok@redhat.com> - 1:1.3.1-3
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 13 2019 Jan ??ern?? <jcerny@redhat.com> - 1:1.3.1-1
- upgrade to the latest upstream release

* Mon Jun 10 22:13:21 CET 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1:1.3.0-7
- Rebuild for RPM 4.15

* Mon Jun 10 15:42:04 CET 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1:1.3.0-6
- Rebuild for RPM 4.15

* Sat Jun 01 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1:1.3.0-5
- Perl 5.30 rebuild

* Mon May 20 2019 Jan ??ern?? <jcerny@redhat.com> - 1.3.0-4
- Upgrade the Epoch to align with F30

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Oct 19 2018 Mat??j T???? <matyc@redhat.com> - 1.3.0-2
- Removed the openscap-perl package to be on par with RHEL.

* Tue Oct 09 2018 Jan ??ern?? <jcerny@redhat.com> - 1.3.0-1
- upgrade to the latest upstream release

* Mon Sep 10 2018 Jan ??ern?? <jcerny@redhat.com> - 1.3.0_alpha2-2
- List subpackages removed in 1.3.0_alpha1-1 as obsoleted (RHBZ#1626801)

* Mon Aug 13 2018 Jan ??ern?? <jcerny@redhat.com> - 1.3.0_alpha2-1
- upgrade to the latest upstream release

* Wed Jul 25 2018 Jan ??ern?? <jcerny@redhat.com> - 1.3.0_alpha1-2
- removed python2-openscap subpackage

* Wed Jul 18 2018 Jan ??ern?? <jcerny@redhat.com> - 1.3.0_alpha1-1
- upgrade to the latest upstream release
- change specfile to use CMake
- dropped commands in the spec file that are no longer relevant
- dropped subpackages in the spec file that are no longer relevant

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.17-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 03 2018 Petr Pisar <ppisar@redhat.com> - 1.2.17-4
- Perl 5.28 rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.2.17-3
- Perl 5.28 rebuild

* Tue Jun 19 2018 Miro Hron??ok <mhroncok@redhat.com> - 1.2.17-2
- Rebuilt for Python 3.7

* Tue May 29 2018 Jan ??ern?? <jcerny@redhat.com> - 1.2.17-1
- upgrade to the latest upstream release

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 12 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.2.16-2
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Tue Nov 14 2017 jcerny@redhat.com - 1.2.16-1
- upgrade to the latest upstream release

* Thu Oct 05 2017 Martin Preisler <mpreisle@redhat.com> - 1.2.15-2
- moved oscap-chroot to openscap-scanner because it's a thin wrapper script with no dependencies

* Fri Aug 25 2017 Jan ??ern?? <jcerny@redhat.com> - 1.2.15-1
- upgrade to the latest upstream release

* Sun Aug 20 2017 Zbigniew J??drzejewski-Szmek <zbyszek@in.waw.pl> - 1.2.14-9
- Add Provides for the old name without %%_isa

* Sat Aug 19 2017 Zbigniew J??drzejewski-Szmek <zbyszek@in.waw.pl> - 1.2.14-8
- Python 2 binary package renamed to python2-openscap
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Fri Aug 11 2017 Igor Gnatenko <ignatenko@redhat.com> - 1.2.14-7
- Rebuilt after RPM update (??? 3)

* Thu Aug 10 2017 Igor Gnatenko <ignatenko@redhat.com> - 1.2.14-6
- Rebuilt for RPM soname bump

* Thu Aug 10 2017 Igor Gnatenko <ignatenko@redhat.com> - 1.2.14-5
- Rebuilt for RPM soname bump

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.2.14-2
- Perl 5.26 rebuild

* Tue Mar 21 2017 Martin Preisler <mpreisle@redhat.com> - 1.2.14-1
- upgrade to the latest upstream release

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 05 2017 Martin Preisler <mpreisle@redhat.com> - 1.2.13-1
- upgrade to the latest upstream release

* Mon Dec 19 2016 Miro Hron??ok <mhroncok@redhat.com> - 1.2.12-2
- Rebuild for Python 3.6

* Tue Nov 22 2016 Martin Preisler <mpreisle@redhat.com> - 1.2.12-1
- upgrade to the latest upstream release

* Wed Oct 19 2016 Martin Preisler <mpreisle@redhat.com> - 1.2.11-1
- upgrade to the latest upstream release

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.10-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue Jul 12 2016 Martin Preisler <mpreisle@redhat.com> - 1.2.10-1
- upgrade to the latest upstream release

* Tue May 17 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.2.9-2
- Perl 5.24 rebuild

* Fri Apr 22 2016 Martin Preisler <mpreisle@redhat.com> - 1.2.9-1
- upgrade to the latest upstream release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 18 2016 ??imon Luka????k <slukasik@redhat.com> - 1.2.8-1
- upgrade to the latest upstream release

* Thu Dec 03 2015 ??imon Luka????k <slukasik@redhat.com> - 1.2.7-1
- upgrade to the latest upstream release

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.6-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Tue Oct 13 2015 Zbyn??k Moravec <zmoravec@redhat.com> - 1.2.6-3
- fix oscap-docker shebang

* Wed Oct 07 2015 ??imon Luka????k <slukasik@redhat.com> - 1.2.6-2
- put oscap-docker to openscap-containers subpackage
- do not require atomic at all

* Mon Oct 05 2015 Zbyn??k Moravec <zmoravec@redhat.com> - 1.2.6-1
- upgrade to the latest upstream release

* Wed Jul 29 2015 Martin Preisler <mpreisle@redhat.com> - 1.2.5-2
- rebuilt because of librpm and librpmio ABI break

* Mon Jul 06 2015 ??imon Luka????k <slukasik@redhat.com> - 1.2.5-1
- upgrade to the latest upstream release

* Sat Jun 20 2015 ??imon Luka????k <slukasik@redhat.com> - 1.2.4-1
- upgrade to the latest upstream release.
- Content of selinux package has been purged.

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.2.3-2
- Perl 5.22 rebuild

* Fri May 01 2015 ??imon Luka????k <slukasik@redhat.com> - 1.2.3-1
- upgrade to the latest upstream release

* Thu Apr 02 2015 ??imon Luka????k <slukasik@redhat.com> - 1.2.2-1
- upgrade to the latest upstream release

* Sat Jan 10 2015 ??imon Luka????k <slukasik@redhat.com> - 1.2.1-1
- upgrade to the latest upstream release

* Tue Dec 02 2014 ??imon Luka????k <slukasik@redhat.com> - 1.2.0-1
- upgrade to the latest upstream release

* Fri Sep 26 2014 ??imon Luka????k <slukasik@redhat.com> - 1.1.1-1
- upgrade to the latest upstream release

* Fri Sep 05 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.1.0-2
- Perl 5.20 rebuild

* Wed Sep 03 2014 ??imon Luka????k <slukasik@redhat.com> - 1.1.0-1
- upgrade

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.0.9-4
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 01 2014 ??imon Luka????k <slukasik@redhat.com> - 1.0.9-2
- Extract oscap tool to a separate package (rhbz#1115116)

* Wed Jun 25 2014 Martin Preisler <mpreisle@redhat.com> - 1.0.9-1
- upgrade

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Mar 26 2014 ??imon Luka????k <slukasik@redhat.com> - 1.0.8-1
- upgrade

* Thu Mar 20 2014 ??imon Luka????k <slukasik@redhat.com> - 1.0.7-1
- upgrade

* Wed Mar 19 2014 ??imon Luka????k <slukasik@redhat.com> - 1.0.6-1
- upgrade

* Fri Mar 14 2014 ??imon Luka????k <slukasik@redhat.com> - 1.0.5-1
- upgrade

* Thu Feb 13 2014 ??imon Luka????k <slukasik@redhat.com> - 1.0.4-1
- upgrade

* Tue Jan 14 2014 ??imon Luka????k <slukasik@redhat.com> - 1.0.3-1
- upgrade
- This upstream release addresses: #1052142

* Fri Jan 10 2014 ??imon Luka????k <slukasik@redhat.com> - 1.0.2-1
- upgrade
- This upstream release addresses: #1018291, #1029879, #1026833

* Thu Nov 28 2013 ??imon Luka????k <slukasik@redhat.com> - 1.0.1-1
- upgrade

* Tue Nov 26 2013 ??imon Luka????k <slukasik@redhat.com> - 1.0.0-3
- expand LT_CURRENT_MINUS_AGE correctly

* Thu Nov 21 2013 ??imon Luka????k <slukasik@redhat.com> - 1.0.0-2
- dlopen libopenscap_sce.so.{current-age} explicitly
  That allows for SCE to work without openscap-engine-sce-devel

* Tue Nov 19 2013 ??imon Luka????k <slukasik@redhat.com> - 1.0.0-1
- upgrade
- package openscap-engine-sce-devel separately

* Fri Nov 15 2013 ??imon Luka????k <slukasik@redhat.com> - 0.9.13-7
- do not obsolete openscap-conten just drop it (#1028706)
  scap-security-guide will bring the Obsoletes tag

* Thu Nov 14 2013 ??imon Luka????k <slukasik@redhat.com> - 0.9.13-6
- only non-noarch packages should be requiring specific architecture

* Sat Nov 09 2013 ??imon Luka????k <slukasik@redhat.com> 0.9.13-5
- specify architecture when requiring base package

* Fri Nov 08 2013 ??imon Luka????k <slukasik@redhat.com> 0.9.13-4
- specify dependency between engine and devel sub-package

* Fri Nov 08 2013 ??imon Luka????k <slukasik@redhat.com> 0.9.13-3
- correct openscap-utils dependencies

* Fri Nov 08 2013 ??imon Luka????k <slukasik@redhat.com> 0.9.13-2
- drop openscap-content package (use scap-security-guide instead)

* Fri Nov 08 2013 ??imon Luka????k <slukasik@redhat.com> 0.9.13-1
- upgrade

* Thu Sep 26 2013 ??imon Luka????k <slukasik@redhat.com> 0.9.12-2
- Start building SQL probes for Fedora

* Wed Sep 11 2013 ??imon Luka????k <slukasik@redhat.com> 0.9.12-1
- upgrade

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 18 2013 Petr Lautrbach <plautrba@redhat.com> 0.9.11-1
- upgrade

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 0.9.10-2
- Perl 5.18 rebuild

* Mon Jul 15 2013 Petr Lautrbach <plautrba@redhat.com> 0.9.10-1
- upgrade

* Mon Jun 17 2013 Petr Lautrbach <plautrba@redhat.com> 0.9.8-1
- upgrade

* Fri Apr 26 2013 Petr Lautrbach <plautrba@redhat.com> 0.9.7-1
- upgrade
- add openscap-selinux sub-package

* Wed Apr 24 2013 Petr Lautrbach <plautrba@redhat.com> 0.9.6-1
- upgrade

* Wed Mar 20 2013 Petr Lautrbach <plautrba@redhat.com> 0.9.5-1
- upgrade

* Mon Mar 04 2013 Petr Lautrbach <plautrba@redhat.com> 0.9.4.1-1
- upgrade

* Tue Feb 26 2013 Petr Lautrbach <plautrba@redhat.com> 0.9.4-1
- upgrade

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Dec 17 2012 Petr Lautrbach <plautrba@redhat.com> 0.9.3-1
- upgrade

* Wed Nov 21 2012 Petr Lautrbach <plautrba@redhat.com> 0.9.2-1
- upgrade

* Mon Oct 22 2012 Petr Lautrbach <plautrba@redhat.com> 0.9.1-1
- upgrade

* Tue Sep 25 2012 Peter Vrabec <pvrabec@redhat.com> 0.9.0-1
- upgrade

* Mon Aug 27 2012 Petr Lautrbach <plautrba@redhat.com> 0.8.5-1
- upgrade

* Tue Aug 07 2012 Petr Lautrbach <plautrba@redhat.com> 0.8.4-1
- upgrade

* Tue Jul 31 2012 Petr Lautrbach <plautrba@redhat.com> 0.8.3-2
- fix Profile and  @hidden issue

* Mon Jul 30 2012 Petr Lautrbach <plautrba@redhat.com> 0.8.3-1
- upgrade

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 08 2012 Petr Pisar <ppisar@redhat.com> - 0.8.2-2
- Perl 5.16 rebuild

* Fri Mar 30 2012 Petr Lautrbach <plautrba@redhat.com> 0.8.2-1
- upgrade

* Tue Feb 21 2012 Peter Vrabec <pvrabec@redhat.com> 0.8.1-1
- upgrade

* Fri Feb 10 2012 Petr Pisar <ppisar@redhat.com> - 0.8.0-3
- Rebuild against PCRE 8.30

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Oct 11 2011 Peter Vrabec <pvrabec@redhat.com> 0.8.0-1
- upgrade

* Mon Jul 25 2011 Peter Vrabec <pvrabec@redhat.com> 0.7.4-1
- upgrade

* Thu Jul 21 2011 Petr Sabata <contyk@redhat.com> - 0.7.3-3
- Perl mass rebuild

* Wed Jul 20 2011 Petr Sabata <contyk@redhat.com> - 0.7.3-2
- Perl mass rebuild

* Fri Jun 24 2011 Peter Vrabec <pvrabec@redhat.com> 0.7.3-1
- upgrade

* Fri Jun 17 2011 Marcela Ma??l????ov?? <mmaslano@redhat.com> - 0.7.2-3
- Perl mass rebuild

* Fri Jun 10 2011 Marcela Ma??l????ov?? <mmaslano@redhat.com> - 0.7.2-2
- Perl 5.14 mass rebuild

* Wed Apr 20 2011 Peter Vrabec <pvrabec@redhat.com> 0.7.2-1
- upgrade

* Fri Mar 11 2011 Peter Vrabec <pvrabec@redhat.com> 0.7.1-1
- upgrade

* Thu Feb 10 2011 Peter Vrabec <pvrabec@redhat.com> 0.7.0-1
- upgrade

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan 31 2011 Peter Vrabec <pvrabec@redhat.com> 0.6.8-1
- upgrade

* Fri Jan 14 2011 Peter Vrabec <pvrabec@redhat.com> 0.6.7-1
- upgrade

* Wed Oct 20 2010 Peter Vrabec <pvrabec@redhat.com> 0.6.4-1
- upgrade

* Tue Sep 14 2010 Peter Vrabec <pvrabec@redhat.com> 0.6.3-1
- upgrade

* Fri Aug 27 2010 Peter Vrabec <pvrabec@redhat.com> 0.6.2-1
- upgrade

* Wed Jul 14 2010 Peter Vrabec <pvrabec@redhat.com> 0.6.0-1
- upgrade

* Wed May 26 2010 Peter Vrabec <pvrabec@redhat.com> 0.5.11-1
- upgrade

* Fri May 07 2010 Peter Vrabec <pvrabec@redhat.com> 0.5.10-1
- upgrade

* Fri Apr 16 2010 Peter Vrabec <pvrabec@redhat.com> 0.5.9-1
- upgrade

* Fri Feb 26 2010 Peter Vrabec <pvrabec@redhat.com> 0.5.7-1
- upgrade
- new utils package

* Mon Jan 04 2010 Peter Vrabec <pvrabec@redhat.com> 0.5.6-1
- upgrade

* Tue Sep 29 2009 Peter Vrabec <pvrabec@redhat.com> 0.5.3-1
- upgrade

* Wed Aug 19 2009 Peter Vrabec <pvrabec@redhat.com> 0.5.2-1
- upgrade

* Mon Aug 03 2009 Peter Vrabec <pvrabec@redhat.com> 0.5.1-2
- add rpm-devel requirement

* Mon Aug 03 2009 Peter Vrabec <pvrabec@redhat.com> 0.5.1-1
- upgrade

* Thu Apr 30 2009 Peter Vrabec <pvrabec@redhat.com> 0.3.3-1
- upgrade

* Thu Apr 23 2009 Peter Vrabec <pvrabec@redhat.com> 0.3.2-1
- upgrade

* Sun Mar 29 2009 Peter Vrabec <pvrabec@redhat.com> 0.1.4-1
- upgrade

* Fri Mar 27 2009 Peter Vrabec <pvrabec@redhat.com> 0.1.3-2
- spec file fixes (#491892)

* Tue Mar 24 2009 Peter Vrabec <pvrabec@redhat.com> 0.1.3-1
- upgrade

* Thu Jan 15 2009 Tomas Heinrich <theinric@redhat.com> 0.1.1-1
- Initial rpm

