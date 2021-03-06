# Generated by go2rpm 1
%bcond_without check

# https://github.com/uber-go/dig
%global goipath         go.uber.org/dig
%global forgeurl        https://github.com/uber-go/dig
Version:                1.10.0

%gometa

%global common_description %{expand:
A reflection based dependency injection toolkit for Go.}

%global golicenses      LICENSE
%global godocs          README.md CHANGELOG.md

Name:           %{goname}
Release:        3%{?dist}
Summary:        A reflection based dependency injection toolkit for Go

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

%if %{with check}
# Tests
BuildRequires:  golang(github.com/stretchr/testify/assert)
BuildRequires:  golang(github.com/stretchr/testify/require)
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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 01 21:49:38 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.10.0-1
- Initial package
