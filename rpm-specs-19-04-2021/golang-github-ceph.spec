# Generated by go2rpm
%bcond_without check

# https://github.com/ceph/go-ceph
%global goipath         github.com/ceph/go-ceph
Version:                0.7.0

%gometa

%global goaltipaths     github.com/noahdesu/go-ceph

%global godevelheader %{expand:
Requires:       librados-devel
Requires:       librbd-devel
Requires:       libcephfs-devel}

%global common_description %{expand:
Set of wrappers around Ceph APIs.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        2%{?dist}
Summary:        Go bindings for Ceph

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  librados-devel
BuildRequires:  librbd-devel
BuildRequires:  libcephfs-devel

# 32 bits is not supported by Ceph
ExcludeArch:    i686 armv7hl

BuildRequires:  golang(golang.org/x/sys/unix)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/gofrs/uuid)
BuildRequires:  golang(github.com/stretchr/testify/assert)
BuildRequires:  golang(github.com/stretchr/testify/require)
BuildRequires:  golang(github.com/stretchr/testify/suite)
%endif
%description
%{common_description}

%gopkg

%prep
%goprep

%install
%gopkginstall

%if %{with check}
%check
%gocheck -d cephfs -d rados -d rbd -d cephfs/admin
%endif

%gopkgfiles

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 14 17:30:33 CET 2021 Robert-André Mauchin <zebob.m@gmail.com> - 0.7.0-1
- Update to 0.7.0

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 24 20:59:30 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.4.0-1
- Update to 0.4.0

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 09 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0-0.12.20190703gite32f9f0
- Add Obsoletes for old names

* Fri May 24 13:10:52 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.11.20190703gite32f9f0
- Bump to commit e32f9f0f2e941422937c0a6c4f0a61b8f0c82995

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-0.10.gitb15639c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-0.9.gitb15639c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-0.8.gitb15639c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-0.7.gitb15639c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-0.6.gitb15639c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-0.5.gitb15639c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-0.4.gitb15639c
- https://fedoraproject.org/wiki/Changes/golang1.7

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-0.3.gitb15639c
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-0.2.gitb15639c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Sep 14 2015 jchaloup <jchaloup@redhat.com> - 0-0.1.gitb15639c
- First package for Fedora
  resolves: #1262711
