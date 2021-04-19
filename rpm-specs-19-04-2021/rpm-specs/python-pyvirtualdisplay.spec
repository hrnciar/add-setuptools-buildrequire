%global pypi_name PyVirtualDisplay
%global dist_name %{py_dist_name %{pypi_name}}

Name:           python-%{dist_name}
Version:        2.1
Release:        1%{?dist}
Summary:        Python wrapper for Xvfb, Xephyr and Xvnc

License:        BSD
URL:            https://github.com/ponty/PyVirtualDisplay
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  %{py3_dist setuptools}
# For Tests
BuildRequires:  %{py3_dist EasyProcess}
BuildRequires:  %{py3_dist pillow}
BuildRequires:  %{py3_dist psutil}
BuildRequires:  %{py3_dist pytest}
BuildRequires:  xmessage
BuildRequires:  xorg-x11-server-Xephyr
BuildRequires:  xorg-x11-server-Xvfb

%global _description %{expand:
pyvirtualdisplay is a python wrapper for Xvfb, Xephyr and Xvnc}

%description %_description

%package -n     python3-%{dist_name}
Summary:        %{summary}

Requires:       %{py3_dist py}
Requires:       xorg-x11-server-Xvfb
%description -n python3-%{dist_name} %_description

%prep
%autosetup -n %{pypi_name}-%{version}
# TODO: package entrypoint2 and vncdotool and enable these tests
rm tests/test_race.py
rm tests/test_xvnc.py

%build
%py3_build

%install
%py3_install

%check
%pytest


%files -n python3-%{dist_name}
%doc README.md
%license LICENSE.txt
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/
%{python3_sitelib}/%{dist_name}/

%changelog
* Sat Feb 13 2021 Scott Talbert <swt@techie.net> - 2.1-1
- Initial package
