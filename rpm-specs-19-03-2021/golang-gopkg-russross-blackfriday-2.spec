# Generated by go2rpm
%bcond_without check

# https://github.com/russross/blackfriday
%global goipath         gopkg.in/russross/blackfriday.v2
%global forgeurl        https://github.com/russross/blackfriday
Version:                2.1.0

%gometa

%global goaltipaths     github.com/russross/blackfriday/v2

%global common_description %{expand:
Blackfriday is a Markdown processor implemented in Go. It is paranoid about its
input (so you can safely feed it user-supplied data), it is fast, it supports
common extensions (tables, smart punctuation substitutions, etc.), and it is
safe for all utf-8 (unicode) input.

HTML output is currently supported, along with Smartypants extensions.}

%global golicenses      LICENSE.txt
%global godocs          README.md

%global gosupfiles glide.lock glide.yaml

Name:           %{goname}
Release:        2%{?dist}
Summary:        Markdown processor for Go

# Upstream license specification: BSD-2-Clause
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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Dec 23 17:55:50 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 2.1.0-1
- Update to 2.1.0
- Close: rhbz#1892192

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 05 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.0.1-5
- Add Obsoletes for old names

* Thu Apr 25 17:55:52 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 2.0.1-4
- Update to new macros

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Oct 25 2018 Robert-André Mauchin <zebob.m@gmail.com> - 2.0.1-2
- Install both v1 and v2 version

* Thu Oct 25 2018 Robert-André Mauchin <zebob.m@gmail.com> - 2.0.1-1
- Update to release 2.0.1
