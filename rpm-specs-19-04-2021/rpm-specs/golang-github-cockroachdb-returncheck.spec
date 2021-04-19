# Generated by go2rpm
%bcond_without check

# https://github.com/cockroachdb/returncheck
%global goipath         github.com/cockroachdb/returncheck
%global commit          92cdbca611dd083736f8bdf426e4fc74791aab9e

%gometa

%global common_description %{expand:
Go return value checker.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.6%{?dist}
Summary:        Go return value checker

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(golang.org/x/tools/go/packages)

%description
%{common_description}

%gopkg

%prep
%goprep

%install
%gopkginstall

%if %{with check}
%check
%gocheck -d .
%endif

%gopkgfiles

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 25 14:03:31 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.4.20200725git92cdbca
- Bump to commit 92cdbca611dd083736f8bdf426e4fc74791aab9e

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May 15 20:46:15 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20190701gite91bb28
- Initial package