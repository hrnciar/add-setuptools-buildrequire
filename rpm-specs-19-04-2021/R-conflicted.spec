%global packname conflicted
%global packver  1.0.4
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          1.0.4
Release:          2%{?dist}
Summary:          An Alternative Conflict Resolution Strategy

License:          GPLv3
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-rlang >= 0.3.4, R-memoise
# Suggests:  R-covr, R-crayon, R-dplyr, R-pkgdown, R-testthat
# LinkingTo:
# Enhances:

BuildArch:        noarch
BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-rlang >= 0.3.4
BuildRequires:    R-memoise
BuildRequires:    R-crayon
BuildRequires:    R-dplyr
BuildRequires:    R-pkgdown
BuildRequires:    R-testthat

%description
R's default conflict management system gives the most recently loaded
package precedence. This can make it hard to detect conflicts, particularly
when they arise because a package update creates ambiguity that did not
previously exist. 'conflicted' takes a different approach, making every
conflict an error and forcing you to choose which function to use.


%prep
%setup -q -c -n %{packname}

# Coverage is not needed.
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
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help


%changelog
* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Nov 15 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.4-1
- initial package for Fedora
