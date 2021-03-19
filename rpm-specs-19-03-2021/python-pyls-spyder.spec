# Created by pyp2rpm-3.3.5
%global pypi_name pyls-spyder

Name:           python-%{pypi_name}
Version:        0.2.1
Release:        2%{?dist}
Summary:        Spyder extensions for the python-language-server

License:        MIT
URL:            https://github.com/spyder-ide/pyls-spyder
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
Spyder extensions to the python language server (pyls)

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(python-language-server)
Requires:       python3dist(setuptools)

%description -n python3-%{pypi_name}
Spyder extensions to the python language server (pyls)


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
%{python3_sitelib}/pyls_spyder
%{python3_sitelib}/pyls_spyder-%{version}-py%{python3_version}.egg-info

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Nov 26 2020 Mukundan Ragavan <nonamedotc@gmail.com> - 0.2.1-1
- Initial package.
