%bcond_with check

%global packname knitr
%global packver  1.31
%global rlibdir  %{_datadir}/R/library

%global __suggests_exclude ^R\\((JuliaCall|gifski|magick|rgl|sass|webshot)\\)

%global with_loop 1
# Mostly unnecessary for a simple build, plus a lot depend on knitr.
%global with_suggests 0

Name:             R-%{packname}
Version:          1.31
Release:          1%{?dist}
Summary:          A General-Purpose Package for Dynamic Report Generation in R

License:          GPLv2+
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-evaluate >= 0.10, R-highr, R-methods, R-markdown, R-stringr >= 0.6, R-yaml >= 2.1.19, R-xfun >= 0.19, R-tools
# Suggests:  R-formatR, R-testit, R-digest, R-rgl >= 0.95.1201, R-codetools, R-rmarkdown, R-htmlwidgets >= 0.7, R-webshot, R-tikzDevice >= 0.10, R-tinytex, R-reticulate >= 1.4, R-JuliaCall >= 0.11.1, R-magick, R-png, R-jpeg, R-gifski, R-xml2 >= 1.2.0, R-httr, R-DBI >= 0.4-1, R-showtext, R-tibble, R-sass, R-ragg, R-styler >= 1.2.0
# LinkingTo:
# Enhances:

BuildArch:        noarch
Recommends:       tex(framed.sty)
Recommends:       tex(listings.sty)
BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-evaluate >= 0.10
BuildRequires:    R-highr
BuildRequires:    R-methods
BuildRequires:    R-markdown
BuildRequires:    R-stringr >= 0.6
BuildRequires:    R-yaml >= 2.1.19
BuildRequires:    R-xfun >= 0.19
BuildRequires:    R-tools
%if %{with check}
BuildRequires:    R-testit
BuildRequires:    R-digest
BuildRequires:    R-codetools
BuildRequires:    R-htmlwidgets >= 0.7
BuildRequires:    R-tikzDevice >= 0.10
BuildRequires:    R-tinytex
BuildRequires:    R-png
BuildRequires:    R-jpeg
BuildRequires:    R-xml2 >= 1.2.0
BuildRequires:    R-DBI >= 0.4.1
BuildRequires:    R-showtext
%if %{with_loop}
BuildRequires:    R-formatR
BuildRequires:    R-rmarkdown
%endif
%if %{with_suggests}
BuildRequires:    R-rgl >= 0.95.1201
BuildRequires:    R-webshot
BuildRequires:    R-reticulate >= 1.4
BuildRequires:    R-JuliaCall >= 0.11.1
BuildRequires:    R-magick
BuildRequires:    R-gifski
BuildRequires:    R-httr
BuildRequires:    R-tibble
BuildRequires:    R-sass
BuildRequires:    R-ragg
BuildRequires:    R-styler >= 1.2.0
# Mostly examples.
BuildRequires:    lyx
BuildRequires;    tex(animate.sty)
BuildRequires;    tex(relsize.sty)
BuildRequires;    tex(beamer.cls)
BuildRequires;    tex(tufte-handout.cls)
%endif
%endif

%description
Provides a general-purpose tool for dynamic report generation in R using
Literate Programming techniques.


%prep
%setup -q -c -n %{packname}

# Can't run from installed location anyway.
rm %{packname}/inst/examples/knit-all.R


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

mkdir %{buildroot}%{_bindir}
sed -e '1d;2i#!%{_bindir}/Rscript' %{buildroot}%{rlibdir}/%{packname}/bin/knit > %{buildroot}%{_bindir}/knit
chmod --reference=%{buildroot}%{rlibdir}/%{packname}/bin/knit %{buildroot}%{_bindir}/knit
touch -r %{buildroot}%{rlibdir}/%{packname}/bin/knit %{buildroot}%{_bindir}/knit
rm -r %{buildroot}%{rlibdir}/%{packname}/bin


%check
%if %{with check}
export LANG=C.UTF-8
%if ! %{with_suggests} || ! %{with_loop}
export _R_CHECK_FORCE_SUGGESTS_=0
%endif
%if ! %{with_loop}
ARGS=--no-examples
%endif

%{_bindir}/R CMD check %{packname} $ARGS
%endif


%files
%{_bindir}/knit
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NEWS.Rd
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/examples
%{rlibdir}/%{packname}/misc
%{rlibdir}/%{packname}/opencpu
%{rlibdir}/%{packname}/shiny
%{rlibdir}/%{packname}/themes


%changelog
* Sun Feb 07 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.31-1
- Update to latest version (#1921250)

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.30-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Sep 23 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.30-1
- Update to latest version (#1881633)

* Fri Aug 14 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.29-1
- Update to latest version (#1849954)

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.28-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun  5 2020 Tom Callaway <spot@fedoraproject.org> - 1.28-2
- conditionalize check to get this built (half the R universe depends on it)
- rebuild for R 4

* Mon Feb 24 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.28-1
- Update to latest version

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.26-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 13 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.26-1
- Update to latest version

* Wed Nov 06 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.25-2
- Exclude Suggests for unavailable packages

* Sat Sep 21 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.25-1
- Update to latest version

* Sat Aug 17 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.24-1
- Update to latest version

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.23-3
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat May 18 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.23-1
- Update to latest version

* Sat Mar 09 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.22-1
- Update to latest version

* Thu Feb 21 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.21-1
- Update to latest version

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.20-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 05 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.20-1
- Update to latest version

* Tue May 01 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.18-1
- Update to latest version
- Rewrite using latest template

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Nov 10 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> 1.17-2
- Fix license tag
- Fix embedding script paths

* Fri Aug 25 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> 1.17-1
- initial package for Fedora
