# Generated by go2rpm 1
%bcond_without check

# https://github.com/avast/retry-go
%global goipath         github.com/avast/retry-go
Version:                3.0.0

%gometa

%global common_description %{expand:
Simple golang library for retry mechanism.}

%global golicenses      LICENSE
%global godocs          examples README.md

Name:           %{goname}
Release:        2%{?dist}
Summary:        Simple golang library for retry mechanism

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

%if %{with check}
# Tests
BuildRequires:  golang(github.com/stretchr/testify/assert)
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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 14 14:41:53 CET 2021 Robert-André Mauchin <zebob.m@gmail.com> - 3.0.0-1
- Update to 3.0.0

* Sat Sep 26 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.6.1-1
- Initial package for Fedora