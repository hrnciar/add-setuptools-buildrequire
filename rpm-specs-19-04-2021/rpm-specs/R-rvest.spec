%global packname rvest
%global packver  1.0.0
%global rlibdir  %{_datadir}/R/library

# Some things use the network.
%bcond_with network

Name:             R-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          Easily Harvest (Scrape) Web Pages

License:          MIT
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz
Patch0001:        0001-Skip-some-tests-if-offline.patch

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-httr >= 0.5, R-lifecycle >= 1.0.0, R-magrittr, R-rlang >= 0.4.10, R-selectr, R-tibble, R-xml2 >= 1.3
# Suggests:  R-covr, R-glue, R-knitr, R-readr, R-rmarkdown, R-repurrrsive, R-spelling, R-stringi >= 0.3.1, R-testthat >= 3.0.2, R-webfakes
# LinkingTo:
# Enhances:

BuildArch:        noarch
BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-httr >= 0.5
BuildRequires:    R-lifecycle >= 1.0.0
BuildRequires:    R-magrittr
BuildRequires:    R-rlang >= 0.4.10
BuildRequires:    R-selectr
BuildRequires:    R-tibble
BuildRequires:    R-xml2 >= 1.3
BuildRequires:    R-glue
BuildRequires:    R-knitr
BuildRequires:    R-readr
BuildRequires:    R-rmarkdown
BuildRequires:    R-repurrrsive
BuildRequires:    R-spelling
BuildRequires:    R-stringi >= 0.3.1
BuildRequires:    R-testthat >= 3.0.2
BuildRequires:    R-webfakes

%description
Wrappers around the 'xml2' and 'httr' packages to make it easy to download,
then manipulate, HTML and XML.


%prep
%setup -q -c -n %{packname}

pushd %{packname}
%patch0001 -p1

# Don't need coverage; it's not packaged either.
sed -i 's/covr, //g' DESCRIPTION
popd


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css


%check
%if %{with network}
%{_bindir}/R CMD check %{packname}
%else
%{_bindir}/R CMD check %{packname} --no-examples --no-vignettes
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
%{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/html-ex
%{rlibdir}/%{packname}/WORDLIST


%changelog
* Wed Mar 10 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.0-1
- Update to latest version (#1937095)

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jul 26 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.3.6-1
- Update to latest version

* Sun Jun  7 2020 Tom Callaway <spot@fedoraproject.org> - 0.3.5-3
- rebuild for R 4

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 13 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.3.5-1
- Update to latest version

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.3.4-3
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May 15 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.3.4-1
- Update to latest version

* Thu Apr 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.3.3-1
- Update to latest version

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed May 02 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.3.2-1
- initial package for Fedora
