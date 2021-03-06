# This is a snapshot of the BCEL trunk for FindBugs 3.0.

%global findbugsver 20140707svn1547656

Name:           findbugs-bcel
Version:        6.0
Release:        0.22.%{findbugsver}%{?dist}
Summary:        Byte Code Engineering Library for FindBugs

License:        ASL 2.0
URL:            http://commons.apache.org/proper/commons-bcel/

# This archive was created with:
#   $ svn export http://svn.apache.org/repos/asf/commons/proper/bcel/trunk -r 1547656 bcel-6.0
#   $ tar -zcf bcel-20140707svn1547656.tgz bcel-6.0
Source0:        bcel-%{findbugsver}.tgz
Source1:        http://central.maven.org/maven2/com/google/code/findbugs/bcel-findbugs/%{version}/bcel-findbugs-%{version}.pom

# Add temporary dependency on javapackages-local, for %%add_maven_depmap macro
# See https://lists.fedoraproject.org/archives/list/java-devel@lists.fedoraproject.org/thread/R3KZ7VI5DPCMCELFIVJQ4AXB2WQED35C/
BuildRequires:  javapackages-local

BuildRequires:  java-devel, jpackage-utils
Requires:       java-headless, jpackage-utils

BuildArch:      noarch

%description
This is a snapshot of Apache's Byte Code Engineering Library (BCEL) for use
with FindBugs 3.0.

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
%{summary}.

%prep
%setup -q -n bcel-%{version}

%build
mkdir classes
find src/main/java -type f -name '*.java' | \
xargs javac -g -d classes -source 1.8 -target 1.8 -encoding ISO8859-1
cd classes
jar cf findbugs-bcel.jar org
cd ..

mkdir javadoc
find src/main/java -type f -name '*.java' | xargs javadoc -sourcepath src/main/java \
  -classpath classes -source 1.8 -encoding ISO8859-1 -d javadoc -Xdoclint:none

%install

mkdir -p $RPM_BUILD_ROOT%{_javadir}
install -d -m 755 %{buildroot}%{_mavenpomdir}
cp -p classes/findbugs-bcel.jar $RPM_BUILD_ROOT%{_javadir}
install -pm 644 %{SOURCE1} %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom

%add_maven_depmap JPP-%{name}.pom %{name}.jar -a "com.google.code.findbugs:bcel"

mkdir -p $RPM_BUILD_ROOT%{_javadocdir}
cp -a javadoc $RPM_BUILD_ROOT%{_javadocdir}/findbugs-bcel

%pretrans javadoc -p <lua>
path = "%{_javadocdir}/%{name}"
st = posix.stat(path)
if st and st.type == "link" then
  os.remove(path)
end

%files -f .mfiles
%doc NOTICE.txt README.txt
%license LICENSE.txt

%files javadoc
%doc NOTICE.txt
%license LICENSE.txt
%{_javadocdir}/findbugs-bcel*

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.0-0.22.20140707svn1547656
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Richard Fearn <richardfearn@gmail.com> - 6.0-0.21.20140707svn1547656
- Use -target 1.8 when compiling

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.0-0.20.20140707svn1547656
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 6.0-0.19.20140707svn1547656
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Sat May 23 2020 Richard Fearn <richardfearn@gmail.com> - 6.0-0.18.20140707svn1547656
- Enable building with JDK 11: use source/target 1.8

* Sun Feb 02 2020 Richard Fearn <richardfearn@gmail.com> - 6.0-0.17.20140707svn1547656
- Use %%license

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.0-0.16.20140707svn1547656
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.0-0.15.20140707svn1547656
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.0-0.14.20140707svn1547656
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jan 05 2019 Richard Fearn <richardfearn@gmail.com> - 6.0-0.13.20140707svn1547656
- Don't remove buildroot in %%install section

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.0-0.12.20140707svn1547656
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.0-0.11.20140707svn1547656
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Sep 16 2017 Richard Fearn <richardfearn@gmail.com> - 6.0-0.10.20140707svn1547656
- Remove unnecessary Group: tags

