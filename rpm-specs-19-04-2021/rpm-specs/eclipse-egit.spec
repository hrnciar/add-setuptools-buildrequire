%global gittag 5.11.0.202103091610-r

Name:             eclipse-egit
Version:          5.11.0
Release:          1%{?dist}
Summary:          Eclipse Git Integration

License:          EPL-2.0
URL:              http://www.eclipse.org/egit
Source0:          https://git.eclipse.org/c/egit/egit.git/snapshot/egit-%{gittag}.tar.xz

BuildRequires:    tycho
BuildRequires:    maven-antrun-plugin
BuildRequires:    eclipse-platform
BuildRequires:    eclipse-jdt
BuildRequires:    eclipse-jgit >= %{version}
BuildRequires:    jgit >= %{version}
BuildRequires:    eclipse-license2
Requires:         eclipse-platform
Requires:         eclipse-jgit >= %{version}
Requires:         jgit >= %{version}

BuildArch:        noarch

# Upstream Eclipse no longer supports non-64bit arches
ExcludeArch: s390 %{arm} %{ix86}

# Obsoletes added in F32
Obsoletes: %{name}-mylyn <= 5.6.0-2
Obsoletes: %{name}-github <= 5.6.0-2

%description
The eclipse-egit package contains Eclipse plugins for
interacting with Git repositories.

%prep
%setup -q -n egit-%{gittag}

# Disable unnecessary plugins for RPM builds
%pom_remove_plugin :maven-enforcer-plugin

%pom_xpath_remove "pom:repositories"
%pom_xpath_remove "pom:dependencies"
%pom_xpath_remove "pom:profiles"
%pom_xpath_remove "pom:build/pom:plugins/pom:plugin/pom:configuration/pom:target"
%pom_xpath_remove "*[local-name() ='plugin' and (child::*[text()='tycho-packaging-plugin'])]"
%pom_xpath_remove "pom:dependencies" org.eclipse.egit.doc/pom.xml
%pom_disable_module org.eclipse.egit.repository
%pom_disable_module org.eclipse.egit.source-feature
%pom_disable_module org.eclipse.egit.target

# Don't build mylyn feature
%pom_disable_module org.eclipse.egit.mylyn.ui
%pom_disable_module org.eclipse.egit.mylyn-feature

# Ensure correct apache sshd bundle gets symlinked
sed -i -e '/jsch/a<import plugin="org.apache.sshd.osgi"/>' org.eclipse.egit-feature/feature.xml

# Disable tests
%pom_disable_module org.eclipse.egit.core.test
%pom_disable_module org.eclipse.egit.ui.test
%pom_disable_module org.eclipse.egit.gitflow.test
%pom_disable_module org.eclipse.egit.mylyn.ui.test
%pom_disable_module org.eclipse.egit.core.junit

%mvn_package "::pom::" __noinstall
%mvn_package :* egit

%build
%mvn_build -j -f

%install
%mvn_install

%files -f .mfiles-egit
%license LICENSE
%doc README.md

%changelog
* Wed Mar 10 2021 Mat Booth <mat.booth@redhat.com> - 5.11.0-1
- Update to latest upstream release

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 15 2021 Alexander Kurtakov <akurtako@redhat.com> 5.10.0-1
- Update to latest upstream release

* Fri Oct 30 2020 Jeff Johnston <jjohnstn@redhat.com> - 5.9.0-1
- Update to latest upstream release

* Fri Aug 21 2020 Mat Booth <mat.booth@redhat.com> - 5.8.1-1
- Update to latest upstream release

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 22 2020 Mat Booth <mat.booth@redhat.com> - 5.8.0-1
- Update to latest upstream release

* Thu Apr 02 2020 Mat Booth <mat.booth@redhat.com> - 5.7.0-2
- Add obsoletes on github/mylyn extension

* Mon Mar 23 2020 Mat Booth <mat.booth@redhat.com> - 5.7.0-1
- Update to latest upstream release

* Mon Jan 27 2020 Mat Booth <mat.booth@redhat.com> - 5.6.0-2
- Dont't ship the Mylyn feature

* Thu Dec 19 2019 Mat Booth <mat.booth@redhat.com> - 5.6.0-1
- Update to latest upstream release

* Tue Sep 17 2019 Mat Booth <mat.booth@redhat.com> - 5.5.0-1
- Update to latest upstream release

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 27 2019 Mat Booth <mat.booth@redhat.com> - 5.4.0-2
- Actually apply the patch

* Thu Jun 27 2019 Mat Booth <mat.booth@redhat.com> - 5.4.0-1
- Update to final tagged release
- Backport additional patch to fix an NPE when fetching gerrit changes

* Fri May 31 2019 Mat Booth <mat.booth@redhat.com> - 5.4.0-0.1
- Update to latest milestone release

