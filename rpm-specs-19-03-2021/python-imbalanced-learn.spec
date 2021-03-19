%bcond_with tests

%global pretty_name imbalanced-learn
%global lib_name imblearn
%global extract_name imbalanced_learn

%global fullversion 0.8.0

%global _description %{expand:
imbalanced-learn is a python package offering a number of re-sampling techniques 
commonly used in datasets showing strong between-class imbalance. It is 
compatible with scikit-learn and is part of scikit-learn-contrib projects.}


Name:           python-%{pretty_name}
Version:        %{?fullversion}
Release:        1%{?dist}
Summary:        A Python Package to Tackle the Imbalanced Datasets in Machine Learning 

License:        MIT
URL:            https://github.com/scikit-learn-contrib/%{pretty_name}
Source0:        %{url}/archive/%{fullversion}/%{pretty_name}-%{fullversion}.tar.gz

BuildArch:      noarch

%description %_description

%package -n python3-%{pretty_name}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist setuptools}

#main deps
BuildRequires:  %{py3_dist numpy}
BuildRequires:  %{py3_dist scipy}
BuildRequires:  %{py3_dist scikit-learn}
BuildRequires:  %{py3_dist joblib}
BuildRequires:  %{py3_dist matplotlib}

#for tests
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist pytest-cov}

%py_provides python3-%{pretty_name}

%description -n python3-%{pretty_name} %_description

%prep
%autosetup -n %{pretty_name}-%{fullversion}
rm -rf %{pretty_name}.egg-info

%build
%py3_build

%install
%py3_install
# Remove extra install files
rm -rf %{buildroot}/%{python3_sitelib}/tests

# some tests are skipped, because of keras and tensorflow deps
%check
%if %{with tests}
%{python3} -m pytest -k 'not test_all_estimators and not test_classification_report_imbalanced_multiclass_with_unicode_label and not test_rusboost and not test_cluster_centroids_n_jobs'
%endif

%files -n python3-%{pretty_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{extract_name}-%{fullversion}-py%{python3_version}.egg-info
%{python3_sitelib}/%{lib_name}

%changelog
* Sat Mar 13 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.8.0-1
- New version - 0.8.0

* Sun Feb 14 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.7.0-5
- Removing dependency generator
- Fresh rebuilt

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan 19 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.7.0-3
- disabling tests - too many problems with missing keras/tensorflow dependencies

* Fri Jan 8 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.7.0-2
- disabling one test - test_cluster_centroids_n_jobs

* Sun Nov 29 2020 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.7.0-1
- Initial package

