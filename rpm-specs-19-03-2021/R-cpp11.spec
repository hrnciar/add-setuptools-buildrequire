%bcond_without bootstrap

%global packname cpp11
%global packver  0.2.6
%global rlibdir  %{_datadir}/R/library

%global __suggests_exclude ^R\\((decor)\\)

Name:             R-%{packname}
Version:          0.2.6
Release:          1%{?dist}
Summary:          A C++11 Interface for R's C Interface

License:          MIT
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:
# Suggests:  R-bench, R-brio, R-callr, R-cli, R-covr, R-decor, R-desc, R-ggplot2, R-glue, R-knitr, R-lobstr, R-mockery, R-progress, R-rmarkdown, R-scales, R-testthat, R-tibble, R-utils, R-vctrs, R-withr
# LinkingTo:
# Enhances:

BuildArch:        noarch
BuildRequires:    R-devel
BuildRequires:    tex(latex)
%if %{without bootstrap}
BuildRequires:    R-bench
BuildRequires:    R-brio
BuildRequires:    R-callr
BuildRequires:    R-cli
BuildRequires:    R-covr
BuildRequires:    R-decor
BuildRequires:    R-desc
BuildRequires:    R-ggplot2
BuildRequires:    R-glue
BuildRequires:    R-knitr
BuildRequires:    R-lobstr
BuildRequires:    R-mockery
BuildRequires:    R-progress
BuildRequires:    R-rmarkdown
BuildRequires:    R-scales
BuildRequires:    R-testthat
BuildRequires:    R-tibble
BuildRequires:    R-utils
BuildRequires:    R-vctrs
BuildRequires:    R-withr
%endif

%description
Provides a header only, C++11 interface to R's C interface.  Compared to
other approaches 'cpp11' strives to be safe against long jumps from the C
API as well as C++ exceptions, conform to normal R function semantics and
supports interaction with 'ALTREP' vectors.


%package devel
Summary:          Development files for %{name}
Requires:         %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for %{name}.


%prep
%setup -q -c -n %{packname}


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
_R_CHECK_FORCE_SUGGESTS_=0 %{_bindir}/R CMD check %{packname} --no-examples --no-tests --no-vignettes
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

%files devel
%{rlibdir}/%{packname}/include


%changelog
* Sun Feb 07 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.2.6-1
- Update to latest version (#1915572)

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Nov 06 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.2.4-1
- Update to latest version (#1895088)

* Wed Oct 14 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.2.3-1
- Update to latest version (#1888126)

* Fri Oct 02 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.2.2-1
- Update to latest version (#1884172)

* Wed Aug 12 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.2.1-1
- Update to latest version

* Mon Aug 10 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.1.0-1
- initial package for Fedora
