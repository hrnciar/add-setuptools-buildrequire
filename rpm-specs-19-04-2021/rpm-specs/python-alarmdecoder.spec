%global pypi_name alarmdecoder

Name:           python-%{pypi_name}
Version:        1.13.9
Release:        2%{?dist}
Summary:        Python interface for the AlarmDecoder (AD2) devices

License:        MIT
URL:            http://github.com/nutechsoftware/alarmdecoder
Source0:        %{pypi_source}
BuildArch:      noarch

%description
This Python library aims to provide a consistent interface for
the AlarmDecoder product line (AD2USB, AD2SERIAL and AD2PI).

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(mock)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pyserial)
BuildRequires:  python3dist(setuptools)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
This Python library aims to provide a consistent interface for
the AlarmDecoder product line (AD2USB, AD2SERIAL and AD2PI).

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%pytest -v test -k "not test_ssl and not test_ssl_exception"

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{_bindir}/ad2-firmwareupload
%{_bindir}/ad2-sslterm
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Oct 05 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.13.9-1
- Initial package for Fedora