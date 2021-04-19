# Version
%global major 7
%global minor 1
%global patchlevel 1

# Revision
%global revnum 9
# set to 1 for hg snapshots, 0 for release
%global usesnapshot 0

# SNAPSHOT version
%global hgrevhash 63ec7d0ee8d9
%global hgrevdate 20200608

%global tarball_name jmc7-%{hgrevhash}

# Install jmc in /usr/lib/jmc (arch-specific and multilib exempt)
%global _jmcdir %{_prefix}/lib/%{name}
%global _eclipsepluginsdir %{_prefix}/lib/eclipse/plugins

%global debug_package %{nil}

%if %{usesnapshot}
  %global releasestr %{revnum}.%{hgrevdate}hg%{hgrevhash}
%else
  %global releasestr %{revnum}
%endif

%ifarch %{ix86}
    %global eclipse_arch x86
%endif
%ifarch %{arm}
    %global eclipse_arch arm
%endif
%ifarch s390x x86_64 aarch64 ppc64le
    %global eclipse_arch %{_arch}
%endif

# Don't export Eclipse libraries
%global __provides_exclude_from ^%{_jmcdir}/plugins/org.eclipse.*$
%global __requires_exclude_from ^%{_jmcdir}/plugins/org.eclipse.*$

%global __requires_exclude ^osgi\\((javax|org\\.apache|org\\.eclipse|org\\.sat4j).*$
%global __provides_exclude ^osgi\\((com|javax|org\\.apache|org\\.glassfish|org\\.kxml2|org\\.sat4j|org\\.tukaani|org\\.w3c|org\\.xmlpull).*$

Name:       jmc
Version:    %{major}.%{minor}.%{patchlevel}
Release:    %{releasestr}%{?dist}.1
Summary:    JDK Mission Control is a profiling and diagnostics tool

# jmc source README.md states: The Mission Control source code is made
# available under the Universal Permissive License (UPL), Version 1.0 or a
# BSD-style license, alternatively. The full open source license text is
# available at license/LICENSE.txt in the JMC project.
License:  UPL or BSD
URL:        http://openjdk.java.net/projects/jmc/

Source0:    https://hg.openjdk.java.net/jmc/jmc7/archive/%{hgrevhash}.tar.gz
Source1:    %{name}.desktop
Source2:    %{name}.1
Source3:    symlink_libs.sh
Source4:    %{name}.appdata.xml

# Remove optional twitter related functionality
Patch0:     0-remove-twitter.patch
# Update javax dependency names to match what is found in Fedora
Patch2:     2-javax.patch
# Remove maven build profiles that won't be used in local build
Patch3:     3-remove-profiles.patch
# Remove localization files that currently cannot be supported
# due to a packaging issue for Eclipse language packs
# eclipse-nls-ja and eclipse-nls-zh
# They currently provide multiple archs within the same package
# and the local build system cannot fulfill dependencies from them
Patch4:     4-remove-localization.patch
# Remove unused module org.openjdk.jmc.ide.jdt
Patch5:     5-remove-ide-jdt.patch
# Remove unused remote repository definition
Patch6:     6-remove-buchen-repo.patch
# Add dependency on org. hamcrest-core to provide class used in unit tests
Patch7:     7-add-hamcrest.patch
# Remove windows and mac arches
Patch8:     8-remove-arch.patch
# Remove unnecessary dependency
Patch9:     9-remove-jacoco-dep.patch
# Revert downloading of flameview assets from the web
Patch10:    10-revert-flameview.patch
# Drop JFR flags (temporary)
Patch11:    11-update-flags.patch
# Use tycho 2.x
Patch12:    12-tycho.patch

# JMC depends on Eclipse which no longer supports non-64bit arches
ExcludeArch: s390 %{arm} %{ix86}

BuildRequires:  desktop-file-utils
BuildRequires:  maven-local

BuildRequires:  eclipse-pde
BuildRequires:  tycho

BuildRequires:  jakarta-mail
BuildRequires:  mvn(org.commonjava.maven.plugins:directory-maven-plugin)
BuildRequires:  mvn(org.openjdk.jmc:common)
BuildRequires:  HdrHistogram >= 2.1.11

BuildRequires: libappstream-glib

Requires:  java-openjdk >= 1:1.8

Requires:  osgi(com.sun.mail.jakarta.mail)
Requires:  osgi(org.openjdk.jmc.common)
Requires:  osgi(org.openjdk.jmc.flightrecorder)
Requires:  osgi(org.openjdk.jmc.flightrecorder.rules)
Requires:  osgi(org.openjdk.jmc.flightrecorder.rules.jdk)
Requires:  osgi(org.owasp.encoder)
Requires:  osgi(org.hdrhistogram.HdrHistogram) >= 2.1.11

Requires: gtk3
Requires: webkitgtk4
Requires: libGLU.so.1()(64bit)

%description
JDK Mission Control is a powerful profiler for HotSpot JVMs and has an
advanced set of tools that enables efficient and detailed analysis of the
extensive data collected by JDK Flight Recorder. The tool chain enables
developers and administrators to collect and analyze data from Java
applications running locally or deployed in production environments.

%prep
%setup -q -n %{tarball_name}

%patch0 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1

%pom_disable_module releng
%pom_disable_module l10n application
%pom_disable_module org.openjdk.jmc.updatesite.ide application
%pom_disable_module org.openjdk.jmc.updatesite.rcp application

# disable tests that require the use of jfr v1
%pom_disable_module org.openjdk.jmc.rjmx.services.jfr.test application/tests
%pom_disable_module org.openjdk.jmc.flightrecorder.controlpanel.ui.test application/tests

%pom_remove_plugin com.github.spotbugs:spotbugs-maven-plugin
%pom_remove_plugin :maven-enforcer-plugin

%pom_remove_plugin :jacoco-maven-plugin application/tests
%pom_remove_plugin :jacoco-maven-plugin application/uitests
%pom_disable_module coverage application

# Info.plist are mac files and we only build for Linux
%pom_remove_plugin name.abuchen:fix-info-plist-maven-plugin application/org.openjdk.jmc.rcp.product

%pom_remove_plugin org.codehaus.mojo:buildnumber-maven-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-deploy-plugin

TYCHO_ENV="<environment><os>linux</os><ws>gtk</ws><arch>%{eclipse_arch}</arch></environment>"
%pom_xpath_set "pom:configuration/pom:environments" "$TYCHO_ENV"

%build
# some tests require large heap and fail with OOM
# depending on the builder resources
%mvn_build -j -- -Dmaven.test.failure.ignore=true -DbuildId=fedora -DbuildNumber=%{hgrevhash} -Dbuild.date=%{hgrevdate}

%install

# not using mvn_install macro because it installs JMC as an Eclipse plugin
# we want to install JMC as an RCP application

# change jmc.ini to use system java (remove -vm option line)
sed -i '/^-vm$/d' %{_builddir}/%{tarball_name}/target/products/org.openjdk.jmc/%{_os}/gtk/%{eclipse_arch}/%{name}.ini
sed -i '/^..\/..\/bin\/$/d' %{_builddir}/%{tarball_name}/target/products/org.openjdk.jmc/%{_os}/gtk/%{eclipse_arch}/%{name}.ini

# delete unnecessary files
rm -r %{_builddir}/%{tarball_name}/target/products/org.openjdk.jmc/%{_os}/gtk/%{eclipse_arch}/p2/

# move contents of target/products/org.openjdk.jmc/%{_os}/gtk/%{eclipse_arch}/ to /usr/lib/jmc/
install -d -m 755 %{buildroot}%{_jmcdir}
cp -p -r %{_builddir}/%{tarball_name}/target/products/org.openjdk.jmc/%{_os}/gtk/%{eclipse_arch}/* %{buildroot}%{_jmcdir}/

# move jmc.ini to /etc/jmc.ini
install -d -m 755 %{buildroot}%{_sysconfdir}
mv %{buildroot}%{_jmcdir}/%{name}.ini %{buildroot}%{_sysconfdir}/%{name}.ini
ln -s %{_sysconfdir}/%{name}.ini %{buildroot}%{_jmcdir}/%{name}.ini

# create symlink to jmc in /usr/bin/
install -d -m 755 %{buildroot}%{_bindir}
ln -s %{_jmcdir}/%{name} %{buildroot}%{_bindir}/%{name}

# replace jars with symlinks to installed libraries
bash %{SOURCE3} %{buildroot}%{_jmcdir}/plugins %{_javadir}/jmc-core

# create application launcher in desktop menu
install -d -m 755 %{buildroot}%{_datadir}/pixmaps
mv %{buildroot}%{_jmcdir}/icon.xpm %{buildroot}%{_datadir}/pixmaps/%{name}.xpm
chmod 644 %{buildroot}%{_datadir}/pixmaps/%{name}.xpm
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}

# install pom file
install -d -m 755 %{buildroot}%{_datadir}/maven-poms/%{name}
install -p -m 644 %{_builddir}/%{tarball_name}/pom.xml %{buildroot}%{_datadir}/maven-poms/%{name}/%{name}.pom

# install manpage and insert location of config file
install -d -m 755 %{buildroot}%{_mandir}/man1
install -p -m 644 %{SOURCE2} %{buildroot}%{_mandir}/man1/%{name}.1
sed -i "/.SH FILES/a .I %{_sysconfdir}/%{name}.ini" %{buildroot}%{_mandir}/man1/%{name}.1

# install appdata and validate it
install -d -m 755 %{buildroot}%{_metainfodir}
install -p -m 644 %{SOURCE4} %{buildroot}%{_metainfodir}/%{name}.appdata.xml
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml

%files
%license license/LICENSE.txt
%license license/THIRDPARTYREADME.txt
%doc README.md
%config(noreplace) %{_sysconfdir}/%{name}.ini
%{_jmcdir}
%{_mandir}/man1/%{name}.1*
%{_bindir}/%{name}
%{_datadir}/maven-poms/%{name}
%{_datadir}/pixmaps/%{name}.xpm
%{_datadir}/applications/%{name}.desktop
%{_metainfodir}/%{name}.appdata.xml

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 7.1.1-9.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2020 Jie Kang <jkang@redhat.com> - 7.1.1-9
- Rebuild for updated jna and tycho 2.x

* Fri Nov 06 2020 Jie Kang <jkang@redhat.com> - 7.1.1-8
- Use jakarta-mail

* Mon Sep 21 2020 Jie Kang <jkang@redhat.com> - 7.1.1-7
- Update license. Use javamail until jakarta-mail is included
- Add appdata and validate it

* Fri Aug 28 2020 Jie Kang <jkang@redhat.com> - 7.1.1-6
- Update to latest upstream
- Drop javax dependencies
- Clean spec

* Fri Aug 07 2020 Alex Macdonald <almacdon@redhat.com> - 7.1.1-5
- Update symlink to match javamail version in rpms/javamail
- Version 1.6.5 is compatible with 1.6.3 according to the upstream compatibility notes

* Wed Jul 29 2020 Alex Macdonald <almacdon@redhat.com> - 7.1.1-4
- Update symlink script with path to jakarta-activation

* Mon Apr 27 2020 Jie Kang <jkang@redhat.com> - 7.1.1-3
- Update to upstream 7.1.1 ga commit

* Wed Mar 11 2020 Alex Macdonald <almacdon@redhat.com> - 7.1.1-2
- Update to latest upstream (to include JMC-6728)

* Tue Feb 25 2020 Alex Macdonald <almacdon@redhat.com> - 7.1.1-1
- Update to latest upstream

* Tue Feb 18 2020 Alex Macdonald <almacdon@redhat.com> - 7.1.0-2
- Add backports of JMC-6554 & JMC-6692 on top of JMC 7 for improved handling of OpenJDK8+JFR

* Thu Jan 09 2020 Alex Macdonald <almacdon@redhat.com> - 7.1.0-1
- Update to latest upstream (7.1.0-ga)
- Update the jmc7 branch to more closely resemble files of the main jmc branch
- Addition of Patch9 and Patch10, updated symlink_libs.sh

* Tue Sep 24 2019 Jie Kang <jkang@redhat.com> - 7.0.0-1
- Update to latest upstream with minor bug fixes

* Mon Jun 03 2019 Jie Kang <jkang@redhat.com> - 7.0.0-0
- Initial package
