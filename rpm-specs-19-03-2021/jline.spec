Name:             jline
Version:          3.18.0
Release:          3%{?dist}
Summary:          Java library for handling console input
License:          BSD
URL:              https://github.com/jline/jline3
BuildArch:        noarch

Source0:          %{url}/archive/jline-parent-%{version}.tar.gz
# Adapt to newer versions of apache-sshd
Patch0:           %{name}-apache-sshd.patch

BuildRequires:  maven-local
BuildRequires:  mvn(com.googlecode.juniversalchardet:juniversalchardet)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(net.java.dev.jna:jna)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(org.apache.sshd:sshd-core) >= 2.6.0
BuildRequires:  mvn(org.apache.sshd:sshd-scp) >= 2.6.0
BuildRequires:  mvn(org.apache.sshd:sshd-sftp) >= 2.6.0
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.easymock:easymock)
BuildRequires:  mvn(org.fusesource.jansi:jansi)

%global _desc %{expand:
JLine is a Java library for handling console input.  It is similar in
functionality to BSD editline and GNU readline but with additional
features that bring it in par with the ZSH line editor.  Those familiar
with the readline/editline capabilities for modern shells (such as bash
and tcsh) will find most of the command editing features of JLine to be
familiar.}

%description %_desc

This package contains the parent POM for the jline project

%package javadoc
Summary:          Javadocs for %{name}

%description javadoc %_desc

This package contains the API documentation for %{name}.

%package        terminal
Summary:        JLine terminal

%description    terminal %_desc

This package contains the basic terminal support for JLine.

%package        terminal-jansi
Summary:        JLine terminal with JANSI
Requires:       %{name}-terminal = %{version}-%{release}

%description    terminal-jansi %_desc

This package contains a functioning terminal based on JANSI.

%package        terminal-jna
Summary:        JLine terminal with JNA
Requires:       %{name}-terminal = %{version}-%{release}

%description    terminal-jna %_desc

This package contains a functioning terminal based on JNA.

%package        reader
Summary:        JLine reader
Requires:       %{name}-terminal = %{version}-%{release}

%description    reader %_desc

This package supports reading lines from a console with customizable key
bindings and input editing.

%package        style
Summary:        JLine style
Requires:       %{name}-terminal = %{version}-%{release}

%description    style %_desc

This package contains a style processor for JLine, which can apply
colors to strings, for example.

%package        builtins
Summary:        JLine builtins
Requires:       %{name}-reader = %{version}-%{release}
Requires:       %{name}-style = %{version}-%{release}
Recommends:     mvn(com.googlecode.juniversalchardet:juniversalchardet)

%description    builtins %_desc

This package contains keybindings to emulate popular tools such as nano
and less.

%package        console
Summary:        JLine console
Requires:       %{name}-builtins = %{version}-%{release}

%description    console %_desc

This package contains a console with command and script execution
support, and tab completion.

%package        remote-ssh
Summary:        JLine remote SSH
Requires:       %{name}-builtins = %{version}-%{release}
Recommends:     mvn(org.apache.sshd:sshd-core) >= 2.6.0
Recommends:     mvn(org.apache.sshd:sshd-scp) >= 2.6.0
Recommends:     mvn(org.apache.sshd:sshd-sftp) >= 2.6.0

%description    remote-ssh %_desc

This package contains an ssh client.

%package        remote-telnet
Summary:        JLine remote telnet
Requires:       %{name}-builtins = %{version}-%{release}
Recommends:     mvn(org.apache.sshd:sshd-core) >= 2.6.0

%description    remote-telnet %_desc

This package contains a telnet client.

%prep
%autosetup -n jline3-jline-parent-%{version} -p0

# remove unnecessary dependency on parent POM
%pom_remove_parent

# We don't need the bundle
%pom_disable_module jline

# Missing dependencies in Fedora
%pom_disable_module demo
%pom_disable_module groovy
%pom_disable_module graal
%pom_remove_plugin :gmavenplus-plugin
%pom_remove_dep :graal-sdk

