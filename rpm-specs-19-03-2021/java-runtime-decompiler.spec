Summary: Application for extraction and decompilation of JVM byte code
Name: java-runtime-decompiler
Version: 4.0
Release: 3%{?dist}
License: GPLv3
URL: https://github.com/pmikova/java-runtime-decompiler
Source0: https://github.com/pmikova/%{name}/archive/%{name}-%{version}.tar.gz
Source1: java-runtime-decompiler
Source2: java-runtime-decompiler.1
Source3: jrd.desktop
Source4: java-runtime-decompiler8
Patch0: remove_rsyntaxtextarea.patch
Patch1: systemFernflower.patch
Patch2: systemProcyon.patch
Patch3: rsyntaxVersion.patch
BuildArch: noarch
BuildRequires: maven-local
BuildRequires: byteman
BuildRequires: rsyntaxtextarea
BuildRequires: junit5
BuildRequires: ant-junit5
BuildRequires: junit
BuildRequires: ant-junit
BuildRequires: maven-surefire-provider-junit
BuildRequires: maven-surefire-provider-junit5
BuildRequires: maven-surefire
BuildRequires: maven-surefire-plugin
BuildRequires: maven-clean-plugin
# depends on devel, not runtime (needs tools.jar, javap attach and manyn others)
BuildRequires: java-11-devel
BuildRequires: java-1.8.0-devel
BuildRequires: google-gson
BuildRequires: desktop-file-utils
Requires: java-11-devel
Recommends: fernflower
Recommends: procyon-decompiler

%description
This application can access JVM memory at runtime,
extract byte code from the JVM and decompile it. 

%package javadoc
Summary: Javadoc for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%package jdk8
Summary: jdk8 comaptible version of %{name}, may miss sme features
Requires: java-1.8.0-devel
Recommends: fernflower
Recommends: procyon-decompiler

%description jdk8
jdk8 comaptible version of %{name}, may miss sme features.
Eg rich text area is missng or the agent need to be adjusted manually

%prep
%setup -q -n %{name}-%{name}-%{version}
%patch0 -p1
%patch1 -p0
%patch2 -p0

%build
pushd runtime-decompiler
%pom_remove_plugin :maven-jar-plugin
popd

export JAVA_HOME=/usr/lib/jvm/java-1.8.0-openjdk
pushd runtime-decompiler
%pom_add_dep com.sun:tools
popd
%mvn_build --xmvn-javadoc --skip-javadoc --skip-install -- -Plegacy
find | grep .jar$
mv -v ./decompiler_agent/target/decompiler-agent-%{version}.0-SNAPSHOT.jar     ../decompiler-agent8.jarx  #to avoid being mvn installed
mv -v ./runtime-decompiler/target/runtime-decompiler-%{version}.0-SNAPSHOT.jar ../runtime-decompiler8.jarx #to avoid being mvn installed
xmvn clean

export JAVA_HOME=/usr/lib/jvm/java-11-openjdk
patch -p1 -R < %{PATCH0}
patch -p0 < %{PATCH3}
pushd runtime-decompiler
%pom_remove_dep com.sun:tools
popd
%mvn_build --xmvn-javadoc

%install
%mvn_install
install -d -m 755 $RPM_BUILD_ROOT%{_mandir}/man1/
install -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_mandir}/man1/

install -d -m 755 $RPM_BUILD_ROOT%{_bindir}
install -m 755 %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/
install -m 755 %{SOURCE4} $RPM_BUILD_ROOT%{_bindir}/
install -d -m 755 $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/
cp -r %{_builddir}/%{name}-%{name}-%{version}/runtime-decompiler/src/plugins/ $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/

install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install --vendor="fedora"                     \
--dir=${RPM_BUILD_ROOT}%{_datadir}/applications %{SOURCE3}

mkdir -p $RPM_BUILD_ROOT%{_datadir}/java/%{name}-jdk8
cp -v %{_builddir}/decompiler-agent8.jarx $RPM_BUILD_ROOT%{_datadir}/java/%{name}-jdk8/decompiler-agent8.jar
cp -v %{_builddir}/runtime-decompiler8.jarx  $RPM_BUILD_ROOT%{_datadir}/java/%{name}-jdk8/runtime-decompiler8.jar


