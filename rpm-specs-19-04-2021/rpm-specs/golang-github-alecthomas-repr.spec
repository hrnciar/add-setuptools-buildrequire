# Generated by go2rpm
%bcond_without check

# https://github.com/alecthomas/repr
%global goipath         github.com/alecthomas/repr
%global commit          bb82daffcca269896bba419bb7e8260f66fed1b4

%gometa

%global common_description %{expand:
This package attempts to represent Go values in a form that can be used almost
directly in Go source code.

Unfortunately, some values (such as pointers to basic types) can not be
represented directly in Go. These values will be represented as &<value>. eg.
&23.}

%global golicenses      COPYING
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.12%{?dist}
Summary:        Python's repr() for Go

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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 08 21:48:40 CET 2021 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20210108gitbb82daf
- Bump to commit bb82daffcca269896bba419bb7e8260f66fed1b4

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 23 13:40:06 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.9.20200723git4184120
- Bump to commit 4184120f674c8860a5b48142509a2411a0a1766f

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 15:12:10 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.6.20181111gitd37bc2a
- Update to new macros

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5.gitd37bc2a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Nov 11 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.4.20181111gitd37bc2a
- Bump to commit d37bc2a10ba1a7951e19dd5dc10f7d59b142d8d7
- Update to new Go packaging

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.gitd44565c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.gitd44565c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Aug 11 2017 mosquito <sensor.wen@gmail.com> - 0-0.1.gitd44565c
- Initial package build
