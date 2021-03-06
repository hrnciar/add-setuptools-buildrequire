Name:           maven-resolver
Epoch:          1
Version:        1.4.2
Release:        5%{?dist}
Summary:        Apache Maven Artifact Resolver library
License:        ASL 2.0

URL:            https://maven.apache.org/resolver/
Source0:        https://archive.apache.org/dist/maven/resolver/%{name}-%{version}-source-release.zip

# keep deprecated and removed aether CacheUtils for a while longer
# some packages still depend on this and things break without it
Patch0:         00-keep-deprecated-aether-CacheUtils.patch

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(javax.inject:javax.inject)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.httpcomponents:httpclient)
BuildRequires:  mvn(org.apache.httpcomponents:httpcore)
BuildRequires:  mvn(org.apache.maven:maven-parent:pom:)
BuildRequires:  mvn(org.apache.maven.wagon:wagon-provider-api)
BuildRequires:  mvn(org.codehaus.plexus:plexus-classworlds)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  mvn(org.eclipse.sisu:org.eclipse.sisu.inject)
BuildRequires:  mvn(org.eclipse.sisu:org.eclipse.sisu.plexus)
BuildRequires:  mvn(org.eclipse.sisu:sisu-maven-plugin)
BuildRequires:  mvn(org.hamcrest:hamcrest-core)
BuildRequires:  mvn(org.mockito:mockito-core)
BuildRequires:  mvn(org.slf4j:jcl-over-slf4j)
BuildRequires:  mvn(org.slf4j:slf4j-api)
BuildRequires:  mvn(org.slf4j:slf4j-simple)
BuildRequires:  mvn(org.sonatype.sisu:sisu-guice::no_aop:)

%description
Apache Maven Artifact Resolver is a library for working with artifact
repositories and dependency resolution. Maven Artifact Resolver deals with the
specification of local repository, remote repository, developer workspaces,
artifact transports and artifact resolution.

%package api
Summary:   Maven Artifact Resolver API

%description api
The application programming interface for the repository system.

%package spi
Summary:   Maven Artifact Resolver SPI

%description spi
The service provider interface for repository system implementations and
repository connectors.

%package util
Summary:   Maven Artifact Resolver Utilities

%description util
A collection of utility classes to ease usage of the repository system.

%package impl
Summary:   Maven Artifact Resolver Implementation

%description impl
An implementation of the repository system.

%package test-util
Summary:   Maven Artifact Resolver Test Utilities

%description test-util
A collection of utility classes to ease testing of the repository system.

%package connector-basic
Summary:   Maven Artifact Resolver Connector Basic

%description connector-basic
A repository connector implementation for repositories using URI-based layouts.

%package transport-classpath
Summary:   Maven Artifact Resolver Transport Classpath

%description transport-classpath
A transport implementation for repositories using classpath:// URLs.

%package transport-file
Summary:   Maven Artifact Resolver Transport File

%description transport-file
A transport implementation for repositories using file:// URLs.

%package transport-http
Summary:   Maven Artifact Resolver Transport HTTP

%description transport-http
A transport implementation for repositories using http:// and https:// URLs.

%package transport-wagon
Summary:   Maven Artifact Resolver Transport Wagon

%description transport-wagon
A transport implementation based on Maven Wagon.

%package        javadoc
Summary:        API documentation for %{name}

%description    javadoc
This package provides %{summary}.


%prep
%setup -q
%patch0 -p1

# tests require jetty 7
%pom_remove_dep :::test maven-resolver-transport-http
rm -r maven-resolver-transport-http/src/test

%pom_disable_module maven-resolver-demos

