# Created by pyp2rpm-3.3.5
%global pypi_name nest_asyncio

%global _description %{expand:
By design asyncio does not allow its event loop to be nested. This presents a 
practical problem: When in an environment where the event loop is already 
running it is impossible to run tasks and wait for the result. Trying to do 
so will give the error "RuntimeError: This event loop is already running". The 
issue pops up in various environments, such as web servers, GUI applications 
and in Jupyter notebooks. This module patches asyncio to allow nested use 
of asyncio.run and loop.run_until_complete.
}

Name:           python-%{pypi_name}
Version:        1.4.3
Release:        3%{?dist}
Summary:        Patch asyncio to allow nested event loops

License:        BSD
URL:            https://github.com/erdewit/nest_asyncio
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
%_description

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%py_provides python3-%{pypi_name}

%description -n python3-%{pypi_name}
%_description

%prep
%autosetup -n %{pypi_name}-%{version}

# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install
mkdir -p %{buildroot}/%{_datadir}/licenses/python3-%{pypi_name}
install -m 0644 LICENSE %{buildroot}/%{_datadir}/licenses/python3-%{pypi_name}

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/__pycache__/%{pypi_name}*
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Nov 28 2020 Mukundan Ragavan <nonamedotc@gmail.com> - 1.4.3-2
- Use pyprovides macro
- Install license correctly

* Thu Nov 26 2020 Mukundan Ragavan <nonamedotc@gmail.com> - 1.4.3-1
- Initial package.
