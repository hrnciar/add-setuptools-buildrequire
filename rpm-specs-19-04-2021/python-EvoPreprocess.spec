%global pypi_name EvoPreprocess

%global _description %{expand:
EvoPreprocess is a Python toolkit for sampling datasets, instance weighting,
and feature selection. It is compatible with scikit-learn and 
imbalanced-learn packages. It is based on the NiaPy library for the 
implementation of nature-inspired algorithms.}

Name:           python-%{pypi_name}
Version:        0.3.4
Release:        3%{?dist}
Summary:        A Python Toolkit for Data Preprocessing 
License:        GPLv3
URL:            https://github.com/karakatic/%{pypi_name}
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch

%global debug_package %{nil}

%description %_description

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires: %{py3_dist numpy}
BuildRequires: %{py3_dist scipy}
BuildRequires: %{py3_dist scikit-learn}
BuildRequires: %{py3_dist imbalanced-learn}
BuildRequires: %{py3_dist NiaPy}

%py_provides python3-%{pypi_name}

%description -n python3-%{pypi_name} %_description

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info
%{python3_sitelib}/%{pypi_name}

%changelog
* Sun Feb 14 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.3.4-3
- Removing dependency generator
- Description fixes
- BuildArch set to noarch
- Fresh rebuilt

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Dec 26 2020 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.3.4-1
- Initial package
