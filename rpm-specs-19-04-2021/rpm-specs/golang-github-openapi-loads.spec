# Generated by go2rpm
%bcond_without check

# https://github.com/go-openapi/loads
%global goipath         github.com/go-openapi/loads
Version:                0.20.0

%gometa

%global common_description %{expand:
Loading of OAI specification documents from local or remote locations. Supports
JSON and YAML documents.}

%global golicenses      LICENSE
%global godocs          CODE_OF_CONDUCT.md README.md

Name:           %{goname}
Release:        2%{?dist}
Summary:        Openapi specification object model

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/go-openapi/analysis)
BuildRequires:  golang(github.com/go-openapi/spec)
BuildRequires:  golang(github.com/go-openapi/swag)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/go-openapi/validate)
BuildRequires:  golang(github.com/stretchr/testify/assert)
BuildRequires:  golang(github.com/stretchr/testify/require)
BuildRequires:  golang(gopkg.in/yaml.v2)
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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec 21 08:34:27 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.20.0-1
- Update to 0.20.0
- Close: rhbz#1897939

* Thu Jul 30 16:57:48 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.19.5-1
- Update to 0.19.5

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.19.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.19.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.19.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun May 12 00:42:51 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.19.0-1
- Initial package