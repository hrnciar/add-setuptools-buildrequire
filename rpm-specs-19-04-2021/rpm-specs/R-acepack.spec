%global packname  acepack
%global packver   1.4.1

Name:             R-%{packname}
Version:          %{packver}
Release:          15%{?dist}
Summary:          ACE and AVAS methods for choosing regression transformations
License:          Public Domain and MIT
URL:              http://cran.r-project.org/web/packages/acepack/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz
Source1:          ace-copyright.txt
BuildRequires:    R-devel >= 3.4.0, gcc-gfortran
BuildRequires:    R-testthat

%description
ACE and AVAS (additivity and variance stabilization) are used to estimate 
transformations for regression.

%prep
%setup -c -q -n %{packname}
cp %{SOURCE1} .
%build

%install
mkdir -p %{buildroot}%{_libdir}/R/library
R CMD INSTALL %{packname} -l %{buildroot}%{_libdir}/R/library 
# Clean up in advance of check
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
%{__rm} -rf %{buildroot}%{_libdir}/R/library/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{_libdir}/R/library/%{packname}
%doc %{_libdir}/R/library/%{packname}/html
%doc %{_libdir}/R/library/%{packname}/DESCRIPTION
%doc %{_libdir}/R/library/%{packname}/NEWS
%doc %{_libdir}/R/library/%{packname}/README*
%doc %{_libdir}/R/library/%{packname}/ace.doc
%license %{_libdir}/R/library/%{packname}/LICENSE
%license ace-copyright.txt
%{_libdir}/R/library/%{packname}/INDEX
%{_libdir}/R/library/%{packname}/libs/
%{_libdir}/R/library/%{packname}/Meta
%{_libdir}/R/library/%{packname}/NAMESPACE
%{_libdir}/R/library/%{packname}/R
%{_libdir}/R/library/%{packname}/help

%changelog
* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 12 2020 Tom Callaway <spot@fedoraproject.org> - 1.4.1-13
- rebuild for R 4.0.0

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 12 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.4.1-11
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed May 16 2018 Tom Callaway <spot@fedoraproject.org> - 1.4.1-7
- rebuild for R 3.5.0

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Feb  2 2018 Tom Callaway <spot@fedoraproject.org> - 1.4.1-5
- rebuild for new libgfortran

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu May 18 2017 Tom Callaway <spot@fedoraproject.org> - 1.4.1-2
- rebuild for R 3.4.0

* Tue Feb 14 2017 Tom Callaway <spot@fedoraproject.org> - 1.4.1-1
- update to 1.4.1

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.3.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Jan 24 2014 Tom Callaway <spot@fedoraproject.org> - 1.3.3.3-1
- update to 1.3-3.3

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Apr 11 2013 Tom Callaway <spot@fedoraproject.org> - 1.3.3.2-1
- update to 1.3.3.2

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Nov  9 2011 Tom Callaway <spot@fedoraproject.org> - 1.3.3.0-1
- update to 1.3-3.0
- rebuild for R 2.14.0

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jan 21 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 1.3.2.3-1
- update to 1.3-2.3
- fix FTBFS

* Tue Aug 11 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 1.3.2.2-7
- fix versioning

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 13 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.3-4
- rebuild for new gcc

* Mon Jan  7 2008 Alex Lancaster <alexlan[AT]fedoraproject org> - 1.3-3
- BuildRequires: R-devel rather than just R

* Tue Nov 20 2007 Tom "spot" Callaway <tcallawa@redhat.com> 1.3-2
- BuildRequires: gfortran

* Tue Oct 30 2007 Tom "spot" Callaway <tcallawa@redhat.com> 1.3-1
- initial package for Fedora
