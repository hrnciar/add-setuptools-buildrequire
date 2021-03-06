# Copyright (c) 2000-2005, JPackage Project
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the
#    distribution.
# 3. Neither the name of the JPackage Project nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

%define scm_version 1_7_7_1

Name:           rhino
Version:        1.7.7.1
Release:        14%{?dist}
Summary:        JavaScript for Java
License:        MPLv2.0

Source0:        https://github.com/mozilla/rhino/archive/Rhino%{scm_version}_RELEASE.tar.gz
Source1:        http://repo1.maven.org/maven2/org/mozilla/rhino/%{version}/rhino-%{version}.pom
Source2:        %{name}.script

Patch0:         %{name}-build.patch
# Add OSGi metadata from Eclipse Orbit project
Patch1:         %{name}-addOrbitManifest.patch

URL:            http://www.mozilla.org/rhino/

BuildRequires:  ant
BuildRequires:  java-devel >= 1:1.6.0.0
BuildRequires:  javapackages-local
Requires:       jline2
# Explicit javapackages-tools requires since rhino script uses
# /usr/share/java-utils/java-functions
Requires:       javapackages-tools
Obsoletes:      %{name}-javadoc < %{version}-%{release}
Obsoletes:      %{name}-manual < %{version}-%{release}

# Disable xmlbeans until we can get it into Fedora
#Requires:       xmlbeans
#BuildRequires:  xmlbeans
BuildArch:      noarch

%description
Rhino is an open-source implementation of JavaScript written entirely
in Java. It is typically embedded into Java applications to provide
scripting to end users.

%package        demo
Summary:        Examples for %{name}

%description    demo
Examples for %{name}.

%prep
%setup -q -n %{name}-Rhino%{scm_version}_RELEASE
%patch0 -p1 -b .build
%patch1 -b .fixManifest

# Fix manifest
sed -i -e '/^Class-Path:.*$/d' src/manifest

# Add jpp release info to version
sed -i -e 's|^implementation.version: Rhino .* release .* \${implementation.date}|implementation.version: Rhino %{version} release %{release} \${implementation.date}|' build.properties

%mvn_alias : rhino:js
%mvn_file : js %{name}

%build
ant deepclean jar copy-all -Dno-xmlbeans=1
%mvn_artifact %{SOURCE1} build/%{name}%{version}/js.jar

pushd examples

export CLASSPATH=../build/%{name}%{version}/js.jar:$(build-classpath xmlbeans/xbean 2>/dev/null)
%{javac} *.java
%{jar} cf ../build/%{name}%{version}/%{name}-examples.jar *.class
popd

%install
%mvn_install