# Unnecessary plugins for an rpm build
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :maven-release-plugin
%pom_remove_plugin :native-image-maven-plugin

# Apache SSHD package names where refactored in 2.6.0
# See https://github.com/apache/mina-sshd/commit/5cbae28a42c478c052ade11d0fc3b84d4ee2f720
sed -i -e 's/org.apache.sshd.server.scp/org.apache.sshd.scp.server/' \
  remote-ssh/src/main/java/org/jline/builtins/ssh/Ssh.java
sed -i -e 's/org.apache.sshd.server.subsystem.sftp/org.apache.sshd.sftp.server/' \
  remote-ssh/src/main/java/org/jline/builtins/ssh/Ssh.java


%build
%mvn_build -s

%install
%mvn_install

%files -f .mfiles-jline-parent
%doc changelog.md README.md
%license LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc changelog.md README.md
%license LICENSE.txt

%files terminal -f .mfiles-jline-terminal
%doc changelog.md README.md
%license LICENSE.txt

%files terminal-jansi -f .mfiles-jline-terminal-jansi

%files terminal-jna -f .mfiles-jline-terminal-jna

%files reader -f .mfiles-jline-reader

%files style -f .mfiles-jline-style

%files builtins -f .mfiles-jline-builtins

%files console -f .mfiles-jline-console

%files remote-ssh -f .mfiles-jline-remote-ssh

%files remote-telnet -f .mfiles-jline-remote-telnet

%changelog
* Fri Mar 12 2021 Mat Booth <mat.booth@redhat.com> - 3.18.0-3
- Fix build against apache-sshd 2.6.0

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.18.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec 14 2020 Jerry James <loganjerry@gmail.com> - 3.18.0-1
- Version 3.18.0
- Remove package name from Summary
- Add patch to adapt to recent versions of apache-sshd
- Break up into subpackages to control dependencies

* Sun Aug 09 2020 Fabio Valentini <decathorpe@gmail.com> - 2.14.6-10
- Drop useless parent POM and powermock build dependencies.

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 2.14.6-8
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Thu Jun 25 2020 Alexander Kurtakov <akurtako@redhat.com> 2.14.6-7
- Fix Java 11 build.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.14.6-2
- Remove explicit invocation of maven-javadoc-plugin

* Thu May 24 2018 Michael Simacek <msimacek@redhat.com> - 2.14.6-1
- Update to upstream version 2.14.6

* Fri Mar 16 2018 Michael Simacek <msimacek@redhat.com> - 2.13-12
- Remove -Werror to fix FTBFS

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.13-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.13-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Feb 16 2017 Michael Simacek <msimacek@redhat.com> - 2.13-9
- Correct license tag to just BSD

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.13-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 02 2017 Michael Simacek <msimacek@redhat.com> - 2.13-7
- Remove BR on site-plugin

* Wed Jun 22 2016 Michael Simacek <msimacek@redhat.com> - 2.13-6
- Remove nondeterministic test

* Wed Jun 15 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.13-5
- Regenerate build-requires

* Thu May 05 2016 Michael Simacek <msimacek@redhat.com> - 2.13-4
- Try to eliminate test nondeterminism

* Mon Mar 14 2016 Severin Gehwolf <sgehwolf@redhat.com> - 2.13-3
- OSGi export jline.internal. Resolves RHBZ#1317551.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Nov 25 2015 Severin Gehwolf <sgehwolf@redhat.com> - 2.13-1
- Update to upstream 2.13 release.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Feb 18 2015 Alexander Kurtakov <akurtako@redhat.com> 2.12.1-1
- Update to upstream 2.12.1 release.

* Mon Jan 26 2015 Mat Booth <mat.booth@redhat.com> - 2.10-15
- Fix FTBFS due to missing BR on site-plugin
- Fix directory ownership
- Fix bogus date in changelog

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.10-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.10-13
- Migrate BuildRequires from junit4 to junit

