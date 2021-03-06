%global srcname resalloc-openstack
%global pkgname resalloc_openstack

%if 0%{?fedora} || 0%{?rhel} > 7
%bcond_with python2
%global default_sitelib %python3_sitelib
%global python python3
%global pythonpfx python3
%else
%bcond_without python2
%global default_sitelib %python2_sitelib
%global python python2
%global pythonpfx python
%endif

Name:       %srcname
Summary:    Resource allocator scripts for OpenStack
Version:    7
Release:    8%{?dist}
License:    GPLv2+
URL:        https://github.com/praiskup/resalloc-openstack
BuildArch:  noarch


BuildRequires: %pythonpfx-devel
BuildRequires: %pythonpfx-setuptools

Requires: %pythonpfx-cinderclient
Requires: %pythonpfx-glanceclient
Requires: %pythonpfx-keystoneauth1
Requires: %pythonpfx-neutronclient
Requires: %pythonpfx-novaclient

Source0: https://github.com/praiskup/%name/releases/download/v%version/%name-%version.tar.gz

%description
Resource allocator spawner/terminator scripts for OpenStack virtual machines,
designed so they either allocate all the sub-resources, or nothing (in case of
some failure).  This is especially useful if working with older OpenStack
deployments which all the time keep orphaned servers, floating IPs, volumes,
etc. dangling around.

These scripts are primarily designed to be used with resalloc-server.rpm, but in
general might be used separately.


%prep
%setup -q


%build
%if %{with python2}
%py2_build
%else
%py3_build
%endif


%install
%if %{with python2}
%py2_install
%else
%py3_install
%endif


%check


%files
%license COPYING
%doc README
%{_bindir}/%{name}-*
%_mandir/man1/%{name}-*.1*
%{default_sitelib}/%{pkgname}
%{default_sitelib}/%{pkgname}-*.egg-info


%changelog
* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 7-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 7-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 7-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 17 2019 Pavel Raiskup <praiskup@redhat.com> - 7-1
- more aggressive volume detach/removal

* Tue Jun 25 2019 Pavel Raiskup <praiskup@redhat.com> - 6-1
- don't indefinitely wait for booting of ERRORed instances

* Thu Jun 13 2019 Pavel Raiskup <praiskup@redhat.com> - 5-2
- start using the released tarball
- more descriptive %%description

* Wed Jun 12 2019 Pavel Raiskup <praiskup@redhat.com> - 5-1
- compat for older novaclient

* Fri Apr 19 2019 Pavel Raiskup <praiskup@redhat.com> - 4-1
- work-around broken fedorainfracloud:
  https://pagure.io/fedora-infrastructure/issue/7711

* Thu Apr 18 2019 Pavel Raiskup <praiskup@redhat.com> - 3-2
- add missing Requires

* Thu Apr 18 2019 Pavel Raiskup <praiskup@redhat.com> - 3-1
- more solid VM termination
- dump verbosely what is going on

* Sat Mar 23 2019 Pavel Raiskup <praiskup@redhat.com> - 2-1
- support v3 connection API

* Wed Oct 31 2018 Pavel Raiskup <praiskup@redhat.com> - 1-1
- rebuild for Python 3.7

* Tue Jan 30 2018 Pavel Raiskup <praiskup@redhat.com> - 1.dev0-0
- first tagged release

* Wed Jan 10 2018 Pavel Raiskup <praiskup@redhat.com> - 0.dev0-4
- add 'resalloc-openstack --nic' option
- 'resalloc-openstack-new --image' accepts image name, too

* Fri Oct 13 2017 Pavel Raiskup <praiskup@redhat.com> - 0.dev0-3
- fix the volume attaching

* Thu Oct 05 2017 Pavel Raiskup <praiskup@redhat.com> - 0.dev0-2
- new: add --key-pair-id option

* Thu Oct 05 2017 Pavel Raiskup <praiskup@redhat.com> - 0.dev0-1
- add handler explicitly for python2

* Wed Oct 04 2017 Pavel Raiskup <praiskup@redhat.com> - 0.dev0-0
- initial build
