# Generated by go2rpm
%bcond_without check

# https://github.com/sigma/go-inotify
%global goipath         github.com/sigma/go-inotify
%global commit          c87b6cf5033d2c6486046f045eeebdc3d910fd38

%gometa

%global common_description %{expand:
Package Go-fsnotify provides a platform-independent interface for file system
notifications}

%global golicenses      LICENSE PATENTS
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.5%{?dist}
Summary:        Platform-independent interface for file system notifications

# Upstream license specification: BSD-3-Clause
License:        BSD
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

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 17 23:00:25 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20190702gitc87b6cf
- Initial package
