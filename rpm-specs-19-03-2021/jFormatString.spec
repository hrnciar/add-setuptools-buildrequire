%global commit f159b88a16be4d103c7e7beb90e07a92617980b9
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global zipcommit %(c=%{commit}; echo ${c:0:12})

Name:           jFormatString
Version:        0
Release:        0.37.20131227git%{shortcommit}%{?dist}
Summary:        Java format string compile-time checker

License:        GPLv2 with exceptions
URL:            http://code.google.com/p/j-format-string/

Source0:        http://j-format-string.googlecode.com/archive/%{commit}.zip
Source1:        http://search.maven.org/remotecontent?filepath=com/google/code/findbugs/jFormatString/2.0.2/jFormatString-2.0.2.pom

# This patch has not been sent upstream, since it is Fedora specific.
Patch0:         %{name}-build.patch

Patch1:         %{name}-java8.patch

# Add temporary dependency on javapackages-local, for %%add_maven_depmap macro
# See https://lists.fedoraproject.org/archives/list/java-devel@lists.fedoraproject.org/thread/R3KZ7VI5DPCMCELFIVJQ4AXB2WQED35C/
BuildRequires:  javapackages-local

BuildRequires:  ant, java-devel, java-1.8.0-javadoc, jpackage-utils, junit
Requires:       java-headless, jpackage-utils

BuildArch:      noarch

%description
This project is derived from Sun's implementation of java.util.Formatter.  It
is designed to allow compile time checks as to whether or not a use of a
format string will be erroneous when executed at runtime.

%package javadoc
Summary:        Javadoc documentation for %{name}
Requires:       java-1.8.0-javadoc

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n j-format-string-%{zipcommit}
%patch0 -p1
%patch1 -p1

cp %{SOURCE1} pom.xml

# delete test code - it requires FindBugs to compile
rm -rfv src/junit

# delete JARs
rm -v lib/*

%build
# Build the JAR
ant jarFile

# Create the javadocs
mkdir docs
javadoc -d docs -source 1.8 -sourcepath src/java \
  -classpath build/classes \
  -link file://%{_javadocdir}/java edu.umd.cs.findbugs.formatStringChecker

%install

# JAR files
mkdir -p %{buildroot}%{_javadir}
install -d -m 755 %{buildroot}%{_mavenpomdir}
cp -p build/%{name}.jar %{buildroot}%{_javadir}/%{name}.jar
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom

%add_maven_depmap JPP-%{name}.pom %{name}.jar

# Javadocs
mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -rp docs/* %{buildroot}%{_javadocdir}/%{name}

%pretrans javadoc -p <lua>
path = "%{_javadocdir}/%{name}"
st = posix.stat(path)
if st and st.type == "link" then
  os.remove(path)
end

%files -f .mfiles

%files javadoc
%{_javadocdir}/%{name}*

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.37.20131227gitf159b88
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.36.20131227gitf159b88
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 0-0.35.20131227gitf159b88
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Sat May 23 2020 Richard Fearn <richardfearn@gmail.com> - 0-0.34.20131227gitf159b88
- Enable building with JDK 11: use source/target 1.8

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.33.20131227gitf159b88
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.32.20131227gitf159b88
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.31.20131227gitf159b88
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Aug 18 2018 Richard Fearn <richardfearn@gmail.com> - 0-0.30.20131227gitf159b88
- Fix JDK Javadoc links (bug #1618962)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.29.20131227gitf159b88
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.28.20131227gitf159b88
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Sep 16 2017 Richard Fearn <richardfearn@gmail.com> - 0-0.27.20131227gitf159b88
- Remove unnecessary Group: tags

* Fri Jul 28 2017 Richard Fearn <richardfearn@gmail.com> - 0-0.26.20131227gitf159b88
- Add temporary dependency on javapackages-local, for %%add_maven_depmap macro

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.25.20131227gitf159b88
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.24.20131227gitf159b88
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Jun 05 2016 Richard Fearn <richardfearn@gmail.com> - 0-0.23.20131227gitf159b88
- Include git commit SHA1 in release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.22.20131227git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Aug 25 2015 Richard Fearn <richardfearn@gmail.com> - 0-0.21.20131227git
- jFormatString-javadoc no longer depends on jFormatString

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.20.20131227git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jan 08 2015 Richard Fearn <richardfearn@gmail.com> - 0-0.19.20131227git
- Install Javadoc into unversioned directory (bug #1068946)

* Tue Jun 10 2014 Richard Fearn <richardfearn@gmail.com> - 0-0.18.20131227git
- Fix JUnit dependency
- Switch to .mfiles

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.17.20131227git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Mar 16 2014 Richard Fearn <richardfearn@gmail.com> - 0-0.16.20131227git
- Change java dependency to java-headless (bug #1068156)

* Sun Feb 23 2014 Richard Fearn <richardfearn@gmail.com> - 0-0.15.20131227git
- Remove jpackage-utils dependency from jFormatString-javadoc

* Mon Jan 13 2014 Marek Goldmann <mgoldman@redhat.com> - 0-0.14.20131227git
- Add com.google.code.findbugs:jFormatString Maven mapping, RHBZ#1052089

* Fri Dec 27 2013 Richard Fearn <richardfearn@gmail.com> - 0-0.13.20131227git
- Bump release after fixing incoherent-version-in-changelog rpmlint warning

* Fri Dec 27 2013 Richard Fearn <richardfearn@gmail.com> - 0-0.12.20131227git
- Build using source from new Google Code j-format-string project

* Mon Sep 09 2013 Richard Fearn <richardfearn@gmail.com> - 0-0.11.20111215svn
- Update to version shipped with FindBugs 2.0.2 (again)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.10.20081016svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Feb 23 2013 Richard Fearn <richardfearn@gmail.com> - 0-0.9.20081016svn
- Switch back to the version of jFormatString shipped with FindBugs 1.3.9

* Sun Feb 10 2013 Richard Fearn <richardfearn@gmail.com> - 0-0.8.20111215svn
- Update to version shipped with FindBugs 2.0.2

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.7.20081016svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.6.20081016svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.5.20081016svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 30 2010 Alexander Kurtakov <akurtako@redhat.com> 0-0.4.20081016svn
- Drop gcj support.
- No more versioned jars.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.3.20081016svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Mar  5 2009 Jerry James <loganjerry@gmail.com> - 0-0.2.20081016svn
- Clean up minor issues raised in package review

* Tue Dec  9 2008 Jerry James <loganjerry@gmail.com> - 0-0.1.20081016svn
- Initial RPM
