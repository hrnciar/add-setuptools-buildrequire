# Generated by go2rpm 1
%bcond_without check

# https://github.com/labstack/echo
%global goipath         github.com/labstack/echo/v4
%global forgeurl        https://github.com/labstack/echo
Version:                4.1.17

%gometa

%global common_description %{expand:
High performance, minimalist Go web framework.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        2%{?dist}
Summary:        High performance, minimalist Go web framework

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/dgrijalva/jwt-go)
BuildRequires:  golang(github.com/labstack/gommon/bytes)
BuildRequires:  golang(github.com/labstack/gommon/color)
BuildRequires:  golang(github.com/labstack/gommon/log)
BuildRequires:  golang(github.com/labstack/gommon/random)
BuildRequires:  golang(github.com/valyala/fasttemplate)
BuildRequires:  golang(golang.org/x/crypto/acme)
BuildRequires:  golang(golang.org/x/crypto/acme/autocert)
BuildRequires:  golang(golang.org/x/net/http2)
BuildRequires:  golang(golang.org/x/net/http2/h2c)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/stretchr/testify/assert)
BuildRequires:  golang(github.com/stretchr/testify/require)
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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan  3 13:12:41 CET 2021 Robert-André Mauchin <zebob.m@gmail.com> - 4.1.17-1
- Update to 4.1.17
- Close: rhbz#1907337
- Close: rhbz#1907338

* Wed Aug 26 2020 Ondřej Budai <obudai@redhat.com> - 4.1.16-1
- Initial package