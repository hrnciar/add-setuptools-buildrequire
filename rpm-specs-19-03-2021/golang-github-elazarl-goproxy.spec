# Generated by go2rpm
%bcond_without check

# https://github.com/elazarl/goproxy
%global goipath         github.com/elazarl/goproxy
Version:                1.1
%global commit          00ad82a08272b0fecb11656032e062525046fdb9

%gometa

%global common_description %{expand:
Package Goproxy provides a customizable HTTP proxy library for Go.

It supports regular HTTP proxy, HTTPS through CONNECT, and "hijacking" HTTPS
connection using "Man in the Middle" style attack.}

%global golicenses      LICENSE
%global godocs          examples README.md

Name:           %{goname}
Release:        7%{?dist}
Summary:        HTTP proxy library for Go

# Upstream license specification: BSD-3-Clause
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}

# Only in examples
# BuildRequires:  golang(github.com/ecordell/goproxy)
BuildRequires:  golang(github.com/gorilla/websocket)
BuildRequires:  golang(github.com/inconshreveable/go-vhost)
BuildRequires:  golang(github.com/rogpeppe/go-charset/charset)
BuildRequires:  golang(github.com/rogpeppe/go-charset/data)

%description
%{common_description}

%gopkg

%prep
%goprep

%install
%gopkginstall

%if %{with check}
%check
# Needs network
%gocheck -d .
%endif

%gopkgfiles

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Aug 16 18:50:21 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.1-5.20200816git0581fc3
- Bump to commit 0581fc3aee2d07555835bed1a876aca196a4a511

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 10 14:36:24 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.1-1
- Initial package
