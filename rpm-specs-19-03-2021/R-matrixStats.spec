%global packname  matrixStats
%global packver   0.58.0

Name:             R-%{packname}
Version:          %{packver}
Release:          1%{?dist}
Summary:          Functions that Apply to Rows and Columns of Matrices (and to Vectors)
License:          Artistic 2.0
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz
BuildRequires:    R-devel >= 3.4.0

%description
High-performing functions operating on rows and columns of matrices, e.g. 
col / rowMedians(), col / rowRanks(), and col / rowSds(). Functions optimized 
per data type and for subsetted calculations such that both memory usage and 
processing time is minimized. There are also optimized vector-based methods, 
e.g. binMeans(), madDiff() and weightedMedian().

%prep
%setup -c -q -n %{packname}
sed -i "s/\r//g" %{packname}/NEWS

%build

%install
mkdir -p %{buildroot}%{_libdir}/R/library
R CMD INSTALL %{packname} -l %{buildroot}%{_libdir}/R/library 
# Clean up in advance of check
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
%{__rm} -rf %{buildroot}%{_libdir}/R/library/R.css

%check
# Too many missing deps
# %%{_bindir}/R CMD check %%{packname}

%files
%dir %{_libdir}/R/library/%{packname}
%doc %{_libdir}/R/library/%{packname}/html
%{_libdir}/R/library/%{packname}/DESCRIPTION
%doc %{_libdir}/R/library/%{packname}/NEWS
%{_libdir}/R/library/%{packname}/INDEX
%{_libdir}/R/library/%{packname}/libs/
%{_libdir}/R/library/%{packname}/Meta
%{_libdir}/R/library/%{packname}/NAMESPACE
%{_libdir}/R/library/%{packname}/R
%{_libdir}/R/library/%{packname}/benchmarking
%{_libdir}/R/library/%{packname}/doc
%{_libdir}/R/library/%{packname}/help
%{_libdir}/R/library/%{packname}/WORDLIST

%changelog
* Tue Feb  2 2021 Tom Callaway <spot@fedoraproject.org> - 0.58.0-1
- update to 0.58.0

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.56.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.56.0-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.56.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun  5 2020 Tom Callaway <spot@fedoraproject.org> - 0.56.0-1
- rebuild for R 4
- update to 0.56.0

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.55.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov  6 2019 Tom Callaway <spot@fedoraproject.org> - 0.55.0-1
- update to 0.55.0

* Mon Aug 12 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.54.0-3
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.54.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Feb 11 2019 Tom Callaway <spot@fedoraproject.org> - 0.54.0-1
- Update to 0.54.0

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.53.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.53.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu May 17 2018 Tom Callaway <spot@fedoraproject.org> - 0.53.1-2
- Rebuild for R 3.5.0

* Fri Mar 23 2018 Tom Callaway <spot@fedoraproject.org> - 0.53.1-1
- update to 0.53.1

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.52.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.52.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.52.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed May 31 2017 Tom Callaway <spot@fedoraproject.org> - 0.52.2-1
- initial package
