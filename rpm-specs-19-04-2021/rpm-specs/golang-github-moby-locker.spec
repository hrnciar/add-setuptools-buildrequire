# Generated by go2rpm 1.2
%bcond_without check

# https://github.com/moby/locker
%global goipath         github.com/moby/locker
Version:                1.0.1

%gometa

%global common_description %{expand:
locker provides a mechanism for creating finer-grained locking to help free up
more global locks to handle other tasks.

This is a direct pull from https://github.com/moby/moby/tree/master/pkg/locker.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        2%{?dist}
Summary:        Go library for locking

# Upstream license specification: Apache-2.0
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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Oct 29 21:45:00 CET 2020 Olivier Lemasle <o.lemasle@gmail.com> - 1.0.1-1
- Initial package
