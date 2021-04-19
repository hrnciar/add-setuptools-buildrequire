# Generated by go2rpm 1.3
%bcond_without check

# https://github.com/iguanesolutions/go-systemd
%global goipath         github.com/iguanesolutions/go-systemd/v5
%global forgeurl        https://github.com/iguanesolutions/go-systemd
Version:                5.0.0

%gometa

%global common_description %{expand:
Golang bindings for systemd notify (including watchdog) & socket activation.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        Golang bindings for systemd notify (including watchdog) & socket activation

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
* Sat Mar 06 08:31:20 CET 2021 Robert-André Mauchin <zebob.m@gmail.com> - 5.0.0-1
- Initial package
