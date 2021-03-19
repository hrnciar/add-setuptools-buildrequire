# Generated by go2rpm
%bcond_without check

# https://github.com/syndtr/gocapability
%global goipath         github.com/syndtr/gocapability
%global commit          42c35b4376354fd554efc7ad35e0b7f94e3a0ffb

%gometa

%global common_description %{expand:
Utilities for manipulating POSIX capabilities in Go.}

%global golicenses      LICENSE

Name:           %{goname}
Version:        0
Release:        0.28%{?dist}
Summary:        Utilities for manipulating POSIX capabilities in Go

# Upstream license specification: BSD-2-Clause
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}

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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 13 17:08:46 CET 2021 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.27.20210113git42c35b4
- Bump to commit 42c35b4376354fd554efc7ad35e0b7f94e3a0ffb

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat May 04 17:47:45 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.23.20190504gitd983527
- Bump to commit d98352740cb2c55f81556b63d4a1ec64c5a319c2

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.22.git2c00dae
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.21.git2c00dae
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.20.git2c00dae
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Oct 04 2017 Troy Dawson <tdawson@redhat.com> - 0-0.19.git2c00dae
- Cleanup spec file conditionals

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.18.git2c00dae
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.17.git2c00dae
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.16.git2c00dae
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.15.git2c00dae
- https://fedoraproject.org/wiki/Changes/golang1.7

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.14.git2c00dae
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.13.git2c00dae
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Nov 26 2015 jchaloup <jchaloup@redhat.com> - 0-0.12.git2c00dae
- Bump to upstream 2c00daeb6c3b45114c80ac44119e7b8801fdd852
  related: #1254599

* Wed Aug 12 2015 Fridolin Pokorny <fpokorny@redhat.com> - 0-0.11.git8e4cdcb
- Update spec file to spec-2.0
  resolves: #1254599

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.10.git8e4cdcb
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Apr 21 2015 jchaloup <jchaloup@redhat.com> - 0-0.9.git8e4cdcb
- Bump to upstream 8e4cdcb3c22b40d5e330ade0b68cb2e2a3cf6f98
  related: #1032750

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.8.git3c85049
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 13 2014 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0-0.7.git
- RHBZ#1109039 update to upstream commit 3c85049eaeb429febe7788d9c7aac42322a377fe

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.6.git3454319
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Jan 17 2014 Lokesh Mandvekar <lsm5@redhat.com> 0-0.5.git3454319
- exclusivearch for el6+

* Fri Jan 17 2014 Lokesh Mandvekar <lsm5@redhat.com> 0-0.4.git3454319
- require golang as runtime dep

* Wed Nov 20 2013 Vincent Batts <vbatts@redhat.com> 0-0.3.git3454319
- typo

* Wed Nov 20 2013 Vincent Batts <vbatts@redhat.com> 0-0.2.git3454319
- clean up per code review (bz1032750)

* Wed Nov 20 2013 Vincent Batts <vbatts@redhat.com> 0-0.1.git3454319
- initial build