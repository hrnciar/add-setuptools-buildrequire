# Generated by go2rpm
# Needs network
%bcond_with check

# https://github.com/globalsign/mgo
%global goipath         github.com/globalsign/mgo
Version:                r2018.06.15
%global tag             r2018.06.15

%gometa

%global common_description %{expand:
Package Mgo (pronounced as "mango") offers a rich MongoDB driver for Go.}

%global golicenses      LICENSE LICENSE-bson
%global godocs          CONTRIBUTING.md README.md README-bson.md

Name:           %{goname}
Release:        7%{?dist}
Summary:        MongoDB driver for Go

# Upstream license specification: BSD-2-Clause and BSD-3-Clause
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}
# https://github.com/globalsign/mgo/pull/356
Patch0:         0001-Fix-debugf-arguments.patch

BuildRequires:  golang(gopkg.in/tomb.v2)

%if %{with check}
# Tests
BuildRequires:  golang(gopkg.in/check.v1)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep
%patch0 -p1
mv bson/README.md README-bson.md
mv bson/LICENSE LICENSE-bson

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - r2018.06.15-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - r2018.06.15-6
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - r2018.06.15-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - r2018.06.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - r2018.06.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Apr 29 20:07:03 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - r2018.06.15-2
- Update to new macros

* Sun Mar 10 2019 Robert-André Mauchin <zebob.m@gmail.com> - r2018.06.15-1
- Release r2018.06.15

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4.git113d396
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.git113d396
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.2.20180628git113d396
- Bump to commit 113d3961e7311526535a1ef7042196563d442761

* Mon Mar 26 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20180416gitf76e4f9
- First package for Fedora
