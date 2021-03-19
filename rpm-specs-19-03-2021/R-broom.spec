%global packname broom
%global packver  0.7.5
%global rlibdir  %{_datadir}/R/library

# Too many optional things.
%bcond_with suggests

%if %{without suggests}
%global __suggests_exclude ^R\\((AER|Hmisc|Kendall|Lahman|akima|bbmle|betareg|binGroup|btergm|caret|drc|e1071|emmeans|epiR|ergm|fixest|gam|gamlss|gamlss\.data|glmnet|glmnetUtils|gmm|irlba|joineRML|ks|lavaan|leaps|lfe|lm.beta|lme4|lsmeans|maptools|mclogit|mclust|mediation|metafor|mfx|modeldata|modeltests|muhaz|network|ordinal|plm|psych|quantreg|robust|robustbase|rsample|spatialreg|spdep|speedglm|survey|tseries)\\)
%else
# Always legally problematic.
%global __suggests_exclude ^R\\((akima)\\)
%endif

Name:             R-%{packname}
Version:          0.7.5
Release:          1%{?dist}
Summary:          Convert Statistical Objects into Tidy Tibbles

License:          MIT
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-backports, R-dplyr >= 1.0.0, R-ellipsis, R-generics >= 0.0.2, R-glue, R-methods, R-purrr, R-rlang, R-stringr, R-tibble >= 3.0.0, R-tidyr >= 1.0.0
# Suggests:  R-AER, R-akima, R-AUC, R-bbmle, R-betareg, R-biglm, R-binGroup, R-boot, R-btergm, R-car, R-caret, R-cluster, R-cmprsk, R-coda, R-covr, R-drc, R-e1071, R-emmeans, R-epiR, R-ergm >= 3.10.4, R-fixest >= 0.5.0, R-gam >= 1.15, R-gamlss, R-gamlss.data, R-gamlss.dist, R-gee, R-geepack, R-ggplot2, R-glmnet, R-glmnetUtils, R-gmm, R-Hmisc, R-irlba, R-joineRML, R-Kendall, R-knitr, R-ks, R-Lahman, R-lavaan, R-leaps, R-lfe, R-lm.beta, R-lme4, R-lmodel2, R-lmtest >= 0.9.38, R-lsmeans, R-maps, R-maptools, R-margins, R-MASS, R-Matrix, R-mclust, R-mediation, R-metafor, R-mfx, R-mgcv, R-mlogit, R-modeldata, R-modeltests, R-muhaz, R-multcomp, R-network, R-nnet, R-orcutt >= 2.2, R-ordinal, R-plm, R-poLCA, R-psych, R-quantreg, R-Rchoice, R-rgeos, R-rmarkdown, R-robust, R-robustbase, R-rsample, R-sandwich, R-sp, R-spdep, R-spatialreg, R-speedglm, R-spelling, R-survey, R-survival, R-systemfit, R-testthat >= 2.1.0, R-tseries, R-vars, R-zoo
# LinkingTo:
# Enhances:

