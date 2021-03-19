# Generated by go2rpm
%bcond_without check

# https://github.com/fatih/color
%global goipath         github.com/fatih/color
Version:                1.10.0

%gometa

%global common_description %{expand:
Color lets you use colorized outputs in terms of ANSI Escape Codes in Go. It has
support for Windows too! The API can be used in several ways, pick one that
suits you.}

%global golicenses      LICENSE.md
%global godocs          README.md

Name:           %{goname}
Release:        2%{?dist}
Summary:        Color package for Go

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/mattn/go-colorable)
BuildRequires:  golang(github.com/mattn/go-isatty)

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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Jan  2 18:59:37 CET 2021 Robert-André Mauchin <zebob.m@gmail.com> - 1.10.0-1
- Update to 1.10.0
- Close: rhbz#1893407

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jul 26 17:12:46 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.9.0-1
- Update to 1.9.0

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Apr 21 18:38:52 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.7.0-4
- Update to new macros

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Sep 25 2018 Robert-André Mauchin <zebob.m@gmail.com> - 1.7.0-2
- Update to new packaging
- Add missing BuildRequires (#1632758)

* Thu Aug 02 2018 Michael Cronenworth <mike@cchtml.com> - 1.7.0-1
- New upstream release.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.4.20170905git1535ebc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.3.20170905git1535ebc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Nov 25 2017 Robert-André Mauchin <zebob.m@gmail.com> - 0.1-0.2.20170905git1535ebc
- Provide alternate name path

* Mon Sep 18 2017 Matthias Runge <mrunge@redhat.com> - 0-0.1.20170905git1535ebc
- update to latest version
- package review (rhbz#1376437)

* Fri Apr 15 2016 Matthias Runge <mrunge@redhat.com> - 0.1-1
- initial package
