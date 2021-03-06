Name:           maven-dependency-analyzer
Version:        1.11.3
Release:        2%{?dist}
Summary:        Maven dependency analyzer
License:        ASL 2.0

URL:            https://maven.apache.org/shared/maven-dependency-analyzer/
Source0:        https://repo1.maven.org/maven2/org/apache/maven/shared/%{name}/%{version}/%{name}-%{version}-source-release.zip

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(commons-io:commons-io)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.commons:commons-lang3)
BuildRequires:  mvn(org.apache.maven.plugin-testing:maven-plugin-testing-tools)
BuildRequires:  mvn(org.apache.maven:maven-artifact)
BuildRequires:  mvn(org.apache.maven:maven-model)
BuildRequires:  mvn(org.apache.maven:maven-project)
BuildRequires:  mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires:  mvn(org.apache.maven.shared:maven-shared-components:pom:)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-annotations)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-metadata)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  mvn(org.ow2.asm:asm) >= 8.0.0

%description
Analyzes the dependencies of a project for undeclared or unused artifacts.

Warning: Analysis is not done at source but bytecode level, then some cases are
not detected (constants, annotations with source-only retention, links in
javadoc) which can lead to wrong result if they are the only use of a
dependency.


%package javadoc
Summary:        API documentation for %{name}

%description javadoc
%{summary}


%prep
%setup -q

# missing maven-artifact dependency in tests:
# org.apache.maven.artifact.handler.DefaultArtifactHandler
%pom_add_dep org.apache.maven:maven-artifact:3.6.0:test

# failing test in our build environment
rm src/test/java/org/apache/maven/shared/dependency/analyzer/DefaultProjectDependencyAnalyzerTest.java


%build
%mvn_build


%install
%mvn_install


%files -f .mfiles
%dir %{_javadir}/%{name}
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE


%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Aug 26 2020 Fabio Valentini <decathorpe@gmail.com> - 1.11.3-1
- Update to version 1.11.3.

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 1.11.1-3
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Aug 18 2019 Fabio Valentini <decathorpe@gmail.com> - 1.11.1-1
- Update to version 1.11.1.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 30 2018 Marian Koncek <mkoncek@redhat.com> - 1.10-1
- Update to upstream version 1.10

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 26 2018 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.8-1
- Update to upstream version 1.8

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu May 04 2017 Michael Simacek <msimacek@redhat.com> - 1.7-1
- Update to upstream version 1.7

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jun 15 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.6-4
- Add missing build-requires
- Remove old obsoletes/provides

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Feb 04 2015 Michal Srb <msrb@redhat.com> - 1.6-1
- Update to upstream version 1.6

* Mon Sep 15 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.5-1
- Update to upstream version 1.5

* Mon Aug  4 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4-6
- Fix build-requires on parent POM

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Mar 04 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.4-4
- Use Requires: java-headless rebuild (#1067528)

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4-3
- Fix unowned directory

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue May 21 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4-1
- Update to upstream version 1.4

* Tue Feb 19 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.3-7
- Build with xmvn

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.3-5
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Tue Jan 22 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.3-4
- Replace asm2 R with objectweb-asm
- Resolves: rhbz#902641

* Fri Dec 21 2012 Tomas Radej <tradej@redhat.com> - 1.3-3
- Added missing Provides/Obsoletes

* Thu Dec 20 2012 Tomas Radej <tradej@redhat.com> - 1.3-2
- Removed xmvn + reworked building without it

* Tue Dec 18 2012 Tomas Radej <tradej@redhat.com> - 1.3-1
- Initial package

