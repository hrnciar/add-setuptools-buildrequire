# Avoid fsspec -> distributed -> dask -> fsspec dependency loop.
%bcond_without bootstrap

%global srcname fsspec

Name:           python-%{srcname}
Version:        2021.4.0
%global Version 2021.04.0
Release:        1%{?dist}
Summary:        Specification for Pythonic file system interfaces

License:        BSD
URL:            https://github.com/intake/filesystem_spec
Source0:        %{url}/archive/%{Version}/%{srcname}-%{Version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-vcr)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(aiohttp)
BuildRequires:  python3dist(cloudpickle)
%if %{without bootstrap}
BuildRequires:  python3dist(distributed)
%endif
# Won't work in a build since it requires the kernel module to be loaded.
#BuildRequires:  python3dist(fusepy)
BuildRequires:  python3dist(lz4)
BuildRequires:  python3dist(pandas)
# Requires a running SSH server in a container.
#BuildRequires:  python3dist(paramiko)
BuildRequires:  python3dist(requests)
%if %{fedora} > 32
BuildRequires:  python3dist(zstandard)
%endif

%global _description %{expand:
Filesystem Spec is a project to unify various projects and classes to work with
remote filesystems and file-system-like abstractions using a standard pythonic
interface.}

%description %{_description}


%package -n     python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname} %{_description}


%prep
%autosetup -n filesystem_spec-%{Version} -p1

# Remove bundled egg-info
rm -rf %{srcname}.egg-info


%build
%py3_build


%install
%py3_install


%check
%{pytest} -vra -k 'not test_find'  # Doesn't have a vcr cassette.


%files -n python3-%{srcname}
%doc README.md
%license LICENSE
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info/


%changelog
* Fri Apr 16 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2021.4.0-1
- Update to latest version (#1950557)

* Tue Apr 06 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.9.0-1
- Update to latest version (#1946308)

* Sat Feb 27 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.8.7-1
- Update to latest version (#1931928)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan 19 2021 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.8.5-1
- Update to latest version (#1888386)

* Fri Sep 25 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.8.3-1
- Update to latest version (#1882492)

* Fri Sep 11 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.8.2-1
- Update to latest version (#1877896)

* Wed Sep 09 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.8.1-1
- Update to latest version (#1877412)

* Sun Aug 02 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.8.0-1
- Update to latest version

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hron??ok <mhroncok@redhat.com> - 0.7.4-2
- Rebuilt for Python 3.9

* Wed May 20 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.7.4-1
- Update to latest version

* Thu Apr 23 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.7.3-1
- Update to latest version

* Wed Apr 08 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.7.2-1
- Update to latest version

* Fri Mar 27 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.7.0-1
- Update to latest version

* Sun Mar 22 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.6.3-1
- Update to latest version

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 09 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.6.2-1
- Update to latest version

* Fri Nov 29 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.6.1-1
- Update to latest version

* Thu Nov 21 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.6.0-1
- Update to latest version

* Thu Oct 17 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.5.2-1
- Update to latest version

* Sat Sep 28 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.5.1-1
- Update to latest version

* Thu Sep 12 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.4.4-1
- Initial package.
