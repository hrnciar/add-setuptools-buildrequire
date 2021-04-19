%global pypi_name metrics2mqtt

Name:           %{pypi_name}
Version:        0.1.18
Release:        2%{?dist}
Summary:        Publish system performance metrics to a MQTT broker

License:        MIT
URL:            https://github.com/jamiebegin/metrics2mqtt
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)

Requires:       python3-%{pypi_name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description
metrics2mqtt is a lightweight wrapper around psutil that publishes
CPU utilization, free memory, and other system-level stats to a MQTT
broker.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
metrics2mqtt is a lightweight wrapper around psutil that publishes
CPU utilization, free memory, and other system-level stats to a MQTT
broker.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info
sed -i -e '/^#!\//, 1d' metrics2mqtt/base.py

%build
%py3_build

%install
%py3_install

%files
%{_bindir}/%{pypi_name}

%files -n python3-%{pypi_name}
%doc README.md
%license LICENSE
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Sep 04 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.1.18-1
- Initial package for Fedora