BuildArch:        noarch
BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-backports
BuildRequires:    R-dplyr >= 1.0.0
BuildRequires:    R-ellipsis
BuildRequires:    R-generics >= 0.0.2
BuildRequires:    R-glue
BuildRequires:    R-methods
BuildRequires:    R-purrr
BuildRequires:    R-rlang
BuildRequires:    R-stringr
BuildRequires:    R-tibble >= 3.0.0
BuildRequires:    R-tidyr >= 1.0.0
BuildRequires:    R-AUC
BuildRequires:    R-biglm
BuildRequires:    R-boot
BuildRequires:    R-car
BuildRequires:    R-cluster
BuildRequires:    R-coda
BuildRequires:    R-gamlss.dist
BuildRequires:    R-ggplot2
BuildRequires:    R-knitr
BuildRequires:    R-lmodel2
BuildRequires:    R-lmtest >= 0.9.38
BuildRequires:    R-maps
BuildRequires:    R-MASS
BuildRequires:    R-Matrix
BuildRequires:    R-mgcv
BuildRequires:    R-multcomp
BuildRequires:    R-nnet
BuildRequires:    R-orcutt >= 2.2
BuildRequires:    R-rgeos
BuildRequires:    R-rmarkdown
BuildRequires:    R-sp
BuildRequires:    R-spelling
BuildRequires:    R-survival
BuildRequires:    R-testthat >= 2.1.0
BuildRequires:    R-zoo
%if %{with suggests}
BuildRequires:    R-AER
BuildRequires:    R-bbmle
BuildRequires:    R-betareg
BuildRequires:    R-binGroup
BuildRequires:    R-btergm
BuildRequires:    R-caret
BuildRequires:    R-cmprsk
BuildRequires:    R-drc
BuildRequires:    R-e1071
BuildRequires:    R-emmeans
BuildRequires:    R-epiR
BuildRequires:    R-ergm >= 3.10.4
BuildRequires:    R-fixest >= 0.5.0
BuildRequires:    R-gam >= 1.15
BuildRequires:    R-gamlss
BuildRequires:    R-gamlss.data
BuildRequires:    R-gee
BuildRequires:    R-geepack
BuildRequires:    R-glmnet
BuildRequires:    R-glmnetUtils
BuildRequires:    R-gmm
BuildRequires:    R-Hmisc
BuildRequires:    R-irlba
BuildRequires:    R-joineRML
BuildRequires:    R-Kendall
BuildRequires:    R-ks
BuildRequires:    R-Lahman
BuildRequires:    R-lavaan
BuildRequires:    R-leaps
BuildRequires:    R-lfe
BuildRequires:    R-lm.beta
BuildRequires:    R-lme4
BuildRequires:    R-lsmeans
BuildRequires:    R-maptools
BuildRequires:    R-margins
BuildRequires:    R-mclust
BuildRequires:    R-mediation
BuildRequires:    R-metafor
BuildRequires:    R-mfx
BuildRequires:    R-mlogit
BuildRequires:    R-modeldata
BuildRequires:    R-modeltests
BuildRequires:    R-muhaz
BuildRequires:    R-network
BuildRequires:    R-ordinal
BuildRequires:    R-plm
BuildRequires:    R-poLCA
BuildRequires:    R-psych
BuildRequires:    R-quantreg
BuildRequires:    R-Rchoice
BuildRequires:    R-robust
BuildRequires:    R-robustbase
BuildRequires:    R-rsample
BuildRequires:    R-sandwich
BuildRequires:    R-spdep
BuildRequires:    R-spatialreg
BuildRequires:    R-speedglm
BuildRequires:    R-survey
BuildRequires:    R-systemfit
BuildRequires:    R-tseries
BuildRequires:    R-vars
%endif

%description
Summarizes key information about statistical objects in tidy tibbles. This
makes it easy to report results, create plots and consistently work with
large numbers of models at once. Broom provides three verbs that each
provide different types of information about a model. tidy() summarizes
information about model components such as coefficients of a regression.
glance() reports information about an entire model, such as goodness of fit
measures like AIC and BIC. augment() adds information about individual
observations to a dataset, such as fitted values or influence measures.


%prep
%setup -q -c -n %{packname}

# Don't need coverage; it's not packaged either.
sed -i 's/covr, //g' %{packname}/DESCRIPTION

# Fix line endings.
for file in %{packname}/NEWS.md %{packname}/inst/doc/*.R*; do
    sed "s|\r||g" ${file} > ${file}.new
    touch -r ${file} ${file}.new
    mv ${file}.new ${file}
done


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css


%check
%if %{with suggests}
%{_bindir}/R CMD check %{packname}
%else
_R_CHECK_FORCE_SUGGESTS_=0 %{_bindir}/R CMD check %{packname} --no-examples
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
%{rlibdir}/%{packname}/WORDLIST


%changelog
* Tue Feb 23 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.7.5-1
- Update to latest version (#1922307)

* Sun Feb 07 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.7.4-1
- Update to latest version (#1922307)

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Dec 24 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.7.3-1
- Update to latest version (#1908491)

* Wed Oct 21 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.7.2-1
- Update to latest version (#1889641)

* Fri Oct 02 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.7.1-1
- Update to latest version (#1884443)

* Mon Sep 07 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.7.0-1
- Update to latest version (#1855314)

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun  8 2020 Tom Callaway <spot@fedoraproject.org> - 0.5.6-2
- rebuild for R 4
- move geepack under with_suggests to break loop

* Thu May 21 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.5.6-1
- Update to latest version

* Sun Mar 01 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.5.5-1
- Update to latest version

* Mon Feb 24 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.5.4-1
- Update to latest version

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 08 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.5.3-2
- Fix line endings

* Wed Jan 08 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.5.3-1
- initial package for Fedora
