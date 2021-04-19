%global packname procmaps
%global packver  0.0.3
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          0.0.3
Release:          2%{?dist}
Summary:          Portable Address Space Mapping

# Overall: GPLv3; bundled gperftools code: BSD
# Note, gperftools code is some internal portion of it, so cannot be unbundled.
License:          GPLv3 and BSD
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:
# Suggests:  R-covr, R-testthat, R-tibble
# LinkingTo:
# Enhances:

BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-covr
BuildRequires:    R-testthat
BuildRequires:    R-tibble

%description
Portable '/proc/self/maps' as a data frame. Determine which library or
other region is mapped to a specific address of a process. -- R packages
can contain native code, compiled to shared libraries at build or
installation time. When loaded, each shared library occupies a portion of
the address space of the main process. When only a machine instruction
pointer is available (e.g. from a backtrace during error inspection or
profiling), the address space map determines which library this instruction
pointer corresponds to.


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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%dir %{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/libs/%{packname}.so
%{rlibdir}/%{packname}/WORDLIST


%changelog
* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Oct 10 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.0.3-1
- initial package for Fedora
