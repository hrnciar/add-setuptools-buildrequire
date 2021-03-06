Name:           bgpq3
Version:        0.1.31
Release:        9%{?dist}
Summary:        Automate BGP filter generation based on routing database information

License:        BSD
URL:            http://snar.spb.ru/prog/bgpq3/
Source0:        http://snar.spb.ru/prog/bgpq3/%{name}-%{version}.tgz
#Patch to fix:
# -destdir
# remove -O0 for optimization
# remove -s so that it does not strip debugging
Patch0:         bgpq3-fix-makefile.patch

BuildRequires:  gcc
BuildRequires: make
%description
You are running BGP in your network and want to automate 
filter generation for your routers? Well, with BGPQ3 it's easy.

%prep
%autosetup

%build
%configure
%make_build

%install
%make_install

%files
%doc CHANGES
%license COPYRIGHT
%{_bindir}/bgpq3
%{_mandir}/man8/bgpq3.8*


%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.31-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.31-8
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.31-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.31-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.31-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.31-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.31-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.31-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Sep 23 2017 Bennie Joubert <bennie.joubert@jsdaav.com> - 0.1.31-1
- Initial package.  