# generate OSGi manifests
for pom in $(find -mindepth 2 -name pom.xml) ; do
  %pom_add_plugin "org.apache.felix:maven-bundle-plugin" $pom \
  "<configuration>
    <instructions>
      <Bundle-SymbolicName>\${project.groupId}$(sed 's:./maven-resolver::;s:/pom.xml::;s:-:.:g' <<< $pom)</Bundle-SymbolicName>
      <Export-Package>!org.eclipse.aether.internal*,org.eclipse.aether*</Export-Package>
      <_nouses>true</_nouses>
    </instructions>
  </configuration>
  <executions>
    <execution>
      <id>create-manifest</id>
      <phase>process-classes</phase>
      <goals><goal>manifest</goal></goals>
    </execution>
  </executions>"
done
%pom_add_plugin "org.apache.maven.plugins:maven-jar-plugin" pom.xml \
"<configuration>
  <archive>
    <manifestFile>\${project.build.outputDirectory}/META-INF/MANIFEST.MF</manifestFile>
  </archive>
</configuration>"

%mvn_package :maven-resolver
%mvn_alias 'org.apache.maven.resolver:maven-resolver{*}' 'org.eclipse.aether:aether@1'
%mvn_file ':maven-resolver{*}' %{name}/maven-resolver@1 aether/aether@1

%build
%mvn_build -s -- -Dmaven.compiler.release=8

%install
%mvn_install


%files -f .mfiles
%license LICENSE NOTICE

%files api -f .mfiles-%{name}-api
%license LICENSE NOTICE
%files spi -f .mfiles-%{name}-spi
%files util -f .mfiles-%{name}-util
%files impl -f .mfiles-%{name}-impl
%files test-util -f .mfiles-%{name}-test-util
%files connector-basic -f .mfiles-%{name}-connector-basic
%files transport-classpath -f .mfiles-%{name}-transport-classpath
%files transport-file -f .mfiles-%{name}-transport-file
%files transport-http -f .mfiles-%{name}-transport-http
%files transport-wagon -f .mfiles-%{name}-transport-wagon

%files javadoc -f .mfiles-javadoc
%license LICENSE NOTICE

%changelog
* Wed Feb 17 2021 Fabio Valentini <decathorpe@gmail.com> - 1:1.4.2-5
- Build with -release 8 for better OpenJDK 8 compatibility.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 1:1.4.2-2
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Sat May 09 2020 Fabio Valentini <decathorpe@gmail.com> - 1:1.4.2-1
- Update to version 1.4.2.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Nov 03 2019 Fabio Valentini <decathorpe@gmail.com> - 1:1.4.1-1
- Update to version 1.4.1.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 14 2019 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:1.3.3-1
- Update to upstream version 1.3.3

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 23 2018 Marian Koncek <mkoncek@redhat.com> - 1:1.3.1-1
- Update to upstream version 1.3.1

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Apr 18 2018 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:1.1.1-2
- Remove aether provides

* Mon Feb 26 2018 Michael Simacek <msimacek@redhat.com> - 1:1.1.1-1
- Update to upstream version 1.1.1

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Nov 27 2017 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:1.1.0-2
- Obsolete aether-ant-tasks
- Resolves: rhbz#1516043

* Wed Oct 25 2017 Michael Simacek <msimacek@redhat.com> - 1:1.1.0-1
- Update to upstream version 1.1.0

* Thu Aug 24 2017 Mat Booth <mat.booth@redhat.com> - 1:1.0.3-7
- Fix OSGi metadata to also export "impl" packages; "internal" packages remain
  unexported

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed May 24 2017 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:1.0.3-5
- Add aether alias for main POM file

* Tue May 23 2017 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:1.0.3-4
- Fix duplicate Bundle-SymbolicName in OSGi manifests

* Mon May 15 2017 Mat Booth <mat.booth@redhat.com> - 1:1.0.3-3
- Restore OSGi metadata that was lost in the switch from "aether" to
  "maven-resolver"

* Wed Apr 12 2017 Michael Simacek <msimacek@redhat.com> - 1:1.0.3-2
- Split into subpackages
- Obsolete and provide aether

* Tue Apr 11 2017 Michael Simacek <msimacek@redhat.com> - 1.0.3-1
- Initial packaging
