%bcond_with     equinox
%bcond_with     groovy

Name:           xbean
Summary:        Java plugin based web server
Version:        4.15
Release:        7%{?dist}
License:        ASL 2.0

URL:            http://geronimo.apache.org/xbean/
Source0:        http://repo2.maven.org/maven2/org/apache/%{name}/%{name}/%{version}/%{name}-%{version}-source-release.zip

# Compatibility with Eclipse Luna (rhbz#1087461)
Patch1:         0002-Port-to-Eclipse-Luna-OSGi.patch
Patch2:         0003-Port-to-QDox-2.0.patch

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(commons-logging:commons-logging-api)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.logging.log4j:log4j-1.2-api)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(org.osgi:osgi.core)
BuildRequires:  mvn(org.ow2.asm:asm)
BuildRequires:  mvn(org.ow2.asm:asm-commons)
BuildRequires:  mvn(org.slf4j:slf4j-api)

%if %{with equinox}
BuildRequires:  mvn(org.eclipse:osgi)
%endif

%if %{with groovy}
BuildRequires:  mvn(org.codehaus.groovy:groovy-all)
%endif

%description
The goal of XBean project is to create a plugin based server
analogous to Eclipse being a plugin based IDE. XBean will be able to
discover, download and install server plugins from an Internet based
repository. In addition, we include support for multiple IoC systems,
support for running with no IoC system, JMX without JMX code,
lifecycle and class loader management, and a rock solid Spring
integration.


%package        javadoc
Summary:        API documentation for %{name}

%description    javadoc
This package provides %{summary}.


%prep
%setup -q
# build failing on this due to doxia-sitetools problems
rm src/site/site.xml

%if %{with equinox}
%patch1 -p1
%endif
%patch2 -p1

%pom_remove_parent
%pom_remove_dep mx4j:mx4j

# use osgi-core instead of felix-osgi-core
%pom_change_dep -r :org.osgi.core org.osgi:osgi.core

# switch from log4j 1.2 compat package to log4j 1.2 API shim
%pom_change_dep -r log4j:log4j org.apache.logging.log4j:log4j-1.2-api

# Unshade ASM
%pom_remove_dep -r :xbean-asm7-shaded
%pom_remove_dep -r :xbean-finder-shaded
%pom_disable_module xbean-asm7-shaded
%pom_disable_module xbean-finder-shaded
%pom_add_dep org.apache.xbean:xbean-asm-util:%{version} xbean-reflect
%pom_xpath_remove pom:optional xbean-reflect xbean-asm-util
%pom_xpath_remove 'pom:scope[text()="provided"]' xbean-reflect xbean-asm-util
sed -i 's/org\.apache\.xbean\.asm7/org.objectweb.asm/g' `find xbean-reflect -name '*.java'`

# Springframework is not available in Fedora
%pom_remove_dep org.springframework:
%pom_disable_module xbean-blueprint
%pom_disable_module xbean-classloader
%pom_disable_module xbean-spring
%pom_disable_module maven-xbean-plugin

# Disable uneeded modules that cannot be built on JDK 11
%pom_disable_module xbean-classpath

# Disable one test that fails on JDK 11
sed -i '/testGetBytecode/i@org.junit.Ignore' xbean-finder/src/test/java/org/apache/xbean/finder/archive/MJarJarArchiveTest.java

# Unused import which is not available in OpenJDK 11
# Forwarded upstream: https://issues.apache.org/jira/browse/XBEAN-329
# Accepted upstream: https://svn.apache.org/viewvc?view=revision&revision=1887532
sed -i '/import com.sun.org.apache.regexp.internal.RE/d' xbean-reflect/src/main/java/org/apache/xbean/propertyeditor/PropertyEditors.java

%if %{without equinox}
  %pom_remove_dep :xbean-bundleutils xbean-finder
  rm -r xbean-finder/src/main/java/org/apache/xbean/finder{,/archive}/Bundle*
  %pom_disable_module xbean-bundleutils
%endif

%if %{without groovy}
%pom_disable_module xbean-telnet
%endif

# maven-xbean-plugin invocation makes no sense as there are no namespaces
%pom_remove_plugin :maven-xbean-plugin xbean-classloader

# Remove plugins useful for upstream only.
%pom_remove_plugin :apache-rat-plugin
%pom_remove_plugin :maven-source-plugin


%build
%mvn_build


%install
%mvn_install


%files -f .mfiles
%license LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%license LICENSE NOTICE


%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.15-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Sep 09 2020 Fabio Valentini <decathorpe@gmail.com> - 4.15-6
- Switch from log4j 1.2 compat package to log4j 1.2 API shim.

* Wed Jul 29 2020 Mat Booth <mat.booth@redhat.com> - 4.15-5
- Remove springframework conditionals, the deps are a long time removed from
  Fedora and this simplifies the spec a bit
- Disable unused modules that can't build on JDK 11

* Sat Jul 11 2020 Jiri Vanek <jvanek@redhat.com> - 4.15-4
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Thu Jun 25 2020 Jeff Johnston <jjohnstn@redhat.com> - 4.15-3
- Fix JVM as 1.8.0 as package cannot be built with Java 9 and above

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 13 2019 Fabio Valentini <decathorpe@gmail.com> - 4.15-1
- Update to version 4.15.