* Mon May 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.10-12
- Remove BuildRequires on maven-surefire-provider-junit4

* Tue Mar 11 2014 Michael Simacek <msimacek@redhat.com> - 2.10-11
- Drop manual requires

* Tue Mar 04 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.10-10
- Use Requires: java-headless rebuild (#1067528)

* Tue Oct 29 2013 Severin Gehwolf <sgehwolf@redhat.com> - 2.10-9
- Package jline 2.x as jline. Resolves RHBZ#1022915.
- Part of a large effort to make jline1 a compat package rather than jline2.
  See RHBZ#1022897.
- Switch to xmvn.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.0-3
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Feb 1 2012 Alexander Kurtakov <akurtako@redhat.com> 1.0-1
- Update to 1.0.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.94-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 13 2011 Alexander Kurtakov <akurtako@redhat.com> 0.9.94-6
- Build with maven 3.x.

* Sat Oct 15 2011 Ville Skyttä <ville.skytta@iki.fi> - 0.9.94-5
- BuildRequire maven2.

* Sat Oct 15 2011 Ville Skyttä <ville.skytta@iki.fi> - 0.9.94-4
- Patch delete to actually behave as delete instead of backspace, include
  keybindings.properties in docs (#720170).
- Drop executable bit from jar.
- Crosslink with local javadocs.
- Include LICENSE.txt in -javadoc.

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.94-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Dec 18 2010 Mat Booth <fedora@matbooth.co.uk> - 0.9.94-2
- Remove pre-built Windows-only binary artifacts.
- Demo package was defined but never built for some reason.
- Don't also package jar in the javadoc package!
- Drop versioned java and javadocs.

* Sat Dec 18 2010 Mat Booth <fedora@matbooth.co.uk> - 0.9.94-1
- Remove bundled jars in %%prep phase.
- Tidy up spec file, fix some rpmlint warnings.
- Add pom and depmaps.

* Mon Mar  8 2010 Peter Lemenkov <lemenkov@gmail.com> - 0:0.9.94-0.6
- Added missing Requires: jpackage-utils (%%{_javadir} and %%{_javadocdir})

* Tue Jan 12 2010 Alexander Kurtakov <akurtako@redhat.com> 0:0.9.94-0.5
- Fix BRs.
- Drop gcj_support.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:0.9.94-0.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:0.9.94-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Jul  9 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0:9.94-0.2
- drop repotag

* Mon Mar 24 2008 Matt Wringe <mwringe@redhat.com> - 0:9.94-0jpp.1
- Update to 0.9.94 (BZ #436204)

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0:0.9.9-2jpp.1
- Autorebuild for GCC 4.3

* Tue Mar 06 2007 Matt Wringe <mwringe@redhat.com> - 0:0.9.9-1jpp.1
- Add option to build with ant.
- Fix various rpmlint issues
- Specify proper license

* Thu May 04 2006 Alexander Kurtakov <akurtkov at gmail.com> - 0:0.9.9-1jpp
- Upgrade to 0.9.9

* Thu May 04 2006 Ralph Apel <r.apel at r-apel.de> - 0:0.9.5-1jpp
- Upgrade to 0.9.5
- First JPP-1.7 release

* Mon Apr 25 2005 Fernando Nasser <fnasser@redhat.com> - 0:0.9.1-1jpp
- Upgrade to 0.9.1
- Disable attempt to include external jars

* Mon Apr 25 2005 Fernando Nasser <fnasser@redhat.com> - 0:0.8.1-3jpp
- Changes to use locally installed DTDs
- Do not try and access sun site for linking javadoc

* Mon Aug 23 2004 Randy Watler <rwatler at finali.com> - 0:0.8.1-2jpp
- Rebuild with ant-1.6.2

* Mon Jan 26 2004 David Walluck <david@anti-microsoft.org> 0:0.8.1-1jpp
- release
