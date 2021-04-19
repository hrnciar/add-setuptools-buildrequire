%global srcname pytest-mpl

Name:           python-%{srcname}
Version:        0.12
Release:        2%{?dist}
Summary:        Pytest plugin for testing figure output from Matplotlib

License:        BSD
URL:            https://github.com/matplotlib/pytest-mpl
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
# Missing file: https://github.com/matplotlib/pytest-mpl/pull/109
Source1:        https://github.com/matplotlib/pytest-mpl/raw/01c5ec39caa5001d700c7819628b57c798f1e2bb/tests/baseline/test_hash_lib.json
# Probably not going upstream.
Patch0001:      0001-Increase-tolerance-for-new-FreeType.patch

BuildArch:      noarch

%global _description \
This is a plugin to facilitate image comparison for Matplotlib figures in \
pytest. Matplotlib includes a number of test utilities and decorators, but \
these are geared towards the nose testing framework. Pytest-mpl makes it easy \
to compare figures produced by tests to reference images when using pytest.

%description %{_description}


%package -n     python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

BuildRequires:  python3-devel
BuildRequires:  python3dist(matplotlib)
BuildRequires:  python3dist(nose)
BuildRequires:  python3dist(pillow)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(setuptools)

%description -n python3-%{srcname} %{_description}


%prep
%autosetup -n %{srcname}-%{version} -p1
cp %SOURCE1 tests/baseline/

# Remove bundled egg-info
rm -rf %{srcname}.egg-info


%build
%py3_build


%install
%py3_install


%check
# Skip networked tests.
MPLBACKEND=Agg %{pytest} --mpl tests -k 'not test_succeeds_remote and not test_succeeds_faulty_mirror'
MPLBACKEND=Agg %{pytest} tests -k 'not test_succeeds_remote and not test_succeeds_faulty_mirror'


%files -n python3-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/pytest_mpl
%{python3_sitelib}/pytest_mpl-%{version}-py%{python3_version}.egg-info


%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Dec 13 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.12-1
- Update to latest version (#1894886)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.11-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 15 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.11-1
- Update to latest version

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.10-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.10-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Oct 19 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.10-1
- Update to latest version

* Wed Jul 18 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.9-2
- Remove unnecessary cache files

* Mon Jul 16 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.9-1
- Initial package.
