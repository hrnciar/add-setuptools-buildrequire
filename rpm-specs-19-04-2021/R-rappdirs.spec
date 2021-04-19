%global packname rappdirs
%global packver  0.3.3
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          0.3.3
Release:          1%{?dist}
Summary:          Application Directories: Determine Where to Save Data, Caches, and Logs

License:          MIT
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:
# Suggests:  R-testthat >= 3.0.0, R-roxygen2, R-covr, R-withr
# LinkingTo:
# Enhances:

BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-roxygen2
BuildRequires:    R-testthat >= 3.0.0
BuildRequires:    R-withr

%description
An easy way to determine which directories on the users computer you should
use to save data, caches and logs. A port of Python's 'Appdirs'
(<https://github.com/ActiveState/appdirs>) to R.


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
%license %{rlibdir}/%{packname}/LICENSE
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%dir %{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/libs/%{packname}.so


%changelog
* Tue Feb 23 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.3.3-1
- Update to latest version (#1921163)

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-7
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun  7 2020 Tom Callaway <spot@fedoraproject.org> - 0.3.1-5
- rebuild for R 4

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.3.1-3
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May 15 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.3.1-1
- initial package for Fedora
