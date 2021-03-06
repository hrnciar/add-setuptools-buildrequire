# Generated by go2rpm 1
%bcond_without check

# https://github.com/liquidweb/liquidweb-go
%global goipath         github.com/liquidweb/liquidweb-go
Version:                1.6.1

%gometa

%global common_description %{expand:
Golang API client for Liquid Web's Storm API.}

%global golicenses      COPYRIGHT LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        4%{?dist}
Summary:        Golang API client for Liquid Web's Storm API

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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jan 26 18:04:38 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.6.1-1
- Initial package
