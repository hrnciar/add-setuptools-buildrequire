# Generated by go2rpm 1
%bcond_without check

# https://github.com/crewjam/saml
%global goipath         github.com/crewjam/saml
Version:                0.4.5

%gometa

%global common_description %{expand:
SAML library for go.}

%global golicenses      LICENSE
%global godocs          example README.md

Name:           %{goname}
Release:        2%{?dist}
Summary:        SAML library for go

# Upstream license specification: BSD-2-Clause
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/beevik/etree)
BuildRequires:  golang(github.com/crewjam/httperr)
BuildRequires:  golang(github.com/dchest/uniuri)
BuildRequires:  golang(github.com/dgrijalva/jwt-go)
BuildRequires:  golang(github.com/kr/pretty)
BuildRequires:  golang(github.com/mattermost/xml-roundtrip-validator)
BuildRequires:  golang(github.com/russellhaering/goxmldsig)
BuildRequires:  golang(github.com/russellhaering/goxmldsig/etreeutils)
BuildRequires:  golang(github.com/zenazn/goji)
BuildRequires:  golang(github.com/zenazn/goji/web)
BuildRequires:  golang(golang.org/x/crypto/bcrypt)
BuildRequires:  golang(golang.org/x/crypto/ripemd160)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/stretchr/testify/assert)
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
%gocheck
%endif

%gopkgfiles

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan  1 22:16:50 CET 2021 Robert-André Mauchin <zebob.m@gmail.com> - 0.4.5-1
- Update to 0.4.5
- Close: rhbz#1868647

* Sun Aug 23 01:15:03 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.4.1-1
- Update to 0.4.1

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Feb 18 11:19:56 CET 2020 Andreas Gerstmayr <agerstmayr@redhat.com> - 0.4.0-1
- Initial package
