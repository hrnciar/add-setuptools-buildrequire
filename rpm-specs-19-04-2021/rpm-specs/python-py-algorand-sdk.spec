%global pypi_name py-algorand-sdk
Name:           python-%{pypi_name}
Version:        1.4.1
Release:        1%{?dist}
Summary:        Algorand Python SDK
License:        MIT

URL:            https://github.com/algorand/py-algorand-sdk
Source0:        %pypi_source
Source1:        https://raw.githubusercontent.com/algorand/py-algorand-sdk/develop/LICENSE

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pynacl
BuildRequires:  python3-pycryptodomex
BuildRequires:  python3-msgpack


%description
A python library for interacting with the Algorand network.

%package -n python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
A python library for interacting with the Algorand network.

%prep
%setup -q -n %{pypi_name}-%{version}


%build
%py3_build

cp %{SOURCE1} .

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/algosdk
%{python3_sitelib}/py_algorand_sdk-%{version}-py%{python3_version}.egg-info
%exclude %{python3_sitelib}/test

%changelog
* Tue Mar 09 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.4.1-1
- Initial package.

