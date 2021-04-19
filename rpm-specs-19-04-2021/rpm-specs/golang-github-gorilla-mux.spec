# Generated by go2rpm
%bcond_without check

# https://github.com/gorilla/mux
%global goipath         github.com/gorilla/mux
Version:                1.8.0

%gometa

%global common_description %{expand:
Package gorilla/mux implements a request router and dispatcher for matching
incoming requests to their respective handler.

The name mux stands for "HTTP request multiplexer". Like the standard
http.ServeMux, mux.Router matches incoming requests against a list of registered
routes and calls a handler for the route that matches the URL or other
conditions. The main features are:

 - It implements the http.Handler interface so it is compatible with the
   standard http.ServeMux.
 - Requests can be matched based on URL host, path, path prefix, schemes,
   header and query values, HTTP methods or using custom matchers.
 - URL hosts, paths and query values can have variables with an optional
   regular expression.
 - Registered URLs can be built, or "reversed", which helps maintaining
   references to resources.
 - Routes can be used as subrouters: nested routes are only tested if the
   parent route matches. This is useful to define groups of routes that share
   common conditions like a host, a path prefix or other repeated attributes.
   As a bonus, this optimizes request matching.
}

%global golicenses      LICENSE
%global godocs          AUTHORS README.md

%global gosupfiles glide.lock glide.yaml

Name:           %{goname}
Release:        2%{?dist}
Summary:        A powerful url router and dispatcher for golang

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
cp %{S:1} %{S:2} .

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan  3 09:24:42 CET 2021 Robert-André Mauchin <zebob.m@gmail.com> - 1.8.0-1
- Update to 1.8.0
- Close: rhbz#1871415

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Feb 16 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.7.4-1
- Update to latest version

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Apr 15 23:21:17 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.7.1-1
- Release 1.7.1

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 30 2018 Robert-André Mauchin <zebob.m@gmail.com> - 1.6.2-1
- Release 1.6.2

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 1.6.1-5.git53c1911
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-4.git53c1911
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 11 2018 Jan Chaloupka <jchaloup@redhat.com> - 1.6.1-3.git53c1911
- Upload glide files

* Tue Feb 20 2018 Jan Chaloupka <jchaloup@redhat.com> - 1.6.1-2
- Autogenerate some parts using the new macros

* Wed Feb 14 2018 Kaushal <kshlmster@gmail.com> - 1.6.1-1
- Update to v1.6.1

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.27.gitbcd8bc7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Sep 26 2017 Jan Chaloupka <jchaloup@redhat.com> - 0-0.26.gitbcd8bc7
- Bump to upstream bcd8bc72b08df0f70df986b97f95590779502d31
  related: #1249384

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.25.git8096f47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.24.git8096f47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.23.git8096f47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.22.git8096f47
- https://fedoraproject.org/wiki/Changes/golang1.7

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.21.git8096f47
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.20.git8096f47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Sep 12 2015 jchaloup <jchaloup@redhat.com> - 0-0.19.git8096f47
- Update to spec-2.1
  related: #1249384

* Sun Aug 02 2015 jchaloup <jchaloup@redhat.com> - 0-0.18.git8096f47
- Update spec file to spec-2.0
  resolves: #1249384

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.17.git8096f47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Apr 21 2015 jchaloup <jchaloup@redhat.com> - 0-0.16.git8096f47
- Bump to upstream 8096f47503459bcc74d1f4c487b7e6e42e5746b5
  related: #1001317

* Thu Jul 31 2014 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0-0.15.git
- do not own dirs owned by golang
- archfulness and defattr for el6 handled separately

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.14.git136d54f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat May 31 2014 Lokesh Mandvekar <lsm5@redhat.com> 0-0.13.git
- update to commit 136d54f81f (required for docker 1.0
https://github.com/dotcloud/docker/issues/5908 )

* Fri Jan 17 2014 Lokesh Mandvekar <lsm5@redhat.com> 0-0.12.gite718e93
- exclusivearch for el6+
- add check

* Fri Jan 17 2014 Lokesh Mandvekar <lsm5@redhat.com> 0-0.11.gite718e93
- revert golang >= 1.2 version requirement

* Wed Jan 15 2014 Lokesh Mandvekar <lsm5@redhat.com> 0-0.10.gite718e93
- require golang 1.2 and later

* Wed Oct 16 2013 Lokesh Mandvekar <lsm5@redhat.com> 0-0.9.gite718e93
- double quotes removed from provides and br

* Tue Oct 08 2013 Lokesh Mandvekar <lsm5@redhat.com> 0-0.8.gite718e93
- noarch for f19+ and rhel7+, exclusivearch otherwise

* Mon Oct 07 2013 Lokesh Mandvekar <lsm5@redhat.com> 0-0.7.gite718e93
- exclusivearch as per golang package
- debug_package nil

* Sun Sep 22 2013 Matthew Miller <mattdm@fedoraproject.org> 0-0.6.gite718e93
- install just the source code for devel package

* Tue Sep 17 2013 Lokesh Mandvekar <lsm5@redhat.com> 0-0.5.gite718e93
- Version format changed
- docdir changed
- debuginfo no longer generated
- package owns all directories in goipath

* Mon Sep 16 2013 Lokesh Mandvekar <lsm5@redhat.com> gite718e93-4
- only devel package generated
- Provides moved to devel package

* Tue Sep 10 2013 Lokesh Mandvekar <lsm5@redhat.com> gite718e93-3
- Depends on golang("github.com/gorilla/context"), not golang directly
- Pkg archives handled (thanks to Vincent Batts (vbatts@redhat.com)
- Devel package generated

* Wed Aug 28 2013 Lokesh Mandvekar <lsm5@redhat.com> 0.0.1-2
- Fixed permissions

* Mon Aug 26 2013 Lokesh Mandvekar <lsm5@redhat.com> 0.0.1-1
- Initial fedora package