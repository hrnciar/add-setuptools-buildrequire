# what it's called on pypi
%global srcname repomd
# what it's imported as
%global libname %{srcname}
# name of egg info directory
%global eggname %{srcname}
# package name fragment
%global pkgname %{srcname}

%global _description \
This library provides an object-oriented interface to get information out of\
dnf/yum repositories.

%bcond_without tests


Name:           python-%{pkgname}
Version:        0.2.1
Release:        7%{?dist}
Summary:        Library for reading dnf/yum repositories
License:        MIT
URL:            https://github.com/carlwgeorge/repomd
Source0:        %pypi_source
BuildArch:      noarch


%description %{_description}


%package -n python3-%{pkgname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools >= 38.6.0
%if %{with tests}
BuildRequires:  python3-pytest
BuildRequires:  python3-defusedxml
BuildRequires:  python3-lxml
%endif
Requires:       python3-defusedxml
Requires:       python3-lxml
%{?python_provide:%python_provide python3-%{pkgname}}


%description -n python3-%{pkgname} %{_description}


%prep
%autosetup -n %{srcname}-%{version}
rm -r source/%{eggname}.egg-info setup.cfg


%build
%py3_build


%install
%py3_install


%if %{with tests}
%check
PYTHONPATH=%{buildroot}%{python3_sitelib} py.test-%{python3_version} --verbose tests
%endif


%files -n python3-%{pkgname}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{libname}.py
%{python3_sitelib}/__pycache__/%{libname}.cpython-%{python3_version_nodots}*.py*
%{python3_sitelib}/%{eggname}-%{version}-py%{python3_version}.egg-info


%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.2.1-5
- Rebuilt for Python 3.9

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.1-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.1-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 25 2019 Carl George <carl@george.computer> - 0.2.1-1
- Latest upstream

* Thu Mar 21 2019 Carl George <carl@george.computer> - 0.2.0-1
- Latest upstream

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Oct 27 2018 Carl George <carl@george.computer> - 0.1.0-1
- Initial package
