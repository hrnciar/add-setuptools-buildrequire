%global srcname itemloaders
%global desc %{expand:
itemloaders is a library that helps you collect data from HTML and XML sources.

It comes in handy to extract data from web pages, as it supports data extraction
using CSS and XPath Selectors.

It's specially useful when you need to standardize the data from many sources.
For example, it allows you to have all your casting and parsing rules in a 
single place.}

Name:		python-itemloaders
Version:	1.0.4
Release:	1%{?dist}
Summary:	Library that helps you collect data from HTML and XML sources.

License:	BSD
URL:		https://github.com/scrapy/itemloaders
Source0:	%{pypi_source}

BuildArch:	noarch


%description
%{desc}

%package -n python3-%{srcname}
Summary:	%{summary}

BuildRequires:	python3-devel
BuildRequires:	python3-setuptools
BuildRequires:	python3-parsel
BuildRequires:	python3-jmespath
BuildRequires:	python3-w3lib



%description -n python3-%{srcname}
%{desc}

%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build


%install
%py3_install


%files -n python3-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/itemloaders
%{python3_sitelib}/itemloaders-*.egg-info

%changelog
* Sat Apr 3 2021 Eduardo Echeverria <echevemaster@gmail.com> - 1.0.4-1
- Initial packaging

