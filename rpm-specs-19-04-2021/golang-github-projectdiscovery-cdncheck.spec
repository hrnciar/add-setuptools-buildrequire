# Generated by go2rpm 1.2
%bcond_without check
%bcond_with network

# https://github.com/projectdiscovery/cdncheck
%global goipath         github.com/projectdiscovery/cdncheck
%global commit          5bc57c3839351b68cbcf7c262dd2a1ae721114b9

%gometa

%global common_description %{expand:
A filter to check for CDN IP addresses during port scanning.}

%global golicenses      LICENSE.md
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.2%{?dist}
Summary:        Filter to check for CDN IP addresses during port scanning

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/yl2chen/cidranger)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/stretchr/testify/require)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep

%install
%gopkginstall


%if %{with network}
%if %{with check}
%check
%gocheck
%endif
%endif

%gopkgfiles

%changelog
* Mon Nov 16 10:01:13 CET 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0-0.2.20201116git5bc57c3
- Tests requires network access (#1881572)
- Update to latest commit

* Tue Sep 22 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0-0.1.20200922git19e1db6
- Initial package for Fedora