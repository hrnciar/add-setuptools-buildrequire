%global major 5

Name:           GLee
Version:        %{major}.4.0
Release:        19%{?dist}
Summary:        GL Easy Extension library

License:        BSD
URL:            http://elf-stone.com/glee.php
Source0:        http://www.elf-stone.com/downloads/%{name}/%{name}-%{version}-src.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  mesa-libGL-devel
BuildRequires: make

%description
GLee (GL Easy Extension library) is a free cross-platform extension loading
library for OpenGL. It provides seamless support for OpenGL functions up
to version 3.0 and 399 extensions. 


%package devel
Summary:        Development headers for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       mesa-libGL-devel

%description devel
Development headers for %{name}


%prep
%setup -q -c %{name}-%{version}

sed -i "s|\r||g" *.h *.c *.txt
chmod -x *.h *.c *.txt
iconv -f=iso-8859-1 -t=utf-8 readme.txt > tmp && mv tmp readme.txt

sed -i -e '/${LDCONFIG}/d' Makefile.in
sed -i -e '/doc/d' Makefile.in

sed -i 's|-shared|-shared -Wl,-soname,lib%{name}.so.%{major} -fPIC|g' Makefile.in
sed -i 's|LIBNAME=.*|LIBNAME=lib%{name}.so.%{version}|g' Makefile.in


%build
%configure
%make_build


%install
install -dm755 %{buildroot}%{_includedir}/GL
install -dm755 %{buildroot}%{_libdir}
make install INCLUDEDIR=%{buildroot}%{_includedir} \
             LIBDIR=%{buildroot}%{_libdir}
ln -s lib%{name}.so.%{version} %{buildroot}%{_libdir}/lib%{name}.so


%ldconfig_scriptlets


%files
%{_libdir}/lib%{name}.so.*
%doc readme.txt


%files devel
%{_libdir}/lib%{name}.so
%{_includedir}/GL/%{name}.h
%doc extensionList.txt


%changelog
* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Sep 14 2017 Lubomir Rintel <lkundrak@v3.sk> - 5.4.0-12
- Minor cleanups for re-review

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.4.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 5.4.0-8
- Rebuilt for GCC 5 C++11 ABI change

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Aug 07 2010 Hicham HAOUARI <hicham.haouari@gmail.com> - 5.4.0-1
- Initial package
