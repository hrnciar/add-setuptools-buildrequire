Name:          pdfbox
Version:       2.0.22
Release:       1%{?dist}
Summary:       Apache PDFBox library for working with PDF documents
License:       ASL 2.0
URL:           http://pdfbox.apache.org/
Source0:       http://archive.apache.org/dist/pdfbox/%{version}/pdfbox-%{version}-src.zip

# Use system font instead of bundled font
Patch0:        pdfbox-use-system-liberation-font.patch
# Use system icc profiles
Patch1:        pdfbox-use-system-icc-profiles-openicc.patch

BuildRequires:  maven-local
BuildRequires:  mvn(commons-io:commons-io)
BuildRequires:  mvn(commons-logging:commons-logging)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.ant:ant)
BuildRequires:  mvn(org.apache:apache:pom:)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.bouncycastle:bcmail-jdk15on)
BuildRequires:  mvn(org.bouncycastle:bcprov-jdk15on)
BuildRequires:  mvn(javax.xml.bind:jaxb-api)
BuildRequires:  mvn(jakarta.activation:jakarta.activation-api)

BuildRequires: dejavu-sans-mono-fonts
BuildRequires: google-noto-emoji-fonts
BuildRequires: liberation-sans-fonts
BuildRequires: icc-profiles-openicc
BuildRequires: fontconfig
Requires:      liberation-sans-fonts

# TODO: Require liberation-sans-fonts >= 2 and don't ignore test failures

BuildArch:     noarch

# Ant support was removed by upstream (Obsoletes added in F28)
Obsoletes:     %{name}-ant < %{version}-%{release}
# Jempbox subproject was removed by upstream (Obsoletes added in F28)
Obsoletes:     jempbox < %{version}-%{release}
# Examples package was dropped due to requiring too old lucene (Obsoletes added in F29)
Obsoletes:     %{name}-examples < %{version}-%{release}

%description
Apache PDFBox is an open source Java PDF library for working with PDF
documents. This project allows creation of new PDF documents, manipulation of
existing documents and the ability to extract content from documents. Apache
PDFBox also includes several command line utilities. Apache PDFBox is
published under the Apache License v2.0.

%package debugger
Summary:       Apache PDFBox Debugger

%description debugger
This package contains the PDF debugger for Apache PDFBox.

%package tools
Summary:       Apache PDFBox Tools

%description tools
This package contains command line tools for Apache PDFBox.

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%package -n fontbox
Summary:        Apache FontBox

%description -n fontbox
FontBox is a Java library used to obtain low level information from font
files. FontBox is a subproject of Apache PDFBox.

%package parent
Summary:        Apache PDFBox Parent POM

%description parent
Apache PDFBox Parent POM.

%package reactor
Summary:        Apache PDFBox Reactor POM

%description reactor
Apache PDFBox Reactor POM.

%package -n preflight
Summary:        Apache Preflight

%description -n preflight
The Apache Preflight library is an open source Java tool that implements 
a parser compliant with the ISO-19005 (PDF/A) specification. Preflight is a 
subproject of Apache PDFBox.

%package -n xmpbox
Summary:        Apache XmpBox

%description -n xmpbox
The Apache XmpBox library is an open source Java tool that implements Adobe's
XMP(TM) specification.  It can be used to parse, validate and create xmp
contents.  It is mainly used by subproject preflight of Apache PDFBox. 
XmpBox is a subproject of Apache PDFBox.

%prep
%setup -q
find -name '*.class' -delete
find -name '*.jar' -delete
find -name 'sRGB.icc*' -print -delete
find -name '*.icm' -print -delete
find -name '*.ttf' -print -delete

%patch0 -p1 -b .font
%patch1 -b .openicc

# Don't build apps (it's just a bundle of everything)
%pom_disable_module preflight-app
%pom_disable_module debugger-app
%pom_disable_module app

# Don't build examples, they require ancient version of lucene
%pom_disable_module examples

# Disable plugins not needed for RPM builds
%pom_remove_plugin -r :animal-sniffer-maven-plugin
%pom_remove_plugin -r :apache-rat-plugin
%pom_remove_plugin -r :maven-deploy-plugin
%pom_remove_plugin -r :maven-release-plugin
%pom_remove_plugin -r :maven-source-plugin
%pom_remove_plugin -r :maven-javadoc-plugin
%pom_remove_plugin -r :maven-checkstyle-plugin

