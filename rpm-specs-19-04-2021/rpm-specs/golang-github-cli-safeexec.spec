# Generated by go2rpm 1.3
%bcond_without check

# https://github.com/cli/safeexec
%global goipath         github.com/cli/safeexec
Version:                1.0.0

%gometa

%global common_description %{expand:
A Go module that provides a safer alternative to exec.LookPath() on Windows.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        2%{?dist}
Summary:        A safer version of exec.LookPath on Windows

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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 17 22:24:12 CET 2021 Robert-André Mauchin <zebob.m@gmail.com> - 1.0.0-1
- Initial package