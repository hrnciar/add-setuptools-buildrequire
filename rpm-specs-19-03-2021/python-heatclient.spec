%{!?sources_gpg: %{!?dlrn:%global sources_gpg 1} }
%global sources_gpg_sign 0x5d2d1e4fb8d38e6af76c50d53d4fec30cf5ce3da
%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%global with_doc 1

%global sname heatclient

%global common_desc \
This is a client for the OpenStack Heat API. There's a Python API (the \
heatclient module), and a command-line script (heat). Each implements 100% of \
the OpenStack Heat API.

Name:    python-heatclient
Version: 2.3.0
Release: 1%{?dist}
Summary: Python API and CLI for OpenStack Heat

License: ASL 2.0
URL:     https://launchpad.net/python-heatclient
Source0: https://tarballs.openstack.org/%{name}/%{name}-%{upstream_version}.tar.gz
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
Source101:        https://tarballs.openstack.org/%{name}/%{name}-%{upstream_version}.tar.gz.asc
Source102:        https://releases.openstack.org/_static/%{sources_gpg_sign}.txt
%endif

BuildArch: noarch

# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
BuildRequires:  /usr/bin/gpgv2
%endif

%description
%{common_desc}

%package -n python3-%{sname}
Summary: Python API and CLI for OpenStack Heat
%{?python_provide:%python_provide python3-heatclient}
Obsoletes: python2-%{sname} < %{version}-%{release}

BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3-pbr
BuildRequires: git-core

Requires: python3-babel
Requires: python3-iso8601
Requires: python3-keystoneauth1 >= 3.4.0
Requires: python3-osc-lib >= 1.14.0
Requires: python3-prettytable
Requires: python3-pbr
Requires: python3-six
Requires: python3-oslo-serialization >= 2.18.0
Requires: python3-oslo-utils >= 3.33.0
Requires: python3-oslo-i18n >= 3.15.3
Requires: python3-swiftclient >= 3.2.0
Requires: python3-requests
Requires: python3-cliff
Requires: python3-PyYAML

%description -n python3-%{sname}
%{common_desc}

%if 0%{?with_doc}
%package doc
Summary: Documentation for OpenStack Heat API Client

BuildRequires: python3-sphinx
BuildRequires: python3-openstackdocstheme
BuildRequires: python3-babel
BuildRequires: python3-iso8601
BuildRequires: python3-keystoneauth1
BuildRequires: python3-osc-lib
BuildRequires: python3-prettytable
BuildRequires: python3-pbr
BuildRequires: python3-six
BuildRequires: python3-oslo-serialization
BuildRequires: python3-oslo-utils
BuildRequires: python3-oslo-i18n
BuildRequires: python3-swiftclient
BuildRequires: python3-requests
BuildRequires: python3-cliff

%description doc
%{common_desc}

This package contains auto-generated documentation.
%endif

%prep
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%endif
%autosetup -n %{name}-%{upstream_version} -S git

rm -rf {test-,}requirements.txt tools/{pip,test}-requires


%build
%{py3_build}

%install
%{py3_install}
echo "%{version}" > %{buildroot}%{python3_sitelib}/heatclient/versioninfo
# Create a versioned binary for backwards compatibility until everything is pure py3
ln -s heat %{buildroot}%{_bindir}/heat-3

mkdir -p %{buildroot}%{_sysconfdir}/bash_completion.d
install -pm 644 tools/heat.bash_completion \
    %{buildroot}%{_sysconfdir}/bash_completion.d/heat

# Delete tests
rm -fr %{buildroot}%{python3_sitelib}/heatclient/tests

%if 0%{?with_doc}
export PYTHONPATH=.
sphinx-build -W -b html doc/source doc/build/html
# Fix hidden-file-or-dir warnings
rm -fr doc/build/html/.doctrees doc/build/html/.buildinfo

# generate man page
sphinx-build -W -b man doc/source doc/build/man
install -p -D -m 644 doc/build/man/heat.1 %{buildroot}%{_mandir}/man1/heat.1
%endif

%files -n python3-%{sname}
%doc README.rst
%license LICENSE
%{python3_sitelib}/heatclient
%{python3_sitelib}/*.egg-info
%{_sysconfdir}/bash_completion.d
%if 0%{?with_doc}
%{_mandir}/man1/heat.1.gz
%endif
%{_bindir}/heat
%{_bindir}/heat-3

%if 0%{?with_doc}
%files doc
%doc doc/build/html
%license LICENSE
%endif

%changelog
* Tue Mar 16 2021 Joel Capitao <jcapitao@redhat.com> 2.3.0-1
- Update to upstream version 2.3.0

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Oct 28 2020 Alfredo Moralejo <amoralej@redhat.com> 2.2.1-2
- Update to upstream version 2.2.1

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 04 2020 Joel Capitao <jcapitao@redhat.com> 2.1.0-1
- Update to upstream version 2.1.0

* Tue May 26 2020 Miro Hron??ok <mhroncok@redhat.com> - 1.18.0-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 05 2019 Alfredo Moralejo <amoralej@redhat.com> 1.18.0-1
- Update to upstream version 1.18.0

* Thu Oct 03 2019 Miro Hron??ok <mhroncok@redhat.com> - 1.17.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hron??ok <mhroncok@redhat.com> - 1.17.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 12 2019 RDO <dev@lists.rdoproject.org> 1.17.0-1
- Update to 1.17.0

