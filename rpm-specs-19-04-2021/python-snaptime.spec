%bcond_without tests

%global pretty_name snaptime
%global download_name snaptime-master
%global extract_name zartstrom-snaptime-b05ae09

%global _description %{expand:
The snaptime package is about transforming timestamps simply.}

Name:           python-%{pretty_name}
Version:        0.2.4
Release:        3%{?dist}
Summary:        Transforming timestamps simply

License:        MIT
URL:            https://github.com/zartstrom/snaptime
Source0:        %{url}/tarball/master/%{download_name}.tar.gz

BuildArch:      noarch

%description %_description

%package -n python3-%{pretty_name}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytz
BuildRequires:  python3-dateutil

%if %{with tests}
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-cov	
%endif

%description -n python3-%{pretty_name} %_description

%prep
%autosetup -n %{extract_name}

%build
%py3_build

%install
%py3_install

%check
#skipping three tests
%if %{with tests}
%{python3} -m pytest -k 'not test_bad_weekday and not test_parse_error and not test_unit_error'
%endif

%files -n python3-%{pretty_name}
%license LICENSE.txt
%doc README.md
%{python3_sitelib}/%{pretty_name}-%{version}-py%{python3_version}.egg-info
%pycached %{python3_sitelib}/%{pretty_name}/main.py
%pycached %{python3_sitelib}/%{pretty_name}/__init__.py

%changelog
* Wed Mar 17 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.2.4-3
- Cosmetic changes

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 21 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.2.4-1
- Initial package
