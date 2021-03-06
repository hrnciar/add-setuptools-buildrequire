%global pypi_name python-registry
%global srcname registry
%{?python_disable_dependency_generator}

Name:           python-%{srcname}
Version:        1.4
Release:        2%{?dist}
Summary:        Read access to Windows Registry files

License:        ASL 2.0
URL:            https://github.com/williballenthin/python-registry
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
python-registry is a pure Python library that provides read-only access to
Windows NT Registry files. These include NTUSER.DAT, userdiff, and SAM. The
interface is two-fold: a high-level interface suitable for most tasks, and
a low level set of parsing objects and methods which may be used for advanced
study of the Windows NT Registry.

%package -n     python3-%{srcname}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-six
BuildRequires:  python3-pytest

Requires:       python3-unicodecsv
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
python-registry is a pure Python library that provides read-only access to
Windows NT Registry files. These include NTUSER.DAT, userdiff, and SAM. The
interface is two-fold: a high-level interface suitable for most tasks, and
a low level set of parsing objects and methods which may be used for advanced
study of the Windows NT Registry.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info
sed -i -e '/^#!\//, 1d' Registry/*.py

%build
%py3_build

%install
%py3_install

%check
%pytest -v tests -k "not test_regsz_value and not test_decoding and not test_utf16le_kanji_with_nulls"

%files -n python3-%{srcname}
%doc CHANGELOG.TXT README.MD
%license LICENSE.TXT
%{python3_sitelib}/Registry/
%{python3_sitelib}/python_registry-*.egg-info/

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 24 2021 Fabian Affolter <mail@fabian-affolter.ch> - 1.4-1
- Add new BR, license file and docs (#1914873)
- Update to latest upstream release 1.4

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hron??ok <mhroncok@redhat.com> - 1.3.1-3
- Rebuilt for Python 3.9

* Mon Mar 23 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.3.1-2
- Disable dep generator to avoid issue with enum-compat (rhbz#1809910)

* Wed Mar 04 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.3.1-1
- Initial package for Fedora
