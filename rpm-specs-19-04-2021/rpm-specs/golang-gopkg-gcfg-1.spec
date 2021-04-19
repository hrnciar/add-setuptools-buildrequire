# Generated by go2rpm
%bcond_without check

# https://github.com/go-gcfg/gcfg
%global goipath         gopkg.in/gcfg.v1
%global forgeurl        https://github.com/go-gcfg/gcfg
Version:                1.2.3

%gometa

# Remove in F33:
%global godevelheader %{expand:
Obsoletes:      golang-googlecode-gcfg-devel < 0-0.17
Obsoletes:      golang-gopkg-gcfg-devel < 0-0.17
Obsoletes:      golang-googlecode-gcfg-unit-test < 0-0.17
}

%global common_description %{expand:
Read ini-style configuration files into go structs; supports user-defined types
and subsections.}

%global golicenses      LICENSE
%global godocs          README

Name:           %{goname}
Release:        6%{?dist}
Summary:        Read ini-style configuration files into go structs

# Upstream license specification: BSD-3-Clause
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(gopkg.in/warnings.v0)

%description
%{common_description}

%gopkg

%prep
%goprep

%install
%gopkginstall

%if %{with check}
%check
# types: https://github.com/go-gcfg/gcfg/issues/17
%gocheck -d types
%endif

%gopkgfiles

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 05 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.2.3-2
- Add Obsoletes for old names

* Tue Apr 23 08:11:49 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.2.3-1
- Release 1.2.3

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.16.git5866678
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.15.git5866678
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.14.git5866678
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.13.git5866678
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.12.git5866678
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.11.git5866678
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.10.git5866678
- https://fedoraproject.org/wiki/Changes/golang1.7

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.9.git5866678
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8.git5866678
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Aug 20 2015 jchaloup <jchaloup@redhat.com> - 0-0.7.git5866678
- Choose the corret devel subpackage
  related: #1250517

* Wed Aug 19 2015 jchaloup <jchaloup@redhat.com> - 0-0.6.git5866678
- Update spec file to spec-2.0
  resolves: #1250517

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.5.gitc2d3050
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jan 22 2015 jchaloup <jchaloup@redhat.com> - 0-0.4.gitc2d3050
- Choose the correct architecture
- Add missing tests
  related: #1141880

* Tue Oct 07 2014 jchaloup <jchaloup@redhat.com> - 0-0.3.gitc2d3050
- updating summary of devel subpackage

* Fri Sep 12 2014 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0-0.2gitc2d3050
- don't own dirs owned by golang
- preserve timestamps
- noarch

* Fri Sep 12 2014 Eric Paris <eparis@redhat.com - 0.0.0-0.1.gitc2d30500
- Bump to upstream c2d3050044d05357eaf6c3547249ba57c5e235cb
