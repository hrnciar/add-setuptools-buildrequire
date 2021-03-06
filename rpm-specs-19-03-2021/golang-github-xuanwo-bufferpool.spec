# Generated by go2rpm 1.3
%bcond_without check

# https://github.com/Xuanwo/go-bufferpool
%global goipath         github.com/Xuanwo/go-bufferpool
%global commit          6225093e8ebac42ee03f845dbc38abd7c5f315d7

%gometa

%global common_description %{expand:
Bufferpool for Golang.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.2%{?dist}
Summary:        Bufferpool for Golang

License:        ASL 2.0

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

* Wed Jan 06 12:30:54 CET 2021 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20210106git6225093
- Initial package
