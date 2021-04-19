%bcond_without tests

%global pypi_name tcxreader
%global fullversion 0.3.6

%global _description %{expand:
This is a simple TCX parser / reader which can read Garmin TCX file
extension files. The package currently does not support laps and merges the
whole exercise into one exercise object. The following data is currently
parsed: longitude, latitude, elevation, time, distance, hr_value, cadence,
watts, TPX_speed (extension).}

Name:           python-%{pypi_name}
Version:        %{?fullversion}
Release:        2%{?dist}
Summary:        tcxreader is a parser/reader for Garmin's TCX file format

License:        MIT
URL:            https://github.com/alenrajsp/tcxreader
Source0:        %{pypi_source}
BuildArch:      noarch

%description %_description

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-cov
BuildRequires:  %{py3_dist pytzdata}
BuildRequires:  python3dist(maya)

%description -n python3-%{pypi_name} %_description

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install
rm -rf %{buildroot}/%{python3_sitelib}/tests

%check
#skipping three tests
%if %{with tests}
%{python3} -m pytest
%endif

%files -n python3-%{pypi_name}
%doc README.md
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Tue Apr 13 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.3.6-2
- Editing dependencies (problems with F32 and F33)

* Tue Mar 30 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.3.6-1
- New version - 0.3.6
- Enable tests

* Mon Mar 22 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.3.3-2
- Removing cosmetic macro

* Sun Mar 14 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.3.3-1
- New version - 0.3.3

* Fri Mar 05 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.3.2-1
- Initial package
