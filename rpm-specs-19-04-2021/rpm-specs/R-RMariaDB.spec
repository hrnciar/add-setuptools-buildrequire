%global packname RMariaDB
%global packver  1.1.0
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          1.1.0
Release:          2%{?dist}
Summary:          Database Interface and 'MariaDB' Driver

License:          GPLv3
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-bit64, R-DBI >= 1.1.0, R-hms >= 0.5.0, R-lubridate, R-methods, R-Rcpp >= 0.12.4
# Suggests:  R-covr, R-DBItest >= 1.7.0, R-rprojroot, R-testthat, R-withr
# LinkingTo: R-BH, R-plogr, R-Rcpp
# Enhances:

BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-bit64
BuildRequires:    R-DBI >= 1.1.0
BuildRequires:    R-hms >= 0.5.0
BuildRequires:    R-lubridate
BuildRequires:    R-methods
BuildRequires:    R-Rcpp-devel >= 0.12.4
BuildRequires:    R-BH-devel
BuildRequires:    R-plogr-devel
BuildRequires:    R-DBItest >= 1.7.0
BuildRequires:    R-rprojroot
BuildRequires:    R-testthat
BuildRequires:    R-withr
BuildRequires:    mariadb-connector-c-devel

%description
Implements a 'DBI'-compliant interface to 'MariaDB'
(<https://mariadb.org/>) and 'MySQL' (<https://www.mysql.com/>) databases.


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
* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 08 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.0-1
- Update to latest version (#1913590)

* Mon Dec 21 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.11-1
- Update to latest version (#1908256)

* Fri Aug 28 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.10-1
- Update to latest version

* Fri Aug 14 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.9-2
- Rebuild to fix dist tag

* Sun Aug 09 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.9-1
- initial package for Fedora
