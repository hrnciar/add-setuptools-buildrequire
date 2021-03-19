# Generated by go2rpm
# Needs fuse.ko loaded
%bcond_with check

# https://github.com/bazil/fuse
%global goipath         bazil.org/fuse
%global forgeurl        https://github.com/bazil/fuse
%global commit          fb710f7dfd05053a3bc9516dd5a7a8f84ead8aab

%gometa

%global common_description %{expand:
bazil.org/fuse is a Go library for writing FUSE userspace filesystems.

It is a from-scratch implementation of the kernel-userspace communication
protocol, and does not use the C library from the project called FUSE.
bazil.org/fuse embraces Go fully for safety and ease of programming.}

%global golicenses      LICENSE
%global godocs          doc examples README.md

Name:           %{goname}
Version:        0
Release:        0.16%{?dist}
Summary:        Fuse library for Go
License:        BSD and MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/tv42/httpunix)
BuildRequires:  golang(golang.org/x/sys/unix)

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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 22 17:08:55 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.14.20200722gitfb710f7
- Bump to commit fb710f7dfd05053a3bc9516dd5a7a8f84ead8aab

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Dec 27 16:49:49 CET 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.12.20191227git3a99aca
- Bump to commit 3a99aca11732d514d92d69035a3751d07833b4a2

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May 01 16:33:34 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.10.20180628git65cc252
- Update to new macros

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9.git65cc252
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Nov 11 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.8.20180628git65cc252
- SPEC refresh

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 0-0.7.20180628git65cc252
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6.git65cc252
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.5.20180628git65cc252
- Bump to commit 65cc252bf6691cb3c7014bcb2c8dc29de91e3a7e

* Wed Mar 14 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.4.20180313git371fbbd
- Fix BuildRequires

* Wed Mar 07 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.3.20180313git371fbbd
- Update with the new Go packaging
- Add doc and examples
- Make devel package arched

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.20160811git371fbbd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jul 24 2017 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20160811git371fbbd
- First package for Fedora