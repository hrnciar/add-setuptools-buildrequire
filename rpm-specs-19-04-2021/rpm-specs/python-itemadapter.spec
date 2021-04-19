%global pkg_name itemadapter
%global desc %{expand:
The ItemAdapter class is a wrapper for data container objects,
providing a common interface to handle objects of different
types in an uniform manner, regardless of their underlying implementation.}
Name:		python-itemadapter
Version:	0.2.0
Release:	1%{?dist}
Summary:	The ItemAdapter class is a wrapper for data container object

License:	BSD
URL:		https://github.com/scrapy/itemadapter
Source0:	%{pypi_source %pkg_name}

BuildArch:	noarch


%description
%{desc}

%package -n python3-%{pkg_name}
Summary:	%{summary}

BuildRequires:	python3-devel
BuildRequires:	python3-setuptools
Requires:	python3-attrs

%py_provides  python3-%{pkg_name}


%description -n python3-%{pkg_name}
%{desc}

%prep
%autosetup -n %{pkg_name}-%{version}

%build
%py3_build


%install
%py3_install

%files -n python3-%{pkg_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/itemadapter
%{python3_sitelib}/itemadapter-*.egg-info

%changelog
* Sat Apr 3 2021 Eduardo Echeverria <echevemaster@gmail.com> - 0.2.0-1
- Initial packaging

