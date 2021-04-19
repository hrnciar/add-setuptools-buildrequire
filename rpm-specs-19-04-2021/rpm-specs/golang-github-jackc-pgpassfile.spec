# Generated by go2rpm 1
%bcond_without check

# https://github.com/jackc/pgpassfile
%global goipath         github.com/jackc/pgpassfile
Version:                1.0.0

%gometa

%global common_description %{expand:
Package Pgpassfile is a parser for PostgreSQL .pgpass files.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        2%{?dist}
Summary:        Parser for PostgreSQL .pgpass files

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Jul 25 13:44:18 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.0.0-1
- Initial package
