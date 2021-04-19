%global pretty_name BatAlgorithm
%global extract_name buma-BatAlgorithm-d913e9d
%global new_name batalgorithm

%global _description %{expand:
Implementation of Bat Algorithm in Python.}

Name:           python-%{new_name}
Version:        0.3.1
Release:        1%{?dist}
Summary:        Bat Algorithm for optimization

License:        MIT
URL:            https://github.com/buma/BatAlgorithm
Source0:        %{url}/tarball/master/%{extract_name}.tar.gz

BuildArch:      noarch

%description %_description

%package -n python3-%{new_name}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description -n python3-%{new_name} %_description

%prep
%autosetup -n %{extract_name}

%build
%py3_build

%install
%py3_install

%files -n python3-%{new_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{pretty_name}-%{version}-py%{python3_version}.egg-info
%pycached %{python3_sitelib}/%{pretty_name}.py

%changelog
* Sun Feb 14 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.3.1-1
- Package rename (BatAlgorithm -> batalgorithm)

* Tue Feb 9 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.3.1-1
- Initial package
