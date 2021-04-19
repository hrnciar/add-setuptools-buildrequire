# Generated by go2rpm 1
%bcond_without check
# Checks need internet access to download test files
%bcond_with network

# https://github.com/dennwc/graphql
%global goipath         github.com/dennwc/graphql
Version:                0.4.18
%global commit          12cfed44bc5de083875506a36d30f9798f9bca47

%gometa

%global common_description %{expand:
An implementation of GraphQL for Go/Golang.}

%global golicenses      LICENSE
%global godocs          examples CONTRIBUTING.md README.md

Name:           %{goname}
Release:        3%{?dist}
Summary:        Implementation of GraphQL

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

%if %{with check} && %{with network}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Apr 08 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.4.18-1.20200408git12cfed4
- Initial package