# man page
mkdir -p %{buildroot}%{_mandir}/man1/
install -m 644 man/%{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

## script
mkdir -p %{buildroot}%{_bindir}
install -m 755 %{SOURCE2} %{buildroot}%{_bindir}/%{name}

# examples
cp -a build/%{name}%{version}/%{name}-examples.jar %{buildroot}%{_javadir}/%{name}-examples.jar
mkdir -p %{buildroot}%{_datadir}/%{name}
cp -a examples/* %{buildroot}%{_datadir}/%{name}
find %{buildroot}%{_datadir}/%{name} -name '*.build' -delete

%files -f .mfiles
%attr(0755,root,root) %{_bindir}/*
%{_javadir}/*
%{_mandir}/man1/%{name}.1*

%files demo
%{_datadir}/%{name}

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.7.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec 14 2020 Jerry James <loganjerry@gmail.com> - 1.7.7.1-13
- Change jline dep to jline2 and jansi dep to jansi1

* Sun Aug 30 2020 Fabio Valentini <decathorpe@gmail.com> - 1.7.7.1-12
- Remove unnecessary dependency on parent POM.

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.7.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 11 2020 Jiri Vanek <jvanek@redhat.com> - 1.7.7.1-10
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.7.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.7.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.7.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Aug 01 2018 Severin Gehwolf <sgehwolf@redhat.com> 1.7.7.1-6
- Add requirement on javapackages-tools since rhino script uses
  java-functions.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.7.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jun 16 2016 Alexander Kurtakov <akurtako@redhat.com> 1.7.7.1-1
- Update to version 1.7.7.1.

* Thu Jun 16 2016 Alexander Kurtakov <akurtako@redhat.com> 1.7.7-5
- Add BR javapackages-local to unbreak build.

* Wed Jun 15 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.7.7-4
- Install JAR and POM with %%mvn_install

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jul 28 2015 Alexander Kurtakov <akurtako@redhat.com> 1.7.7-2
- Fix launch script.

* Fri Jun 26 2015 Alexander Kurtakov <akurtako@redhat.com> 1.7.7-1
- Update to upstream 1.7.7 release.

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7R4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jun 10 2014 Alexander Kurtakov <akurtako@redhat.com> 1.7R4-10
- No longer ship javadoc subpackage and obsolete it.

* Tue Jun 10 2014 Alexander Kurtakov <akurtako@redhat.com> 1.7R4-9
- Use mfiles.

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7R4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Jan 14 2014 Mat??j Cepl <mcepl@redhat.com> - 1.7R4-7
- Add overlow detection patch from the upstream (RHBZ# 1011947)
- Update all patches.

* Mon Sep 09 2013 Elliott Baron <ebaron@redhat.com> 1.7R4-6
- Update and add missing options for Rhino shell man page.

* Thu Aug 29 2013 Alexander Kurtakov <akurtako@redhat.com> 1.7R4-5
- Drop R on java-devel  - rhbz #991706.

* Thu Aug 1 2013 akurtakov <akurtakov@localhost.localdomain> 1.7R4-4
- Add R on java-devel as rhino requires tools.jar at runtime.

* Mon Jun 24 2013 Elliott Baron <ebaron@redhat.com> 1.7R4-3
- Add man page for Rhino shell.

* Thu Feb 28 2013 Krzysztof Daniel <kdaniel@redhat.com> 1.7R4-2
- Add a depmap to keep compatibility with previous versions.

* Tue Feb 26 2013 Alexander Kurtakov <akurtako@redhat.com> 1.7R4-1
- Update to 1.7R4.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7R3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Nov  2 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.7R3-7
- Add maven POM

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7R3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 12 2012 Bill Nottingham - 1.7R3-5
- build against OpenJDK 1.7

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7R3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Oct 16 2011 Ville Skytt?? <ville.skytta@iki.fi> - 1.7R3-3
- Crosslink javadocs with Java's.
- Drop versioned jars and javadoc dir.
- Exclude patch backup files from -examples.

* Wed Sep 21 2011 Mat??j Cepl <mcepl@redhat.com> - 1.7R3-2
- Remove bea-stax-api dependency (and perl as well)

* Fri Sep 16 2011 Mat??j Cepl <mcepl@redhat.com> - 1.7R3-1
- Fix numbering of the package (this is not a prerelease)
- Remove unnecessary macros
- Increase happines of rpmlint (better Group tags)

* Wed Sep 14 2011 Mat??j Cepl <mcepl@redhat.com> - 1.7-0.10.r3
- New upstream pre-release.

* Wed Jul 6 2011 Andrew Overholt <overholt@redhat.com> 0:1.7-0.9.r2
- Inject OSGi metadata from Eclipse Orbit project.

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.7-0.8.r2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.7-0.7.r2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun May 31 2009 Toshio Kuratomi <toshio@fedoraproject.org> - 0:1.7-0.6.r2
- Update to rhino1_7R2
- Add patch from Steven Elliott to fix exception in the interpreter shell.

* Mon Apr 20 2009 Lillian Angel <langel@redhat.com> - 0:1.7-0.4.r2pre.1.1
- Added jpackage-utils requirement.
- Resolves: rhbz#496435

* Thu Mar 26 2009 Lillian Angel <langel@redhat.com> - 0:1.7-0.3.r2pre.1.1
- Updated rhino-build.patch
- License for treetable has been fixed. Re-included this code, and removed patch.
- Resolves: rhbz#457336

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.7-0.2.r2pre.1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 13 2009 Lillian Angel <langel@redhat.com> - 0:1.7-0.1.r2pre.1.1
- Upgraded to 1.7r2pre.
- Resolves: rhbz#485135

* Thu Jul 10 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0:1.6-0.1.r5.1.3
- drop repotag
- fix license tag

* Thu Mar 15 2007 Matt Wringe <mwringe@redhat.com> 0:1.6-0.1.r5.1jpp.2
- Remove script from build as the debugging tool is disabled due to it
  containing proprietary code from Sun.

* Wed Mar 07 2007 Deepak Bhole <dbhole@redhat.com> 0:1.6-0.1.r5.1jpp.1
- Upgrade to 1.6r5
- Change release per Fedora guidelines
- Disable dependency on xmlbeans (optional component, not in Fedora yet)
- Disable building of debugger tool, as it needs confidential code from Sun
- Remove post/postuns for javadoc and add the two dirs as %%doc

* Wed Jun 14 2006 Ralph Apel <r.apel@r-apel.de> 0:1.6-0.r2.2jpp
- Add bea-stax-api in order to build xmlimpl classes

* Wed May 31 2006 Fernando Nasser <fnasser@redhat.com> 0:1.6-0.r2.1jpp
- Upgrade to RC2

* Mon Apr 24 2006 Fernando Nasser <fnasser@redhat.com> 0:1.6-0.r1.2jpp
- First JPP 1.7 build

* Thu Dec 02 2004 David Walluck <david@jpackage.org> 0:1.6-0.r1.1jpp
- 1_6R1
- add demo subpackage containing example code
- add jpp release info to implementation version
- add script to launch js shell
- build E4X implementation (Requires: xmlbeans)
- remove `Class-Path' from manifest

* Tue Aug 24 2004 Fernando Nasser <fnasser@redhat.com> - 0:1.5-1.R5.1jpp
- Update to 1.5R5.
- Rebuild with Ant 1.6.2

* Sat Jul 19 2003 Ville Skytt?? <ville.skytta@iki.fi> - 0:1.5-1.R4.1.1jpp
- Update to 1.5R4.1.
- Non-versioned javadoc dir symlink.

* Fri Apr 11 2003 David Walluck <davdi@anti-microsoft.org> 0:1.5-0.R4.2jpp
- remove build patches in favor of perl
- add epoch

* Sun Mar 30 2003 Ville Skytt?? <ville.skytta@iki.fi> - 1.5-0.r4.1jpp
- Update to 1.5R4.
- Rebuild for JPackage 1.5.

* Wed May 08 2002 Guillaume Rousse <guillomovitch@users.sourceforge.net> 1.5-0.R3.1jpp
- 1.5R3
- versioned dir for javadoc

* Sun Mar 10 2002 Guillaume Rousse <guillomovitch@users.sourceforge.net> 1.5-0.R2.9jpp
- versioned compatibility symlink

* Mon Jan 21 2002 Guillaume Rousse <guillomovitch@users.sourceforge.net> 1.5-0.R2.8jpp
- section macro
- new release scheme

* Thu Jan 17 2002 Guillaume Rousse <guillomovitch@users.sourceforge.net> 1.5R2-7jpp
- spec cleanup
- changelog corrections

* Fri Jan 11 2002 2002 Guillaume Rousse <guillomovitch@users.sourceforge.net> 1.5R2-6jpp
- backward compatibility js.jar symlink
- used original swing exemples archive
- fixed javadoc empty package-list file
- no dependencies for manual and javadoc packages

* Sat Dec 1 2001 Guillaume Rousse <guillomovitch@users.sourceforge.net> 1.5R2-5jpp
- javadoc in javadoc package
- fixed offline build

* Wed Nov 21 2001 Christian Zoffoli <czoffoli@littlepenguin.org> 1.5R2-4jpp
- changed extension --> jpp

* Sat Oct 6 2001 Guillaume Rousse <guillomovitch@users.sourceforge.net> 1.5R2-3jpp
- first unified release
- s/jPackage/JPackage
- corrected license to MPL

* Sat Sep 15 2001 Guillaume Rousse <guillomovitch@users.sourceforge.net> 1.5R2-2mdk
- spec cleanup
- standardized cvs references

* Fri Aug 31 2001 Guillaume Rousse <guillomovitch@users.sourceforge.net> 1.5R2-1mdk
- first Mandrake release
