Name:           junit
Epoch:          1
Version:        4.13
Release:        3%{?dist}
Summary:        Java regression test package
License:        EPL-1.0
URL:            http://www.junit.org/
BuildArch:      noarch

# ./clean-tarball.sh %%{version}
Source0:        %{name}4-%{version}-clean.tar.gz
Source3:        create-tarball.sh

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires:  mvn(org.hamcrest:hamcrest-core)
BuildRequires:  mvn(org.hamcrest:hamcrest-library)

Obsoletes:      %{name}-demo < 4.12

%description
JUnit is a regression testing framework written by Erich Gamma and Kent Beck. 
It is used by the developer who implements unit tests in Java. JUnit is Open
Source Software, released under the Common Public License Version 1.0 and 
hosted on GitHub.

%package manual
Summary:        Manual for %{name}

%description manual
Documentation for %{name}.

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
Javadoc for %{name}.

%prep
%autosetup -n %{name}4-r%{version}

%pom_remove_plugin :replacer
sed s/@version@/%{version}/ src/main/java/junit/runner/Version.java.template >src/main/java/junit/runner/Version.java

%pom_remove_plugin :animal-sniffer-maven-plugin

# Removing hamcrest source jar references (not available and/or necessary)
%pom_remove_plugin :maven-javadoc-plugin

# Add proper Apache Felix Bundle Plugin instructions
# so that we get a reasonable OSGi manifest.
%pom_xpath_inject pom:project "<packaging>bundle</packaging>"
%pom_xpath_inject pom:build/pom:plugins "
    <plugin>
      <groupId>org.apache.felix</groupId>
      <artifactId>maven-bundle-plugin</artifactId>
      <extensions>true</extensions>
      <configuration>
        <instructions>
          <Bundle-SymbolicName>org.junit</Bundle-SymbolicName>
          <Export-Package>{local-packages},!org.hamcrest*,*;x-internal:=true</Export-Package>
          <_nouses>true</_nouses>
        </instructions>
      </configuration>
    </plugin>"

# Use compiler release flag when building on JDK >8 for correct cross-compiling
%pom_xpath_inject pom:profiles "
    <profile>
      <id>jdk-release-flag</id>
      <activation>
        <jdk>[9,)</jdk>
      </activation>
      <properties>
        <maven.compiler.release>\${jdkVersion}</maven.compiler.release>
      </properties>
    </profile>"

%pom_xpath_set //pom:compilerVersion 1.8

%mvn_file : %{name}

%build
%mvn_build -- -DjdkVersion=8

%install
%mvn_install

%files -f .mfiles
%license LICENSE-junit.txt
%doc README.md

%files javadoc -f .mfiles-javadoc
%license LICENSE-junit.txt

