%{!?sources_gpg: %{!?dlrn:%global sources_gpg 1} }
%global sources_gpg_sign 0x2426b928085a020d8a90d0d879ab7008d0896c8a

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%global client python-tackerclient
%global sclient tackerclient
%global executable tacker
%global with_doc 1

Name:       %{client}
Version:    1.3.0
Release:    3%{?dist}
Summary:    OpenStack Tacker client
License:    ASL 2.0
URL:        http://launchpad.net/%{client}/

Source0:    http://tarballs.openstack.org/%{client}/%{client}-%{upstream_version}.tar.gz
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
Source101:        http://tarballs.openstack.org/%{client}/%{client}-%{upstream_version}.tar.gz.asc
Source102:        https://releases.openstack.org/_static/%{sources_gpg_sign}.txt
%endif

BuildArch:  noarch

# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
BuildRequires:  /usr/bin/gpgv2
%endif

BuildRequires:  git

%package -n python3-%{sclient}
Summary:    OpenStack tacker client
%{?python_provide:%python_provide python3-%{sclient}}
Obsoletes: python2-%{sclient} < %{version}-%{release}

BuildRequires:  python3-devel
BuildRequires:  python3-mock
BuildRequires:  python3-fixtures
BuildRequires:  python3-flake8
BuildRequires:  python3-hacking
BuildRequires:  python3-keystoneclient
BuildRequires:  python3-oslo-log
BuildRequires:  python3-oslo-serialization
BuildRequires:  python3-pbr
BuildRequires:  python3-reno
BuildRequires:  python3-requests-mock
BuildRequires:  python3-setuptools
BuildRequires:  python3-stestr
BuildRequires:  python3-subunit
BuildRequires:  python3-testtools
BuildRequires:  python3-cliff
BuildRequires:  python3-osc-lib
BuildRequires:  python3-ddt

Requires:   python3-pbr >= 2.0.0
Requires:   python3-babel >= 2.3.4
Requires:   python3-cliff >= 2.8.0
Requires:   python3-iso8601 >= 0.1.11
Requires:   python3-keystoneclient >= 1:3.8.0
Requires:   python3-oslo-i18n >= 3.15.3
Requires:   python3-oslo-log >= 3.36.0
Requires:   python3-oslo-serialization >= 2.18.0
Requires:   python3-oslo-utils >= 3.40.0
Requires:   python3-requests >= 2.14.2
Requires:   python3-six >= 1.10.0
Requires:   python3-stevedore >= 1.20.0
Requires:   python3-osc-lib >= 1.8.0
Requires:   python3-netaddr >= 0.7.18
Requires:   python3-simplejson >= 3.5.1

%description -n python3-%{sclient}
OpenStack tacker client


%package -n python3-%{sclient}-tests-unit
Summary:    OpenStack taker client unit tests
Requires:   python3-%{sclient} = %{version}-%{release}

Requires:  python3-fixtures
Requires:  python3-flake8
Requires:  python3-hacking
Requires:  python3-oslo-log
Requires:  python3-oslo-serialization
Requires:  python3-pbr
Requires:  python3-setuptools
Requires:  python3-subunit
Requires:  python3-testtools
Requires:  python3-mock
Requires:  python3-stestr

%description -n python3-%{sclient}-tests-unit
OpenStack tacker client unit tests

This package contains the tacker client test files.


%if 0%{?with_doc}
%package -n python-%{sclient}-doc
Summary:    OpenStack tacker client documentation

BuildRequires: python3-sphinx
BuildRequires: python3-openstackdocstheme

%description -n python-%{sclient}-doc
OpenStack tacker client documentation

This package contains the documentation for tacker client.
%endif

%description
OpenStack tacker client.

%prep
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%endif
%autosetup -n %{client}-%{upstream_version} -S git

# Fix rpmlint warning for CRLF line termination
sed -i 's/\r$//' ./doc/source/cli/vnf_package_commands.rst ./doc/source/cli/commands.rst

# Let's handle dependencies ourseleves
rm -f *requirements.txt

%build
%{py3_build}

%if 0%{?with_doc}
# generate html docs
export PYTHONPATH=.
sphinx-build -W -b html doc/source doc/build/html
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

sphinx-build -W -b man doc/source doc/build/man
%endif

%install

%{py3_install}

%if 0%{?with_doc}
install -p -D -m 644 -v doc/build/man/tacker.1 %{buildroot}%{_mandir}/man1/tacker.1
%endif

# Create a versioned binary for backwards compatibility until everything is pure py3
ln -s %{executable} %{buildroot}%{_bindir}/%{executable}-3

%check
export OS_TEST_PATH='./tackerclient/tests/unit'
PYTHON=%{__python3} stestr --test-path $OS_TEST_PATH run

%files -n python3-%{sclient}
%license LICENSE
%{python3_sitelib}/%{sclient}
%{python3_sitelib}/*.egg-info
%exclude %{python3_sitelib}/%{sclient}/tests
%{_bindir}/%{executable}-3
%{_bindir}/%{executable}

%if 0%{?with_doc}
%{_mandir}/man1/*
%endif

%files -n python3-%{sclient}-tests-unit
%license LICENSE
%{python3_sitelib}/%{sclient}/tests

%if 0%{?with_doc}
%files -n python-%{sclient}-doc
%license LICENSE
%doc doc/build/html README.rst
%endif

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Oct 28 2020 Alfredo Moralejo <amoralej@redhat.com> 1.3.0-2
- Update to upstream version 1.3.0

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 04 2020 Joel Capitao <jcapitao@redhat.com> 1.1.0-1
- Update to upstream version 1.1.0

* Tue May 26 2020 Miro Hron??ok <mhroncok@redhat.com> - 0.16.1-4
- Rebuilt for Python 3.9

* Fri Mar 13 2020 Alfredo Moralejo <amoralej@redhat.com> - 0.16.1-3
- Replace assertItemsEqual with assertCountEqual

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 06 2019 Alfredo Moralejo <amoralej@redhat.com> 0.16.1-1
- Update to upstream version 0.16.1

* Thu Oct 03 2019 Miro Hron??ok <mhroncok@redhat.com> - 0.15.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hron??ok <mhroncok@redhat.com> - 0.15.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 11 2019 RDO <dev@lists.rdoproject.org> 0.15.0-1
- Update to 0.15.0


