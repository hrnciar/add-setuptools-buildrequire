%global _eclipsedir %{_prefix}/lib/eclipse

# This exclude breaks the cyclic dependency on the platform to aide in
# bootstrapping
%global __requires_exclude .*org\.eclipse\.equinox.*

%global git_tag bc2e29e0d5cf49d05bd97dbb082d2ab58eedd13b

Name:           eclipse-ecf
Version:        3.14.19
Release:        2%{?dist}
Summary:        Eclipse Communication Framework (ECF) Eclipse plug-in

# Note: The org.jivesoftware.smack bundle is Apache licensed
# Note: The ch.ethz.iks.r_osgi.remote bundle is BSD licensed
License:        EPL-2.0 and ASL 2.0 and BSD
URL:            https://www.eclipse.org/ecf/
Source0:        https://git.eclipse.org/c/ecf/org.eclipse.ecf.git/snapshot/org.eclipse.ecf-%{git_tag}.tar.xz

# Change how feature deps are specified, to avoid embedding versions
Patch0: 0001-Avoid-hard-coding-dependency-versions-by-using-featu.patch

# Unneeded dep on JDT prevents bootstrap mode
Patch1: 0002-Remove-unneeded-dep-on-jdt-annotations.patch

BuildRequires:  tycho
BuildRequires:  tycho-extras
BuildRequires:  eclipse-license2
BuildRequires:  httpcomponents-client
BuildRequires:  httpcomponents-core
BuildRequires:  apache-commons-codec
BuildRequires:  apache-commons-logging

BuildArch: noarch

# Upstream Eclipse no longer supports non-64bit arches
ExcludeArch: s390 %{arm} %{ix86}

%description
ECF is a set of frameworks for building communications into applications and
services. It provides a lightweight, modular, transport-independent, fully
compliant implementation of the OSGi Remote Services standard.

%package   core
Summary:   Eclipse ECF Core
Requires:  httpcomponents-client
Requires:  httpcomponents-core
# Obsolete SDK and runtime packages since F33
Obsoletes: %{name}-runtime < 3.14.17-3
Obsoletes: %{name}-sdk < 3.14.17-3

%description core
ECF bundles required by eclipse-platform.

%prep
%setup -q -n org.eclipse.ecf-%{git_tag}

find . -type f -name "*.jar" -exec rm {} \;
find . -type f -name "*.class" -exec rm {} \;

%patch0 -p1
%patch1 -p1

# Requires Optional from Java 8
sed -i -e 's/JavaSE-1.7/JavaSE-1.8/' providers/bundles/org.eclipse.ecf.provider.filetransfer.httpclient45/META-INF/MANIFEST.MF

# Don't use target platform or jgit packaging bits
%pom_xpath_remove "pom:target"
%pom_xpath_remove "pom:plugin[pom:artifactId='tycho-packaging-plugin']/pom:dependencies"
%pom_xpath_remove "pom:plugin[pom:artifactId='tycho-packaging-plugin']/pom:configuration/pom:sourceReferences"
%pom_xpath_remove "pom:plugin[pom:artifactId='tycho-packaging-plugin']/pom:configuration/pom:timestampProvider"
%pom_disable_module releng/org.eclipse.ecf.releng.repository

# Don't build bundles that are not relevant to our platform
%pom_disable_module providers/bundles/org.eclipse.ecf.provider.filetransfer.httpclient45.win32
%pom_xpath_remove "feature/plugin[@os='win32']" releng/features/org.eclipse.ecf.filetransfer.httpclient45.feature/feature.xml

# Only build core modules needed by Eclipse platform
%pom_xpath_replace "pom:modules" "<modules>
<module>releng/features/org.eclipse.ecf.core.feature</module>
<module>releng/features/org.eclipse.ecf.core.ssl.feature</module>
<module>releng/features/org.eclipse.ecf.filetransfer.feature</module>
<module>releng/features/org.eclipse.ecf.filetransfer.httpclient45.feature</module>
<module>releng/features/org.eclipse.ecf.filetransfer.ssl.feature</module>
<module>framework/bundles/org.eclipse.ecf</module>
<module>framework/bundles/org.eclipse.ecf.identity</module>
<module>framework/bundles/org.eclipse.ecf.filetransfer</module>
<module>framework/bundles/org.eclipse.ecf.ssl</module>
<module>providers/bundles/org.eclipse.ecf.provider.filetransfer</module>
<module>providers/bundles/org.eclipse.ecf.provider.filetransfer.httpclient45</module>
<module>providers/bundles/org.eclipse.ecf.provider.filetransfer.ssl</module>
</modules>"

# Don't install poms
%mvn_package "::{pom,target}::" __noinstall

# Don't install source bundles
%mvn_package "::jar:{sources,sources-feature}:" __noinstall
%mvn_package ":"

