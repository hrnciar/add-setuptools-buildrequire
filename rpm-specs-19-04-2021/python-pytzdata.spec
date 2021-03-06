%global pypi_name pytzdata

%global appsum Timezone database for Python
%global appdesc The Olson timezone database for Python.

Name: python-%{pypi_name}
Version: 2020.1
Release: 2%{?dist}
Summary: %{appsum}

License: MIT
URL: https://github.com/sdispater/%{pypi_name}
Source0: %{pypi_source}
BuildArch: noarch

BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
%{appdesc}.

%package -n python3-%{pypi_name}
Summary: %{appsum}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%{appdesc}.

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-*.egg-info

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2020.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec 14 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 2020.1-1
- Updated to version 2020.1.

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2019.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 24 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 2019.3-2
- Added python3-setuptools to build requirements.

* Thu Jun 18 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 2019.3-1
- Initial SPEC release.
