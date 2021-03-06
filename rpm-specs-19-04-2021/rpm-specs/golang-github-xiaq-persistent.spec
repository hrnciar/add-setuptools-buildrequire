# Generated by go2rpm 1
%bcond_without check

# https://github.com/xiaq/persistent
%global goipath         github.com/xiaq/persistent
%global commit          3175cfb92e14776bbe31ed7bd320aab8d516d792

%gometa

%global common_description %{expand:
Persistent data structure in Go.}

%global golicenses      epl-v10.html
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.5%{?dist}
Summary:        Persistent data structure in Go

License:        EPL-1.0
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

* Wed Jan 13 18:13:08 CET 2021 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.4.20210113git3175cfb
- Bump to commit 3175cfb92e14776bbe31ed7bd320aab8d516d792

* Tue Aug 04 18:59:40 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.3.20200804git14b5bdc
- Bump to commit 14b5bdc771d3d31df26872d83c271412832bf6fe

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 19 21:43:53 EDT 2020 Carson Black <uhhadd@gmail.com> - 0-0.1.20200519gita1d9ac4
- Initial package
