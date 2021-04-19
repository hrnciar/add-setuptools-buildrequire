%global pypi_name aioitertools

Name:           python-%{pypi_name}
Version:        0.7.0
Release:        2%{?dist}
Summary:        Itertools and builtins for AsyncIO and mixed iterables

License:        MIT
URL:            https://github.com/omnilib/aioitertools
Source0:        %{pypi_source}
BuildArch:      noarch

%description
Implementation of itertools, builtins, and more for AsyncIO and mixed-type
iterables.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Implementation of itertools, builtins, and more for AsyncIO and mixed-type
iterables.

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Oct 06 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.7.0-1
- Initial package for Fedora