* Sat Mar 16 2019 Mat Booth <mat.booth@redhat.com> - 5.3.0-2
- Rebuild against apache sshd 2

* Wed Mar 13 2019 Mat Booth <mat.booth@redhat.com> - 5.3.0-1
- Update to 2019-03 release
- Restrict to same architectures as Eclipse itself

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Dec 07 2018 Mat Booth <mat.booth@redhat.com> - 5.2.0-1
- Update to 5.2.0 release

* Tue Sep 25 2018 Mat Booth <mat.booth@redhat.com> - 5.1.1-1
- Update to 5.1.1 release

* Wed Aug 22 2018 Mat Booth <mat.booth@redhat.com> - 5.1.0-0.1
- Update to latest snapshot

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 22 2018 Mat Booth <mat.booth@redhat.com> - 5.0.1-1
- Update to latest upstream release

* Wed Mar 21 2018 Alexander Kurtakov <akurtako@redhat.com> 4.11.0-1
- Update to upstream 4.11.0.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 05 2018 Mat Booth <mat.booth@redhat.com> - 4.10.0-1
- Update to latest upstream release

* Fri Dec 15 2017 Mat Booth <mat.booth@redhat.com> - 4.9.1-1
- Update to latest upstream version

* Tue Nov 21 2017 Mat Booth <mat.booth@redhat.com> - 4.9.0-1
- Update to latest upstream version

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jun 23 2017 Mat Booth <mat.booth@redhat.com> - 4.8.0-2
- Avoid unnecessary dep on Mylyn Wikitest

* Fri Jun 16 2017 Mat Booth <mat.booth@redhat.com> - 4.8.0-1
- Update to Oxygen release
- Update bootstrap mode

* Wed May 10 2017 Mat Booth <mat.booth@redhat.com> - 4.7.0-2
- Regenerate symlinks

* Mon Apr 10 2017 nboldt <nickboldt+redhat@gmail.com> - 4.7.0-1
- Update to latest upstream release 4.7.0

* Fri Mar 31 2017 Nick Boldt <nboldt@redhat.com> - 4.6.1-1
- Update to Neon.3 release version; depends on eclipse-jgit 4.6.1

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 04 2017 Mat Booth <mat.booth@redhat.com> - 4.6.0-1
- Update to latest release

* Tue Oct 4 2016 Alexander Kurtakov <akurtako@redhat.com> 4.5.0-1
- Upgrade to 4.5.0.

* Wed Aug 03 2016 Sopot Cela <scela@redhat.com> - 4.4.1-1
- Upgrade to 4.4.1

* Wed Jun 15 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 4.4.0-2
- Add missing build-requires

* Mon Jun 13 2016 Mat Booth <mat.booth@redhat.com> - 4.4.0-1
- Update to latest release

* Sun May 01 2016 Mat Booth <mat.booth@redhat.com> - 4.3.0-2
- Patch to build against smart import extension point that moved into
  Eclipse Neon platform.

* Fri Apr 15 2016 Sopot Cela <scela@redhat.com> - 4.3.0-1
- Upgrade to 4.3.0

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 26 2016 Sopot Cela <scela@redhat.com> - 4.2.0-1
- Update to 4.2

* Tue Dec 08 2015 Mat Booth <mat.booth@redhat.com> - 4.1.1-1
- Update to latest upstream release

* Wed Sep 30 2015 Mat Booth <mat.booth@redhat.com> - 4.1.0-1
- Update to 4.1.0 release

* Mon Sep 14 2015 Roland Grunberg <rgrunber@redhat.com> - 4.0.1-5
- Rebuild as an Eclipse p2 Droplet.

* Mon Jul 13 2015 Alexander Kurtakov <akurtako@redhat.com> 4.0.1-4
- Enable importer plugin.

* Wed Jul 08 2015 Mat Booth <mat.booth@redhat.com> - 4.0.1-3
- Fix bootstrap build

* Thu Jul 02 2015 Mat Booth <mat.booth@redhat.com> - 4.0.1-2
- Drop incomplete SCL macros

* Wed Jun 24 2015 Alexander Kurtakov <akurtako@redhat.com> 4.0.1-1
- Update to 4.0.1.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 10 2015 Alexander Kurtakov <akurtako@redhat.com> 4.0.0-1
- Update to 4.0 final.

* Mon Jun 1 2015 Alexander Kurtakov <akurtako@redhat.com> 4.0.0-0.2.rc2
- Rebuild for jgit.

* Thu May 28 2015 Alexander Kurtakov <akurtako@redhat.com> 4.0.0-0.1.rc2
- Update to 4.0 rc2.

* Thu May 14 2015 Alexander Kurtakov <akurtako@redhat.com> 3.7.1-1
- Update to upstream 3.7.1 release.

* Mon Mar 02 2015 Roland Grunberg <rgrunber@redhat.com> - 3.7.0-1
- Update to upstream 3.7.0 release.

