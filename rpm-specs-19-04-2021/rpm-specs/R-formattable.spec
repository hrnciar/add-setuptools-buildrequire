%global packname formattable
%global packver  0.2.1
%global rlibdir  %{_datadir}/R/library

# Not available yet.
%global with_suggests 0

Name:             R-%{packname}
Version:          0.2.1
Release:          2%{?dist}
Summary:          Create 'Formattable' Data Structures

License:          MIT
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-methods, R-htmltools, R-htmlwidgets, R-knitr, R-rmarkdown
# Suggests:  R-testthat, R-DT, R-shiny, R-covr
# LinkingTo:
# Enhances:

BuildArch:        noarch
BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-methods
BuildRequires:    R-htmltools
BuildRequires:    R-htmlwidgets
BuildRequires:    R-knitr
BuildRequires:    R-rmarkdown
BuildRequires:    R-testthat
BuildRequires:    R-DT
BuildRequires:    R-shiny

%description
Provides functions to create formattable vectors and data frames.
'Formattable' vectors are printed with text formatting, and formattable
data frames are printed with multiple types of formatting in HTML to
improve the readability of data presented in tabular form rendered in web
pages.


%prep
%setup -q -c -n %{packname}

# Don't need coverage; it's not packaged either.
sed -i 's/, covr//g' %{packname}/DESCRIPTION


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
%doc %{rlibdir}/%{packname}/NEWS
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/htmlwidgets


%changelog
* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 08 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.2.1-1
- Update to latest version (#1913976)

* Sun Aug 02 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.2.0.1-1
- initial package for Fedora
