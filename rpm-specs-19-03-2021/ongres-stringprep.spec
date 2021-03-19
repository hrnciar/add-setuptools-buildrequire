%global     upstream_name   stringprep

Name:       ongres-%upstream_name
Version:    1.1
Release:    1%{?dist}
Summary:    RFC 3454 Preparation of Internationalized Strings in pure Java
License:    BSD
URL:            https://github.com/ongres/%upstream_name
Source0:        https://github.com/ongres/%upstream_name/archive/%{version}/%upstream_name-%{version}.tar.gz
BuildRequires:  maven-local
BuildRequires:  junit5
BuildRequires:  velocity
BuildRequires:  maven-plugin-build-helper
BuildRequires:  exec-maven-plugin
BuildRequires:  maven-enforcer-plugin
BuildArch:  noarch

%description
The stringprep protocol does not stand on its own;
it has to be used by other protocols at precisely-defined 
places in those other protocols.

%package javadoc
Summary:    Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}

%prep
%autosetup -p1 -n "%upstream_name-%{version}"
find \( -name '*.jar' -o -name '*.class' \) -delete

%pom_remove_dep :velocity-tools codegenerator

%pom_remove_plugin :nexus-staging-maven-plugin
%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin -r :maven-javadoc-plugin

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%license LICENSE

%files javadoc -f .mfiles-javadoc
%license LICENSE

%changelog
* Fri Feb 12 2021 Ondrej Dubaj <odubaj@redhat.com> - 1.1-1
- initial rpm
