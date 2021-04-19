%global packname qcc

Name:             R-%{packname}
Version:          2.7
Release:          3%{?dist}
Source0:          http://cran.r-project.org/src/contrib/qcc_%{version}.tar.gz
License:          GPLv2+
URL:              http://cran.r-project.org/web/packages/qcc/index.html
Summary:          SQC package for R
BuildRequires:    R-devel >= 3.0.0, tex(latex)
BuildRequires:    R-knitr >= 1.12
BuildRequires:    R-rmarkdown >= 0.9
BuildArch:        noarch

%description
An R package for quality control charting and statistical process control.

The qcc package for the R statistical environment provides:
- Plot Shewhart quality control charts
- Plot Cusum and EMWA charts for continuous data
- Draw operating characteristic curves
- Perform process capability analysis
- Draw Pareto charts and cause-and-effect diagrams

%prep
%setup -q -c -n %{packname}
#Fix permissions
find -type f | xargs chmod -x
#Fix line ending
mv qcc/inst/CITATION qcc/inst/CITE
tr -d '\r' <qcc/inst/CITE >qcc/inst/CITATION
rm -f qcc/inst/CITE

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/R/library
%{_bindir}/R CMD INSTALL -l $RPM_BUILD_ROOT%{_datadir}/R/library %{packname}
# Clean up in advance of check
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -rf $RPM_BUILD_ROOT%{_datadir}/R/library/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{_datadir}/R/library/%{packname}
%doc %{_datadir}/R/library/%{packname}/html
%doc %{_datadir}/R/library/%{packname}/CITATION
%doc %{_datadir}/R/library/%{packname}/DESCRIPTION
%doc %{_datadir}/R/library/%{packname}/NEWS
%{_datadir}/R/library/%{packname}/doc
%{_datadir}/R/library/%{packname}/INDEX
%{_datadir}/R/library/%{packname}/NAMESPACE
%{_datadir}/R/library/%{packname}/Meta
%{_datadir}/R/library/%{packname}/R
%{_datadir}/R/library/%{packname}/data
%{_datadir}/R/library/%{packname}/help

%changelog
* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun  5 2020 Tom Callaway <spot@fedoraproject.org> - 2.7-1
- update to 2.7
- rebuild for R 4

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 12 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.2-18
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 02 2018 José Abílio Matos <jamatos@fc.up.pt> - 2.2-14
- rebuild with R 3.5.0

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Apr 11 2013 Tom Callaway <spot@fedoraproject.org> - 2.2-6
- rebuild for R3

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Dec  5 2011 John J. McDonough <jjmcd@fedoraproject.org> - 2.2-3
- Remove extraneout BuildRoot and clean

* Sat Dec  3 2011 John J. McDonough <jjmcd@fedoraproject.org> - 2.2-2
- Minor .spec changes

* Sat Nov 19 2011 John J. McDonough <jjmcd@fedoraproject.org> - 2.2-1
- Updated tar from upstream
- Adjust DOS format inst/CITATION

* Fri Nov  2 2011 John J. McDonough <jjmcd@fedoraproject.org> - 2.0.1-2
- Reflect updated .spec template
- Correct spec problems

* Fri Jul 15 2011 John J. McDonough <jjmcd@fedoraproject.org> - 2.0.1-1
- Initial RPM

