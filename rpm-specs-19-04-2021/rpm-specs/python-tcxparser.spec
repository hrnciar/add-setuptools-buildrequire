%bcond_without tests

%global pretty_name tcxparser
%global pypi_name python-%{pretty_name}
%global extract_name python_tcxparser

%global _description %{expand:
python-tcxparser is a minimal parser for Garmin's TCX file format. It is not in
any way exhaustive. It extracts just enough data to show the most important
attributes of sport activity.}

Name:           python-%{pretty_name}
Version:        2.0.0
Release:        1%{?dist}
Summary:        Tcxparser is a minimal parser for Garmin TCX file format

License:        BSD
URL:            https://github.com/vkurup/%{pypi_name}
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  %{py3_dist lxml}

%{?python_enable_dependency_generator}

%description %_description

%package -n python3-%{pretty_name}
Summary:        %{summary}

%description -n python3-%{pretty_name} %_description

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

%check
%{python3} setup.py test

%files -n python3-%{pretty_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{extract_name}-%{version}-py%{python3_version}.egg-info
%{python3_sitelib}/%{pretty_name}

%changelog
* Sun Feb 7 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 2.0.0-1
- New version - 2.0.0

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 1.1.0-2
- Same dependencies removed

* Sat Nov 14 2020 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 1.1.0-1
- Initial package

