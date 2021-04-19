%global pypi_name dbus-next
%global srcname   dbus_next

%bcond_without  tests

Name:           python-%{pypi_name}
Version:        0.2.2
Release:        1%{?dist}
Summary:        Zero-dependency DBus library for Python with asyncio support

License:        MIT
URL:            https://github.com/altdesktop/python-dbus-next
# pypi_source archive does not include test data
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
%if %{with tests}
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-asyncio)
BuildRequires:  python3dist(pytest-timeout)
BuildRequires:  /usr/bin/dbus-run-session
%endif

%global _description %{expand:
python-dbus-next is a Python library for DBus that aims to be a fully
featured high level library primarily geared towards integration of
applications into Linux desktop and mobile environments.

Desktop application developers can use this library for integrating their
applications into desktop environments by implementing common DBus
standard interfaces or creating custom plugin interfaces.

Desktop users can use this library to create their own scripts and
utilities to interact with those interfaces for customization of their
desktop environment.

python-dbus-next plans to improve over other DBus libraries for Python in
the following ways:

 -  Zero dependencies and pure Python 3.
 -  Support for multiple IO backends including asyncio and the GLib main
    loop.
 -  Nonblocking IO suitable for GUI development.
 -  Target the latest language features of Python for beautiful services
    and clients.
 -  Complete implementation of the DBus type system without ever guessing
    types.
 -  Integration tests for all features of the library.
 -  Completely documented public API.}

%description %{_description}

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name} %{_description}


%prep
%autosetup
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
# Fix permissions for examples
chmod -x examples/*.py

%build
%py3_build

%install
%py3_install

%if %{with tests}
%check
# tests require dbus daemon to be running
%global __pytest  /usr/bin/dbus-run-session -- %{__pytest}
%pytest

%endif

%files -n python3-%{pypi_name}
%license LICENSE
%doc CHANGELOG.md README.md examples/
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info

%changelog
* Mon Mar 01 2021 Aleksei Bavshin <alebastr@fedoraproject.org> - 0.2.2-1
- Initial import (#1929001)
