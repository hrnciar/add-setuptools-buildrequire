# Created by pyp2rpm-3.3.2
%global pypi_name pykeepass

Name:           python-%{pypi_name}
Version:        4.0.0
Release:        1%{?dist}
Summary:        Python library to interact with keepass databases

License:        GPLv3
URL:            https://github.com/pschmitt/pykeepass
Source0:        %{pypi_source}
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
This library allows you to write entries to a KeePass database.


%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
 
Requires:       python3dist(argon2-cffi) >= 19.2.0
Requires:       python3dist(construct) >= 2.10.54
Requires:       python3dist(future) >= 0.18.2
Requires:       python3dist(lxml) >= 4.3.5
Requires:       python3dist(pycryptodomex) >= 3.9.8
Requires:       python3dist(python-dateutil) >= 2.8.1

%description -n python3-%{pypi_name}
This library allows you to write entries to a KeePass database.


%prep
%autosetup -n %{pypi_name}-%{version}

# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

sed -i 's|pycryptodomex==|pycryptodomex>=|' requirements.txt
sed -i 's|construct==|construct>=|' requirements.txt
sed -i 's|construct==|construct>=|' setup.py


%build
%py3_build


%install
%py3_install


%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/


%changelog
* Mon Feb 08 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 4.0.0-1
- build(update): 4.0.0

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov 30 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 3.2.1-1
- build(update): 3.2.1

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.2.0-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 19 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 3.2.0-1
- Update to 3.2.0

* Wed Sep 25 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 3.0.3-2
- Built with with system 'pycryptodomex'
- Cleanup spec file

* Fri Jun 14 2019 Pavlo Rudyi <paulcarroty@fedoraproject.org> - 3.0.3-1
- initial build
