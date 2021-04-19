# Created by pyp2rpm-3.3.5
%global pypi_name yaml2ical

%global common_description %{expand:
yaml2ical converts a series of meeting descriptions in YAML format
into one or several .ics files suitable for calendaring. It checks for
scheduling conflicts in specific locations.}

Name:           python-%{pypi_name}
Version:        0.12.0
Release:        1%{?dist}
Summary:        Convert YAML meeting descriptions into iCalendar files

License:        ASL 2.0
URL:            http://docs.openstack.org/infra/system-config/
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  sed
BuildRequires:  python3-devel
BuildRequires:  python3dist(coverage) >= 3.6
BuildRequires:  python3dist(fixtures) >= 3
BuildRequires:  python3dist(icalendar)
BuildRequires:  python3dist(jinja2) >= 2.8
BuildRequires:  python3dist(pbr) >= 1.6
BuildRequires:  python3dist(python-subunit) >= 0.0.18
BuildRequires:  python3dist(pyyaml) >= 3.1
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(testrepository) >= 0.0.18
BuildRequires:  python3dist(testscenarios) >= 0.4
BuildRequires:  python3dist(testtools) >= 1.4

%description
%{common_description}

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%if 0%{?fedora} < 33 || 0%{?rhel} < 9
%py_provides    python3-%{pypi_name}
%endif

%description -n python3-%{pypi_name}
%{common_description}

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
# Remove unnecessary shebang
sed -e '\|#!/usr/bin/env python|d' -i yaml2ical/tests/sample_data.py

%build
%py3_build

%install
%py3_install

%check
PYTHON=%{__python3} %{__python3} setup.py test

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{_bindir}/yaml2ical
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Wed Apr 07 2021 Davide Cavalca <dcavalca@fedoraproject.org> - 0.12.0-1
- Update to 0.12.0

* Tue Feb 16 2021 Davide Cavalca <dcavalca@fedoraproject.org> - 0.11.0-1
- New upstream release

* Tue Feb 02 2021 Davide Cavalca <dcavalca@fedoraproject.org> - 0.10.0-2
- Drop unnecessary Requires
- Switch to py_provides
- Remove unnecessary shebang

* Tue Feb 02 2021 Davide Cavalca <dcavalca@fedoraproject.org> - 0.10.0-1
- Initial package.
