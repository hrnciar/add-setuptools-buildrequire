%global pypi_name pyls_black

%global _description %{expand:
Black plugin for the Python Language Server. pyls-black can either format an 
entire file or just the selected text. The code will only be formatted if 
it is syntactically valid Python. Text selections are treated as if they 
were a separate Python file.
}

Name:           python-%{pypi_name}
Version:        0.4.6
Release:        2%{?dist}
Summary:        Black plugin for the Python Language Server

License:        MIT
URL:            https://github.com/rupert/pyls-black
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/pyls-black-%{version}.tar.gz

# license file not present in pypi tarball
Source1:        LICENSE
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(flake8)
BuildRequires:  python3dist(isort)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(setuptools)

%description
%_description

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(black)
Requires:       python3dist(python-language-server)
Requires:       python3dist(setuptools)

%description -n python3-%{pypi_name}
%_description


%prep
%autosetup -n pyls-black-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

# install license
mkdir -p %{buildroot}%{_datadir}/licenses/python3-%{pypi_name}
install -m 0644 %{SOURCE1} %{buildroot}%{_datadir}/licenses/python3-%{pypi_name}

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Nov 26 2020 Mukundan Ragavan <nonamedotc@gmail.com> - 0.4.6-1
- Initial package.
