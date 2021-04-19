%bcond_without bootstrap

%global packname isoband
%global packver  0.2.4
%global rlibdir  %{_libdir}/R/library

%global __suggests_exclude ^R\\((sf)\\)

Name:             R-%{packname}
Version:          0.2.4
Release:          1%{?dist}
Summary:          Generate Isolines and Isobands from Regularly Spaced Elevation Grids

License:          MIT
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz
Patch0001:        0001-Unbundle-catch1.patch

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-grid, R-utils
# Suggests:  R-covr, R-ggplot2, R-knitr, R-magick, R-microbenchmark, R-rmarkdown, R-sf, R-testthat, R-xml2
# LinkingTo:
# Enhances:

BuildRequires:    catch1-devel
BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-grid
BuildRequires:    R-utils
BuildRequires:    R-knitr
BuildRequires:    R-microbenchmark
BuildRequires:    R-rmarkdown
BuildRequires:    R-testthat
BuildRequires:    R-xml2
%if %{without bootstrap}
BuildRequires:    R-ggplot2
BuildRequires:    R-magick
BuildRequires:    R-sf
%endif

%description
A fast C++ implementation to generate contour lines (isolines) and contour
polygons (isobands) from regularly spaced grids containing elevation data.


%prep
%setup -q -c -n %{packname}

pushd %{packname}
%patch0001 -p1
popd


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css


%check
%if %{without bootstrap}
%{_bindir}/R CMD check %{packname}
%else
_R_CHECK_FORCE_SUGGESTS_=0 %{_bindir}/R CMD check %{packname} --no-examples --no-vignettes || ( cat %{packname}.Rcheck/tests/testthat.R* && exit 1 )
%endif


%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS.md
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/extdata
%dir %{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/libs/%{packname}.so


%changelog
* Wed Mar 10 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.2.4-1
- Update to latest version (#1934758)
- Un-bundle catch1, to fix build with latest glibc

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Dec 04 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.2.3-1
- Update to latest version (#1903110)

* Mon Aug 03 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.2.2-1
- initial package for Fedora
