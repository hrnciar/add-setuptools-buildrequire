%global pypi_name jupyter_client
%global pypi_name_dash jupyter-client

Name:           python-%{pypi_name_dash}
Version:        6.1.12
Release:        2%{?dist}
Summary:        Jupyter protocol implementation and client libraries

License:        BSD
URL:            http://jupyter.org
Source0:        %pypi_source

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

%bcond_without doc
%bcond_without tests

%if %{with tests}
# The zmq tests are split in RPM only, the dependency is not tracked on Python level:
BuildRequires:  python3-zmq-tests
%endif

%description
This package contains the reference implementation of the Jupyter protocol.
It also provides client and kernel management APIs for working with kernels.

It also provides the `jupyter kernelspec` entrypoint for installing kernelspecs
for use with Jupyter frontends.

%package -n     python3-%{pypi_name_dash}
Summary:        Jupyter protocol implementation and client libraries
%{?python_provide:%python_provide python3-%{pypi_name_dash}}

# It fallbacks to ifconfig without this, and ifconfig is deprecated
Recommends:     python3-netifaces

%description -n python3-%{pypi_name_dash}
This package contains the reference implementation of the Jupyter protocol.
It also provides client and kernel management APIs for working with kernels.

It also provides the `jupyter kernelspec` entrypoint for installing kernelspecs
for use with Jupyter frontends.

%if %{with doc}
%package -n python-%{pypi_name_dash}-doc
Summary:        Documentation of the Jupyter protocol reference implementation
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_rtd_theme
BuildRequires:  python3-sphinxcontrib-github-alt

%description -n python-%{pypi_name_dash}-doc
Documentation of the reference implementation of the Jupyter protocol
%endif

%prep
%autosetup -p1 -n %{pypi_name}-%{version}

%if %{with doc}
# Use local objects.inv for intersphinx:
sed -i "s|\(('http://ipython.readthedocs.io/en/stable/', \)None)|\1'/usr/share/doc/python3-ipython-doc/html/objects.inv')|" docs/conf.py
%endif


%generate_buildrequires
%pyproject_buildrequires %{?with_tests:-x test}


%build
%pyproject_wheel

%if %{with doc}
PYTHONPATH=build/lib/ sphinx-build-3 docs html
# remove the sphinx-build leftovers
rm -r html/.{doctrees,buildinfo}
%endif


%install
%pyproject_install
%pyproject_save_files %{pypi_name}


%if %{with tests}
%check
%pytest -v
%endif


%global _docdir_fmt %{name}

%files -n python3-%{pypi_name_dash} -f %{pyproject_files}
%doc README.md
%license COPYING.md
%{_bindir}/jupyter-kernel
%{_bindir}/jupyter-kernelspec
%{_bindir}/jupyter-run

%if %{with doc}
%files -n python-%{pypi_name_dash}-doc
%doc html
%endif

%changelog
* Fri Apr 09 2021 Karolina Surma <ksurma@redhat.com> - 6.1.12-1
- Update to 6.1.12
Resolves: rhbz#1938505

* Fri Mar 05 2021 Miro Hron??ok <mhroncok@redhat.com> - 6.1.11-2
- Unpin jedi to make the package installable again with jedi 0.18

* Fri Jan 29 8:25:17 CET 2021 Tomas Hrnciar <thrnciar@redhat.com> - 6.1.11-1
- Update to 6.1.11 (#1914202)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Sep 17 2020 Tomas Hrnciar <thrnciar@redhat.com> - 6.1.7-1
- Update to 6.1.7 (#1856627)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Lum??r Balhar <lbalhar@redhat.com> - 6.1.5-1
- Update to 6.1.5 (#1852265)

* Sun May 24 2020 Miro Hron??ok <mhroncok@redhat.com> - 5.3.4-4
- Rebuilt for Python 3.9

* Sun May 24 2020 Miro Hron??ok <mhroncok@redhat.com> - 5.3.4-3
- Bootstrap for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 12 2019 Miro Hron??ok <mhroncok@redhat.com> - 5.3.4-1
- Update to 5.3.4 (#1759726)
- Run tests

* Thu Sep 26 2019 Jerry James <loganjerry@gmail.com> - 5.3.3-1
- Update to 5.3.3 (bz 1727659, also fixes bz 1755635)
- Drop old workaround for dual python2/python3 builds
- Use local objects.inv for intersphinx, BR python3-ipython-doc

* Sun Aug 18 2019 Miro Hron??ok <mhroncok@redhat.com> - 5.2.3-10
- Rebuilt for Python 3.8

* Sun Aug 18 2019 Miro Hron??ok <mhroncok@redhat.com> - 5.2.3-9
- Bootstrap for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Feb 14 2019 Miro Hron??ok <mhroncok@redhat.com> - 5.2.3-7
- Subpackage python2-jupyter-client has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 20 2018 Miro Hron??ok <mhroncok@redhat.com> - 5.2.3-4
- Rebuilt for Python 3.7

* Tue Jun 19 2018 Miro Hron??ok <mhroncok@redhat.com> - 5.2.3-3
- Bootstrap for Python 3.7

* Wed Mar 14 2018 Miro Hron??ok <mhroncok@redhat.com> - 5.2.3-1
- Updated to 5.2.3 (#1538378)
- Do not have 3.6 bytecode in 2.7 package

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 30 2018 Miro Hron??ok <mhroncok@redhat.com> - 5.2.1-3
- Enable automatic dependency generator, drop manual Python requires
- Fixes missing dependency on dateutil
- Add missing BRs for docs

* Sun Jan 14 2018 Miro Hron??ok <mhroncok@redhat.com> - 5.2.1-2
- Recommend netifaces (#1534203)

* Thu Jan 04 2018 Miro Hron??ok <mhroncok@redhat.com> - 5.2.1-1
- Updated to 5.2.1 (#1425248)
- Use Python 3 to build the docs, add BR on python3-sphinxcontrib-github-alt

* Fri Sep 01 2017 Miro Hron??ok <mhroncok@redhat.com> - 4.4.0-5
- Remove -2, -3, etc. executables (#1410332)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hron??ok <mhroncok@redhat.com> - 4.4.0-2
- Rebuild for Python 3.6

* Mon Sep 26 2016 Thomas Spura <tomspur@fedoraproject.org> - 4.4.0-1
- update to 4.4.0
- Source0: use files.pythonhosted.org

* Mon Apr 25 2016 Thomas Spura <tomspur@fedoraproject.org> - 4.2.2-4
- Use simpler docdir_fmt
- Fix BR/R requires

* Tue Apr 19 2016 Thomas Spura <tomspur@fedoraproject.org> - 4.2.2-3
- Fix docs generation (Zbigniew, #1327989)
- Require python2- instead python- where possible

* Mon Apr 18 2016 Thomas Spura <tomspur@fedoraproject.org> - 4.2.2-2
- Use dash in name
- Adjust description
- Use %%license

* Mon Apr 18 2016 Thomas Spura <tomspur@fedoraproject.org> - 4.2.2-1
- Initial package.