%build
# Qualifier generated from last modification time of source tarball
QUALIFIER=$(date -u -d"$(stat --format=%y %{SOURCE0})" +v%Y%m%d-%H%M)
%mvn_build -j -- -DforceContextQualifier=$QUALIFIER

%install
%mvn_install

# Move to libdir due to being part of core platform
install -d -m 755 %{buildroot}%{_eclipsedir}
mv %{buildroot}%{_datadir}/eclipse/droplets/ecf/{plugins,features} %{buildroot}%{_eclipsedir}
rm -r %{buildroot}%{_datadir}/eclipse/droplets/ecf

# Fixup metadata
sed -i -e 's|%{_datadir}/eclipse/droplets/ecf|%{_eclipsedir}|' %{buildroot}%{_datadir}/maven-metadata/eclipse-ecf.xml
sed -i -e 's|%{_datadir}/eclipse/droplets/ecf/features/|%{_eclipsedir}/features/|' \
       -e 's|%{_datadir}/eclipse/droplets/ecf/plugins/|%{_eclipsedir}/plugins/|' .mfiles
sed -i -e '/droplets/d' .mfiles

# Remove any symlinks that might be created during bootstrapping due to missing platform bundles
for del in $( (cd %{buildroot}%{_eclipsedir}/plugins && ls | grep -v -e '^org\.eclipse\.ecf' ) ) ; do
rm %{buildroot}%{_eclipsedir}/plugins/$del
sed -i -e "/$del/d" .mfiles
done

# Symlink jars into javadir
install -d -m 755 %{buildroot}%{_javadir}/eclipse
location=%{_eclipsedir}/plugins
while [ "$location" != "/" ] ; do
    location=$(dirname $location)
    updir="$updir../"
done
pushd %{buildroot}%{_javadir}/eclipse
for J in ecf{,.identity,.ssl,.filetransfer,.provider.filetransfer{,.ssl,.httpclient4{,.ssl}}} ecf.provider.filetransfer.httpclient45 ; do
    DIR=$updir%{_eclipsedir}/plugins
    [ -e "`ls $DIR/org.eclipse.${J}_*.jar`" ] && ln -s $DIR/org.eclipse.${J}_*.jar ${J}.jar
done
popd

