# Generated by go2rpm
%bcond_without check

# https://github.com/pborman/uuid
%global goipath         github.com/pborman/uuid
Version:                1.2.1

%gometa

%global common_description %{expand:
The Uuid package generates and inspects UUIDs.

UUIDs are based on RFC 4122 and DCE 1.1: Authentication and Security Services.}

%global golicenses      LICENSE
%global godocs          CONTRIBUTING.md CONTRIBUTORS README.md

Name:           %{goname}
Release:        2%{?dist}
Summary:        Generate and inspect UUIDs

# Upstream license specification: BSD-3-Clause
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/google/uuid)

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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec 21 10:37:25 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.2.1-1
- Update to 1.2.1
- Close: rhbz#1869082

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 09 20:09:52 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.2.0-1
- Release 1.2.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.17.gitb984ec7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.16.gitb984ec7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.15.gitb984ec7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.14.gitb984ec7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.13.gitb984ec7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.12.gitb984ec7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 18 2017 Jan Chaloupka <jchaloup@redhat.com> - 0-0.11.gitb984ec7
- Bump to upstream b984ec7fa9ff9e428bd0cf0abf429384dfbe3e37
  related: #1250523

* Tue Aug 09 2016 jchaloup <jchaloup@redhat.com> - 0-0.10.gitca53cad
- Enable devel and unit-test for epel7
  related: #1250523

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.9.gitca53cad
- https://fedoraproject.org/wiki/Changes/golang1.7

* Thu Apr 14 2016 jchaloup <jchaloup@redhat.com> - 0-0.8.gitca53cad
- Polish spec file
- Support github.com/pborman/uuid ipprefix as well
  related: #1250523

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.7.gitca53cad
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6.gitca53cad
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Aug 20 2015 jchaloup <jchaloup@redhat.com> - 0-0.5.gitca53cad
- Update spec file to spec-2.0
  resolves: #1250523

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.4.hg7dda39b2e7d5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Feb 15 2015 jchaloup <jchaloup@redhat.com> - 0-0.3.hg7dda39b2e7d5
- Fix incorrect provides
  resolves: #1192652

* Mon Sep 15 2014 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0-0.2.hg7dda39b2e7d5
- preserve timestamps
- do not own dirs owned by golang

* Mon Aug 04 2014 Adam Miller <maxamillion@fedoraproject.org> - 0-0.1.hg7dda39b2e7d5
- First package for Fedora.
