# Generated by go2rpm 1
%bcond_without check

# https://github.com/uber-go/goleak
%global goipath         go.uber.org/goleak
%global forgeurl        https://github.com/uber-go/goleak
Version:                1.1.10

%gometa

%global common_description %{expand:
Goroutine leak detector.}

%global golicenses      LICENSE
%global godocs          README.md CHANGELOG.md

Name:           %{goname}
Release:        2%{?dist}
Summary:        Goroutine leak detector

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

%if %{with check}
# Tests
BuildRequires:  golang(github.com/stretchr/testify/assert)
BuildRequires:  golang(github.com/stretchr/testify/require)
%endif

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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Jan 23 00:44:03 CET 2021 Robert-André Mauchin <zebob.m@gmail.com> - 1.1.10-1
- Update to 1.1.10

* Thu Jul 16 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.0-1
- Initial package for Fedora