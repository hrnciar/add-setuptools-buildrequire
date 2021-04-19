# Generated by go2rpm 1
%bcond_without check

# https://github.com/graph-gophers/graphql-go
%global goipath         github.com/graph-gophers/graphql-go
%global commit          beb923fada293249384c7a9fa0c5078ea92466f3

%gometa

%global common_description %{expand:
GraphQL server with a focus on ease of use.}

%global golicenses      LICENSE
%global godocs          docs example CONTRIBUTING.md README.md

Name:           %{goname}
Version:        0
Release:        0.5%{?dist}
Summary:        GraphQL server with a focus on ease of use

# Upstream license specification: BSD-3-Clause and BSD-2-Clause
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/opentracing/opentracing-go)
BuildRequires:  golang(github.com/opentracing/opentracing-go/ext)
BuildRequires:  golang(github.com/opentracing/opentracing-go/log)

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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Jan 09 20:25:55 CET 2021 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.4.20210109gitbeb923f
- Buçp to commit beb923fada293249384c7a9fa0c5078ea92466f3

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 17:39:44 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.2.20200727gitc1d9693
- Bump to commit c1d9693c95a652356f724716e4a1bc97f1100c15

* Wed May 20 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0-0.1.20200520gitdae41bd
- Initial package for Fedora