%global pypi_name aiosqlite

Name:           python-%{pypi_name}
Version:        0.17.0
Release:        1%{?dist}
Summary:        Asyncio bridge to the standard SQLite3 module

License:        MIT
URL:            https://github.com/jreese/aiosqlite
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
aiosqlite AsyncIO bridge to the standard SQLite3 module for Python 3.5+.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(aiounittest)
BuildRequires:  pyproject-rpm-macros
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
aiosqlite AsyncIO bridge to the standard SQLite3 module for Python 3.5+.

%generate_buildrequires
%pyproject_buildrequires -r

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc CHANGELOG.md README.rst

%changelog
* Wed Feb 24 2021 Fabian Affolter <mail@fabian-affolter.ch> - 0.17.0-1
- Update to latest upstream release 0.17.0 (#1919588)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 24 2021 Fabian Affolter <mail@fabian-affolter.ch> - 0.16.1-1
- Update to latest upstream release 0.16.1 (#1919588)

* Thu Dec 03 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.16.0-1
- Update to latest upstream release 0.16.0

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.12.0-2
- Rebuilt for Python 3.9

* Sun May 03 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.12.0-1
- Update to latest upstream release 0.12.0

* Thu Jan 30 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.11.0-4
- Fix ownership

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 07 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.11.0-2
- Use var for souce URL
- Better use of wildcards (rhbz#1786955)

* Sun Dec 29 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.11.0-1
- Initial package for Fedora
