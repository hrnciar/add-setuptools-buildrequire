Name:           python-google-i18n-address
%global srcname %(echo %{name} | sed 's/^python-//')

Version:        2.4.0
Release:        2%{?dist}
Summary:        Address validation helpers for Google's i18n address database

License:        BSD with advertising
URL:            https://pypi.python.org/pypi/google-i18n-address/
Source0:        %{pypi_source}

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%global _description %{expand:
This package contains a copy of Google’s i18n address metadata
repository that contains great data but comes with no uptime guarantees.

Contents of this package will allow you to programatically build address
forms that adhere to rules of a particular region or country, validate
local addresses and format them to produce a valid address label for
delivery.

The package also contains a Python interface for address validation.}

%description %_description

%package -n python3-%{srcname}
Summary: Address validation helpers for Google's i18n address database
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname} %_description


%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build

%check
# warns about obsolete testing, and then downloads files from the internet
#{__python3} setup.py test

%install
%py3_install
# names used for test files are sure to cause clashses with other packages :/
rm -rf %{buildroot}/%{python3_sitelib}/tests

%files -n python3-%{srcname}
%license PKG-INFO
%doc README.rst
%{python3_sitelib}/i18naddress
%{python3_sitelib}/google_i18n_address*egg-info/

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Oct  8 11:30:10 EDT 2020 Paul Wouters <pwouters@redhat.com> - 2.4.0-1
- Initial package
