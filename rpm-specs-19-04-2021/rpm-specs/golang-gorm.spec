# Generated by go2rpm 1.3
%bcond_without check

# https://github.com/go-gorm/gorm
%global goipath         gorm.io/gorm
%global forgeurl        https://github.com/go-gorm/gorm
Version:                1.20.11

%gometa

%global common_description %{expand:
The fantastic ORM library for Golang, aims to be developer friendly.}

%global golicenses      License
%global godocs          README.md

Name:           %{goname}
Release:        2%{?dist}
Summary:        ORM library for Golang

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/jinzhu/inflection)
BuildRequires:  golang(github.com/jinzhu/now)

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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.20.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 14 19:28:13 CET 2021 Robert-André Mauchin <zebob.m@gmail.com> - 1.20.11-1
- Initial package
