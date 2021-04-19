# what it's called on pypi
%global srcname anyio
# what it's imported as
%global libname %{srcname}
# name of egg info directory
%global eggname %{srcname}
# package name fragment
%global pkgname %{srcname}

%global common_description %{expand:
AnyIO is a asynchronous compatibility API that allows applications and
libraries written against it to run unmodified on asyncio, curio and trio.}

Name:           python-%{pkgname}
Version:        2.0.2
Release:        1%{?dist}
Summary:        Compatibility layer for multiple asynchronous event loop implementations
License:        MIT
URL:            https://github.com/agronholm/%{srcname}
Source0:        %pypi_source
# cherry picked from master
Patch0:         0001-Moved-pytest-and-coverage-configurations-to-pyprojec.patch
# cherry picked from master
Patch1:         0002-Fixed-pytest-configuration-in-pyproject.toml.patch
# https://github.com/agronholm/anyio/pull/188
Patch2:         0003-Add-network-mark-to-getaddrinfo-test.patch

BuildArch:      noarch


%description %{common_description}


%package -n python3-%{pkgname}
Summary:        %{summary}
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(curio)
BuildRequires:  python3dist(trio)

%generate_buildrequires
%pyproject_buildrequires -x test,doc

%description -n python3-%{pkgname} %{common_description}


%package -n python-%{srcname}-doc
Summary:        anyio documentation
%description -n python-%{srcname}-doc
Documentation for anyio


%prep
%autosetup -n %{srcname}-%{version} -p1
rm -rf %{eggname}.egg-info

%build
%pyproject_wheel
# generate html docs
PYTHONPATH=${PWD} sphinx-build-3 docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%pyproject_install
%pyproject_save_files anyio


%check
%pytest -m "not network"


%files -n python3-%{pkgname} -f %{pyproject_files}
%license LICENSE
%doc README.rst

%files -n python-%{srcname}-doc
%doc html
%license LICENSE


%changelog
* Thu Jan 28 2021 Dan Čermák <dan.cermak@cgc-instruments.com> - 2.0.2-1
- New upstream release 2.0.2

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 02 2020 Carl George <carl@george.computer> - 1.3.1-1
- Latest upstream

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.2.3-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 13 2020 Carl George <carl@george.computer> - 1.2.3-1
- Latest upstream rhbz#1786957

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 16 2019 Carl George <carl@george.computer> - 1.0.0-1
- Initial package
