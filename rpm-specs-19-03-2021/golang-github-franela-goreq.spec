# Generated by go2rpm
%bcond_without check

# https://github.com/franela/goreq
%global goipath         github.com/franela/goreq
%global commit          bcd34c9993f899273c74baaa95e15386cd97b6e7

%gometa

%global common_description %{expand:
Minimal and simple request library for Go.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.5%{?dist}
Summary:        Minimal and simple request library for Go

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}
# Fix tests, not upsteamed because dead upstream
Patch0:         0001-Import-github.com-franela-goblin-as-goblin.patch

%if %{with check}
# Tests
BuildRequires:  golang(github.com/franela/goblin)
BuildRequires:  golang(github.com/onsi/gomega)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep
%patch0 -p1

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

* Mon Apr 22 23:36:14 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20190623gitbcd34c9
- Initial package