* Fri Jan 23 2015 Alexander Kurtakov <akurtako@redhat.com> 3.6.2-1
- Update to upstream 3.6.2 release.

* Mon Jan 19 2015 Roland Grunberg <rgrunber@redhat.com> - 3.6.1-2
- Add bootstrapping capability.

* Mon Jan 5 2015 Alexander Kurtakov <akurtako@redhat.com> 3.6.1-1
- Update to upstream 3.6.1 release.

* Fri Dec 19 2014 Alexander Kurtakov <akurtako@redhat.com> 3.5.3-1
- Update to upstream 3.5.3 release.

* Thu Dec 18 2014 Alexander Kurtakov <akurtako@redhat.com> 3.5.2-1
- Update to upstream 3.5.2 release.

* Fri Nov 07 2014 Mat Booth <mat.booth@redhat.com> - 3.5.0-2
- Build/install with mvn_build/mvn_install

* Fri Oct 03 2014 Mat Booth <mat.booth@redhat.com> - 3.5.0-1
- Update to latest upstream release 3.5.0

* Thu Jun 26 2014 Mat Booth <mat.booth@redhat.com> - 3.4.1-1
- Update to latest upstream release 3.4.1

* Fri Jun 13 2014 Roland Grunberg <rgrunber@redhat.com> - 3.4.0-1
- Update to 3.4.0.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 22 2014 Sami Wagiaalla <swagiaal@redhat.com> - 3.3.2-2
- Fix build agains the lates o.e.jface.util.Policy.

* Mon Apr 28 2014 Mat Booth <mat.booth@redhat.com> - 3.3.2-1
- Update to 3.3.2.

* Fri Mar 28 2014 Alexander Kurtakov <akurtako@redhat.com> 3.3.1-1
- Update to 3.3.1.

* Tue Mar 11 2014 Alexander Kurtakov <akurtako@redhat.com> 3.3.0-1
- Update to 3.3.0.

* Sun Dec 29 2013 Alexander Kurtakov <akurtako@redhat.com> 3.2.0-1
- Update to 3.2.0.

* Mon Oct 21 2013 Krzysztof Daniel <kdaniel@redhat.com> 3.1.0-3
- Fix feature installation.

* Wed Oct 16 2013 Krzysztof Daniel <kdaniel@redhat.com> 3.1.0-2
- Package Egit integration for mylyn.
- Changed building process to reflect upstream one.

* Thu Oct 3 2013 Krzysztof Daniel <kdaniel@redhat.com> 3.1.0-1
- Update to Kepler SR1.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jul 5 2013 Neil Brian Guzman <nguzman@redhat.com> 3.0.0-3
- Bump release

* Tue Jun 25 2013 Neil Brian Guzman <nguzman@redhat.com> 3.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jun 25 2013 Krzysztof Daniel <kdaniel@redhat.com> 3.0.0-1
- Update to 3.0.0.

* Thu Feb 21 2013 Sami Wagiaalla <swagiaal@redhat.com> 2.3.1-1
- SCL-ized.

* Thu Feb 21 2013 Sami Wagiaalla <swagiaal@redhat.com> 2.3.1-1
- Update to 2.3.1.

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jan 3 2013 Krzysztof Daniel <kdaniel@redhat.com> 2.2.0-1
- Update to latest upstream.

* Mon Oct 1 2012 Alexander Kurtakov <akurtako@redhat.com> 2.1.0-1
- Update to 2.1.0 release.

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 2 2012 Alexander Kurtakov <akurtako@redhat.com> 2.0.0-1
- Update to 2.0.0 upstream release.

* Fri Apr 27 2012 Severin Gehwolf <sgehwolf@redhat.com> 1.3.0-3
- Use eclipse-pdebuild over pdebuild in lib.

* Thu Apr 26 2012 Severin Gehwolf <sgehwolf@redhat.com> 1.3.0-2
- Fix 1.3.0 which was previously using wrong sources.
- Fix JGit BR/R since EGit depends on the same version of JGit.

* Fri Feb 17 2012 Andrew Robinson <arobinso@redhat.com> 1.3.0-1
- Update to 1.3.0 upstream release.

* Thu Jan 5 2012 Alexander Kurtakov <akurtako@redhat.com> 1.2.0-1
- Update to upstream 1.2.0.

* Fri Nov 18 2011 Alexander Kurtakov <akurtako@redhat.com> 1.1.0-2
- Add patch to fix New git repo wizard.

* Mon Jun 27 2011 Andrew Robinson <arobinso@redhat.com> 1.1.0-1
- Update to upstream release 1.1.0.

* Tue Jun 14 2011 Chris Aniszczyk <zx@redhat.com> 1.0.0-2
- Update to final upstream release v1.0.0.201106090707-r.

