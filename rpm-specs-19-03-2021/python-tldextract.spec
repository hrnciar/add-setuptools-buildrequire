%global pypi_name tldextract

%global py3_prefix python%{python3_pkgversion}

Name:           python-%{pypi_name}
Version:        3.1.0
Release:        2%{?dist}
Summary:        Accurately separate the TLD from the registered domain and subdomains of a URL

License:        BSD
URL:            https://pypi.python.org/pypi/tldextract
Source0:        %{pypi_source}
# pytest-pylint is not packaged in Fedora
Patch0:         %{pypi_name}-remove-pytest-modules.patch
# setuptools_scm is not packaged for EPEL 7/Python 2 and the upstream tarball
# already ships "tldextract/_version.py"
Patch1:         %{pypi_name}-no-setuptools_scm.patch

BuildArch:      noarch

BuildRequires:  %{py3_prefix}-devel
BuildRequires:  %{py3_prefix}-idna
BuildRequires:  %{py3_prefix}-filelock >= 3.0.8
BuildRequires:  %{py3_prefix}-pytest
BuildRequires:  %{py3_prefix}-pytest-mock
BuildRequires:  %{py3_prefix}-requests >= 2.1.0
BuildRequires:  %{py3_prefix}-requests-file >= 1.4
BuildRequires:  %{py3_prefix}-responses
BuildRequires:  %{py3_prefix}-setuptools
BuildRequires:  %{py3_prefix}-setuptools_scm

%description
Accurately separate the TLD from the registered domain and
subdomains of a URL, using the Public Suffix List. By default,
this includes the public ICANN TLDs and their exceptions. You can
optionally support the Public Suffix List's private domains as
well.

%package -n     %{py3_prefix}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       %{py3_prefix}-idna
Requires:       %{py3_prefix}-filelock >= 3.0.8
Requires:       %{py3_prefix}-requests >= 2.1.0
Requires:       %{py3_prefix}-requests-file >= 1.4
Requires:       %{py3_prefix}-setuptools

%description -n %{py3_prefix}-%{pypi_name}
Accurately separate the TLD from the registered domain and
subdomains of a URL, using the Public Suffix List. By default,
this includes the public ICANN TLDs and their exceptions. You can
optionally support the Public Suffix List's private domains as
well.

This is the Python 3 version of the package.

%prep
%setup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
%patch0 -p1

# emulate setuptools_scm for RHEL 7
%if 0%{?rhel} && 0%{?rhel} == 7
%patch1 -p1
sed -i 's/@@VERSION@@/%{version}/' setup.py
# PKG-INFO file must be kept when using setuptools_scm
rm PKG-INFO
%endif

%build
%py3_build

%install
%py3_install

%check
# test_log_snapshot_diff is an integration test and requires network access
# (additionally that test requires python3-pytest-mock which is not available
# in EPEL 7)
TEST_SELECTOR="not test_log_snapshot_diff"

py.test-3 -x -vk "$TEST_SELECTOR" tests

%files -n %{py3_prefix}-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/tldextract
%{python3_sitelib}/tldextract-%{version}-py%{python3_version}.egg-info
%{_bindir}/tldextract

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Nov 24 2020 Felix Schwarz <fschwarz@fedoraproject.org> - 3.1.0-1
- update to 3.1.0

* Wed Nov 04 2020 Felix Schwarz <fschwarz@fedoraproject.org> - 3.0.2-1
- update to 3.0.2

* Tue Aug 18 2020 Felix Schwarz <fschwarz@fedoraproject.org> - 2.2.3-1
- update to 2.2.3

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.2.2-3
- Rebuilt for Python 3.9

* Sun May 17 2020 Felix Schwarz <fschwarz@fedoraproject.org> - 2.2.2-2
- enable Python 3 tests for EPEL 7

* Tue Apr 28 2020 Felix Schwarz <fschwarz@fedoraproject.org> - 2.2.2-1
- update to 2.2.2
- run tests in %%check
- add Python 3 subpackage in EPEL 7

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Oct 07 2019 Eli Young <elyscape@gmail.com> - 2.2.1-5
- Support EPEL8 builds

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.2.1-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.2.1-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 05 2019 Eli Young <elyscape@gmail.com> - 2.2.1-1
- Update to 2.2.1 (#1685688)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Dec 13 2018 Eli Young <elyscape@gmail.com> - 2.2.0-5
- Remove Python 2 package in Fedora 30+

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.2.0-3
- Rebuilt for Python 3.7

* Mon Feb 26 2018 Nick Bebout <nb@usi.edu> - 2.2.0-2
- Add python2- prefix where possible

* Thu Feb 15 2018 Eli Young <elyscape@gmail.com> - 2.2.0-1
- Initial package (#1545951)
