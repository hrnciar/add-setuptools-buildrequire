%global packname parallelly
%global packver  1.24.0
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          1.24.0
Release:          1%{?dist}
Summary:          Enhancing the 'parallel' Package

License:          LGPLv2+
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-parallel, R-tools, R-utils
# Suggests:
# LinkingTo:
# Enhances:

BuildArch:        noarch
BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-parallel
BuildRequires:    R-tools
BuildRequires:    R-utils

%description
Utility functions that enhance the 'parallel' package and support the
built-in parallel backends of the 'future' package.  For example,
availableCores() gives the number of CPU cores available to your R process
as given by the operating system, 'cgroups' and Linux containers, R
options, and environment variables, including those set by job schedulers
on high-performance compute clusters. If none is set, it will fall back to
parallel::detectCores(). Another example is makeClusterPSOCK(), which is
backward compatible with parallel::makePSOCKcluster() while doing a better
job in setting up remote cluster workers without the need for configuring
the firewall to do port-forwarding to your local computer.


%prep
%setup -q -c -n %{packname}


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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/WORDLIST


%changelog
* Sun Mar 14 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.24.0-1
- Update to latest version (#1938591)

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.23.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 10 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.23.0-1
- Update to latest version (#1912610)

* Fri Jan 01 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.22.0-1
- Update to latest version (#1911873)

* Fri Dec 04 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.21.0-1
- initial package for Fedora
