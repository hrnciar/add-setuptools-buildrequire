# Generated by go2rpm
# https://github.com/prometheus/procfs/issues/319
%ifarch x86_64
%bcond_without check
%endif

# https://github.com/prometheus/procfs
%global goipath         github.com/prometheus/procfs
Version:                0.3.0

%gometa

%global common_description %{expand:
Procfs provides functions to retrieve system, kernel and process metrics from
the pseudo-filesystem proc.}

%global golicenses      LICENSE NOTICE
%global godocs          CONTRIBUTING.md MAINTAINERS.md README.md

%global gosupfiles glide.lock glide.yaml

Name:           %{goname}
Release:        2%{?dist}
Summary:        Retrieve system, kernel and process metrics from proc

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}
Source1:        glide.yaml
Source2:        glide.lock

BuildRequires:  golang(golang.org/x/sync/errgroup)
BuildRequires:  golang(golang.org/x/sys/unix)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/google/go-cmp/cmp)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep
cp %{S:1} %{S:2} .

%install
%gopkginstall

%if %{with check}
%check
# Tests require that fixtures are extracted
./ttar -x -f fixtures.ttar
%gocheck
%endif

%gopkgfiles

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 21 20:39:46 CET 2021 Robert-André Mauchin <zebob.m@gmail.com> - 0.3.0-1
- Update to 0.3.0
- Close: rhbz#1915102

* Thu Jan  7 18:32:18 CET 2021 Robert-André Mauchin <zebob.m@gmail.com> - 0.2.0-1
- Update to 0.2.0
- Close: rhbz#1882130

* Fri Jul 31 22:28:56 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.1.3-1
- Update to 0.1.3

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 24 21:02:30 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.0.2-1
- Release 0.0.2

* Sun Apr 21 12:09:44 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.27.20190622git8368d24
- Bump to commit 8368d24ba045f26503eb745b624d930cbe214c79

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.26.gitfe93d37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 0-0.25.gitfe93d37
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.24.gitfe93d37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 26 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.23.gitfe93d37
- Upload glide files

* Fri May 25 2018 Paul Gier <pgier@redhat.com> - 0-0.22.20180525gita6e9df8
- Update to new snapshot a6e9df898b1336106c743392c48ee0b71f5c4efa
- Update spec file to new format

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.21.gita1dba9c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Sep 22 2017 Jan Chaloupka <jchaloup@redhat.com> - 0-0.20.gita1dba9c
- Bump to upstream a1dba9ce8baed984a2495b658c82687f8157b98f
  related: #1326057

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.19.gitfcdb11c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.18.gitfcdb11c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Mar 16 2017 Jan Chaloupka <jchaloup@redhat.com> - 0-0.17.gitfcdb11c
- Bump to upstream fcdb11ccb4389efb1b210b7ffb623ab71c5fdd60
  related: #1326057

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.16.git406e5b7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.15.git406e5b7
- https://fedoraproject.org/wiki/Changes/golang1.7

* Mon Apr 11 2016 jchaloup <jchaloup@redhat.com> - 0-0.14.git406e5b7
- Polish the spec file
  resolves: #1326057

* Mon Apr 11 2016 Than Ngo <than@redhat.com> - 0-0.13.git406e5b7
- use os.Getpagesize instead syscall.Getpagesize

* Mon Apr 11 2016 Than Ngo <than@redhat.com> 0-0.12.git406e5b7
- fix build issue on ppc64, use the syscall.Getpagesize to get correct pagesize

* Sun Apr 10 2016 Peter Robinson <pbrobinson@fedoraproject.org> 0-0.10.git406e5b7
- Bump to upstream 406e5b7bfd8201a36e2bb5f7bdae0b03380c2ce8
- Spec cleanups

* Sun Mar 06 2016 jchaloup <jchaloup@redhat.com> - 0-0.10.gitb1afdc2
- Bump to upstream b1afdc266f54247f5dc725544f5d351a8661f502
  related: #1214778

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.9.git454a56f
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8.git454a56f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Oct 19 2015 jchaloup <jchaloup@redhat.com> - 0-0.7.git454a56f
- Bump to upstream 454a56f35412459b5e684fd5ec0f9211b94f002a
  related: #1214778

* Fri Aug 07 2015 Fridolin Pokorny <fpokorny@redhat.com> - 0-0.6.gitc91d8ee
- Update spec file to spec-2.0
  resolves: #1214778

* Thu Jul 23 2015 jchaloup <jchaloup@redhat.com> - 0-0.5.gitc91d8ee
- Bump to upstream c91d8eefde16bd047416409eb56353ea84a186e4
  resolves: #1214778

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.4.git490cc6e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Apr 23 2015 jchaloup <jchaloup@redhat.com> - 0-0.3.git490cc6e
- Bump to upstream 490cc6eb5fa45bf8a8b7b73c8bc82a8160e8531d
  resolves: #1214778

* Wed Mar 04 2015 jchaloup <jchaloup@redhat.com> - 0-0.2.git6c34ef8
- Bump to upstream 6c34ef819e19b4e16f410100ace4aa006f0e3bf8
  related: #1190413

* Sat Feb 07 2015 jchaloup <jchaloup@redhat.com> - 0-0.1.git92faa30
- First package for Fedora
  resolves: #1190413