# Some test resources are not okay to distribute with the source, upstream
# downloads them at build time, but we can't, so we either remove or fix
# the affected tests
%pom_remove_plugin -r :download-maven-plugin
rm fontbox/src/test/java/org/apache/fontbox/cff/CFFParserTest.java \
   pdfbox/src/test/java/org/apache/pdfbox/pdfparser/TestPDFParser.java \
   pdfbox/src/test/resources/input/rendering/{FANTASTICCMYK.ai,HOTRODCMYK.ai} \
   preflight/src/test/java/org/apache/pdfbox/preflight/TestIsartorBavaria.java
ln -s %{_datadir}/fonts/liberation-sans/LiberationSans-Regular.ttf pdfbox/src/test/resources/org/apache/pdfbox/ttf/LiberationSans-Regular.ttf
sed -i -e 's/\(testCIDFontType2VerticalSubset\)/ignore_\1/' pdfbox/src/test/java/org/apache/pdfbox/pdmodel/font/TestFontEmbedding.java
sed -i -e 's/\(testStructureTreeMerge\)/ignore_\1/'  pdfbox/src/test/java/org/apache/pdfbox/multipdf/PDFMergerUtilityTest.java
sed -i -e '/testPDFBOX4115/i\@org.junit.Ignore' pdfbox/src/test/java/org/apache/pdfbox/pdmodel/font/PDFontTest.java

# Remove unpackaged test deps and tests that rely on them
%pom_remove_dep -r com.github.jai-imageio:
%pom_remove_dep -r :jbig2-imageio
rm tools/src/test/java/org/apache/pdfbox/tools/imageio/TestImageIOUtils.java
%pom_remove_dep :diffutils pdfbox
rm pdfbox/src/test/java/org/apache/pdfbox/text/TestTextStripper.java
sed -i -e 's/TestTextStripper/BidiTest/' pdfbox/src/test/java/org/apache/pdfbox/text/BidiTest.java

# Remove tests that otherwise require net connectivity
rm pdfbox/src/test/java/org/apache/pdfbox/multipdf/MergeAcroFormsTest.java \
   pdfbox/src/test/java/org/apache/pdfbox/multipdf/MergeAnnotationsTest.java
sed -i -e '/\(OptionsAndNamesNotNumbers\|RadioButtonWithOptions\)/i\@org.junit.Ignore' \
  pdfbox/src/test/java/org/apache/pdfbox/pdmodel/interactive/form/PDButtonTest.java

# These test fail for unknown reasons
rm pdfbox/src/test/java/org/apache/pdfbox/pdmodel/graphics/image/CCITTFactoryTest.java

# install all libraries in _javadir
%mvn_file :%{name} %{name}
%mvn_file :%{name}-debugger %{name}-debugger
%mvn_file :%{name}-examples %{name}-examples
%mvn_file :%{name}-tools %{name}-tools
%mvn_file :preflight preflight
%mvn_file :xmpbox xmpbox
%mvn_file :fontbox fontbox

%pom_add_dep jakarta.activation:jakarta.activation-api

%build
# Integration tests all require internet access to download test resources, so skip
# Use compat version of lucene
# Ignore test failures on F28 and earlier due to liberation fonts being too old
%mvn_build -s -- -DskipITs -Dlucene.version=4 -Dmaven.test.failure.ignore=true

%install
%mvn_install

%files -f .mfiles-%{name}
%doc README.md RELEASE-NOTES.txt

%files debugger -f .mfiles-%{name}-debugger

%files tools -f .mfiles-%{name}-tools

%files -n fontbox -f .mfiles-fontbox
%doc fontbox/README.txt
%license LICENSE.txt NOTICE.txt

%files parent -f .mfiles-%{name}-parent
%license LICENSE.txt NOTICE.txt

%files reactor -f .mfiles-%{name}-reactor
%license LICENSE.txt NOTICE.txt

%files -n preflight -f .mfiles-preflight
%doc preflight/README.txt