%files manual
%license LICENSE-junit.txt
%doc doc/*

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Aug 16 2020 Fabio Valentini <decathorpe@gmail.com> - 1:4.13-2
- Bump release to account for previously untagged 4.13-1.fc33 build.

* Thu Aug 13 2020 Jerry James <loganjerry@gmail.com> - 1:4.13-1
- Update to upstream version 4.13

* Tue Aug 04 2020 Mat Booth <mat.booth@redhat.com> - 1:4.12-18
- Add automatic module name

* Tue Aug 04 2020 Mat Booth <mat.booth@redhat.com> - 1:4.12-17
- Allow building on Java 11

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.12-16
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.12-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 1:4.12-14
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.12-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.12-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.12-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.12-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul  2 2018 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:4.12-9
- Update license tag

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.12-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.12-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jul 15 2016 Mat Booth <mat.booth@redhat.com> - 1:4.12-5
- Add missing BR

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:4.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jan 21 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:4.12-2
- Export internal OSGi packages and mark them with x-internal
- Resolves: rhbz#1184144

* Mon Jan 19 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:4.12-1
- Update to upstream version 4.12
- Build with Maven
- Remove demo package

* Mon Jun  9 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:4.11-14
- Add epoch as workaround for a bug in koji-shadow

* Mon Jun  9 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 4.11-13
- Remove epoch

* Sun Jun  8 2014 Peter Robinson <pbrobinson@fedoraproject.org> 4.11-12
- Re-add Epoch. Once you have it you can't remove it as it breaks upgrade paths

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.11-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 22 2014 Alexander Kurtakov <akurtako@redhat.com> 4.11-10
- Update OSGi manifest to state 4.11.

* Wed May 21 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 4.11-9
- Update to current packaging guidelines
- Drop old Obsoletes/Provides for junit4 rename
- Disable test which fails with Java 8

* Tue Mar 04 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0:4.11-8
- Use Requires: java-headless rebuild (#1067528)

* Fri Aug 23 2013 Michal Srb <msrb@redhat.com> - 0:4.11-7
- Drop "-SNAPSHOT" from version ID
- See: https://lists.fedoraproject.org/pipermail/java-devel/2013-August/004923.html

* Mon Aug 19 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0:4.11-6
- Fix version in pom.xml (#998266)

* Fri Aug 02 2013 Michal Srb <msrb@redhat.com> - 0:4.11-5
- Add create-tarball.sh script to SRPM

* Fri Jun 28 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:4.11-4
- Rebuild to regenerate API documentation
- Resolves: CVE-2013-1571

* Fri Jun 21 2013 Michal Srb <msrb@redhat.com> - 0:4.11-3
- Build from clean tarball

* Mon May 06 2013 Tomas Radej <tradej@redhat.com> - 0:4.11-2
- Removed uneeded dependencies

* Thu Mar 21 2013 Tomas Radej <tradej@redhat.com> - 0:4.11-1
- Updated to latest upstream version

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:4.10-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Dec 18 2012 Michal Srb <msrb@redhat.com> - 0:4.10-7
- Build-time dependency perl-MD5 replaced with perl(Digest::MD5)
- Description cleanup (Resolves: #888389)

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:4.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Apr 30 2012 Krzysztof Daniel <kdaniel@redhat.com> 0:4.10-5
- Update OSGi metadata to match 4.10.0 release.

* Thu Feb 09 2012 Harald Hoyer <harald@redhat.com> 4.10-4
- removed Conflicts with itsself

* Thu Jan 26 2012 Roland Grunberg <rgrunber@redhat.com> 0:4.8.2-3
- Add OSGi metadata to junit.jar manifest.

* Thu Jan 26 2012 Tomas Radej <tradej@redhat.com> - 0:4.10-2
- Fixed versioning

* Wed Jan 25 2012 Tomas Radej <tradej@redhat.com> - 0:4.10-1
- Updated to upstream 4.10
- Obsoleted junit4
- Epoch added

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.8.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.8.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Oct 7 2010 Alexander Kurtakov <akurtako@redhat.com> 3.8.2-7
- Drop gcj support.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.8.2-6.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.8.2-5.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Jul  9 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 3.8.2-4.4
- drop repotag

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 3.8.2-4jpp.3
- Autorebuild for GCC 4.3

* Thu Sep 20 2007 Deepak Bhole <dbhole@redhat.com> - 3.8.2-3jpp.3
- Fix location of stylesheet for javadocs

* Thu Sep 20 2007 Deepak Bhole <dbhole@redhat.com> - 3.8.2-3jpp.2
- Rebuild for ppc32 execmem issue and new build-id

* Mon Feb 12 2007 Thomas Fitzsimmons <fitzsim@redhat.com> - 3.8.2-3jpp.1.fc7
- Add dist tag

* Mon Feb 12 2007 Thomas Fitzsimmons <fitzsim@redhat.com> - 3.8.2-3jpp.1
- Committed on behalf of Tania Bento <tbento@redhat.com>
- Update per Fedora review process
- Resolves rhbz#225954

* Thu Aug 10 2006 Deepak Bhole <dbhole@redhat.com> -  0:3.8.2-3jpp.1
- Added missing requirements.

* Thu Aug 10 2006 Karsten Hopp <karsten@redhat.de> 0:3.8.2-2jpp_3fc
- Require(post/postun): coreutils

* Fri Jun 23 2006 Deepak Bhole <dbhole@redhat.com> -  0:3.8.2-2jpp_2fc
- Rebuilt.

* Thu Jun 22 2006 Deepak Bhole <dbhole@redhat.com> -  0:3.8.2-2jpp_1fc
- Upgrade to 3.8.2
- Added conditional native compilation.
- Fix path where demo is located.

* Fri Mar 03 2006 Ralph Apel <r.apel at r-apel.de> - 0:3.8.2-1jpp
- First JPP-1.7 release

* Mon Aug 23 2004 Randy Watler <rwatler at finali.com> - 0:3.8.1-4jpp
- Rebuild with ant-1.6.2
* Fri May 09 2003 David Walluck <david@anti-microsoft.org> 0:3.8.1-3jpp
- update for JPackage 1.5

* Fri Mar 21 2003 Nicolas Mailhot <Nicolas.Mailhot (at) JPackage.org> 3.8.1-2jpp
- For jpackage-utils 1.5

* Fri Sep 06 2002 Henri Gomez <hgomez@users.sourceforge.net> 3.8.1-1jpp
- 3.8.1

* Sun Sep 01 2002 Guillaume Rousse <guillomovitch@users.sourceforge.net> 3.8-2jpp 
- used original zip file

* Thu Aug 29 2002 Guillaume Rousse <guillomovitch@users.sourceforge.net> 3.8-1jpp 
- 3.8
- group, vendor and distribution tags

* Sat Jan 19 2002 Guillaume Rousse <guillomovitch@users.sourceforge.net> 3.7-6jpp
- versioned dir for javadoc
- no dependencies for manual and javadoc packages
- stricter dependency for demo package
- additional sources in individual archives
- section macro

* Sat Dec 1 2001 Guillaume Rousse <guillomovitch@users.sourceforge.net> 3.7-5jpp
- javadoc in javadoc package

* Wed Nov 21 2001 Christian Zoffoli <czoffoli@littlepenguin.org> 3.7-4jpp
- fixed previous releases ...grrr

* Wed Nov 21 2001 Christian Zoffoli <czoffoli@littlepenguin.org> 3.7-3jpp
- added jpp extension
- removed packager tag

* Sun Sep 30 2001 Guillaume Rousse <guillomovitch@users.sourceforge.net> 3.7-2jpp
- first unified release
- s/jPackage/JPackage

* Mon Sep 17 2001 Guillaume Rousse <guillomovitch@users.sourceforge.net> 3.7-1mdk
- 3.7
- vendor tag
- packager tag
- s/Copyright/License/
- truncated description to 72 columns in spec
- spec cleanup
- used versioned jar
- moved demo files to %%{_datadir}/%%{name}

* Sat Feb 17 2001 Guillaume Rousse <g.rousse@linux-mandrake.com> 3.5-1mdk
- first Mandrake release