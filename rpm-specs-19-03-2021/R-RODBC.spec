%global packname  RODBC
%global packver   1.3
%global packrel   17

Name:             R-%{packname}
Version:          %{packver}.%{packrel}
Release:          3%{?dist}
Summary:          An ODBC database interface for R
License:          GPLv2 or GPLv3
URL:              http://cran.r-project.org/web/packages/RODBC/
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{packver}-%{packrel}.tar.gz
BuildRequires:    R-devel >= 3.0.0, tetex-latex, unixODBC-devel, texinfo-tex

%description
An ODBC database interface for R.

%prep
%setup -c -q -n %{packname}
%build

%install
mkdir -p %{buildroot}%{_libdir}/R/library
%{_bindir}/R CMD INSTALL %{packname} -l %{buildroot}%{_libdir}/R/library 
# Clean up in advance of check
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -rf %{buildroot}%{_libdir}/R/library/R.css
rm -rf %{buildroot}%{_libdir}/R/library/RODBC/doc/Makefile

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{_libdir}/R/library/%{packname}
%doc %{_libdir}/R/library/%{packname}/html
%doc %{_libdir}/R/library/%{packname}/DESCRIPTION
%dir %{_libdir}/R/library/%{packname}/doc/
%doc %{_libdir}/R/library/%{packname}/doc/index.html
%doc %{_libdir}/R/library/%{packname}/doc/RODBC.*
%dir %{_libdir}/R/library/%{packname}/po/
%lang(da) %{_libdir}/R/library/%{packname}/po/da/
%lang(de) %{_libdir}/R/library/%{packname}/po/de/
%lang(en) %{_libdir}/R/library/%{packname}/po/en*/
%lang(pl)  %{_libdir}/R/library/%{packname}/po/pl/
%{_libdir}/R/library/%{packname}/INDEX
%{_libdir}/R/library/%{packname}/NAMESPACE
%{_libdir}/R/library/%{packname}/Meta
%{_libdir}/R/library/%{packname}/R
%{_libdir}/R/library/%{packname}/help
%{_libdir}/R/library/%{packname}/libs/
%{_libdir}/R/library/%{packname}/tests.R

%changelog
* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun  3 2020 Tom Callaway <spot@fedoraproject.org> - 1.3.17-1
- update to 1.3-17, rebuild for R 4

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.15-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 12 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.3.15-9
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.15-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.15-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.15-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu May 17 2018 Tom Callaway <spot@fedoraproject.org> - 1.3.15-5
- rebuild for R 3.5.0

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed May 31 2017 Tom Callaway <spot@fedoraproject.org> - 1.3.15
- update to 1.3-15

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Jan 24 2014 Tom Callaway <spot@fedoraproject.org> - 1.3.10-1
- update to 1.3-10

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Apr 11 2013 Tom Callaway <spot@fedoraproject.org> - 1.3.6-1
- update to 1.3.6

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Nov  8 2011 Tom Callaway <spot@fedoraproject.org> - 1.3.3-1
- update to 1.3-3
- rebuild for R 2.14.0

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jan 21 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 1.3.1-1
- update to 1.3-1

* Tue Aug 11 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 1.3.0-1
- Update to 1.3-0

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Mar 28 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 1.2-2
- fix licensing tag

* Fri Mar 20 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 1.2-1
- initial package for Fedora
