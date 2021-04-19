%bcond_with bootstrap

%global packname rprojroot
%global packver  2.0.2
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          2.0.2
Release:          2%{?dist}
Summary:          Finding Files in Project Subdirectories

License:          MIT
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:
# Suggests:  R-covr, R-knitr, R-lifecycle, R-mockr, R-rmarkdown, R-testthat >= 3.0.0, R-withr
# LinkingTo:
# Enhances:

BuildArch:        noarch
BuildRequires:    R-devel
BuildRequires:    tex(latex)
%if %{without bootstrap}
BuildRequires:    R-knitr
BuildRequires:    R-lifecycle
BuildRequires:    R-mockr
BuildRequires:    R-rmarkdown
BuildRequires:    R-testthat >= 3.0.0
BuildRequires:    R-withr
%endif

%description
Robust, reliable and flexible paths to files below a project root. The
'root' of a project is defined as a directory that matches a certain
criterion, e.g., it contains a certain regular file.


%prep
%setup -q -c -n %{packname}

# Don't need coverage.
sed -i 's/covr, //' %{packname}/DESCRIPTION


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css


%check
%if %{without bootstrap}
export NOT_CRAN=true
%{_bindir}/R CMD check %{packname}
%else
_R_CHECK_FORCE_SUGGESTS_=0 %{_bindir}/R CMD check %{packname} --no-tests
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
%{rlibdir}/%{packname}/WORDLIST


%changelog
* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Nov 15 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.0.2-1
- Update to latest version (#1897908)
- Rename check and with_doc conditions to bootstrap

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun  3 2020 Tom Callaway <spot@fedoraproject.org> - 1.3.2-8
- conditionalize check to break testthat loop
- rebuild for R 4

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.3.2-6
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Mar 06 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.3.2-4
- Enable docs and fuller test suite

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Apr 26 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.3.2-1
- Update to latest version

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Nov 09 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> 1.2-1
- initial package for Fedora
