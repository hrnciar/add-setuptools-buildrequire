# Generated by go2rpm 1
%bcond_without check

# https://github.com/vmihailenco/msgpack
%global goipath         github.com/vmihailenco/msgpack
Version:                3.3.3

%gometa

%global goaltipaths    gopkg.in/vmihailenco/msgpack.v3

%global common_description %{expand:
MessagePack encoding for Golang.}

%global golicenses      LICENSE
%global godocs          CHANGELOG.md README.md

Name:           %{goname}
Release:        2%{?dist}
Summary:        MessagePack encoding for Golang

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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 11 01:08:09 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 3.3.3-1
- Initial package
