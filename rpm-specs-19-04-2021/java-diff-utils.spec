Name:           java-diff-utils
Version:        4.9
Release:        2%{?dist}
Summary:        Java library to create and apply patches

License:        ASL 2.0
URL:            https://java-diff-utils.github.io/java-diff-utils/
Source0:        https://github.com/%{name}/%{name}/archive/%{name}-parent-%{version}.tar.gz
# Eliminate all but 1 unchecked or unsafe operations
# https://github.com/java-diff-utils/java-diff-utils/pull/108
Patch0:         %{name}-unchecked.patch
# Fix some incorrect javadoc constructs
# https://github.com/java-diff-utils/java-diff-utils/pull/109
Patch1:         %{name}-javadoc.patch

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.surefire:surefire-junit-platform)
BuildRequires:  mvn(org.apiguardian:apiguardian-api)
BuildRequires:  mvn(org.assertj:assertj-core)
BuildRequires:  mvn(org.eclipse.jgit:org.eclipse.jgit)
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter)

BuildArch:      noarch

%global _desc %{expand:
The Java Diff Utils library is an open source library for performing
comparison operations between texts: computing diffs, applying patches,
generating or parsing unified diffs, generating diff output for easy
display (e.g., side-by-side view), and so on.}

%description %_desc

%package        parent
Summary:        Java Diff Utils parent POM

%description    parent %_desc

This package contains the parent POM for Java Diff Utils.

%package        jgit
Summary:        Java Diff Utils extension using jgit difference algorithms
Requires:       %{name} = %{version}-%{release}

%description    jgit %_desc

This package contains an extension to the main package that uses jgit's
difference algorithms.

%{?javadoc_package}

%prep
%autosetup -n %{name}-%{name}-parent-%{version} -p0

# Unnecessary plugins for an RPM build
%pom_remove_plugin -r :maven-checkstyle-plugin
%pom_remove_plugin -r :maven-javadoc-plugin
%pom_remove_plugin :maven-release-plugin

%build
%mvn_build -s

%install
%mvn_install

%files -f .mfiles-java-diff-utils
%license LICENSE

%files parent -f .mfiles-java-diff-utils-parent
%license LICENSE

%files jgit -f .mfiles-java-diff-utils-jgit

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Nov 24 2020 Jerry James <loganjerry@gmail.com> - 4.9-1
- Initial RPM
