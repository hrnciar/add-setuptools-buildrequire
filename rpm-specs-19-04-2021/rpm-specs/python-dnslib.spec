%global pypi_name dnslib

Name:           python-%{pypi_name}
Version:        0.9.14
Release:        2%{?dist}
Summary:        Simple library to encode/decode DNS packets

License:        BSD
URL:            https://github.com/paulc/dnslib
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
Simple library to encode/decode DNS wire-format packets.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pytest)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Simple library to encode/decode DNS wire-format packets.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info
sed -i -e '/^#!\//, 1d' dnslib/test_decode.py

%build
%py3_build

%install
%py3_install

%check
./run_tests.sh

%files -n python3-%{pypi_name}
%doc README
%license LICENSE
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 24 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.14-1
- Initial package for Fedora