%files core -f .mfiles
%{_javadir}/eclipse/*

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.14.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 15 2021 Mat Booth <mat.booth@redhat.com> - 3.14.19-1
- Update to latest upstream release

* Thu Nov 19 2020 Mat Booth <mat.booth@redhat.com> - 3.14.17-2
- Obsolete runtime and SDK subpackages
- No need to ship old httpclient4 provider

* Wed Oct 28 2020 Mat Booth <mat.booth@redhat.com> - 3.14.17-1
- Update to latest upstream release

* Wed Oct 07 2020 Jie Kang <jkang@redhat.com> - 3.14.8-6
- Update fedora macro to include eln

* Sun Aug 16 2020 Mat Booth <mat.booth@redhat.com> - 3.14.8-5
- Fix build against ASM 8

* Mon Aug 10 2020 Mat Booth <mat.booth@redhat.com> - 3.14.8-4
- Allow building on JDK 11

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.14.8-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.14.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 18 2020 Mat Booth <mat.booth@redhat.com> - 3.14.8-1
- Update to latest upstream release
- License switch to EPL 2

* Fri Mar 20 2020 Mat Booth <mat.booth@redhat.com> - 3.14.7-1
- Update to latest upstream release

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.14.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Dec 19 2019 Mat Booth <mat.booth@redhat.com> - 3.14.6-3
- Full build

* Wed Dec 18 2019 Mat Booth <mat.booth@redhat.com> - 3.14.6-2
- Enable bootstrap mode

* Wed Dec 18 2019 Mat Booth <mat.booth@redhat.com> - 3.14.6-1
- Update to latest upstream release

* Mon Jul 01 2019 Mat Booth <mat.booth@redhat.com> - 3.14.5-3
- Add BSD to the license tag

* Tue Jun 25 2019 Mat Booth <mat.booth@redhat.com> - 3.14.5-2
- Remove unnecessary BR on xpp

* Sun Jun 16 2019 Mat Booth <mat.booth@redhat.com> - 3.14.5-1
- Update to latest upstream release

* Wed May 08 2019 Mat Booth <mat.booth@redhat.com> - 3.14.4-4
- Avoid building additional ECF providers that are not needed

* Wed May 08 2019 Mat Booth <mat.booth@redhat.com> - 3.14.4-3
- Restrict to same architectures as Eclipse itself

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.14.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Dec 04 2018 Mat Booth <mat.booth@redhat.com> - 3.14.4-1
- Update to 2018-12 release

* Tue Aug 21 2018 Mat Booth <mat.booth@redhat.com> - 3.14.1-3
- Non-bootstrap build

* Sun Aug 19 2018 Mat Booth <mat.booth@redhat.com> - 3.14.1-2
- Fix bootstrap build mode

* Fri Aug 17 2018 Mat Booth <mat.booth@redhat.com> - 3.14.1-1
- Update to latest release
- License correction and fix embedded lib symlinks

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.14.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue May 15 2018 Mat Booth <mat.booth@redhat.com> - 3.14.0-1
- Update to Photon release

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.13.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Sep 14 2017 Mat Booth <mat.booth@redhat.com> - 3.13.8-1
- Update to 3.13.8
- Fix build against asm 6

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.13.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 15 2017 Mat Booth <mat.booth@redhat.com> - 3.13.7-3
- Add a bootstrap mode for building in new buildroots

* Thu Jun 15 2017 Mat Booth <mat.booth@redhat.com> - 3.13.7-2
- Allow conditionally building extra providers

* Thu Jun 15 2017 Mat Booth <mat.booth@redhat.com> - 3.13.7-1
- Update to Oxygen release

* Tue May 09 2017 Mat Booth <mat.booth@redhat.com> - 3.13.6-1
- Update to latest upstream release

* Thu Apr 06 2017 Mat Booth <mat.booth@redhat.com> - 3.13.3-3
- Make package noarch now that Eclipse is in the same location on all arches
- Disable SLP provider

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.13.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 03 2017 Mat Booth <mat.booth@redhat.com> - 3.13.3-1
- Update to latest release

* Wed Sep 14 2016 Mat Booth <mat.booth@redhat.com> - 3.13.2-1
- Update to latest release
- Set qualifiers to source-modification-time instead of build-time, to
  eliminate descrepancies between architectures
- Add SDK package for sources

* Fri Apr 15 2016 Mat Booth <mat.booth@redhat.com> - 3.13.1-1
- Update to latest release
- Add a new subpackage to ship additional ECF bundles

* Tue Mar 15 2016 Mat Booth <mat.booth@redhat.com> - 3.12.2-2
- Avoid embedding versions of external deps in features. This avoids the need to
  rebuild when a dependency changes version.

* Mon Feb 29 2016 Mat Booth <mat.booth@redhat.com> - 3.12.2-1
- Update to Mars.2 release

* Mon Feb 29 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.12.0-3
- Rebuild for httpcomponents-client 4.5.2

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Dec 07 2015 Mat Booth <mat.booth@redhat.com> - 3.12.0-1
- Update to latest release

* Mon Nov  2 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.11.0-2
- Rebuild for httpcomponents-core-4.4.4 update

* Mon Sep 28 2015 Mat Booth <mat.booth@redhat.com> - 3.11.0-1
- Update to latest upstream release

* Wed Sep 16 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.10.1-5
- Rebuild for httpcomponents-client-4.5.1 update

* Wed Sep  9 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.10.1-4
- Rebuild for httpcomponents-core-4.4.3 update

* Mon Sep 07 2015 Michael Simacek <msimacek@redhat.com> - 3.10.1-3
- Rebuild for httpcomponents-core-4.4.2

* Mon Aug 31 2015 Roland Grunberg <rgrunber@redhat.com> - 3.10.1-2
- Minor changes to build as a droplet.

* Tue Aug 25 2015 Mat Booth <mat.booth@redhat.com> - 3.10.1-1
- Update to latest upstream version
- Use XZ compressed tarball
- Make symlink generation more dynamic

* Wed Aug 05 2015 Mat Booth <mat.booth@redhat.com> - 3.10.0-5
- Rebuilt using xmvn/tycho

* Mon Jun 29 2015 Mat Booth <mat.booth@redhat.com> - 3.10.0-4
- Drop incomplete and forbidden SCL macros

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 04 2015 Michael Simacek <msimacek@redhat.com> - 3.10.0-2
- Rebuild against httpcomponents-client-4.5

* Wed May 13 2015 Mat Booth <mat.booth@redhat.com> - 3.10.0-1
- Update to 3.10.0 release

* Tue Mar 31 2015 Mat Booth <mat.booth@redhat.com> - 3.9.3-2
- Add requires on httpcompnents-* >= 4.4.1

* Tue Mar 31 2015 Mat Booth <mat.booth@redhat.com> - 3.9.3-1
- Update to latest upstream release

* Tue Mar 31 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.9.2-4
- Rebuild for httpcomponents-client-4.4.1 update

* Thu Mar 19 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.9.2-3
- Rebuild for httpcomponents-core-4.4.1 update

* Thu Feb 19 2015 Mat Booth <mat.booth@redhat.com> - 3.9.2-2
- Rebuild for latest httpcomponents

* Mon Jan 19 2015 Mat Booth <mat.booth@redhat.com> - 3.9.2-1
- Update to latest upstream release

* Mon Jan 19 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.9.1-3
- Rebuild for httpcomponents 4.4 update

* Tue Dec 09 2014 Roland Grunberg <rgrunber@redhat.com> - 3.9.1-2
- Symlink ECF bundles into javadir.

* Thu Nov 27 2014 Mat Booth <mat.booth@redhat.com> - 3.9.1-1
- Update to latest upstream release

* Thu Nov 27 2014 Mat Booth <mat.booth@redhat.com> - 3.9.0-3
- Make core package archful so it can be installed into libdir
  where eclipse-platform expects it to be

* Tue Nov 18 2014 Mat Booth <mat.booth@redhat.com> - 3.9.0-2
- Rebuild for new commons-codec

* Tue Aug 19 2014 Mat Booth <mat.booth@redhat.com> - 3.9.0-1
- Update to latest upstream release
- Drop unneeded patch

* Wed Aug 6 2014 Alexander Kurtakov <akurtako@redhat.com> 3.8.1-3
- Rebuild against latest httpcomponents.

* Mon Jul 21 2014 Alexander Kurtakov <akurtako@redhat.com> 3.8.1-2
- Rebuild for apache-commons-logging 1.2.

* Wed Jun 25 2014 Mat Booth <mat.booth@redhat.com> - 3.8.1-1
- Update to latest upstream release

* Wed Jun 11 2014 Roland Grunberg <rgrunber@redhat.com> - 3.8.0-4
- Remove problematic manifest alterations from specfile.

* Fri Jun 06 2014 Mat Booth <mat.booth@redhat.com> - 3.8.0-3
- Rebuild against latest httpcomponents.

* Mon May 12 2014 Alexander Kurtakov <akurtako@redhat.com> 3.8.0-2
- Rebuild against latest httpcomponents.

* Wed Mar 19 2014 Mat Booth <fedora@matbooth.co.uk> - 3.8.0-1
- Update to latest upstream.
- Now necessary to explicitly build more fine-grained features.
- Drop unneeded dep on jakarta-commons-httpclient.
- Fixed mixed use of tabs and spaces.
- Switch core package to R: java-headless, rhbz #1068037

* Tue Sep 3 2013 Krzysztof Daniel <kdaniel@redhat.com> 3.6.1-1
- Update to latest upstream.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jun 21 2013 Krzysztof Daniel <kdaniel@redhat.com> 3.6.0-2
- 974112: Remove versions and timestamps from ECF.

* Wed May 1 2013 Krzysztof Daniel <kdaniel@redhat.com> 3.6.0-1
- Update to latest upstream.

* Mon Apr 8 2013 Krzysztof Daniel <kdaniel@redhat.com> 3.5.7-0.6
- Rebuild with old commons logging.

* Mon Apr 8 2013 Krzysztof Daniel <kdaniel@redhat.com> 3.5.7-0.5
- Drop v3 httpclient.
- Make dependency to commons loggigng less strict.

* Wed Mar 20 2013 Krzysztof Daniel <kdaniel@redhat.com> 3.5.7-0.4
- Add direct dependency to jakarta-commons-httpclient.

* Wed Mar 20 2013 Krzysztof Daniel <kdaniel@redhat.com> 3.5.7-0.3
- Symlink deps against /usr/share/java/.

* Fri Mar 15 2013 Krzysztof Daniel <kdaniel@redhat.com> 3.5.7-0.2
- Explicitly build httpclient4 feature.

* Thu Mar 14 2013 Krzysztof Daniel <kdaniel@redhat.com> 3.5.7-0.1
- Update to latest upstream.
- Initial SCLization.

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Oct 8 2012 Krzysztof Daniel <kdaniel@redhat.com> 3.5.6-7
- Use __requires_exclude instead of __provides_exclude.

* Mon Oct 8 2012 Krzysztof Daniel <kdaniel@redhat.com> 3.5.6-6
- Try out __provides_exclude

* Mon Oct 8 2012 Krzysztof Daniel <kdaniel@redhat.com> 3.5.6-5
- Use new way of changing auto required dependencies.

* Fri Oct 5 2012 Krzysztof Daniel <kdaniel@redhat.com> 3.5.6-4
- Don't generate autorreuquire.

* Mon Aug 27 2012 Krzysztof Daniel <kdaniel@redhat.com> 3.5.6-3
- Don't duplicate org.apache* plugins
- Use context qualifier to avoid constant feature version changes.

* Wed Aug 8 2012 Krzysztof Daniel <kdaniel@redhat.com> 3.5.6-2
- Review issues fixed.

* Wed Aug 8 2012 Krzysztof Daniel <kdaniel@redhat.com> 3.5.6-1
- Initial packaging.
