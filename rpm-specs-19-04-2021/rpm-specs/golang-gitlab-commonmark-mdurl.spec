# Generated by go2rpm
%bcond_without check

# https://gitlab.com/golang-commonmark/mdurl
%global goipath         gitlab.com/golang-commonmark/mdurl
%global forgeurl        https://gitlab.com/golang-commonmark/mdurl
%global commit          932350d1cb841423f436264e83e4f0bdbc798f67

%gometa

%global goaltipaths     github.com/golang-commonmark/mdurl

%global common_description %{expand:
Package Mdurl provides functions for parsing, decoding and encoding URLs.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.6%{?dist}
Summary:        Utilities for parsing, decoding and encoding URLs

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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Aug 05 13:32:15 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.5.20200805git932350d
- Bump to commit 932350d1cb841423f436264e83e4f0bdbc798f671

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May 15 21:35:52 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20190701gite5bce34
- Initial package