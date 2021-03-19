%bcond_without check

# https://github.com/nathanaelle/syslog5424
%global goipath         github.com/nathanaelle/syslog5424/v2
%global forgeurl        https://github.com/nathanaelle/syslog5424
Version:                2.0.5

%gometa

%global common_description %{expand:
Log.Logger-friendly RFC-5424 syslog library.}

%global golicenses      LICENSE.txt
%global godocs          ReadMe.md

Name:           %{goname}
Release:        2%{?dist}
Summary:        Log.Logger-friendly RFC-5424 syslog library

# Upstream license specification: BSD-2-Clause
License:        BSD
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
* Thu Mar 11 2021 Brandon Perkins <bperkins@redhat.com> - 2.0.5-2
- Update to version 2.0.5 (Fixes rhbz#1930941)

* Fri Feb 19 2021 Brandon Perkins <bperkins@redhat.com> - 2.0.5-1
- Initial package

