# Generated by go2rpm
%bcond_without check

# https://github.com/facebookgo/clock
%global goipath         github.com/facebookgo/clock
%global commit          600d898af40aa09a7a93ecb9265d87b0504b6f03

%gometa

%global common_description %{expand:
Clock is a small library for mocking time in Go. It provides an interface around
the standard library's time package so that the application can use the realtime
clock while tests can use the mock clock.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.5%{?dist}
Summary:        Small library for mocking time in Go

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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon May 06 00:02:45 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20190627git600d898
- Initial package
