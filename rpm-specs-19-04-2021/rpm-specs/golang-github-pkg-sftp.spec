# Generated by go2rpm
%bcond_without check

# https://github.com/pkg/sftp
%global goipath         github.com/pkg/sftp
Version:                1.13.0

%gometa

%global common_description %{expand:
The sftp package provides support for file system operations on remote ssh
servers using the SFTP subsystem. It also implements an SFTP server for serving
files from the filesystem.}

%global golicenses      LICENSE
%global godocs          examples CONTRIBUTORS README.md request-readme.md

%global gosupfiles glide.lock glide.yaml

Name:           %{goname}
Release:        1%{?dist}
Summary:        SFTP support for the  Go crypto/ssh package

# Upstream license specification: BSD-2-Clause
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}
Source1:        glide.yaml
Source2:        glide.lock

BuildRequires:  golang(github.com/kr/fs)
BuildRequires:  golang(github.com/pkg/errors)
BuildRequires:  golang(golang.org/x/crypto/ssh)
BuildRequires:  golang(golang.org/x/crypto/ssh/agent)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/stretchr/testify/assert)
BuildRequires:  golang(github.com/stretchr/testify/require)
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
%gocheck
%endif

%gopkgfiles

%changelog
* Wed Apr  7 23:08:35 CEST 2021 Robert-André Mauchin <zebob.m@gmail.com> - 1.13.0-1
- Update to 1.13.0
- Close: rhbz#1936169

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 24 22:44:45 CET 2021 Robert-André Mauchin <zebob.m@gmail.com> - 1.12.0-2
- Add patch to fix FTBFS with Go 1.16

* Tue Jan  5 18:12:17 CET 2021 Robert-André Mauchin <zebob.m@gmail.com> - 1.12.0-1
- Update to 1.12.0
- Close: rhbz#1872837

* Thu Jul 30 22:11:24 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.11.0-1
- Update to 1.11.0

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Apr 26 14:09:59 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.10.0-2
- Update to new macros

* Sat Mar 02 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.10.0-1
- Update to release 1.10.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Oct 25 2018 Robert-André Mauchin <zebob.m@gmail.com> - 1.8.3-1
- Update to release 1.8.3

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 1.8.0-3
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Steve Miller (copart) <code@rellims.com> - 1.8.0-1
- Bump to upstream v1.8.0

* Thu Jun 21 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.7.git4d0e916
- Upload glide files

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6.git4d0e916
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5.git4d0e916
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4.git4d0e916
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.git4d0e916
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 03 2017 Jan Chaloupka <jchaloup@redhat.com> - 0-0.2.git4d0e916
- Bump to upstream 4d0e916071f68db74f8a73926335f809396d6b42
  resolves: #1412748

* Thu Oct 20 2016 jchaloup <jchaloup@redhat.com> - 0-0.1.git8197a2e
- First package for Fedora
  resolves: #1387131