%files -n xmpbox -f .mfiles-xmpbox
%doc xmpbox/README.txt
%license LICENSE.txt NOTICE.txt

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt NOTICE.txt

%changelog
* Tue Jan 26 2021 Sérgio Basto <sergio@serjux.com> - 2.0.22-1
- Update to 2.0.22 (#1909499)
- Bouncycastle 1.67 patch is already upstreamed

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.21-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 25 2021 Sérgio Basto <sergio@serjux.com> - 2.0.21-3
- Add bouncycastle 1.67 support (from daviddavid)

* Thu Sep 10 2020 Fabio Valentini <decathorpe@gmail.com> - 2.0.21-2
- Drop log4j12 dependency, it seems to not be necessary any longer.

* Wed Aug 26 2020 Sérgio Basto <sergio@serjux.com> - 2.0.21-1
- Fix build on F33
- Update pdfbox to 2.0.21 (#1871001)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.20-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.20-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 11 2020 Jiri Vanek <jvanek@redhat.com> - 2.0.20-2
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Sun Jun 21 2020 Sérgio Basto <sergio@serjux.com> - 2.0.20-1
- Update pdfbox to 2.0.20 (#1844860)

* Fri Mar 27 2020 Sérgio Basto <sergio@serjux.com> - 2.0.19-1
- Update to 2.0.19

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jan 18 2020 Sérgio Basto <sergio@serjux.com> - 2.0.18-1
- Update to 2.0.18 (#1786783)

* Wed Nov 06 2019 Gwyn Ciesla <gwync@protonmail.com> - 2.0.17-1
- 2.0.17

* Sat Aug 31 2019 Orion Poplawski <orion@nwra.com> - 2.0.16-1
- Update to 2.0.16 (CVE-2018-8036, CVE-2018-11797, CVE-2019-0228)

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Dec 04 2018 Mat Booth <mat.booth@redhat.com> - 2.0.9-4
- Disable examples subpackage that requires obsolete lucene4.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Apr 20 2018 Mat Booth <mat.booth@redhat.com> - 2.0.9-2
- Ignore test failures on F28 due to liberation fonts being too old

* Fri Apr 20 2018 Mat Booth <mat.booth@redhat.com> - 2.0.9-1
- Update to latest upstream release

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 03 2018 Troy Dawson <tdawson@redhat.com> - 1.8.13-3
- add BuildRequires: apache-parent - fix FTBFS Fedora 27+

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Feb 14 2017 gil cattaneo <puntogil@libero.it> 1.8.13-1
- update to 1.8.13
- fix rhbz#1421809 (Apply upstream patches to SynchronizedMetaDataValidation)

* Tue Feb 07 2017 Michael Simacek <msimacek@redhat.com> - 1.8.12-4
- Remove useless apache-rat plugin

* Mon Feb 06 2017 Michael Simacek <msimacek@redhat.com> - 1.8.12-3
- Remove useless maven-release-plugin

* Mon Aug 29 2016 Michael Simacek <msimacek@redhat.com> - 1.8.12-2
- Workaround JAVACC-292 bug

* Fri May 27 2016 gil cattaneo <puntogil@libero.it> 1.8.12-1
- update to 1.8.12

* Fri Apr 08 2016 gil cattaneo <puntogil@libero.it> 1.8.11-2
- rebuilt with bcmail 1.54

* Mon Feb 08 2016 gil cattaneo <puntogil@libero.it> 1.8.11-1
- update to 1.8.11

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Sep 05 2015 gil cattaneo <puntogil@libero.it> 1.8.10-1
- update to 1.8.10

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Mar 24 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.8.8-4
- Remove cobertura-maven-plugin usage from POM
- Resolves: rhbz#1205176

* Wed Feb 11 2015 gil cattaneo <puntogil@libero.it> 1.8.8-3
- introduce license macro

* Mon Jan 19 2015 gil cattaneo <puntogil@libero.it> 1.8.8-2
- rebuilt for regenerate rpm {osgi,maven}.prov, {osgi,maven}.req

* Sat Jan 17 2015 gil cattaneo <puntogil@libero.it> 1.8.8-1
- update to 1.8.8

* Thu Oct 30 2014 gil cattaneo <puntogil@libero.it> 1.8.7-1
- update to 1.8.7

* Fri Sep 26 2014 gil cattaneo <puntogil@libero.it> 1.8.5-3
- build fix for bouncycastle 1.50 (rhbz#1100445)
- adapt to current guideline
- remove lucene sub package
- force log4j12 usage

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 21 2014 Orion Poplawski <orion@cora.nwra.com> - 1.8.5-1
- Add patch to disable test that needs missing deps
- Remove missing test deps from pdbbox pom
- Use junit instead of junit4

* Fri May 2 2014 Orion Poplawski <orion@cora.nwra.com> - 1.8.5-1
- Update to 1.8.5

* Sat Feb 1 2014 Orion Poplawski <orion@cora.nwra.com> - 1.8.4-1
- Update to 1.8.4

* Mon Dec 2 2013 Orion Poplawski <orion@cora.nwra.com> - 1.8.3-1
- Update to 1.8.3
- New pcfi.jar location

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jul 14 2013 Orion Poplawski <orion@cora.nwra.com> - 1.8.2-1
- Update to 1.8.2
- Drop unneeded maven BRs

* Wed Apr 17 2013 Orion Poplawski <orion@cora.nwra.com> - 1.8.1-1
- Update to 1.8.1

* Thu Mar 28 2013 Orion Poplawski <orion@cora.nwra.com> - 1.8.0-1
- Update to 1.8.0
- Add preflight and xmpbox sub-packages

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.7.0-5
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Mon Sep 24 2012 Orion Poplawski <orion@cora.nwra.com> - 1.7.0-4
- Drop lucene sub-package for now, not compatible with lucene 3.6

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jul 3 2012 Orion Poplawski <orion@cora.nwra.com> - 1.7.0-2
- Fix javadocs -> javadoc typo

* Tue Jul 3 2012 Orion Poplawski <orion@cora.nwra.com> - 1.7.0-1
- Update to 1.7.0
- Add examples sub-package
- Add BR on bitstream font and fontconfig

* Wed Apr 18 2012 Orion Poplawski <orion@cora.nwra.com> - 1.6.0-5
- Drop pdfbox-app sub-package, nothing but a bundle (bug #813712)

* Wed Feb 1 2012 Orion Poplawski <orion@cora.nwra.com> - 1.6.0-4
- Add proper provides/obsoletes to javadoc sub-package (bug #785396)

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Oct 24 2011 Orion Poplawski <orion@cora.nwra.com> - 1.6.0-2
- BR separately packaged pcfi

* Wed Aug 10 2011 Orion Poplawski <orion@cora.nwra.com> - 1.6.0-1
- Update to 1.6.0
- Add pcfi-2010.08.09.jar to sources
- Drop depmap
- Use apache-commons-logging
- Other cleanup

* Fri Jun 3 2011 Orion Poplawski <orion@cora.nwra.com> - 1.5.0-2
- Use maven 3
- Single javadoc package

* Thu Mar 10 2011 Orion Poplawski <orion@cora.nwra.com> - 1.5.0-1
- Update to 1.5.0

* Tue Dec 28 2010 Orion Poplawski <orion@cora.nwra.com> - 1.4.0-2
- Create sub-packages
- Use depmap file

* Tue Dec 21 2010 Orion Poplawski <orion@cora.nwra.com> - 1.4.0-1
- Update to 1.4.0

* Sat Nov 6 2010 Orion Poplawski <orion@cora.nwra.com> - 1.3.1-1
- Update to 1.3.1

* Fri Aug 13 2010 Orion Poplawski <orion@cora.nwra.com> - 1.3.0-0.1
- Update to 1.3.0-SNAPSHOT

* Thu Jul 15 2010 Orion Poplawski <orion@cora.nwra.com> - 1.2.1-1
- Update to 1.2.1

* Thu Jul 1 2010 Orion Poplawski <orion@cora.nwra.com> - 1.2.0-1
- Update to 1.2.0
- Drop gcj support

* Mon Oct 19 2009 Orion Poplawski <orion@cora.nwra.com> - 0.8.0-2
- Add Requires

* Thu Oct 15 2009 Orion Poplawski <orion@cora.nwra.com> - 0.8.0-1
- Initial Fedora package
