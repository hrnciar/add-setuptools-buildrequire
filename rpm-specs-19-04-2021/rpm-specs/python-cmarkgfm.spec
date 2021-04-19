%global pypi_name cmarkgfm

Name:           python-%{pypi_name}
Version:        0.5.2
Release:        2%{?dist}
Summary:        Minimal bindings to GitHub's fork of cmark

License:        MIT
URL:            https://github.com/jonparrott/cmarkgfm
Source0:        %{pypi_source}

BuildRequires:  gcc

%description
Bindings to GitHub's cmark Minimalist bindings to GitHub's fork of cmark.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-cffi
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytest
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Bindings to GitHub's cmark Minimalist bindings to GitHub's fork of cmark.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info
chmod -x README.rst LICENSE.txt

%build
%py3_build

%install
%py3_install

%check
%pytest -v tests

%files -n python3-%{pypi_name}
%license LICENSE.txt
%doc README.rst
%{python3_sitearch}/%{pypi_name}/
%{python3_sitearch}/%{pypi_name}-%{version}-py*.egg-info/

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 01 2021 Fabian Affolter <mail@fabian-affolter.ch> - 0.5.2-1
- Update to latest upstream release 0.5.2 (#1911858)

* Mon Dec 14 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.5.1-1
- Update to latest upstream release 0.5.1 (#1906646)

* Thu Nov 26 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.5.0-1
- Update to latest upstream release 0.5.0 (#1900317)

* Fri Jul 03 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.4.2-2
- Run tests (rhbz#1827045)

* Thu Apr 23 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.4.2-1
- Initial package
