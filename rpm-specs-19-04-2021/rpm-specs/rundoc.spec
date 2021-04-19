Name:           rundoc
Version:        0.11
Release:        16%{?dist}
Summary:        An Ant task designed to help with the single-sourcing of program documentation

License:        BSD
URL:            http://www.martiansoftware.com/lab/rundoc/
Source0:        http://martiansoftware.com/lab/rundoc/rundoc-0.11-src.zip
BuildArch:      noarch

BuildRequires:  ant
BuildRequires:  javapackages-local
#/usr/share/java must be owned: 
Requires:       javapackages-tools


%description
An Ant task designed to help with the single-sourcing of program documentation.

%package	javadoc
Summary:        Javadocs for %{name}
%description    javadoc
This package contains the API documentation for %{name}.


%prep
%setup -qc -n %{name}-%{version}

rm %{name}-%{version}.jar
rm -rf javadoc/ 

%build
ant jar javadoc


%install
mkdir -p %{buildroot}%{_javadir}
install -pm  0755 dist/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

mkdir -p %{buildroot}%{_javadocdir}/
mv javadoc/ %{buildroot}%{_javadocdir}/%{name}


%files 
%{_javadir}/%{name}.jar
%doc LICENSE.txt

%files javadoc
%doc LICENSE.txt
%{_javadocdir}/%{name}


%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 11 2020 Jiri Vanek <jvanek@redhat.com> - 0.11-14
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Aug 20 2014 Ismael Olea <ismael@olea.org> - 0.11-4
- final suggestion: https://bugzilla.redhat.com/show_bug.cgi?id=1130755#c9

* Mon Aug  18 2014 Ismael Olea <ismael@olea.org> - 0.11-3
- all suggestions from https://bugzilla.redhat.com/show_bug.cgi?id=1130755#c1

* Mon Aug  18 2014 Ismael Olea <ismael@olea.org> - 0.11-2
- sonme suggestions from https://bugzilla.redhat.com/show_bug.cgi?id=1130755#c1

* Sat Aug  16 2014 Ismael Olea <ismael@olea.org> - 0.11-1
- first release
