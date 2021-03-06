# Generated by go2rpm
%bcond_without check

# https://github.com/gorilla/context
%global goipath         github.com/gorilla/context
Version:                1.1.1

%gometa

%global common_description %{expand:
Package gorilla/context stores values shared during a request lifetime.

For example, a router can set variables extracted from the URL and later
application handlers can access those values, or it can be used to store
sessions values to be saved at the end of a request. There are several
other common uses.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        8%{?dist}
Summary:        Golang registry for global request variables

# Upstream license specification: BSD-3-Clause
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}
Source1:        glide.yaml
Source2:        glide.lock

%description
%{common_description}

%gopkg

%prep
%goprep

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-7
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Apr 15 23:36:30 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.1.1-3
- Update to new macros

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 30 2018 Robert-André Mauchin <zebob.m@gmail.com> - 1.1.1-1
- Release 1.1.1

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 1.1-5.git1ea2538
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-4.git1ea2538
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 11 2018 Jan Chaloupka <jchaloup@redhat.com> - 1.1-3.git1ea2538
- Upload glide files

* Tue Feb 20 2018 Jan Chaloupka <jchaloup@redhat.com> - 1.1-2
- Autogenerate some parts using the new macros

* Wed Feb 14 2018 Kaushal <kshlmster@gmail.com> - 1.1-1
- Update to v1.1

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.38.git215affd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.37.git215affd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.36.git215affd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.35.git215affd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.34.git215affd
- https://fedoraproject.org/wiki/Changes/golang1.7

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.33.git215affd
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.32.git215affd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Sep 12 2015 jchaloup <jchaloup@redhat.com> - 0-0.31.git215affd
- Update to spec-2.1
  related: #1214614

* Sat Aug 01 2015 jchaloup <jchaloup@redhat.com> - 0-0.30.git215affd
- Update spec file to spec-2.0
  related: #1214614

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.29.git215affd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Apr 23 2015 jchaloup <jchaloup@redhat.com> - 0-0.28.git215affd
- Bump to upstream 215affda49addc4c8ef7e2534915df2c8c35c6cd
  resolves: #1214614

* Thu Jul 31 2014 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0-0.27.git
- remove conditionals for arch specification (handle el6 separately)
- defattr only for el6

* Thu Jul 24 2014 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0-0.26.git
- disable debuginfo

* Mon Jul 21 2014 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0-0.25.git
- update to commit 14f550f51a for docker 1.1.0 (and 1.1.1)
- use golang packaging macros wherever applicable
- do not own directories owned by 'golang' package

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.24.gitb06ed15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat May 31 2014 Lokesh Mandvekar <lsm5@redhat.com> 0-0.23.git
- update to commit b06ed15e1c (required for docker 1.0
https://github.com/dotcloud/docker/issues/5908 )

* Wed Jan 15 2014 Lokesh Mandvekar <lsm5@redhat.com> 0-0.22.git708054d
- golang exclusivearch for el6+
- add check

* Wed Jan 15 2014 Lokesh Mandvekar <lsm5@redhat.com> 0-0.21.git708054d
- revert golang 1.2 requirement

* Wed Jan 15 2014 Lokesh Mandvekar <lsm5@redhat.com> 0-0.20.git708054d
- require golang 1.2 and up

* Wed Oct 16 2013 Lokesh Mandvekar <lsm5@redhat.com> 0-0.19.git708054d
- double quotes removed from provides

* Tue Oct 08 2013 Lokesh Mandvekar <lsm5@redhat.com> 0-0.18.git708054d
- noarch for f19+ and rhel7+, exclusivearch otherwise

* Mon Oct 07 2013 Lokesh Mandvekar <lsm5@redhat.com> 0-0.17.git708054d
- exclusivearch as per golang package
- debug_package nil

* Sun Oct 06 2013 Lokesh Mandvekar <lsm5@redhat.com> 0-0.16.git708054d
- excluded for ppc64

* Sun Sep 22 2013 Matthew Miller <mattdm@fedoraproject.org> 0-0.15.git708054d
- install just the source code for devel package

* Tue Sep 17 2013 Lokesh Mandvekar <lsm5@redhat.com> 0-0.14.git708054d
- docdir unversioned

* Tue Sep 17 2013 Lokesh Mandvekar <lsm5@redhat.com> 0-0.13.git708054d
- Version format changed

* Mon Sep 16 2013 Lokesh Mandvekar <lsm5@redhat.com> git708054d-12
- debuginfo not generated, was empty to begin with
- devel package buildrequires golang
- package owns all directories in goipath

* Mon Sep 16 2013 Lokesh Mandvekar <lsm5@redhat.com> git708054d-11
- Only devel package generated
- docdir corrected
- Provides moved to devel package

* Thu Sep 12 2013 Lokesh Mandvekar <lsm5@redhat.com> git708054d-10
- package owns directories it creates
- devel package requires golang

* Wed Sep 11 2013 Lokesh Mandvekar <lsm5@redhat.com> git708054d-9
- rm from install removed

* Tue Sep 10 2013 Lokesh Mandvekar <lsm5@redhat.com> git708054d-8
- cleanup in prep and build as per guidelines

* Tue Sep 10 2013 Lokesh Mandvekar <lsm5@redhat.com> git708054d-7
- rpm builds under all circumstances

* Mon Sep 09 2013 Lokesh Mandvekar <lsm5@redhat.com> git708054d-6
- Devel package summary corrected

* Mon Sep 09 2013 Lokesh Mandvekar <lsm5@redhat.com> git708054d-5
- Installed files listed explicitly
- Pkg archive directory issues solved (thanks to Vincent Batts)
- Pkg archive files installed in devel package

* Thu Aug 29 2013 Lokesh Mandvekar <lsm5@redhat.com> git708054d-4
- variables introduced: pkgarch, GOPATH and so on- arch specific .a archives installed
- credit to Vincent Batts (vbatts@redhat.com) for golang-* help

* Thu Aug 29 2013 Lokesh Mandvekar <lsm5@redhat.com> 0.0.1-3
- global debug lines removed
- package name changed
- source file installation location updated

* Wed Aug 28 2013 Lokesh Mandvekar <lsm5@redhat.com> 0.0.1-2
- Fixed permissions

* Mon Aug 26 2013 Lokesh Mandvekar <lsm5@redhat.com> 0.0.1-1
- Initial fedora package

