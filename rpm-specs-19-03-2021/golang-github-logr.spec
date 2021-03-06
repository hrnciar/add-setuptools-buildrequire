# Generated by go2rpm
%bcond_without check

# https://github.com/go-logr/logr
%global goipath         github.com/go-logr/logr
Version:                0.3.0

%gometa

%global common_description %{expand:
A more minimal logging API for Go.}

%global golicenses      LICENSE
%global godocs          examples README.md

Name:           %{goname}
Release:        2%{?dist}
Summary:        Simple logging interface for Go

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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec 21 02:52:32 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.3.0-1
- Update to 0.3.0
- Close: rhbz#1876027

* Mon Aug 17 15:46:49 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.2.0-3.20200817gitee2de8d
- Bump to commit ee2de8da5be655b0a1755b264167fcca1d3193f5

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 16:15:46 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.2.0-1
- Update to 0.2.0

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 09 20:28:49 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.1.0-1
- Initial package
