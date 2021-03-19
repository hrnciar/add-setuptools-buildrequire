%global pypi_name adext

Name:           python-%{pypi_name}
Version:        0.3
Release:        2%{?dist}
Summary:        Python module to extend AlarmDecoder module

License:        MIT
URL:            https://github.com/ajschmidt8/adext
Source0:        %{pypi_source}
BuildArch:      noarch

%description
adext is a small package that extends the alarmdecoder module to
include some additional methods.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
adext is a small package that extends the alarmdecoder module to
include some additional methods.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info
sed -i -e 's/alarmdecoder==1.13.2/alarmdecoder/g' setup.py

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.md
# https://github.com/ajschmidt8/adext/pull/5
#%%license LICENSE
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Oct 20 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.3-1
- Initial package for Fedora
