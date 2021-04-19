%global srcname molecule-docker
%global setup_flags SKIP_PIP_INSTALL=1 PBR_VERSION=%{version}

Name: python-molecule-docker
Version: 0.2.4
Release: 2%{?dist}
Summary: Molecule Docker plugin
License: MIT

URL: https://github.com/ansible-community/molecule-docker
Source0: %{pypi_source}

BuildArch: noarch

BuildRequires: python3-toml
BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3-setuptools_scm
BuildRequires: python3-setuptools_scm_git_archive

%description
Molecule Docker Plugin is designed to allow use docker containers for
provisioning test resources.

%package -n python3-molecule-docker
Summary: %summary

Requires: python3-docker
Requires: python3-molecule


%{?python_disable_dependency_generator}
%{?python_provide:%python_provide python3-%{srcname}}
%description -n python3-molecule-docker
Molecule Docker Plugin is designed to allow use docker containers for
provisioning test resources.

%prep
%setup -q -n %{srcname}-%{version}

%build
%{py3_build}

%install
%{py3_install}

%files -n python3-molecule-docker
%license LICENSE
%{python3_sitelib}/molecule_docker-%{version}-py%{python3_version}.egg-info
%{python3_sitelib}/molecule_docker/

%doc *.rst

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec 21 2020 Chedi Toueiti <chedi.toueiti@gmail.com> - 0.2.4-1
- update to version 0.2.4

* Thu Oct 15 2020 Chedi Toueiti <chedi.toueiti@gmail.com> - 0.2-1
- initial package
