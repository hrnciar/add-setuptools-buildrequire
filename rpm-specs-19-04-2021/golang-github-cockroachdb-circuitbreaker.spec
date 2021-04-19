# Generated by go2rpm
%bcond_without check

# https://github.com/cockroachdb/circuitbreaker
%global goipath         github.com/cockroachdb/circuitbreaker
Version:                2.2.1
%global commit          a614b14ccf63dd2311d4ff646c30c61b8ed34aa8

%gometa

%global common_description %{expand:
Circuitbreaker provides an easy way to use the Circuit Breaker pattern in a Go
program.}

%global golicenses      LICENSE
%global godocs          CHANGELOG.md README.md

Name:           %{goname}
Release:        5%{?dist}
Summary:        Circuit Breakers in Go

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/cenkalti/backoff)
BuildRequires:  golang(github.com/facebookgo/clock)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/peterbourgon/g2s)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep
find . -name "*.go" -exec sed -i "s|github.com/cenk/backoff|github.com/cenkalti/backoff|" "{}" +;

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May 15 19:49:12 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 2.2.1-1.20190701gita614b14
- Initial package