* Wed Sep 18 2019 Fabio Valentini <decathorpe@gmail.com> - 4.14-2
- Migrate from the obsolete felix-osgi-core to osgi-core.

* Tue Aug 20 2019 Fabio Valentini <decathorpe@gmail.com> - 4.14-1
- Update to version 4.14.

* Sun Jul 28 2019 Fabio Valentini <decathorpe@gmail.com> - 4.9-5
- Disable support for spring and groovy.

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 09 2019 Fabio Valentini <decathorpe@gmail.com> - 4.9-3
- Disable eclipse equinox functionality to fix the FTBFS issue on 32bit arches.

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Aug 07 2018 Michael Simacek <msimacek@redhat.com> - 4.9-1
- Update to upstream version 4.9

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Apr 19 2018 Michael Simacek <msimacek@redhat.com> - 4.8-1
- Update to upstream version 4.8

* Tue Mar 13 2018 Michael Simacek <msimacek@redhat.com> - 4.6-1
- Update to upstream version 4.6

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb  1 2017 Mikolaj Izdebski <mizdebsk@redhat.com> - 4.5-6
- Introduce groovy build conditional

* Wed Feb 01 2017 Michael Simacek <msimacek@redhat.com> - 4.5-5
- Fix build with conditionals

* Wed Feb 01 2017 Michael Simacek <msimacek@redhat.com> - 4.5-4
- Port to current QDox

* Thu Jun 16 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 4.5-3
- Add missing build-requires

* Thu May 12 2016 Michael Simacek <msimacek@redhat.com> - 4.5-2
- Enable xbean-asm-util

* Mon May 02 2016 Michael Simacek <msimacek@redhat.com> - 4.5-1
- Update to upstream version 4.5

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 24 2015 Michael Simacek <msimacek@redhat.com> - 4.4-1
- Update to upstream version 4.4
- Rebase patches
- Remove obsolete groovy patch

* Mon Jul 13 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 4.3-1
- Update to upstream version 4.3

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Apr  1 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 4.2-1
- Update to upstream version 4.2

* Thu Feb  5 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 4.1-2
- Fix patch unshading ASM

* Fri Nov 21 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 4.1-1
- Update to upstream version 4.1

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Apr 14 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.17-1
- Update to upstream version 3.17
- Add patch for Eclipse Luna

* Thu Dec  5 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.16-1
- Update to upstream version 3.16

* Thu Aug 08 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 3.13-4
- Update to latest packaging guidelines

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Apr 29 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.13-2
- Remove unneeded BR: maven-idea-plugin

* Fri Mar 15 2013 Michal Srb <msrb@redhat.com> - 3.13-1
- Update to upstream version 3.13

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 3.12-5
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Mon Dec 17 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.12-4
- Enable xbean-spring, resolves rhbz#887496
- Disable xbean-blueprint due to FTBFS

* Mon Oct 22 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.12-3
- Replace eclipse-rcp requires with eclipse-equinox-osgi
- Reenable Equinox

* Tue Oct 16 2012 gil cattaneo <puntogil@libero.it> - 3.12-2
- Enable xbean-blueprint and xbean-classloader modules

* Wed Oct 10 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.12-1
- Update to upstream version 3.12

* Wed Oct 10 2012 Krzysztof Daniel <kdaniel@redhat.com> 3.11.1-8
- Revert previous changes.

* Wed Oct 10 2012 Krzysztof Daniel <kdaniel@redhat.com> 3.11.1-7
- Disable parts dependent on Eclipse (for bootstraping purpose).

* Wed Oct 10 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.11.1-6
- Implement equinox and spring conditionals

* Mon Sep  3 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.11.1-5
- Fix eclipse requires

* Mon Aug 27 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.11.1-4
- Fix felix-framework enabling patch

* Mon Aug  6 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.11.1-3
- Enable xbean-spring
- Enable maven-xbean-plugin
- Remove RPM bug workaround

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.11.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jul 13 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.11.1-1
- Update to the upstream version 3.11.1
- Force use of Equinox instead of Felix
- Convert patch to POM macros

* Thu May  3 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 3.8-5
- Remove mx4j from deps (javax.management provided by JDK 1.5+)

* Tue Apr 24 2012 Alexander Kurtakov <akurtako@redhat.com> 3.8-4
- BR felix-framework instead of felix-osgi-core.

* Tue Apr 24 2012 Alexander Kurtakov <akurtako@redhat.com> 3.8-3
- Do not build equinox specific parts for RHEL.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec  6 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 3.8-1
- Update to latest upstream version
- Build with maven 3
- Packaging & guidelines fixes

* Sat May 28 2011 Marek Goldmann <mgoldman@redhat.com> - 3.7-7
- Added xbean-finder and xbean-bundleutils submodules

* Fri Mar  4 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 3.7-6
- Add comment for removing javadoc
- Fix maven 3 build

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Dec  6 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 3.7-4
- Fix pom filename (Resolves rhbz#655827)
- Add depmap for main pom file
- Fixes according to new guidelines (versionless jars, javadocs)

* Fri Jul 30 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 3.7-3
- Use javadoc:aggregate to generate javadocs

* Fri Jul  9 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 3.7-2
- Add license to javadoc subpackage

* Mon Jun 21 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 3.7-1
- First release

