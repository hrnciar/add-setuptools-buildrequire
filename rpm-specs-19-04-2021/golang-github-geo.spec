# Generated by go2rpm 1
# Rounding errors on other arches
%ifarch x86_64
%bcond_without check
%endif

# https://github.com/golang/geo
%global goipath         github.com/golang/geo
%global commit          a63082ebfb66b1be7a21e9088824139583d9a8f2

%gometa

%global common_description %{expand:
S2 geometry library in Go.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.5%{?dist}
Summary:        S2 geometry library in Go

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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Jan 09 18:12:45 CET 2021 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.4.20210109gita63082e
- Bump to commit a63082ebfb66b1be7a21e9088824139583d9a8f2

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Apr 04 21:57:22 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20200411git673a6f8
- Initial package
