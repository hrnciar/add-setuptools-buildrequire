%global srcname sphinxcontrib-zopeext

Name:           python-%{srcname}
Version:        0.2.4
Release:        4%{?dist}
Summary:        Sphinx extension for documenting Zope interfaces

License:        BSD
URL:            https://pypi.org/project/sphinxcontrib-zopeext/
Source0:        %pypi_source
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  %{py3_dist docutils}
BuildRequires:  %{py3_dist pip}
BuildRequires:  %{py3_dist setuptools}
BuildRequires:  %{py3_dist sphinx}
BuildRequires:  %{py3_dist wheel}
BuildRequires:  %{py3_dist zope.interface}

%description
This sphinx extension provides an autointerface directive for Zope
interfaces.

%package     -n python3-%{srcname}
Summary:        Sphinx extension for documenting Zope interfaces

# This can be removed when Fedora 36 reaches EOL
Obsoletes:      python3-j1m.sphinxautointerface < 0.3.0-15

%description -n python3-%{srcname}
This sphinx extension provides an autointerface directive for Zope
interfaces.

%prep
%autosetup -n %{srcname}-%{version}

# pytest-runner is deprecated and unused anyway
sed -i "s/'pytest-runner'//" setup.py

%build
%py3_build

%install
%py3_install

%files -n python3-%{srcname}
%doc CHANGES README.rst
%{python3_sitelib}/sphinxcontrib/zopeext/
%{python3_sitelib}/sphinxcontrib_zopeext*

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 15 2020 Jerry James <loganjerry@gmail.com> - 0.2.4-2
- Be more specific about owned directories
- Drop the deprecated pytest-runner BR and remove the dep from setup.py

* Mon Jun 15 2020 Jerry James <loganjerry@gmail.com> - 0.2.4-1
- Initial RPM
