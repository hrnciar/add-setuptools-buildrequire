%global pypi_name josepy

%global py3_prefix python%{python3_pkgversion}

%bcond_without docs

Name:           python-%{pypi_name}
Version:        1.8.0
Release:        1%{?dist}
Summary:        JOSE protocol implementation in Python

License:        ASL 2.0
URL:            https://pypi.python.org/pypi/josepy
Source0:        %{pypi_source}
Source1:        %{pypi_source}.asc
# Key mentioned in https://github.com/certbot/josepy/blob/master/tools/release.sh#L37
# Keyring generation steps as follows:
#   gpg2 --keyserver pool.sks-keyservers.net --recv-key A2CFB51FA275A7286234E7B24D17C995CD9775F2
#   gpg2 --export --export-options export-minimal A2CFB51FA275A7286234E7B24D17C995CD9775F2 > gpg-A2CFB51FA275A7286234E7B24D17C995CD9775F2.gpg
Source2:        gpg-A2CFB51FA275A7286234E7B24D17C995CD9775F2.gpg
BuildArch:      noarch

# Remove various unpackaged testing dependencies that are used only for linting
Patch0:         0000-ignore-missing-linters.patch

BuildRequires:  %{py3_prefix}-devel
BuildRequires:  %{py3_prefix}-pytest
BuildRequires:  %{py3_prefix}-setuptools

# Used to verify OpenPGP signature
BuildRequires:  gnupg2
%if 0%{?rhel} && 0%{?rhel} == 8
# "gpgverify" macro, not in COPR buildroot by default
BuildRequires:  epel-rpm-macros >= 8-5
%endif

%if %{with docs}
BuildRequires:  make
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_rtd_theme
%endif

%description
JOSE protocol implementation in Python using cryptography.


%package -n     %{py3_prefix}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       %{py3_prefix}-cryptography
Requires:       %{py3_prefix}-pyOpenSSL
Requires:       %{py3_prefix}-setuptools
BuildRequires:  %{py3_prefix}-cryptography
BuildRequires:  %{py3_prefix}-pyOpenSSL
BuildRequires:  %{py3_prefix}-setuptools

%if %{with docs}
Recommends:     python-%{pypi_name}-doc
%endif

%description -n %{py3_prefix}-%{pypi_name}
JOSE protocol implementation in Python using cryptography.

This is the Python 3 version of the package.

%if %{with docs}
%package -n python-%{pypi_name}-doc
Summary:        Documentation for python-%{pypi_name}
Conflicts:      python2-%{pypi_name} < 1.1.0-9
Conflicts:      %{py3_prefix}-%{pypi_name} < 1.1.0-9
%description -n python-%{pypi_name}-doc
Documentation for python-%{pypi_name}
%endif

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

# Build documentation
%if %{with docs}
%{__python3} setup.py install --user
make -C docs man PATH=${HOME}/.local/bin:$PATH SPHINXBUILD=sphinx-build-3
%endif

%install
%py3_install

%if %{with docs}
install -Dpm0644 -t %{buildroot}%{_mandir}/man1 docs/_build/man/*.1*
%endif

%check
py.test-3 -x -v

%files -n %{py3_prefix}-%{pypi_name}
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/josepy
%{python3_sitelib}/josepy-%{version}-py%{python3_version}.egg-info
%{_bindir}/jws

%if %{with docs}
%files -n python-%{pypi_name}-doc
%license LICENSE.txt
%doc README.rst
%{_mandir}/man1/*
%endif

%changelog
* Tue Mar 16 2021 Felix Schwarz <fschwarz@fedoraproject.org> - 1.8.0-1
- update to 1.8.0

* Tue Feb 23 2021 Nick Bebout <nb@fedoraproject.org> - 1.7.0-1
- Update to 1.7.0

* Tue Feb 02 2021 Nick Bebout <nb@fedoraproject.org> - 1.6.0-1
- Update to 1.6.0

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Nov 04 2020 Felix Schwarz <fschwarz@fedoraproject.org> - 1.5.0-1
- update to 1.5.0

* Tue Aug 18 2020 Felix Schwarz <fschwarz@fedoraproject.org> - 1.4.0-1
- update to 1.4.0

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.3.0-3
- Rebuilt for Python 3.9

* Tue Mar 24 2020 Felix Schwarz <fschwarz@fedoraproject.org> - 1.3.0-2
- build Python 3 subpackage also in EPEL7

* Wed Jan 29 2020 Felix Schwarz <fschwarz@fedoraproject.org> 1.3.0-1
- Update to 1.3.0 (#1795747)

* Wed Jan 29 2020 Felix Schwarz <fschwarz@fedoraproject.org> 1.2.0-6
- enable GPG source file verification

* Mon Oct 07 2019 Eli Young <elyscape@gmail.com> - 1.2.0-5
- Support EPEL8 builds

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 01 2019 Eli Young <elyscape@gmail.com> - 1.2.0-1
- Update to 1.2.0 (#1725899)

* Thu Jun 27 2019 Eli Young <elyscape@gmail.com> - 1.1.0-9
- Split docs to separate package (#1700273)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Dec 13 2018 Eli Young <elyscape@gmail.com> - 1.1.0-7
- Remove Python 2 package in Fedora 30+ (#1658534)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 02 2018 Eli Young <elyscape@gmail.com> - 1.1.0-5
- Enable tests

* Mon Jul 02 2018 Miro Hrončok <mhroncok@redhat.com> - 1.1.0-4
- Rebuilt for Python 3.7

* Fri Jun 29 2018 Eli Young <elyscape@gmail.com> - 1.1.0-3
- Use available python2 metapackages for EPEL7
- Specify binary name for sphinx-build
- Fix permissions on man files

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.1.0-2
- Rebuilt for Python 3.7

* Tue Apr 17 2018 Eli Young <elyscape@gmail.com> - 1.1.0-1
- Update to 1.1.0 (#1567455)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Eli Young <elyscape@gmail.com> - 1.0.1-1
- Initial package.
