%global pypi_name PyQt-builder
%global srcname PyQt-builder

Name:           %{srcname}
Version:        1.6.0
Release:        3%{?dist}
Summary:        The PEP 517 compliant PyQt build system

License:        BSD
URL:            https://www.riverbankcomputing.com/software/pyqt/
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  sip5

Requires: sip5

%description
PyQt-builder is the PEP 517 compliant build system for PyQt and projects that
extend PyQt. It extends the sip build system and uses Qt's qmake to perform the
actual compilation and installation of extension modules.Projects that use
PyQt- builder provide an appropriate pyproject.toml file and an optional
project.py.

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install
# These dll files are from openssl and microsoft visiual studio
# While we can redistribute them, we don't have source and it's 
# unlikely anyone will want to bundle a windows executable from linux.
rm -rf %{buildroot}/%{python3_sitelib}/pyqtbuild/bundle/dlls

%files
%{_bindir}/pyqt-bundle
%{python3_sitelib}/pyqtbuild
%{python3_sitelib}/PyQt_builder-%{version}-py%{python3_version}.egg-info

%changelog
* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec 29 2020 Kevin Fenzi <kevin@scrye.com> - 1.6.0-2
- Remove shipped dlls.

* Tue Dec 15 2020 Kevin Fenzi <kevin@scrye.com> - 1.6.0-1
- Initial package.
