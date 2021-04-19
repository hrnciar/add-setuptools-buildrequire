# Generated by go2rpm 1
%bcond_without check

# https://github.com/jarcoal/httpmock
%global goipath         github.com/jarcoal/httpmock
Version:                1.0.7

%gometa

%global common_description %{expand:
HTTP mocking for Golang.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        2%{?dist}
Summary:        HTTP mocking for Golang

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

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 17 18:58:20 CET 2021 Robert-André Mauchin <zebob.m@gmail.com> - 1.0.7-1
- Update to 1.0.7

* Wed Sep 09 15:08:22 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.0.6-1
- Initial package
