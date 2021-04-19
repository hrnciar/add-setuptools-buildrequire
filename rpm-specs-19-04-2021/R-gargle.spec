%global packname gargle
%global packver  1.1.0
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          1.1.0
Release:          1%{?dist}
Summary:          Utilities for Working with Google APIs

License:          MIT
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-cli >= 2.3.1, R-fs >= 1.3.1, R-glue >= 1.3.0, R-httr >= 1.4.0, R-jsonlite, R-rappdirs, R-rlang >= 0.4.9, R-rstudioapi, R-stats, R-withr
# Suggests:  R-covr, R-httpuv, R-knitr, R-mockr, R-rmarkdown, R-sodium, R-spelling, R-testthat >= 3.0.0
# LinkingTo:
# Enhances:

BuildArch:        noarch
BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-cli >= 2.3.1
BuildRequires:    R-fs >= 1.3.1
BuildRequires:    R-glue >= 1.3.0
BuildRequires:    R-httr >= 1.4.0
BuildRequires:    R-jsonlite
BuildRequires:    R-rappdirs
BuildRequires:    R-rlang >= 0.4.9
BuildRequires:    R-rstudioapi
BuildRequires:    R-stats
BuildRequires:    R-withr
BuildRequires:    R-httpuv
BuildRequires:    R-knitr
BuildRequires:    R-mockr
BuildRequires:    R-rmarkdown
BuildRequires:    R-sodium
BuildRequires:    R-spelling
BuildRequires:    R-testthat >= 3.0.0

%description
Provides utilities for working with Google APIs
<https://developers.google.com/apis-explorer>.  This includes functions and
classes for handling common credential types and for preparing, executing, and
processing HTTP requests.


%prep
%setup -q -c -n %{packname}

# Don't need coverage; it's not packaged either.
sed -i 's/covr, //g' %{packname}/DESCRIPTION


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
%{rlibdir}/%{packname}/discovery-doc-ingest
%{rlibdir}/%{packname}/secret
%{rlibdir}/%{packname}/WORDLIST


%changelog
* Sat Apr 03 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.0-1
- Update to latest version (#1945859)

* Fri Mar 05 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.0-1
- Update to latest version (#1934743)

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun  7 2020 Tom Callaway <spot@fedoraproject.org> - 0.5.0-2
- rebuild for R 4

* Thu May 21 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.5.0-1
- Update to latest version

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Oct 06 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.4.0-1
- Update to latest version

* Mon Aug 26 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.3.1-1
- initial package for Fedora
