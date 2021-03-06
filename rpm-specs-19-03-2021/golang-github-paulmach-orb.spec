# Generated by go2rpm 1
%ifarch x86_64
%bcond_without check
%endif

# https://github.com/paulmach/orb
%global goipath         github.com/paulmach/orb
Version:                0.2.1

%gometa

%global common_description %{expand:
Types and utilities for working with 2d geometry in Golang.}

%global golicenses      LICENSE.md
%global godocs          README.md

Name:           %{goname}
Release:        2%{?dist}
Summary:        Types and utilities for working with 2d geometry in Golang

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/gogo/protobuf/proto)
BuildRequires:  golang(github.com/paulmach/protoscan)

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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan 19 15:37:01 CET 2021 Robert-André Mauchin <zebob.m@gmail.com> - 0.2.1-1
- Update to 0.2.1

* Mon Aug 17 10:07:01 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.1.6-1
- Initial package
