Name:			antlr-maven-plugin
Version:		2.2
Release:		29%{?dist}
Summary:		Maven plugin that generates files based on grammar file(s)
License:		ASL 2.0
URL:			http://mojo.codehaus.org/antlr-maven-plugin/

Source0:		http://repo1.maven.org/maven2/org/codehaus/mojo/%{name}/%{version}/%{name}-%{version}-source-release.zip

# Modern modello expects to see <models></models>, even if there is only one.
Patch0:			maven-antlr-plugin-2.2-modello-issue.patch
# siteRenderer.createSink doesn't exist anymore
Patch2:			maven-antlr-plugin-2.1-sinkfix.patch
# Fix grammar processing bug (bz 1020312)
Patch3:			0001-MANTLR-34-Fix-NPE-when-building-Jenkins.patch

BuildArch:		noarch

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.commons:commons-exec)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven:maven-project)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven.reporting:maven-reporting-impl)
BuildRequires:  mvn(org.apache.maven.shared:maven-plugin-testing-harness)
BuildRequires:  mvn(org.apache.maven.wagon:wagon-provider-api)
BuildRequires:  mvn(org.codehaus.modello:modello-maven-plugin)
BuildRequires:  mvn(org.codehaus.mojo:mojo-parent:pom:)
BuildRequires:  mvn(org.codehaus.plexus:plexus-i18n)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)

%description
The Antlr Plugin has two goals:
- antlr:generate Generates file(s) to a target directory based on grammar
  file(s).
- antlr:html Generates Antlr report for grammar file(s).

%package javadoc
Summary:		Javadocs for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q
%patch0 -p1 -b .modello
%patch2 -b .sink
%patch3 -p1 -b .fixnpe

# reporting eventually pulls in another antlr and we'd break with weird errors
%pom_xpath_inject "pom:dependency[pom:artifactId[text()='maven-reporting-impl']]/pom:exclusions" "
        <exclusion>
            <groupId>antlr</groupId>
            <artifactId>antlr</artifactId>
        </exclusion>"

# remove all binary bits
find -name '*.class' -exec rm -f '{}' \;
find -name '*.jar' -exec rm -f '{}' \;

%mvn_file : %{name}

%build
%mvn_build --xmvn-javadoc -- -Dmaven.test.skip=true

%install
%mvn_install

%files -f .mfiles

%files javadoc -f .mfiles-javadoc

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 2.2-27
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Thu Jun 18 2020 Tom Callaway <spot@fedoraproject.org> - 2.2-26
- fix javadoc

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jul 15 2016 Michael Simacek <msimacek@redhat.com> - 2.2-18
- Regenerate buildrequires

* Mon Jun 20 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.2-17
- Add missing build-requires

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Mat Booth <mat.booth@redhat.com> - 2.2-15
- Fix FTBFS
- Remove ancient provides/obsoletes

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Oct 18 2013 Tom Callaway <spot@fedoraproject.org> - 2.2-12
- Fix grammar processing bug (bz 1020312)
  Thanks to Michal Srb

* Sat Aug 24 2013 Mat Booth <fedora@matbooth.co.uk> - 2.2-11
- Remove unneeded BR on maven2-common-poms
- Update for newer guidelines

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Mar 04 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.2-9
- Add dependency exclusion for antlr (#911054)

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 2.2-7
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Dec 05 2011 Tomas Radej <tradej@redhat.com> - 2.2-4
- Modello + maven-enforcer-plugin BR
- Guideline fixes

* Thu Apr 28 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.2-3
- Add apache-commons-exec to R

* Wed Mar 9 2011 Alexander Kurtakov <akurtako@redhat.com> 2.2-2
- Build with maven 3.
- Use upstream sources.
- Adapt to current guidelines.

* Thu Mar  3 2011 Tom Callaway <spot@fedoraproject.org> 2.2-1.20110307svn13719
- update to 2.2 tag

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-4.20101012svn12849
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Oct 13 2010 Tom "spot" Callaway <tcallawa@redhat.com> 2.1-3.20101012svn12849
- fix provides/obsoletes to replace old (dead) package
- don't own mavendepmapfragdir, just the files inside it
- don't set buildarch on javadoc (entire package is noarch already)

* Wed Oct 13 2010 Tom "spot" Callaway <tcallawa@redhat.com> 2.1-2.20101012svn12849
- add post/postun
- fix pom filename
- svn export
- comment patchset
- provides for maven-antlr-plugin
- drop unnecessary symlinks
- use maven macros

* Tue Oct 12 2010 Tom "spot" Callaway <tcallawa@redhat.com> 2.1-1.20101012svn12849
- initial package