* Fri Jul 28 2017 Richard Fearn <richardfearn@gmail.com> - 6.0-0.9.20140707svn1547656
- Add temporary dependency on javapackages-local, for %%add_maven_depmap macro

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.0-0.8.20140707svn1547656
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.0-0.7.20140707svn1547656
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 6.0-0.6.20140707svn1547656
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.0-0.5.20140707svn1547656
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 11 2015 Richard Fearn <richardfearn@gmail.com> - 6.0-0.4.20140707svn1547656
- Disable doclint when building Javadoc

* Thu Jun 11 2015 Richard Fearn <richardfearn@gmail.com> - 6.0-0.3.20140707svn1547656
- Use POM from Maven Central; add alias for backward compatibility (bug #1230833)
- (Thanks to gil cattaneo!)

* Thu Jan 08 2015 Richard Fearn <richardfearn@gmail.com> - 6.0-0.2.20140707svn1547656
- Install Javadoc into unversioned directory (bug #1068944)

* Mon Jul 07 2014 Richard Fearn <richardfearn@gmail.com> - 6.0-0.1.20140707svn1547656
- Update to 6.0 snapshot for FindBugs 3.0.0

* Tue Jun 10 2014 Richard Fearn <richardfearn@gmail.com> - 5.3-0.7.20130910svn1521566
- Switch to .mfiles
- Remove redundant %%defattr

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.3-0.6.20130910svn1521566
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Mar 16 2014 Richard Fearn <richardfearn@gmail.com> - 5.3-0.5.20130910svn1521566
- Change java dependency to java-headless (bug #1068071)

* Sun Feb 23 2014 Richard Fearn <richardfearn@gmail.com> - 5.3-0.4.20130910svn1521566
- Remove jpackage-utils dependency from findbugs-bcel-javadoc

* Sat Feb 22 2014 Richard Fearn <richardfearn@gmail.com> - 5.3-0.3.20130910svn1521566
- Remove versioned JAR (bug #1022098)

* Mon Jan 13 2014 Marek Goldmann <mgoldman@redhat.com> - 5.3-0.2.20130910svn1521566
- Add com.google.code.findbugs:bcel Maven mapping, RHBZ#1052087

* Tue Sep 10 2013 Richard Fearn <richardfearn@gmail.com> - 5.3-0.1.20130910svn1521566
- Update to trunk snapshot for FindBugs 2.0.2

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.2-1.3.8.9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.2-1.3.8.8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.2-1.3.8.7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.2-1.3.8.6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.2-1.3.8.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 30 2010 Alexander Kurtakov <akurtako@redhat.com> 5.2-1.3.8.4
- Drop gcj.

* Sun Jul 18 2010 Richard Fearn <richardfearn@gmail.com> - 5.2-1.3.8.3
- Fix non-standard groups

* Sun Jul 18 2010 Richard Fearn <richardfearn@gmail.com> - 5.2-1.3.8.2
- Add licence files to -javadoc subpackage to comply with new Subpackage
  Licensing requirements

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.2-1.3.8.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Mar 17 2009 Jerry James <loganjerry@gmail.com> - 5.2-1.3.8
- Update to the findbugs 1.3.8 version of the BCEL patch
- The BCEL patch now applies cleanly, so drop workaround code

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.2-1.3.7.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jan 13 2009 Jerry James <loganjerry@gmail.com> - 5.2-1.3.7.1
- Add '-source 1.5' to the javac and javadoc invocations

* Fri Jan  2 2009 Jerry James <loganjerry@gmail.com> - 5.2-1.3.7
- Update to the findbugs 1.3.7 version of the BCEL patch

* Mon Dec  8 2008 Jerry James <loganjerry@gmail.com> - 5.2-1.3.6
- Update to the findbugs 1.3.6 version of the BCEL patch

* Thu Sep 18 2008 Jerry James <loganjerry@gmail.com> - 5.2-1.3.5
- Initial RPM
