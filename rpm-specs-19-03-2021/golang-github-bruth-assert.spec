# Generated by go2rpm
%bcond_without check

# https://github.com/bruth/assert
%global goipath         github.com/bruth/assert
%global commit          de420fa3b72e87255136e10ade1e267581cc3947

%gometa

%global common_description %{expand:
Simple test assertions for Go. This is a fork of a fork of a bmizerany/assert
with improved support for things like nil pointers, etc.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.7%{?dist}
Summary:        Simple test assertions for Golang tests

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}
Patch0:         add-license.patch

BuildRequires:  golang(github.com/kr/pretty)

%description
%{common_description}

%gopkg

%prep
%goprep
%patch0 -p1

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon May 20 17:37:15 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.3.20180813gitde420fa
- Update to new macros

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.gitde420fa
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Aug 13 2018 Gabe <redhatrises@gmail.com> - 0-0.1.20180813gitde420fa
- First package for Fedora
