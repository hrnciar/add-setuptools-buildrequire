%bcond_with bootstrap

%global packname desc
%global packver  1.3.0
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          1.3.0
Release:          1%{?dist}
Summary:          Manipulate DESCRIPTION Files

License:          MIT
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-utils, R-R6, R-crayon, R-rprojroot
# Suggests:  R-covr, R-testthat, R-whoami, R-withr, R-spelling, R-gh
# LinkingTo:
# Enhances:

BuildArch:        noarch
BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-utils
BuildRequires:    R-R6
BuildRequires:    R-crayon
BuildRequires:    R-rprojroot
%if %{without bootstrap}
BuildRequires:    R-testthat
BuildRequires:    R-whoami
BuildRequires:    R-withr
BuildRequires:    R-spelling
BuildRequires:    R-gh
%endif

%description
Tools to read, write, create, and manipulate DESCRIPTION files. It is
intended for packages that create or manipulate other packages.


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
%doc %{rlibdir}/%{packname}/README.Rmd
%doc %{rlibdir}/%{packname}/README.html
%doc %{rlibdir}/%{packname}/NEWS.md
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/WORDLIST


%changelog
* Sat Mar 06 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.3.0-1
- Update to latest version (#1936004)
- Rename check conditional to bootstrap

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun  3 2020 Tom Callaway <spot@fedoraproject.org> - 1.2.0-7
- conditionalize check to break testthat loop
- rebuild for R 4

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.2.0-5
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri May 04 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.2.0-1
- initial package for Fedora