%files -f .mfiles
%attr(755, root, -) %{_bindir}/java-runtime-decompiler
%{_mandir}/man1/java-runtime-decompiler.1*
# wrappers for decompilers shared with jdk8 subpackage
%dir %{_sysconfdir}/%{name}
%dir %{_sysconfdir}/%{name}/plugins
%config %{_sysconfdir}/%{name}/plugins/FernflowerDecompilerWrapper.java
%config(noreplace) %{_sysconfdir}/%{name}/plugins/FernflowerDecompilerWrapper.json
%config %{_sysconfdir}/%{name}/plugins/ProcyonDecompilerWrapper.java
%config(noreplace) %{_sysconfdir}/%{name}/plugins/ProcyonDecompilerWrapper.json
%license LICENSE

%dir %{_datadir}/applications
%{_datadir}/applications/fedora-jrd.desktop

%files javadoc -f .mfiles-javadoc
%license LICENSE

%files jdk8
%attr(755, root, -) %{_bindir}/java-runtime-decompiler8
%dir %{_datadir}/java/%{name}-jdk8
%{_datadir}/java/%{name}-jdk8/runtime-decompiler8.jar
%{_datadir}/java/%{name}-jdk8/decompiler-agent8.jar
# wrappers for decompilers shared with main
%dir %{_sysconfdir}/%{name}
%dir %{_sysconfdir}/%{name}/plugins
%config %{_sysconfdir}/%{name}/plugins/FernflowerDecompilerWrapper.java
%config(noreplace) %{_sysconfdir}/%{name}/plugins/FernflowerDecompilerWrapper.json
%config %{_sysconfdir}/%{name}/plugins/ProcyonDecompilerWrapper.java
%config(noreplace) %{_sysconfdir}/%{name}/plugins/ProcyonDecompilerWrapper.json
%license LICENSE

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec 08 2020 Jiri Vanek <jvanek@redhat.com> - 4.0-2
- Added subpackage built by jdk8 to allow looking into jdk8 apps
- for some reason, jdk8 vm can not look into jdk11 vm, even if agent is correctly jdk8 version
- the config is still share, which is stupid, but I doubt there is another target audeince then me

* Tue Dec 08 2020 Jiri Vanek <jvanek@redhat.com> - 4.0-1
- built by jdk11

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 3.0-8
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Tue Mar 17 2020 Jiri Vanek <jvanek@redhat.com> - 3.0-7
- aligned rsyntaxtextarea version, fixed javadoc generation

* Tue Mar 17 2020 Jiri Vanek <jvanek@redhat.com> - 3.0-6
- changed jdk8 requirement

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Aug 27 2019 Jiri Vanek <jvanek@redhat.com> - 3.0-3
- all stdouts from customlauncher moved to stderr

* Mon Aug 26 2019 Jiri Vanek <jvanek@redhat.com> - 3.0-0
- moved to usptream version 3.0
- adjusted configs, removed lambda patch

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 17 2019 Jiri Vanek <jvanek@redhat.com> - 2.0-5
- improved Patch3, includeLambdas.patch to sort the lamdas t the bottom

* Thu Jan 17 2019 Jiri Vanek <jvanek@redhat.com> - 2.0-4
- added depndence of procyon decompiler (currenlty under review
- added and applied Patch2, systemProcyon.patch to enable system procyon out of thebox
- added and applied Patch3, includeLambdas.patch to at least list lamdas untill fixed in upstream

* Thu Jan 10 2019 Jiri Vanek <jvanek@redhat.com> - 2.0-3
- added depndence of fernflower decompiler
- added and applied Patch1, systemFernflower.patch to enable system fernflower

* Wed Nov 28 2018 Petra Mikova <petra.alice.mikova@gmail.com> - 2.0-2
- fixed changelog

* Mon Nov 19 2018 Petra Mikova <petra.alice.mikova@gmail.com> - 2.0-1
- fixed issues listed in review (rhbz#1636019)
- added installation of desktop file

* Wed Jun 06 2018 Petra Mikova <petra.alice.mikova@gmail.com> - 1.1-1
- initial commit
