# Generated by go2rpm 1.3
%bcond_without check

# https://github.com/nrdcg/desec
%global goipath         github.com/nrdcg/desec
Version:                0.5.0

%gometa

%global common_description %{expand:
Go library for accessing the deSEC API.}

%global golicenses      LICENSE
%global godocs          readme.md

Name:           %{goname}
Release:        2%{?dist}
Summary:        Go library for accessing the deSEC API

# Upstream license specification: MPL-2.0
License:        MPLv2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(golang.org/x/time/rate)

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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec 07 04:29:12 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.5.0-1
- Initial package
