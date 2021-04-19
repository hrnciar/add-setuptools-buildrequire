%global packname MatrixGenerics
%global packver 1.2.1

Name:             R-%{packname}
Version:          %{packver}
Release:          1%{?dist}
Source0:          http://www.bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{packver}.tar.gz
License:          Artistic 2.0
URL:              http://www.bioconductor.org/packages/release/bioc/html/%{packname}.html
Summary:          S4 Generic Summary Statistic Functions that Operate on Matrix-Like Objects
BuildRequires:    R-devel >= 3.4.0, tetex-latex, R-methods, R-matrixStats > 0.57.0
BuildArch:        noarch

%description
S4 generic functions modeled after the 'matrixStats' API for alternative matrix
implementations. Packages with alternative matrix implementation can depend on
this package and implement the generic functions that are defined here for a
useful set of row and column summary statistics. Other package developers can
import this package and handle a different matrix implementations without
worrying about incompatibilities.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p $RPM_BUILD_ROOT%{_datadir}/R/library
%{_bindir}/R CMD INSTALL -l $RPM_BUILD_ROOT%{_datadir}/R/library %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -rf $RPM_BUILD_ROOT%{_datadir}/R/library/R.css

%check
# Too many missing deps
# %%{_bindir}/R CMD check %%{packname}

%files
%dir %{_datadir}/R/library/%{packname}
%doc %{_datadir}/R/library/%{packname}/html
%{_datadir}/R/library/%{packname}/DESCRIPTION
%{_datadir}/R/library/%{packname}/INDEX
%{_datadir}/R/library/%{packname}/NAMESPACE
%{_datadir}/R/library/%{packname}/NEWS.Rd
%{_datadir}/R/library/%{packname}/Meta
%{_datadir}/R/library/%{packname}/help
%{_datadir}/R/library/%{packname}/R

%changelog
* Wed Feb  3 2021 Tom Callaway <spot@fedoraproject.org> - 1.2.1-1
- initial package
