# Generated by go2rpm 1.3
%bcond_without check

# https://github.com/siddontang/go-snappy
%global goipath         github.com/siddontang/go-snappy
%global commit          d8f7bb82a96d89c1254e5a6c967134e1433c9ee2

%gometa

%global common_description %{expand:
Snappy library for Go.}

%global golicenses      LICENSE
%global godocs          AUTHORS CONTRIBUTORS README

Name:           %{goname}
Version:        0
Release:        0.2%{?dist}
Summary:        Snappy library for Go

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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 10 12:50:24 CET 2021 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20210110gitd8f7bb8
- Initial package