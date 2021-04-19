# Generated by go2rpm 1
%bcond_without check

# https://github.com/xuri/efp
%global goipath         github.com/xuri/efp
%global commit          031c29024257bee4520d676cc27709117cdcbf34

%gometa

%global common_description %{expand:
Go Microsoft Excel Formula Parser.}

%global golicenses      LICENSE
%global godocs          CODE_OF_CONDUCT.md README.md SECURITY.md

Name:           %{goname}
Version:        0
Release:        0.3%{?dist}
Summary:        Go Microsoft Excel Formula Parser

# Upstream license specification: BSD-3-Clause
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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 13 18:26:46 CET 2021 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.2.20210113git031c290
- Bump to commit 031c29024257bee4520d676cc27709117cdcbf34

* Fri Sep 18 19:55:18 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20200918gitba68910
- Initial package