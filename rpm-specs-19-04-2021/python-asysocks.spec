%global pypi_name asysocks

Name:           python-%{pypi_name}
Version:        0.1.1
Release:        1%{?dist}
Summary:        Socks5/Socks4 client and server library

License:        MIT
URL:            https://github.com/skelsec/asysocks
Source0:        %{pypi_source}
Source1:        https://raw.githubusercontent.com/skelsec/asysocks/master/LICENSE
BuildArch:      noarch

%description
A Python Socks5/Socks4 client and server library.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
A Python Socks5/Socks4 client and server library.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info
cp -a %{SOURCE1} LICENSE
sed -i -e '/^#!\//, 1d' asysocks/__init__.py

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.md
%license LICENSE
%{_bindir}/asysock*
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py*.egg-info/

%changelog
* Sun Feb 28 2021 Fabian Affolter <mail@fabian-affolter.ch> - 0.1.1-1
- Update to latest upstream release 0.1.1 (#1933456)

* Tue Feb 09 2021 Fabian Affolter <mail@fabian-affolter.ch> - 0.1.0-1
- Update to latest upstream release 0.1.0 (#1926506)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 11 2021 Fabian Affolter <mail@fabian-affolter.ch> - 0.0.11-1
- Update to latest upstream release 0.0.11 (#1914697)

* Fri Oct 30 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.0.10-1
- Update to latest upstream release 0.0.10

* Thu Sep 03 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.0.7-1
- Update to latest upstream release 0.0.7

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 29 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.0.5-1
- Update to latest upstream release 0.0.5

* Mon Jun 22 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.0.4-1
- Update to latest upstream release 0.0.4

* Mon Jun 15 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.0.3-1
- Update to latest upstream release 0.0.3

* Tue May 26 2020 Miro Hron??ok <mhroncok@redhat.com> - 0.0.2-2
- Rebuilt for Python 3.9

* Tue Mar 03 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.0.2-1
- Initial package for Fedora
