%global pypi_name volvooncall

Name:           python-%{pypi_name}
Version:        0.8.12
Release:        3%{?dist}
Summary:        Communicate with Volvo On Call

License:        Unlicense
URL:            https://github.com/molobrakos/volvooncall
Source0:        %{pypi_source}
BuildArch:      noarch

%description
Retrieve statistics about your Volvo from the Volvo On Call
(VOC) online service.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Retrieve statistics about your Volvo from the Volvo On Call
(VOC) online service.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info
sed -i -e '/^#!\//, 1d' volvooncall/{mqtt.py,volvooncall.py}

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.md
# https://github.com/molobrakos/volvooncall/pull/64
#%%license LICENSE
%{_bindir}/voc
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Oct 26 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.8.12-2
- Remove shebang (#1888351)

* Wed Oct 14 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.8.12-1
- Initial package for Fedora
