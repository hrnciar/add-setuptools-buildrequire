%bcond_without tests

%global pretty_name maya

%global fullversion 0.6.1

%global _description %{expand:
Datetimes are very frustrating to work with in Python, especially when dealing
with different locales on different systems. This library exists to make the 
simple things much easier, while admitting that time is an 
illusion (timezones doubly so).}


Name:           python-%{pretty_name}
Version:        %{?fullversion}
Release:        1%{?dist}
Summary:        Datetimes for Humans

License:        MIT
URL:            https://github.com/timofurrer/%{pretty_name}
Source0:        %{url}/archive/v%{version}/%{pretty_name}-%{version}.tar.gz

BuildArch:      noarch

%description %_description

%package -n python3-%{pretty_name}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist setuptools}
BuildRequires:  %{py3_dist snaptime}
BuildRequires:  %{py3_dist pendulum}
BuildRequires:  %{py3_dist humanize}
BuildRequires:  %{py3_dist dateparser}
BuildRequires:  %{py3_dist pytz}
BuildRequires:  %{py3_dist tzlocal}
BuildRequires:  %{py3_dist pytzdata}
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist freezegun}

%py_provides python3-%{pretty_name}

%description -n python3-%{pretty_name} %_description

%prep
%autosetup -n %{pretty_name}-%{fullversion}
rm -rf %{pretty_name}.egg-info

%build
%py3_build

%install
%py3_install
# Remove extra install files
rm -rf %{buildroot}/%{python3_sitelib}/tests

%check
%if %{with tests}
%{python3} -m pytest
%endif

%files -n python3-%{pretty_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pretty_name}-%{fullversion}-py%{python3_version}.egg-info
%{python3_sitelib}/%{pretty_name}

%changelog
* Sun Feb 14 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.6.1-1
- Removing dependency generator

* Mon Feb 8 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.6.1-1
- Initial package
