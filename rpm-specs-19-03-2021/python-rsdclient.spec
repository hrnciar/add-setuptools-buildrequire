%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%global with_doc 1

%global sname rsdclient
%global pyname python_rsdclient

Name:           python-%{sname}
Version:        1.0.2
Release:        3%{?dist}
Summary:        OpenStack client plugin for Rack Scale Design

License:        ASL 2.0
URL:            http://git.openstack.org/cgit/openstack/%{name}
Source0:        http://tarballs.openstack.org/%{name}/%{name}-%{version}.tar.gz
BuildArch:      noarch

%description
This is a client for the RSD Pod Manager API, which is based on OpenStack
client framework. It provides a Python API (rsdclient/v1 module) and a RSD
specific plugin for OpenStack client (rsdclient/osc).

%package -n     python3-%{sname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{sname}}

BuildRequires:  git
BuildRequires:  python3-devel
BuildRequires:  python3-oslotest >= 1.10.0
BuildRequires:  python3-setuptools
BuildRequires:  python3-testrepository >= 0.0.18
BuildRequires:  python3-testtools >= 1.4.0

Requires:       python3-six >= 1.10.0
Requires:       python3-osc-lib >= 1.7.0
Requires:       python3-pbr >= 2.0
Requires:       python3-rsd-lib >= 1.2.0
%description -n python3-%{sname}
This is a client for the RSD Pod Manager API, which is based on OpenStack
client framework. It provides a Python API (rsdclient/v1 module) and a RSD
specific plugin for OpenStack client (rsdclient/osc).

%package -n python3-%{sname}-tests
Summary: python-rsdclient tests
Requires: python3-%{sname} = %{version}-%{release}

%description -n python3-%{sname}-tests
Tests for python-rsdclient

%if 0%{?with_doc}
%package -n python-%{sname}-doc
Summary: python-rsdclient documentation
BuildRequires: python3-sphinx
BuildRequires: python3-openstackdocstheme >= 1.11.0

%description -n python-%{sname}-doc
Documentation for python-rsdclient
%endif

%prep
%autosetup -n %{name}-%{upstream_version} -S git

%build
%{py3_build}

%if 0%{?with_doc}
# generate html docs
%{__python3} setup.py build_sphinx
# remove the sphinx-build-3 leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}
%endif

%install
%{py3_install}

# Setup directories
install -d -m 755 %{buildroot}%{_datadir}/%{pyname}
install -d -m 755 %{buildroot}%{_sharedstatedir}/%{pyname}
install -d -m 755 %{buildroot}%{_localstatedir}/log/%{pyname}

%files -n python3-%{sname}
%license LICENSE
%doc README.rst doc/source/readme.rst
%{python3_sitelib}/%{sname}
%{python3_sitelib}/%{pyname}-*.egg-info
%exclude %{python3_sitelib}/%{sname}/tests

%files -n python3-%{sname}-tests
%license LICENSE
%{python3_sitelib}/%{sname}/tests

%if 0%{?with_doc}
%files -n python-%{sname}-doc
%license LICENSE
%doc doc/build/html README.rst
%endif

%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 04 2020 Joel Capitao <jcapitao@redhat.com> 1.0.2-1
- Update to upstream version 1.0.2

* Tue May 26 2020 Miro Hron??ok <mhroncok@redhat.com> - 1.0.0-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 06 2019 Alfredo Moralejo <amoralej@redhat.com> 1.0.0-1
- Update to upstream version 1.0.0

* Thu Oct 03 2019 Miro Hron??ok <mhroncok@redhat.com> - 0.2.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hron??ok <mhroncok@redhat.com> - 0.2.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Apr 05 2019 RDO <dev@lists.rdoproject.org> 0.2.0-1
- Update to 0.2.0
