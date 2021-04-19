%global pypi_name python-magic
%global srcname magic

Name:           %{pypi_name}
Version:        0.4.22
Release:        1%{?dist}
Summary:        File type identification using libmagic

License:        MIT
URL:            https://github.com/ahupp/python-magic
Source0:        %{pypi_source %{pypi_name}}
#Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
This module uses ctypes to access the libmagic file type identification
library. It makes use of the local magic database and supports both textual
and MIME-type output.

%package -n     python3-%{srcname}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

Requires:       file-devel
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
This module uses ctypes to access the libmagic file type identification
library. It makes use of the local magic database and supports both textual
and MIME-type output.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{srcname}
%doc README.md
%license LICENSE
%{python3_sitelib}/magic/
%{python3_sitelib}/python_magic-%{version}-py*.egg-info

%changelog
* Wed Feb 17 2021 Fabian Affolter <mail@fabian-affolter.ch> - 0.4.22-1
- Update to latest upstream release 0.4.22 (#1929455)

* Wed Feb 10 2021 Fabian Affolter <mail@fabian-affolter.ch> - 0.4.20-1
- Update to latest upstream release 0.4.20 (#1901860)

* Mon Feb 01 2021 Fabian Affolter <mail@fabian-affolter.ch> - 0.4.19-1
- Update to latest upstream release 0.4.19 (#1901860)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Nov 15 2020 Christian Birk <mail@birkc.de> - 0.4.18-1
- New upstream release 0.4.18

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.4.15-3
- Rebuilt for Python 3.9

* Thu Jan 23 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.4.15-2
- Rename package (rhbz#1790100)

* Sat Jan 11 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.4.15-1
- Initial package for Fedora
