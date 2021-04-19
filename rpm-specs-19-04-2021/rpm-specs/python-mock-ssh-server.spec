%global srcname mock-ssh-server

Name:           python-%{srcname}
Version:        0.8.2
Release:        2%{?dist}
Summary:        Mock SSH server for testing purposes

License:        MIT
URL:            https://github.com/carletes/%{srcname}
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz 
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python%{python3_pkgversion}-paramiko

%global _description\
An SSH server for testing purposes mocksshserver packs a Python context\
manager that implements an SSH server for testing purposes. It is built\
on top of paramiko, so it does not need OpenSSH binaries to be installed.

%description %{_description}

%package -n     python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
 
Requires:       python%{python3_pkgversion}-paramiko

%description -n python%{python3_pkgversion}-%{srcname} %{_description}


%prep
%autosetup -n %{srcname}-%{version}
# Remove bundled egg-info
rm -rf *.egg-info

%build
%py3_build

%install
%py3_install


%files -n python%{python3_pkgversion}-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/mockssh/
%{python3_sitelib}/mock_ssh_server-%{version}-py%{python3_version}.egg-info

%changelog
* Thu Dec 03 2020 Raphael Groner <raphgro@fedoraproject.org> - 0.8.2-2
- fix minor issues for package review 

* Wed Sep 09 2020 Raphael Groner <raphgro@fedoraproject.org> - 0.8.2-1
- initial
