# Generated by go2rpm 1
%bcond_without check

# https://github.com/robfig/cron
%global goipath         github.com/robfig/cron
Version:                1.2.0

%gometa

%global common_description %{expand:
A cron library for go.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        2%{?dist}
Summary:        A cron library for go

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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 18 18:40:39 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.2.0-1
- Initial package