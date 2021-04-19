%global pypi_name python-language-server

%global short_name language-server

%global _description %{expand:
A Python implementation of the Language Server Protocol.
}

Name:           %{pypi_name}
Version:        0.36.2
Release:        4%{?dist}
Summary:        Python Language Server for the Language Server Protocol

License:        MIT
URL:            https://github.com/palantir/python-language-server
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
# Jedi compatibility (for version 0.18.0)
# Proposed upstream: https://github.com/palantir/python-language-server/pull/901
# and already merge to the new fork: https://github.com/python-ls/python-ls/pull/2/
Patch0:         jedi_compat.patch
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(autopep8)
BuildRequires:  python3dist(coverage)
BuildRequires:  python3dist(flake8)
BuildRequires:  python3dist(jedi)
BuildRequires:  python3dist(matplotlib)
BuildRequires:  python3dist(mccabe)
BuildRequires:  python3dist(mock)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(pandas)
BuildRequires:  python3dist(pluggy)
BuildRequires:  python3dist(pycodestyle)
BuildRequires:  python3dist(pydocstyle) >= 2.0.0
BuildRequires:  python3dist(pyflakes) >= 1.6.0
BuildRequires:  python3dist(pylint)
BuildRequires:  python3dist(pyqt5)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-cov)
BuildRequires:  python3dist(python-jsonrpc-server)
BuildRequires:  python3dist(rope) >= 0.10.5
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(ujson)
BuildRequires:  python3-versioneer
BuildRequires:  python3dist(yapf)
BuildRequires:  python3dist(flaky)

%description %_description

%package -n     python3-%{short_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{short_name}}

Requires:       python3dist(jedi)
Requires:       python3dist(python-jsonrpc-server)
Requires:       python3dist(pluggy)
Requires:       python3dist(ujson)

%description -n python3-%{short_name}
%_description

%prep
%autosetup -n %{pypi_name}-%{version} -p 1

# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
# https://github.com/palantir/python-language-server/issues/906
%pytest -v -k '(not test_folding and not test_pylint and not test_symbols and not test_symbols_all_scopes and not test_numpy_hover and not test_snippet_parsing)'


%files -n python3-%{short_name}
%license LICENSE
%doc README.rst
%{_bindir}/pyls
%{python3_sitelib}/pyls
%{python3_sitelib}/python_language_server-%{version}-py%{python3_version}.egg-info

%changelog
* Tue Mar 02 2021 Lumír Balhar <lbalhar@redhat.com> - 0.36.2-4
- Fix compatibility with jedi 0.18.0

* Sat Feb 06 2021 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.36.2-3
- Disable failing tests (upstream issue filed)
- Fixes bz#1914248

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.36.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Nov 26 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.36.2-1
- Update to 0.36.2

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.34.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.34.1-1
- Update to 0.34.1

* Mon Jun 29 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.31.10-5
- Drop failing list temporarily

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.31.10-4
- Rebuilt for Python 3.9

* Sun May 03 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.31.10-3
- Drop BR on configparser (python2 only)

* Mon Apr 27 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.31.10-2
- Enable tests
- Disable incompatible tests

* Thu Apr 23 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.31.10-1
- Fix license field
- Update to 0.31.10
- Fix requires list

* Wed Apr 22 2020 Mukundan Ragavan <nonamedotc@gmail.com> - 0.31.9-1
- Initial package.
