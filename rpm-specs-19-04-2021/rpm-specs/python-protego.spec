%global pkg_name protego
%global pypi_name Protego
%global desc %{expand:
Protego is a pure-Python `robots.txt` parser with support for modern
conventions.}

Name:		python-protego
Version:	0.1.16
Release:	1%{?dist}
Summary:	Pure-Python robots.txt parser with support for modern conventions

License:	BSD
URL:		https://github.com/scrapy/protego
Source0:	%{pypi_source}

BuildArch:	noarch


%description
%{desc}

%package -n python3-%{pkg_name}
Summary:	%{summary}

BuildRequires:	python3-devel
BuildRequires:	python3-setuptools
BuildRequires:	python3-pytest
BuildRequires:	python3-six


%description -n python3-%{pkg_name}
%{desc}

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build


%install
%py3_install

%check
%pytest

%files -n python3-%{pkg_name}
%license LICENSE
%doc README.md
%pycached %{python3_sitelib}/protego.py
%{python3_sitelib}/Protego-*.egg-info

%changelog
* Sat Apr 3 2021 Eduardo Echeverria <echevemaster@gmail.com> - 0.1.16-1
- Initial packaging

