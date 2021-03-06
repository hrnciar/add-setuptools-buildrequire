# Created by pyp2rpm-3.3.2
%global pypi_name python-socketio
%global srcname socketio

%global _description %{expand:
Socket.IO is a transport protocol that enables real-time bidirectional 
event-based communication between clients (typically, though not always, 
web browsers) and a server. The official implementations of the client 
and server components are written in JavaScript. This package provides 
Python implementations of both, each with standard and asyncio variants.}

Name:           python-%{srcname}
Version:        4.6.0
Release:        2%{?dist}
Summary:        Socket.IO server

License:        MIT
URL:            http://github.com/miguelgrinberg/python-socketio/
# pypi source tarball does not contain tests
#Source0:        https://files.pythonhosted.org/packages/source/p/{pypi_name}/{pypi_name}-{version}.tar.gz
Source0:        https://github.com/miguelgrinberg/%{name}/archive/v%{version}.tar.gz

BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(aiohttp) >= 3.4
BuildRequires:  python3dist(mock)
BuildRequires:  python3dist(python-engineio) >= 3.9.0
BuildRequires:  python3dist(requests) >= 2.21.0
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(six) >= 1.9.0
BuildRequires:  python3dist(websocket-client) >= 0.54.0
BuildRequires:  python3dist(websockets) >= 7.0

%description %_description

%package -n     python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
 
Requires:       python3dist(aiohttp) >= 3.4
Requires:       python3dist(python-engineio) >= 3.9.0
Requires:       python3dist(requests) >= 2.21.0
Requires:       python3dist(six) >= 1.9.0
Requires:       python3dist(websocket-client) >= 0.54.0
Requires:       python3dist(websockets) >= 7.0

%description -n python3-%{srcname} %_description


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/socketio
%{python3_sitelib}/python_socketio-%{version}-py%{python3_version}.egg-info

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Sep 03 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 4.6.0-1
- Update to 4.6.0

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hron??ok <mhroncok@redhat.com> - 4.4.0-4
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 30 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 4.4.0-2
- Use expand macro for description

* Sun Dec 22 2019 Mukundan Ragavan <nonamedotc@gmail.com> - 4.4.0-1
- Initial package.
