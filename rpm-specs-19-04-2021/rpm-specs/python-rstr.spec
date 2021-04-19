# Created by pyp2rpm-3.3.5
%global pypi_name rstr
%global _description %{expand:
rstr is a helper module for easily generating random strings of various types.
It could be useful for fuzz testing, generating dummy data, or other
applications.}

Name:           python-%{pypi_name}
Version:        2.2.6
Release:        1%{?dist}
Summary:        Generate random strings in Python

License:        BSD
URL:            https://files.pythonhosted.org/packages/source/r/rstr/%{name}-%{version}.tar.gz
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python3dist(setuptools)

%description %_description

%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python%{python3_pkgversion}-%{pypi_name} %_description

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
export PYTHONPATH=%{buildroot}%{python3_sitelib}
%{__python3} setup.py test

%files -n python3-%{pypi_name}
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Thu Feb 04 2021 Frédéric Pierret (fepitre) <frederic.pierret@qubes-os.org> - 2.2.6-1
- Update to 2.2.6

* Tue Jan 05 2021 Frédéric Pierret (fepitre) <frederic.pierret@qubes-os.org> - 2.1.0-1
- Initial package.
