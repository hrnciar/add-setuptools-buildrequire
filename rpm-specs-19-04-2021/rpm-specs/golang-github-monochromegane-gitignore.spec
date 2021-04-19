# Generated by go2rpm 1
%bcond_without check

# https://github.com/monochromegane/go-gitignore
%global goipath         github.com/monochromegane/go-gitignore
%global commit          205db1a8cc001de79230472da52edde4974df734

%gometa

%global common_description %{expand:
A fast gitignore matching library for Go.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.2%{?dist}
Summary:        A fast gitignore matching library for Go

License:        MIT
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

* Sat Sep 19 20:05:29 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20200921git205db1a
- Initial package