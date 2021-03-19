%global packname  rhub
%global rlibdir  %{_datadir}/R/library

# Tests require the network
%bcond_with network

Name:             R-%{packname}
Version:          1.1.1
Release:          7%{?dist}
Summary:          Connect to 'R-hub'

License:          MIT
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-assertthat, R-callr, R-cli >= 1.1.0, R-crayon, R-desc, R-digest, R-httr, R-jsonlite, R-parsedate, R-pillar, R-prettyunits, R-processx, R-R6, R-rappdirs, R-rcmdcheck >= 1.2.1, R-rematch, R-tibble, R-utils, R-uuid, R-whoami, R-withr
# Suggests:  R-covr, R-testthat, R-knitr, R-rmarkdown
# LinkingTo:
# Enhances:

BuildArch:        noarch
BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-assertthat
BuildRequires:    R-callr
BuildRequires:    R-cli >= 1.1.0
BuildRequires:    R-crayon
BuildRequires:    R-desc
BuildRequires:    R-digest
BuildRequires:    R-httr
BuildRequires:    R-jsonlite
BuildRequires:    R-parsedate
BuildRequires:    R-pillar
BuildRequires:    R-prettyunits
BuildRequires:    R-processx
BuildRequires:    R-R6
BuildRequires:    R-rappdirs
BuildRequires:    R-rcmdcheck >= 1.2.1
BuildRequires:    R-rematch
BuildRequires:    R-tibble
BuildRequires:    R-utils
BuildRequires:    R-uuid
BuildRequires:    R-whoami
BuildRequires:    R-withr
BuildRequires:    R-testthat
BuildRequires:    R-knitr
BuildRequires:    R-rmarkdown

%description
Run 'R CMD check' on any of the 'R-hub' (<https://builder.r-hub.io/>)
architectures, from the command line. The current architectures include
Windows, macOS, Solaris and various Linux distributions.


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
%if %{with network}
%{_bindir}/R CMD check %{packname}
%else
%{_bindir}/R CMD check %{packname} --no-tests
%endif


%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/bin


%changelog
* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun  7 2020 Tom Callaway <spot@fedoraproject.org> - 1.1.1-5
- rebuild for R 4

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.1-3
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 19 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.1-1
- initial package for Fedora
