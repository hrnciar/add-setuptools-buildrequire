%global packname here
%global packver  1.0.1
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          1.0.1
Release:          2%{?dist}
Summary:          A Simpler Way to Find Your Files

License:          MIT
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-rprojroot >= 2.0.2
# Suggests:  R-conflicted, R-covr, R-fs, R-knitr, R-palmerpenguins, R-plyr, R-readr, R-rlang, R-rmarkdown, R-testthat, R-uuid, R-withr
# LinkingTo:
# Enhances:

BuildArch:        noarch
BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-rprojroot >= 2.0.2
BuildRequires:    R-conflicted
BuildRequires:    R-fs
BuildRequires:    R-knitr
# BuildRequires:    R-palmerpenguins
BuildRequires:    R-plyr
BuildRequires:    R-readr
BuildRequires:    R-rlang
BuildRequires:    R-rmarkdown
BuildRequires:    R-testthat
BuildRequires:    R-uuid
BuildRequires:    R-withr

%description
Constructs paths to your project's files. Declare the relative path of a
file within your project with 'i_am()'. Use the 'here()' function as a
drop-in replacement for 'file.path()', it will always locate the files
relative to your project root.


%prep
%setup -q -c -n %{packname}

# Coverage is not needed.
# palmerpenguins is just a demo project.
sed -i -e 's/covr, //g' -e 's/palmerpenguins, //g' %{packname}/DESCRIPTION


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
%doc %{rlibdir}/%{packname}/demo-project
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
* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Dec 13 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.1-1
- Update to latest version (#1907141)

* Sun Dec 06 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.0-1
- Update to latest version (#1897944)

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun  7 2020 Tom Callaway <spot@fedoraproject.org> - 0.1-5
- rebuild for R 4

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.1-3
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Feb 20 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.1-1
- initial package for Fedora
