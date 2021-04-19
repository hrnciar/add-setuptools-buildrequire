# Created by pyp2rpm-3.3.5
%global pypi_name jupyterlab_pygments

Name:           python-%{pypi_name}
Version:        0.1.2
Release:        2%{?dist}
Summary:        Pygments theme

License:        BSD
URL:            https://github.com/jupyterlab/jupyterlab_pygments
Source0:        %{pypi_source}

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
This package contains a syntax coloring theme for pygments making use of the 
JupyterLab CSS variables.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       (python3dist(pygments) >= 2.4.1 with python3dist(pygments) < 3)

%description -n python3-%{pypi_name}
This package contains a syntax coloring theme for pygments making use of the 
JupyterLab CSS variables.



%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Nov 26 2020 Mukundan Ragavan <nonamedotc@gmail.com> - 0.1.2-1
- Initial package.
