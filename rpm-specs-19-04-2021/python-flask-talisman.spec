%global pypi_name flask-talisman

Name:           python-%{pypi_name}
Version:        0.7.0
Release:        1%{?dist}
Summary:        HTTP security headers for Flask

License:        ASL 2.0
URL:            https://github.com/GoogleCloudPlatform/flask-talisman
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(six) >= 1.9

%description
Talisman is a small Flask extension that handles setting HTTP headers
that can help protect against a few common web application security issues.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Talisman is a small Flask extension that handles setting HTTP headers
that can help protect against a few common web application security issues.


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.rst
%license LICENSE
%{python3_sitelib}/flask_talisman
%{python3_sitelib}/flask_talisman-%{version}-py%{python3_version}.egg-info

%changelog
* Sun Mar 21 2021 Neal Gompa <ngompa13@gmail.com> - 0.7.0-1
- Initial package.
