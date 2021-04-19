%global common_description %{expand:
Jedi is a static analysis tool for Python that can be used in IDEs/editors. Its
historic focus is autocompletion, but does static analysis for now as well.
Jedi is fast and is very well tested. It understands Python on a deeper level
than all other static analysis frameworks for Python.}

%bcond_without tests

# %%global commit 209e2713fd699b8a54aa4c8bbd0915e6c51f2092
# %%global shortcommit %%(c=%%{commit}; echo ${c:0:7})
%global baseversion 0.18.0

# jedi bundles 2 other projects
# when using the git tarball, the proejcts need to be pulled separately
# when using tarballs from PyPI, those are included
%global django_stubs_commit fd057010f6cbf176f57d1099e82be46d39b99cb9
%global typeshed_commit     d38645247816f862cafeed21a8f4466d306aacf3

Name:           python-jedi
Version:        %{baseversion}
Release:        1%{?dist}
Summary:        An auto completion tool for Python that can be used for text editors

# jedi is MIT
# django-stubs is MIT
# typeshed is MIT ASL 2.0
License:        MIT and ASL 2.0

URL:            https://jedi.readthedocs.org
Source0:        https://github.com/davidhalter/jedi/archive/v%{version}/jedi-%{version}.tar.gz
Source1:        https://github.com/davidhalter/django-stubs/archive/%{django_stubs_commit}/django-stubs-%{django_stubs_commit}.tar.gz
Source2:        https://github.com/davidhalter/typeshed/archive/%{typeshed_commit}/typeshed-%{typeshed_commit}.tar.gz
BuildArch:      noarch


%description %{common_description}

%package -n python%{python3_pkgversion}-jedi
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
%if %{with tests}
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-docopt
BuildRequires:  python%{python3_pkgversion}-colorama
BuildRequires:  python%{python3_pkgversion}-parso >= 0.8
%endif
%{?python_provide:%python_provide python%{python3_pkgversion}-jedi}

Provides:       bundled(python3dist(django-stubs)) = %{django_stubs_commit}
Provides:       bundled(typeshed) = %{typeshed_commit}

%description -n python%{python3_pkgversion}-jedi %{common_description}


%prep
%autosetup -n jedi-%{version} -p 1

# git submodules
pushd jedi/third_party
rmdir django-stubs typeshed
tar xf %{SOURCE1} && mv django-stubs-%{django_stubs_commit} django-stubs
tar xf %{SOURCE2} && mv typeshed-%{typeshed_commit} typeshed
popd
cp -p jedi/third_party/django-stubs/LICENSE.txt LICENSE-django-stubs.txt
cp -p jedi/third_party/typeshed/LICENSE LICENSE-typeshed.txt


%build
%py3_build


%install
%py3_install


%if %{with tests}
%check
# TODO investigate failing / skipped tests
# venv_and_pths: %%pytest manipulates the sys.path
%pytest --ignore test/test_integration.py -k "not (string_annotation[annotations9-result9-] or venv_and_pths)"
%endif


%files -n python%{python3_pkgversion}-jedi
%license LICENSE.txt LICENSE-django-stubs.txt LICENSE-typeshed.txt
%doc AUTHORS.txt CHANGELOG.rst README.rst
%{python3_sitelib}/jedi/
%{python3_sitelib}/jedi-%{baseversion}-py%{python3_version}.egg-info/


%changelog
* Tue Mar 02 2021 Lumír Balhar <lbalhar@redhat.com> - 0.18.0-1
- Update to 0.18.0
Resolves: rhbz#1910879

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.2^20200805git209e271-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Oct 30 2020 Miro Hrončok <mhroncok@redhat.com> - 0.17.2^20200805git209e271-1
- Update to a git snapshot to support parso 0.8
- Add provides for bundled django-stubs and typeshed
- Adapt the license tag to include the license of bundled projects
- Enable tests, except integration

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.17.1-1
- Update to 0.17.1

* Sun May 24 2020 Miro Hrončok <mhroncok@redhat.com> - 0.15.1-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 17 2019 Carl George <carl@george.computer> - 0.15.1-1
- Latest upstream

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.14.1-3
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Thu Aug 15 2019 Miro Hrončok <mhroncok@redhat.com> - 0.14.1-2
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Carl George <carl@george.computer> - 0.14.1-1
- Latest upstream
- Disable python2 subpackage on F31+ and EL8+ rhbz#1732815

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Sep 04 2018 Carl George <carl@george.computer> - 0.12.1-2
- Remove _docdir_fmt macro to allow upgrading subpackages separately rhbz#1625015
- Standardize on srcname, modname, eggname, and pkgname macros

* Fri Aug 24 2018 Pavel Raiskup <praiskup@redhat.com> - 0.12.1-1
- new upstream version

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 15 2018 Carl George <carl@george.computer> - 0.12.0-3
- Add patch0 to parse correct AST entry for version on Python 3.7.0b5

* Fri Jun 15 2018 Miro Hrončok <mhroncok@redhat.com> - 0.12.0-2
- Rebuilt for Python 3.7

* Mon Apr 16 2018 Carl George <carl@george.computer> - 0.12.0-1
- Latest upstream
- Enable test suite
- Share doc and license dir between subpackages

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jul 28 2017 Michel Alexandre Salim <salimma@fedoraproject.org> - 0.10.2-3
- Enable python3 subpackage for EPEL

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Apr 18 2017 Carl George <carl.george@rackspace.com> - 0.10.2-1
- Latest upstream

* Mon Apr 03 2017 Carl George <carl.george@rackspace.com> - 0.10.0-1
- Latest upstream
- Upstream license changed to MIT and Python
- Align spec with Python packaging guidelines

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.9.0-6
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu May 07 2015 Petr Hracek <phracek@kiasportyw-brq-redhat-com> - 0.9.0-1
- new upstream version 0.9.0 (#1217032)

* Mon Jan 19 2015 Petr Hracek <phracek@redhat.com> - 0.8.1-1
- new upstream version 0.8.1 (#1178815)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 0.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Mon Jan 06 2014 Petr Hracek <phracek@redhat.com> - 0.7.0-3
- Fix: Enable python3 subpackage (#1038398)

* Fri Aug 23 2013 Petr Hracek <phracek@redhat.com> - 0.7.0-1
- new upstream version 0.7.0

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu May 16 2013 Petr Hracek <phracek@redhat.com> - 0.6.0-1
- new upstream version 0.6.0

* Wed Apr 17 2013 Petr Hracek <phracek@redhat.com> - 0.5b5-3
- Test suite is available only on dev branch. It will not be used.

* Thu Apr 11 2013 Petr Hracek <phracek@redhat.com> - 0.5b5-2
- Some type warnings.
- Added dependency to python2-devel
- tests were run and 5/679 failed

* Thu Apr 11 2013 Petr Hracek <phracek@redhat.com> - 0.5b5-1
- Initial package.
