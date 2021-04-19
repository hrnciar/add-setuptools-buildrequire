%global pypi_name wled

Name:           python-%{pypi_name}
Version:        0.4.4
Release:        2%{?dist}
Summary:        Python client for WLED

License:        MIT
URL:            https://github.com/frenck/python-wled
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
This package allows you to control and monitor an WLED device
programmatically. It is mainly created to allow third-party
programs to automate the behavior of WLED.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  %{py3_dist aiohttp}
BuildRequires:  %{py3_dist attrs}
BuildRequires:  %{py3_dist setuptools}
BuildRequires:  %{py3_dist yarl}
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist backoff}
BuildRequires:  %{py3_dist aresponses}
BuildRequires:  %{py3_dist pytest-asyncio}

%description -n python3-%{pypi_name}
This package allows you to control and monitor an WLED device
programmatically. It is mainly created to allow third-party
programs to automate the behavior of WLED.

%prep
%autosetup -n python-%{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%pytest -v tests
%files -n python3-%{pypi_name}
%license LICENSE.md
%doc README.md
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%changelog
* Wed Jan 20 2021 Fabian Affolter <mail@fabian-affolter.ch> - 0.4.4-2
- Update to new macros (#1903509)

* Wed Dec 02 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.4.4-1
- Initial package
