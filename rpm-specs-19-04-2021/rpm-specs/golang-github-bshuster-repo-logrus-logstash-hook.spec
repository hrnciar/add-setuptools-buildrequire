# Generated by go2rpm
%bcond_without check

# https://github.com/bshuster-repo/logrus-logstash-hook
%global goipath         github.com/bshuster-repo/logrus-logstash-hook
Version:                1.0.0

%gometa

%global common_description %{expand:
Use this hook to send the logs to Logstash.}

%global golicenses      LICENSE
%global godocs          CHANGELOG.md README.md

Name:           %{goname}
Release:        3%{?dist}
Summary:        Logstash hook for logrus

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/sirupsen/logrus)

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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 24 16:02:35 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.0.0-1
- Update to 1.0.0

* Wed Jan 29 17:06:18 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.4.1-4
- Fix test error with Go 1.14

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May 01 17:42:07 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.4.1-1
- Initial package
