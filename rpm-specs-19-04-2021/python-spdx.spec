%global srcname spdx

Name:		python-spdx	
Version:	2.5.0
Release:	5%{?dist}
Summary:	SPDX license list database

License:	CC0
URL:		https://github.com/bbqsrc/spdx-python
Source0:	%pypi_source
BuildArch:	noarch

%description
A Python module incorporating an interface to the SPDX license database.

%package -n python%{python3_pkgversion}-%{srcname}
Summary:	SPDX license list database
%{?python_provide:%python_provide python3-%{srcname}}

BuildRequires:	python%{python3_pkgversion}-devel
BuildRequires:	python%{python3_pkgversion}-setuptools

%description -n python%{python3_pkgversion}-%{srcname}
A Python module incorporating an interface to the SPDX license database.

%prep
%setup -q -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%files -n python%{python3_pkgversion}-%{srcname}
%doc README.rst
%license LICENSE
%{python3_sitelib}/spdx-*.egg-info/
%{python3_sitelib}/spdx/

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.5.0-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Sep 29 2019 Jeremy Bertozzi <jeremy.bertozzi> - 2.5.0-1
- Initial package

