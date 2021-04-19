%global pypi_name three_merge

%global _description %{expand:
Simple Python library to perform a 3-way merge between strings, based on 
diff-match-patch. This library performs merges at a character level, as 
opposed to most VCS systems, which opt for a line-based approach.
}


Name:           python-%{pypi_name}
Version:        0.1.1
Release:        2%{?dist}
Summary:        Simple library for merging two strings with respect to a base one

License:        MIT
URL:            https://github.com/spyder-ide/three-merge
Source0:        https://files.pythonhosted.org/packages/source/t/%{pypi_name}/three-merge-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
%_description

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(diff-match-patch)
Requires:       python3dist(flaky)
Requires:       python3dist(pytest)
Requires:       python3dist(pytest-cov)
Requires:       python3dist(pytest-timeout)

%description -n python3-%{pypi_name}
%_description

%prep
%autosetup -n three-merge-%{version}

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
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Nov 27 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.1.1-1
- Update to 0.1.1

* Wed Nov 25 2020 Mukundan Ragavan <nonamedotc@gmail.com> - 0.1.0-1
- Initial package.
