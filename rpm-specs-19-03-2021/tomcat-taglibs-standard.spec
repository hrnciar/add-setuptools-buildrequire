%global short_name      taglibs-standard

Name:           tomcat-taglibs-standard
Version:        1.2.5
Release:        13%{?dist}
Epoch:          0
Summary:        Apache Standard Taglib
License:        ASL 2.0
URL:            http://tomcat.apache.org/taglibs/
Source0:        http://apache.cbox.biz/tomcat/taglibs/taglibs-standard-%{version}/taglibs-standard-%{version}-source-release.zip
Patch0: servlet31.patch

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(javax.el:el-api)
BuildRequires:  mvn(javax.servlet.jsp:jsp-api)
BuildRequires:  mvn(javax.servlet:servlet-api)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.taglibs:taglibs-parent:pom:)
BuildRequires:  mvn(org.easymock:easymock)
BuildRequires:  mvn(xalan:xalan)

Obsoletes: jakarta-taglibs-standard < 1.1.2-13

%description
An implementation of the JSP Standard Tag Library (JSTL).

%package        javadoc
Summary:        Javadoc for %{name}
Obsoletes: jakarta-taglibs-standard-javadoc < 1.1.2-13

%description    javadoc
Javadoc for %{name}.

%prep
%setup -q -n %{short_name}-%{version}
%patch0 -b .sav

%mvn_alias org.apache.taglibs:taglibs-standard-impl javax.servlet:jstl
%mvn_alias org.apache.taglibs:taglibs-standard-impl org.eclipse.jetty.orbit:javax.servlet.jsp.jstl
%mvn_alias org.apache.taglibs:taglibs-standard-compat org.eclipse.jetty.orbit:org.apache.taglibs.standard.glassfish

%build
%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8

%install
%mvn_install

%files -f .mfiles
%license LICENSE
%doc README_src.txt README_bin.txt NOTICE

%files javadoc -f .mfiles-javadoc
%license LICENSE
%doc NOTICE

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0:1.2.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0:1.2.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 18 2020 Fabio Valentini <decathorpe@gmail.com> - 0:1.2.5-11
- Set javac source and target to 1.8 to fix Java 11 builds.

* Sat Jul 11 2020 Jiri Vanek <jvanek@redhat.com> - 0:1.2.5-10
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0:1.2.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0:1.2.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0:1.2.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0:1.2.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0:1.2.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0:1.2.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Feb 07 2017 Michael Simacek <msimacek@redhat.com> - 0:1.2.5-3
- Regenerate buildrequires

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0:1.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Alexander Kurtakov <akurtako@redhat.com> 0:1.2.5-1
- Update to upstream 1.2.5

* Thu Mar 5 2015 Alexander Kurtakov <akurtako@redhat.com> 0:1.2.3-2
- Fix url.

* Wed Mar 4 2015 Alexander Kurtakov <akurtako@redhat.com> 0:1.2.3-1
- Initial package.