* Tue Jun 07 2011 Chris Aniszczyk <zx@redhat.com> 1.0.0-1
- Update to upstream release 1.0.0.

* Tue May 03 2011 Chris Aniszczyk <zx@redhat.com> 0.12.1-1
- Update to upstream release 0.12.1.

* Tue Feb 22 2011 Chris Aniszczyk <zx@redhat.com> 0.11.3-2
- Update to fix issue with GitCloneWizard file.

* Tue Feb 22 2011 Chris Aniszczyk <zx@redhat.com> 0.11.3-1
- Update to upstream release 0.11.3.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 22 2010 Chris Aniszczyk <zx@redhat.com> 0.10.1-1
- Update to upstream release 0.10.1.

* Thu Oct 7 2010 Chris Aniszczyk <zx@redhat.com> 0.9.3-1
- Update to upstream release 0.9.3.

* Wed Sep 15 2010 Severin Gehwolf <sgehwolf@redhat.com> 0.9.1-1
- Update to upstream release 0.9.1.
- Remove git-core dependency.

* Thu Aug 26 2010 Severin Gehwolf <sgehwolf at, redhat.com> 0.9.0-0.1.20100825git
- Make release tag more readable (separate "0.1" and pre-release tag by ".").

* Wed Aug 25 2010 Severin Gehwolf <sgehwolf at, redhat.com> 0.9.0-0.120100825git
- Pre-release of EGit 0.9.0

* Thu Jun 24 2010 Severin Gehwolf <sgehwolf at, redhat.com> 0.8.4-1
- Rebase to 0.8.4 release.

* Tue Apr 13 2010 Jeff Johnston <jjohnstn@redhat.com> 0.7.1-2
- Bump up release.

* Tue Apr 13 2010 Jeff Johnston <jjohnstn@redhat.com> 0.7.1-1
- Rebase to 0.7.1.

* Fri Mar 19 2010 Alexander Kurtakov <akurtako@redhat.com> 0.7.0-1
- Update to 0.7.0.
- License is only EPL now.

* Tue Feb 9 2010 Alexander Kurtakov <akurtako@redhat.com> 0.6.0-0.1.git20100208
- New git snapshot.

* Tue Nov 10 2009 Alexander Kurtakov <akurtako@redhat.com> 0.6.0-0.1.git20091029
- Update to 0.6 git.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jul 17 2009 Alexander Kurtakov <akurtako@redhat.com> 0.5.0-1
- Update to 0.5.0.

* Mon Mar 23 2009 Alexander Kurtakov <akurtako@redhat.com> 0.4.0-3.20090323
- Update to latest snapshot.

* Mon Mar 23 2009 Alexander Kurtakov <akurtako@redhat.com> 0.4.0-3.20090217
- Rebuild to not ship p2 context.xml.

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-2.20090217
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 17 2009 Alexander Kurtakov <akurtako@redhat.com> 0.4.0-1.20090217
- New snapshot.

* Wed Dec 10 2008 Alexander Kurtakov <akurtako@redhat.com> 0.4.0-1
- Update to 0.4.0.

* Wed Oct 22 2008 Alexander Kurtakov <akurtako@redhat.com> 0.3.1.20081022-3
- New git version.

* Wed Jul 30 2008 Andrew Overholt <overholt@redhat.com> 0.3.1-2
- Move files and update build for Eclipse SDK 3.4
- Use pdebuild

* Thu Jul 17 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.3.1-1
- fix license tag

* Tue Apr 08 2008 Jesse Keating <jkeating@redhat.com> - 0.3.1-0
- New upstream release 0.3.1, makes committing / diffing actually work

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.3.0-3
- Autorebuild for GCC 4.3

* Thu Oct 04 2007 Ben Konrath <bkonrath@redhat.com> 0.3.0-2.fc8
- Require git-core instead of git.
- Resolves: #319321

* Mon Sep 24 2007 Ben Konrath <bkonrath@redhat.com> 0.3.0-1.fc8
- 0.3.0

* Wed Sep 19 2007 Ben Konrath <bkonrath@redhat.com> 0.2.99-0.git20070919.fc8
- 0.2.99 git20070919

* Mon Sep 17 2007 Ben Konrath <bkonrath@redhat.com> 0.2.2-2.git20070911.fc8
- Update add feature and plugin patch.

* Mon Sep 17 2007 Ben Konrath <bkonrath@redhat.com> 0.2.2-1.git20070911.fc8
- Require eclipse-platform >= 3.2.1 

* Fri Sep 14 2007 Ben Konrath <bkonrath@redhat.com> 0.2.2-0.git20070911.fc8
- Update to git20070911.
- Update feature and accosicated branding plugin.

* Wed Aug 29 2007 Ben Konrath <bkonrath@redhat.com> 0.2.2-0.git20070826.fc8
- Initial version
