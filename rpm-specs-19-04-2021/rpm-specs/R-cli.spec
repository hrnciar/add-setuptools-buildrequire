%bcond_with bootstrap

%global packname cli
%global packver  2.4.0
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          2.4.0
Release:          1%{?dist}
Summary:          Helpers for Developing Command Line Interfaces

License:          MIT
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-glue, R-methods, R-utils
# Suggests:  R-callr, R-covr, R-grDevices, R-htmlwidgets, R-knitr, R-mockery, R-ps >= 1.3.4.9000, R-rmarkdown, R-rstudioapi, R-prettycode >= 1.1.0, R-testthat, R-withr
# LinkingTo:
# Enhances:

BuildArch:        noarch
BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-glue
BuildRequires:    R-methods
BuildRequires:    R-utils
%if %{without bootstrap}
BuildRequires:    R-callr
BuildRequires:    R-grDevices
BuildRequires:    R-htmlwidgets
BuildRequires:    R-knitr
BuildRequires:    R-mockery
BuildRequires:    R-ps >= 1.3.4.9000
BuildRequires:    R-rmarkdown
BuildRequires:    R-rstudioapi
BuildRequires:    R-prettycode >= 1.1.0
BuildRequires:    R-testthat
BuildRequires:    R-withr
%endif

%description
A suite of tools to build attractive command line interfaces ('CLIs'), from
semantic elements: headings, lists, alerts, paragraphs, etc. Supports
custom themes via a 'CSS'-like language. It also contains a number of lower
level 'CLI' elements: rules, boxes, trees, and 'Unicode' symbols with
'ASCII' alternatives. It support ANSI colors and text styles as well.


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
%if %{without bootstrap}
export LANG=C.UTF-8
%{_bindir}/R CMD check %{packname}
%endif


%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/examples
%{rlibdir}/%{packname}/logo.txt
%{rlibdir}/%{packname}/scripts


%changelog
* Tue Apr 06 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.4.0-1
- Update to latest version (#1946272)

* Tue Feb 23 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.3.1-1
- Update to latest version (#1932004)

* Sun Feb 07 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.3.0-1
- Update to latest version (#1922820)

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Nov 28 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.2.0-1
- Update to latest version (#1899946)
- Rename check conditional to bootstrap

* Mon Oct 12 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.1.0-1
- Update to latest version (#1887512)

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun  3 2020 Tom Callaway <spot@fedoraproject.org> - 2.0.2-2
- conditionalize check to break testthat loop
- rebuild for R 4

* Fri Feb 28 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.0.2-1
- Update to latest version

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 09 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.0.1-1
- Update to latest version

* Tue Jan 07 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.0.0-1
- Update to latest version

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.0-3
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Mar 20 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.0-1
- Update to latest version

* Thu Feb 21 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.1-1
- Update to latest version

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 14 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> 1.0.0-1
- initial package for Fedora
