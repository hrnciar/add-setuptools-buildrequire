# Generated by go2rpm
%bcond_without check

# https://github.com/akamai/AkamaiOPEN-edgegrid-golang
%global goipath         github.com/akamai/AkamaiOPEN-edgegrid-golang
Version:                1.0.1

%gometa

%global common_description %{expand:
This library implements an Authentication handler for net/http that provides the
Akamai OPEN Edgegrid Authentication scheme.}

%global golicenses      LICENSE
%global godocs          examples README.md

Name:           %{goname}
Release:        2%{?dist}
Summary:        Authentication handler for the Akamai OPEN EdgeGrid Authentication scheme

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/google/go-querystring/query)
BuildRequires:  golang(github.com/google/uuid)
BuildRequires:  golang(github.com/mitchellh/go-homedir)
BuildRequires:  golang(github.com/patrickmn/go-cache)
BuildRequires:  golang(github.com/sirupsen/logrus)
BuildRequires:  golang(github.com/xeipuuv/gojsonschema)
BuildRequires:  golang(gopkg.in/ini.v1)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/stretchr/testify/assert)
BuildRequires:  golang(github.com/stretchr/testify/require)
BuildRequires:  golang(gopkg.in/h2non/gock.v1)
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
# client-v1: needs network
%gocheck -d client-v1
%endif

%gopkgfiles

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan  8 10:14:01 CET 2021 Robert-André Mauchin <zebob.m@gmail.com> - 1.0.1-1
- Update to 1.0.1
- Close: rhbz#1912377

* Tue Dec 15 03:17:20 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.0.0-1
- Update to 1.0.0
- Close: rhbz#1888844

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 23 09:24:02 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.9.18-1
- Update to 0.9.18

* Thu Apr 02 21:38:05 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.9.10-1
- Update to 0.9.10

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 02 16:37:54 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.7.4-1
- Initial package
