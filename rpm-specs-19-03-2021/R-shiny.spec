%global packname shiny
%global packver  1.5.0
%global rlibdir  %{_datadir}/R/library

%global __suggests_exclude ^R\\((dygraphs|reactlog)\\)

%bcond_without bootstrap
%global with_suggests 0

Name:             R-%{packname}
Version:          1.5.0
Release:          3%{?dist}
Summary:          Web Application Framework for R

# Mainly GPLv3, JavaScript files are a mix of BSD and MIT; see bundling list below.
License:          GPLv3 and BSD and MIT and OFL
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:   R-methods
# Imports:   R-utils, R-grDevices, R-httpuv >= 1.5.2, R-mime >= 0.3, R-jsonlite >= 0.9.16, R-xtable, R-digest, R-htmltools >= 0.4.0.9003, R-R6 >= 2.0, R-sourcetools, R-later >= 1.0.0, R-promises >= 1.1.0, R-tools, R-crayon, R-rlang >= 0.4.0, R-fastmap >= 1.0.0, R-withr, R-commonmark >= 1.7, R-glue >= 1.3.2
# Suggests:  R-datasets, R-Cairo >= 1.5-5, R-testthat >= 2.1.1, R-knitr >= 1.6, R-markdown, R-rmarkdown, R-ggplot2, R-reactlog >= 1.0.0, R-magrittr, R-shinytest, R-yaml, R-future, R-dygraphs, R-ragg, R-showtext
# LinkingTo:
# Enhances:

BuildArch:        noarch
BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-methods
BuildRequires:    R-utils
BuildRequires:    R-grDevices
BuildRequires:    R-httpuv >= 1.5.2
BuildRequires:    R-mime >= 0.3
BuildRequires:    R-jsonlite >= 0.9.16
BuildRequires:    R-xtable
BuildRequires:    R-digest
BuildRequires:    R-htmltools >= 0.4.0.9003
BuildRequires:    R-R6 >= 2.0
BuildRequires:    R-sourcetools
BuildRequires:    R-later >= 1.0.0
BuildRequires:    R-promises >= 1.1.0
BuildRequires:    R-tools
BuildRequires:    R-crayon
BuildRequires:    R-rlang >= 0.4.0
BuildRequires:    R-fastmap >= 1.0.0
BuildRequires:    R-withr
BuildRequires:    R-commonmark >= 1.7
BuildRequires:    R-glue >= 1.3.2
BuildRequires:    R-datasets
BuildRequires:    R-Cairo >= 1.5.5
BuildRequires:    R-testthat >= 2.1.1
BuildRequires:    R-knitr >= 1.6
BuildRequires:    R-markdown
BuildRequires:    R-rmarkdown
BuildRequires:    R-ggplot2
BuildRequires:    R-magrittr
BuildRequires:    R-yaml
BuildRequires:    R-future
BuildRequires:    R-ragg
BuildRequires:    R-showtext
%if %{without bootstrap}
BuildRequires:    R-reactlog >= 1.0.0
BuildRequires:    R-shinytest
%endif
%if %{with_suggests}
BuildRequires:    R-dygraphs
%endif

#
# Unbundle some things and mark others.
#

# Bootstrap, not in Fedora properly.
# shiny/inst/www/shared/bootstrap/: MIT
Provides:         bundled(xstatic-bootstrap-common) = 3.4.1

BuildRequires:    xstatic-datatables-common >= 1.10.5
Requires:         xstatic-datatables-common >= 1.10.5

# Should be >=1.6.4, but 1.3.1.0 works too.
BuildRequires:    xstatic-bootstrap-datepicker-common
Requires:         xstatic-bootstrap-datepicker-common

# Too old in Fedora to unbundle.
# shiny/inst/www/shared/fontawesome/: OFL and MIT
Provides:         bundled(fontawesome-fonts) = 5.13.0
Provides:         bundled(fontawesome-fonts-web) = 5.13.0

