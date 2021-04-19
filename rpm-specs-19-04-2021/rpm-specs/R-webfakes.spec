%global packname webfakes
%global packver  1.1.1
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          1.1.1
Release:          1%{?dist}
Summary:          Fake Web Apps for HTTP Testing

License:          MIT
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-stats, R-tools, R-utils
# Suggests:  R-callr, R-curl, R-glue, R-jsonlite, R-httr, R-httpuv, R-testthat >= 3.0.0, R-withr, R-xml2
# LinkingTo:
# Enhances:

BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-stats
BuildRequires:    R-tools
BuildRequires:    R-utils
BuildRequires:    R-callr
BuildRequires:    R-curl
BuildRequires:    R-glue
BuildRequires:    R-jsonlite
BuildRequires:    R-httr
BuildRequires:    R-httpuv
BuildRequires:    R-testthat >= 3.0.0
BuildRequires:    R-withr
BuildRequires:    R-xml2

%description
Create a web app that makes it easier to test web clients without using the
internet. It includes a web app framework with path matching, parameters
and templates. Can parse various 'HTTP' request bodies. Can send 'JSON'
data or files from the disk. Includes a web app that implements the
<https://httpbin.org> web service.


%prep
%setup -q -c -n %{packname}


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css


%check
%{_bindir}/R CMD check %{packname}


%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS.md
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%dir %{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/libs/%{packname}.so
%{rlibdir}/%{packname}/credits
%{rlibdir}/%{packname}/examples
%{rlibdir}/%{packname}/views


%changelog
* Tue Mar 02 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.1-1
- initial package for Fedora
