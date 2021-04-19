# Generated by go2rpm
%bcond_without check

# https://github.com/getkin/kin-openapi
%global goipath         github.com/getkin/kin-openapi
Version:                0.35.0

%gometa

%global common_description %{expand:
A Go project for handling OpenAPI files. We target the latest OpenAPI version
(currently 3), but the project contains support for older OpenAPI versions too.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        2%{?dist}
Summary:        OpenAPI 3.0 implementation for Go

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/ghodss/yaml)
BuildRequires:  golang(github.com/go-openapi/jsonpointer)

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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.35.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan  5 21:51:14 CET 2021 Robert-André Mauchin <zebob.m@gmail.com> - 0.35.0-1
- Update to 0.35.0
- Close: rhbz#1913010

* Sat Jan  2 19:05:17 CET 2021 Robert-André Mauchin <zebob.m@gmail.com> - 0.34.0-1
- Update to 0.34.0
- Close: rhbz#1910404

* Fri Dec 18 12:34:43 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.33.0-1
- Update to 0.33.0
- Close: rhbz#1868452

* Sun Aug 23 15:47:18 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.20.0-1
- Update to 0.20.0

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.19.0-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.19.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 21 23:29:03 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.19.0-1
- Update to 0.19.0 (#1814487)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 14 18:53:34 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.2.0-1
- Initial package
