%global commit 6289d25a42cfdb5dfcac863b1b1b4ace32ce31b7
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           podman-compose
Version:        0.1.7
Release:        4.git20210129%{?dist}
Summary:        Run docker-compose.yml using podman
License:        GPLv2
URL:            https://github.com/containers/podman-compose
Source0:        https://github.com/containers/podman-compose/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

BuildArch:      noarch
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-pyyaml
Requires:       python%{python3_pkgversion}
Requires:       python%{python3_pkgversion}-pyyaml
Requires:       podman

%description
An implementation of docker-compose with podman backend.
The main objective of this project is to be able to run docker-compose.yml
unmodified and rootless.

%prep
%autosetup -n %{name}-%{commit}

%build
%py3_build
 
%install
%py3_install 

#Drop spurious shebang
sed -i /python3/d %{buildroot}%{python3_sitelib}/podman_compose.py


%files
%doc README.md CONTRIBUTING.md docs/ examples
%license LICENSE
%{_bindir}/podman-compose
%{python3_sitelib}/__pycache__/podman_compose*pyc
%{python3_sitelib}/podman_compose*

%changelog
* Fri Jan 29 2021 Gwyn Ciesla <gwync@protonmail.com> - 0.1.7-4.git20210129
- Update to latest git.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-3.git20201120
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov 23 2020 Mikel Olasagasti Uranga <mikel@olasagasti.info> 0.1.7-2.git20201120
- Change deps to be able to build in EPEL8

* Fri Nov 20 2020 Mikel Olasagasti Uranga <mikel@olasagasti.info> - 0.1.7-1.git20201120
- update to the latest git HEAD

* Wed Jul 29 2020 Pavel Raiskup <praiskup@redhat.com> - 0.1.6-1.git20200615
- update to the latest git HEAD; namely to allow spawning privileged containers
  and to fix volume initialization

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-5.git20191107
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.1.5-4.git20191107
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-3.git20191107
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 07 2019 Gwyn Ciesla <gwync@protonmail.com> - 0.1.5-2.git20191107
- Fix for service extension with the same name.

* Mon Oct 28 2019 Gwyn Ciesla <gwync@protonmail.com> - 0.1.5-1.git20191030
- Initial build.
