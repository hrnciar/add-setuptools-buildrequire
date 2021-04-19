%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:          mvel
Version:       2.4.10
Release:       2%{?dist}
Summary:       MVFLEX Expression Language
License:       ASL 2.0
Url:           https://github.com/mvel
Source0:       https://github.com/mvel/mvel/archive/%{name}2-%{namedversion}.tar.gz
Source1:       %{name}-script
Patch0:        0-use-system-asm.patch
# remove tests which require internal objectweb-asm libraries
Patch1:        1-remove-internal-asm-tests.patch
Patch2:        2-remove-underscore-identifier.patch

BuildRequires: maven-local
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-surefire-report-plugin)
BuildRequires: mvn(org.ow2.asm:asm)
BuildRequires: mvn(org.ow2.asm:asm-util)
# Explicit requires for javapackages-tools since mvel script
# uses /usr/share/java-utils/java-functions
Requires:      javapackages-tools

BuildArch:     noarch

%description
MVEL is a powerful expression language for Java-based applications. It
provides a plethora of features and is suited for everything from the
smallest property binding and extraction, to full blown scripts.

%package javadoc
Summary:       Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{name}2-%{namedversion}
find . -name "*.jar" -delete
find . -name "*.class" -delete

rm ASM-LICENSE.txt

%patch0 -p1
rm -rf src/main/java/org/mvel2/asm
%patch1 -p1
%patch2 -p1


# Unwanted task
%pom_remove_plugin :maven-source-plugin
# Remove org.apache.maven.wagon:wagon-webdav:1.0-beta-2
%pom_xpath_remove "pom:project/pom:build/pom:extensions"

sed -i 's/\r//' LICENSE.txt

%mvn_file :%{name}2 %{name}

%build

# Tests fails only on ARM builder
%mvn_build -f

%install
%mvn_install

mkdir -p %{buildroot}%{_bindir}
install -pm 755 %{SOURCE1} %{buildroot}%{_bindir}/%{name}

%files -f .mfiles
%{_bindir}/%{name}
%license LICENSE.txt

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt

%changelog
* Fri Feb 12 2021 Alex Macdonald <almacdon@redhat.com> - 2.4.10-2
- remove unnecessary dependency

* Wed Sep 30 2020 Alex Macdonald <almacdon@redhat.com> - 2.4.10-1
- update to upstream version 2.4.10.Final
- removed the local unsafe removal patch because unsafe usage was removed in upstream version 2.4.0

* Thu Aug 27 2020 Alex Macdonald <almacdon@redhat.com> - 2.3.2-3
- remove import and usage of sun.*

* Wed Aug 05 2020 Alex Macdonald <almacdon@redhat.com> - 2.3.2-2
- remove usage of native2ascii; it was removed in ojdk9, and fedora 33 >= will use ojdk11
- remove underscore identifier (using modified upstream patch 54eba360a2b43cb439b8cb198c396884b69ef27a from v2.4.8-Final)

* Wed Jul 29 2020 Alex Macdonald <almacdon@redhat.com> - 2.3.2-1
- update to 2.3.2.Final
- regenerate the "use-system-asm" patch

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Aug 31 2018 Severin Gehwolf <sgehwolf@redhat.com> - 2.2.8-6
- Add explicit requirement on javapackages-tools since mvel
  script uses java-functions. See RHBZ#1600426.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Oct 17 2016 gil cattaneo <puntogil@libero.it> 2.2.8-1
- update to 2.2.8.Final

* Thu Jun 30 2016 gil cattaneo <puntogil@libero.it> 2.2.7-2
- add missing build requires

* Thu Feb 11 2016 gil cattaneo <puntogil@libero.it> 2.2.7-1
- update to 2.2.7.Final

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Aug 25 2015 gil cattaneo <puntogil@libero.it> 2.2.6-1
- update to 2.2.6.Final

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Feb 10 2015 gil cattaneo <puntogil@libero.it> 2.2.2-2
- introduce license macro

* Thu Dec 18 2014 gil cattaneo <puntogil@libero.it> 2.2.2-1
- update to 2.2.2.Final

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 09 2014 gil cattaneo <puntogil@libero.it> 2.1.6-2
- fix rhbz#1095339

* Mon Sep 16 2013 gil cattaneo <puntogil@libero.it> 2.1.6-1
- update to 2.1.6.Final

* Fri Jul 05 2013 gil cattaneo <puntogil@libero.it> 2.0.19-5
- switch to XMvn
- minor changes to adapt to current guideline

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.19-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 2.0.19-3
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat May 26 2012 gil cattaneo <puntogil@libero.it> 2.0.19-1
- initial rpm
