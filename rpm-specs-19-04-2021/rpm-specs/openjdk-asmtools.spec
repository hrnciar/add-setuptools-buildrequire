#Definig major and minor because Version allows only '-'
%global major 7.0
%global minor b10
#Using pre-release snapshot versioning
%global commit 7eadbbf8f41b8174f7991a5ad1fe79519fe108d4
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate 20210122

Name:           openjdk-asmtools
Version:        %{major}.%{minor}
Release:        0.1.%{commitdate}.git%{shortcommit}%{?dist}
Summary:        To develop tools create proper & improper Java '.class' files

License:        GPLv2+
URL:            https://github.com/openjdk/asmtools
#If we use regular versioning then Source0 looks as below
#Source0:        https://github.com/openjdk/%%{name}/archive/%%{major}-%%{minor}.tar.gz
#As we are using pre-release snapshot versioning, Source0 looks as below
#To download source: spectool -g openjdk-asmtools.spec
Source0:        https://github.com/openjdk/asmtools/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
Source1:        openjdk-asmtools.in
Source2:        openjdk-asmtools.1

BuildArch:      noarch

BuildRequires:  java-devel
BuildRequires:  maven-local
BuildRequires:  maven-compiler-plugin
BuildRequires:  maven-jar-plugin
Requires:  java-headless

%description
AsmTools helps develop tools to create proper and improper Java '.class' files.
Aids various Java .class based testing and OpenJDK development applications.
Asmtools supports latest class file formats, in lock-step with JDK development.
AsmTools consist of a set of (Java class file) assembler/dis-assemblers:
Jasm/Jdis:
An assembler language to provide Java-like declaration of member signatures,
providing Java VM specification compliant mnemonics for byte-code instructions.
JCod/JDec:
An assembler language to provide byte-code containers of class-file constructs.

%package        javadoc
Summary:        Javadoc for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
#This is commented till the version on the master branch is released
#%%setup -q -n asmtools-%%{version}
#Added to handle pre-release version
%autosetup -n asmtools-%{commit}

%build
cd maven
sed -i "s|ln -sv|cp -r|g" mvngen.sh
sh mvngen.sh
%mvn_build

%install
rm -rf $RPM_BUILD_ROOT
pushd maven
%mvn_install
popd

mkdir -p $RPM_BUILD_ROOT%{_bindir}/
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1/
install -d -m 755 $RPM_BUILD_ROOT%{_bindir}
#!/bin/sh
for launcher in "" "-jasm" "-jdis" "-jcoder" "-jdec" "-jcdec"; do
  switch=`echo $launcher |sed "s/-//"`
  cat %{SOURCE1} | sed "s/@SCD@/$switch/"  > $RPM_BUILD_ROOT%{_bindir}/%{name}$launcher
done
install -d -m 755 $RPM_BUILD_ROOT%{_mandir}/man1/
install -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_mandir}/man1/

%files -f maven/.mfiles
%license LICENSE
%doc README.md
%attr(755, root, -) %{_bindir}/*
%{_mandir}/man1/openjdk-asmtools.1*

%files javadoc -f maven/.mfiles-javadoc

%changelog
* Wed Jan 27 2021 Jayashree Huttanagoudar <jhuttana@redhat.com> - 7.0.b10-0.1.20210122.git7eadbbf
- Initial openjdk-asmtools package for fedora
