# Generated by go2rpm 1.3
%bcond_without check

# https://github.com/richardlehane/mscfb
%global goipath         github.com/richardlehane/mscfb
Version:                1.0.3

%gometa

%global common_description %{expand:
Golang reader for the Microsoft Compound File Binary File format.}

%global golicenses      LICENSE.txt
%global godocs          README.md

Name:           %{goname}
Release:        2%{?dist}
Summary:        Golang reader for the Microsoft Compound File Binary File format

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/richardlehane/msoleps/types)

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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 14 10:16:28 CET 2021 Robert-André Mauchin <zebob.m@gmail.com> - 1.0.3-1
- Initial package
