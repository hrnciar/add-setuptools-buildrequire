Name:           python-numpydoc
Version:        1.1.0
Release:        3%{?dist}
Summary:        Sphinx extension to support docstrings in NumPy format

License:        BSD
URL:            https://pypi.python.org/pypi/numpydoc
Source0:        https://files.pythonhosted.org/packages/source/n/numpydoc/numpydoc-%{version}.tar.gz
# Upstream patch to ignore doc/ directory during tests
Patch0:         https://github.com/numpy/numpydoc/pull/296.patch
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

%description
Numpydoc inserts a hook into Sphinx's autodoc that converts docstrings
following the NumPy/SciPy format to a form palatable to Sphinx.


%package -n     python3-numpydoc
Summary:        %{summary}
%{?python_provide:%python_provide python3-numpydoc}
%description -n python3-numpydoc
Numpydoc inserts a hook into Sphinx's autodoc that converts docstrings
following the NumPy/SciPy format to a form palatable to Sphinx.


%prep
%autosetup -p1 -n numpydoc-%{version}
# let's not measure coverage:
sed -i '/pytest-cov/d' test_requirements.txt
sed -Ei 's/\s+--cov\S+//g' setup.cfg

%generate_buildrequires
%pyproject_buildrequires -x testing

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files numpydoc

%check
# Deselected tests need to download an inventory from docs.python.org
%pytest -k "not test_MyClass and not test_my_function"


%files -n python3-numpydoc -f %pyproject_files
%license LICENSE.txt
%doc README.rst

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Nov 13 2020 Miro Hrončok <mhroncok@redhat.com> - 1.1.0-2
- Don't BR pytest-cov

* Wed Sep 09 2020 Lumír Balhar <lbalhar@redhat.com> - 1.1.0-1
- Update to 1.1.0 (#1701764)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon May 25 2020 Miro Hrončok <mhroncok@redhat.com> - 0.9.2-4
- Rebuilt for Python 3.9

* Fri May 08 2020 Orion Poplawski <orion@nwra.com> - 0.9.2-3
- Add upstream patch for python 3.9 compatibility

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Dec 28 2019 Orion Poplawski <orion@nwra.com> - 0.9.2-1
- Update to 0.9.2

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9.1-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9.1-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May  7 2019 Orion Poplawski <orion@nwra.com> - 0.9.1-1
- Update to 0.9.1

* Wed Mar 06 2019 Miro Hrončok <mhroncok@redhat.com> - 0.8.0-5
- Subpackage python2-numpydoc has been removed
  See https://fedoraproject.org/wiki/Changes/Sphinx2

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.8.0-2
- Rebuilt for Python 3.7

* Tue May 29 2018 Thomas Spura <tomspur@fedoraproject.org> - 0.8.0-1
- update to 0.8.0 (#1562463)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Aug 15 2017 Miro Hrončok <mhroncok@redhat.com> - 0.7.0-1
- Updated to 0.7.0 (#1481761)
- Rewrote the spec completely

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.5-6
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Aug 27 2014 Thomas Spura <tomspur@fedoraproject.org> - 0.5-1
- update to 0.5 (#1134171)
- enable python3 subpackage

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Aug  5 2013 Thomas Spura <tomspur@fedoraproject.org> - 0.4-2
- BR python2-devel, python-sphinx, python-nose
- use macro in URL
- disable python3 package for now

* Fri Aug  2 2013 Thomas Spura <tomspur@fedoraproject.org> - 0.4-1
- initial package
