%global pypi_name entry_point_inspector
%global sname epi

Name:           python-%{sname}
Version:        0.1.2
Release:        2%{?dist}
Summary:        Tool for looking at the entry point plugins on a system

License:        ASL 2.0
URL:            https://github.com/dhellmann/entry_point_inspector
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
Entry Point Inspector is a tool for looking at the entry point plugins
installed on a system.

%package -n     python3-%{sname}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
%{?python_provide:%python_provide python3-%{sname}}

%description -n python3-%{sname}
Entry Point Inspector is a tool for looking at the entry point plugins
installed on a system.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{sname}
%doc README.rst announce.rst
%license LICENSE
%{_bindir}/epi
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Dec 03 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.1.2-1
- Remove Python 2
- Update to latest upstream release 0.1.2 (#1787845)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.1.1-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.1-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.1-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Alan Pevec <alan.pevec@redhat.com> 0.1.1-1
- Update to 0.1.1
- Drop python2 in Fedora

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.1-10
- Rebuilt for Python 3.7

* Wed Feb 21 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.1-9
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.1-5
- Rebuild for Python 3.6

* Thu Oct 20 2016 Chandan Kumar <chkumar246@gmail.com> - 0.1-4
- Fixed package name

* Wed Sep 28 2016 Chandan Kumar <chkumar246@gmail.com> - 0.1-3
- Fixed source macro in prep section

* Wed Sep 28 2016 Chandan Kumar <chkumar246@gmail.com> - 0.1-2
- Added sources for LICENSE, README.rst and announce.rst
- Included check macro to run unit tests

* Tue Sep 27 2016 Chandan Kumar <chkumar246@gmail.com> - 0.1-1
- Initial package.
