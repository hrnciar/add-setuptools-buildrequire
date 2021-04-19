# Generated by go2rpm 1
%bcond_without check

# https://github.com
%global goipath         gopkg.in/eapache/channels.v1 
%global forgeurl        https://github.com/eapache/channels/tree/v1.1.0
Version:                1.1.0

%gometa

%global common_description %{expand:
A collection of helper functions and special types 
for working with and extending Go's existing channels. 
Due to limitations of Go's type system, importing 
this library directly is often not practical for 
production code.}

%global golicenses      LICENSE
%global godocs          README.md CHANGELOG.md

Name:           %{goname}
Release:        2%{?dist}
Summary:        Golang channel helpers and special types

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/eapache/queue)

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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 23:47:55 CST 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 1.1.0-1
- Initial package

