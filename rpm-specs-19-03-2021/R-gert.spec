%bcond_with network

%global packname gert
%global packver  1.2.0
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          1.2.0
Release:          1%{?dist}
Summary:          Simple Git Client for R

License:          MIT
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-askpass, R-credentials >= 1.2.1, R-openssl >= 1.4.1, R-rstudioapi >= 0.11, R-sys, R-zip >= 2.1.0
# Suggests:  R-spelling, R-knitr, R-rmarkdown, R-testthat
# LinkingTo:
# Enhances:

BuildRequires:    pkgconfig(libgit2)
BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-askpass
BuildRequires:    R-credentials >= 1.2.1
BuildRequires:    R-openssl >= 1.4.1
BuildRequires:    R-rstudioapi >= 0.11
BuildRequires:    R-sys
BuildRequires:    R-zip >= 2.1.0
BuildRequires:    R-spelling
BuildRequires:    R-knitr
BuildRequires:    R-rmarkdown
BuildRequires:    R-testthat

%description
Simple git client for R based on 'libgit2' with support for SSH and HTTPS
remotes. All functions in 'gert' use basic R data types (such as vectors
and data-frames) for their arguments and return values. User credentials
are shared with command line 'git' through the git-credential store and ssh
keys stored on disk or ssh-agent.


%prep
%setup -q -c -n %{packname}


%build


%install
export USE_SYSTEM_LIBGIT2=1
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css


%check
%if %{with network}
%{_bindir}/R CMD check %{packname}
%else
%{_bindir}/R CMD check %{packname} --no-examples
%endif


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
%dir %{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/libs/%{packname}.so
%{rlibdir}/%{packname}/WORDLIST


%changelog
* Tue Feb 23 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.2.0-1
- Update to latest version (#1920277)

* Sun Feb 07 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.0-1
- Update to latest version (#19202770

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Dec 26 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.2-1
- initial package for Fedora
