# Generated by go2rpm
# Fixed upstream
%ifnarch %{ix86} %{arm} s390x
%bcond_without check
%endif

# https://github.com/performancecopilot/speed
%global goipath         github.com/performancecopilot/speed
Version:                3.0.1

%gometa

%global common_description %{expand:
Package Speed implements a Golang client for the Performance Co-Pilot
instrumentation API.}

%global golicenses      LICENSE
%global godocs          examples CHANGELOG.md README.md

Name:           %{goname}
Release:        5%{?dist}
Summary:        Go implementation of the PCP instrumentation API

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/codahale/hdrhistogram)
BuildRequires:  golang(github.com/edsrzf/mmap-go)
BuildRequires:  golang(github.com/pkg/errors)

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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May 15 00:45:50 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 3.0.1-1
- Initial package