# shiny/inst/www/shared/highlight/: BSD
Provides:         bundled(js-highlight) = 6.2
# shiny/inst/www/shared/ionrangeslider/: MIT
Provides:         bundled(js-ionrangeslider) = 2.1.6
# shiny/inst/www/shared/jquery-*: MIT
# shiny/inst/www/shared/legacy: MIT
Provides:         bundled(js-jquery) = 3.5.1
# shiny/inst/www/shared/jqueryui/: MIT
Provides:         bundled(xstatic-jquery-ui-common) = 1.12.1
# shiny/inst/www/shared/json2-min.js: *No copyright* UNKNOWN
Provides:         bundled(json2) = 2014.02.04
# shiny/inst/www/shared/selectize/: ASL 2.0
Provides:         bundled(selectize) = 0.11.2
# shiny/inst/www/shared/showdown/: BSD
Provides:         bundled(nodejs-showdown) = 0.3.1
# shiny/inst/www/shared/strftime/strftime-min.js: Mit
Provides:         bundled(js-strftime) = 0.9.2

%description
Makes it incredibly easy to build interactive web applications with R.
Automatic "reactive" binding between inputs and outputs and extensive prebuilt
widgets make it possible to build beautiful, responsive, and powerful
applications with minimal effort.


%prep
%setup -q -c -n %{packname}


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

# Unbundle things; can't be done before install since it copies symlink targets.

# DataTables
rm -r %{buildroot}%{rlibdir}/%{packname}/www/shared/datatables/css/dataTables.bootstrap.css
rm -r %{buildroot}%{rlibdir}/%{packname}/www/shared/datatables/{images,js,upgrade1.10.txt}
for f in /usr/share/javascript/datatables/css/*; do
    ln -s $f %{buildroot}%{rlibdir}/%{packname}/www/shared/datatables/css${f##*/}
done
ln -s /usr/share/javascript/datatables/images \
    %{buildroot}%{rlibdir}/%{packname}/www/shared/datatables/images
ln -s /usr/share/javascript/datatables/js \
    %{buildroot}%{rlibdir}/%{packname}/www/shared/datatables/js

rm -r %{buildroot}%{rlibdir}/%{packname}/www/shared/datepicker/*
mkdir %{buildroot}%{rlibdir}/%{packname}/www/shared/datepicker/css
ln -s /usr/share/javascript/bootstrap_datepicker/datepicker3.css \
    %{buildroot}%{rlibdir}/%{packname}/www/shared/datepicker/css/bootstrap-datepicker3.css
mkdir %{buildroot}%{rlibdir}/%{packname}/www/shared/datepicker/js
ln -s /usr/share/javascript/bootstrap_datepicker/bootstrap-datepicker.js \
    %{buildroot}%{rlibdir}/%{packname}/www/shared/datepicker/js/bootstrap-datepicker.js
ln -s /usr/share/javascript/bootstrap_datepicker/locales \
    %{buildroot}%{rlibdir}/%{packname}/www/shared/datepicker/js/locales


%check
%if %{without bootstrap}
%{_bindir}/R CMD check %{packname}
%else
_R_CHECK_FORCE_SUGGESTS_=0 %{_bindir}/R CMD check %{packname}
%endif


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
%{rlibdir}/%{packname}/app_template
%{rlibdir}/%{packname}/examples
%{rlibdir}/%{packname}/template
%{rlibdir}/%{packname}/www-dir
%{rlibdir}/%{packname}/www


%changelog
* Tue Feb 23 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.5.0-3
- Re-bundle jQuery libraries
- Fix License tag to include bundled library licenses

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Aug 14 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.5.0-1
- Update to latest version (#1850173)

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.4.0.2-3
- Re-bundle showdown

* Sun Jun  7 2020 Tom Callaway <spot@fedoraproject.org> - 1.4.0.2-2
- rebuild for R 4

* Sun Mar 15 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.4.0.2-1
- Update to latest version

* Wed Mar 04 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.4.0-3
- Re-bundle highlighjs, which is broken in Fedora

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Oct 16 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.4.0-1
- Update to latest version

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.3.2-3
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 23 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.3.2-1
- initial package for Fedora
