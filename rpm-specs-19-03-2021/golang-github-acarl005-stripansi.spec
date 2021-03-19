# Generated by go2rpm 1
%bcond_without check

# https://github.com/acarl005/stripansi
%global goipath         github.com/acarl005/stripansi
%global commit          5a71ef0e047df0427e87a79f27009029921f1f9b

%gometa

%global common_description %{expand:
A little Go package for removing ANSI color escape codes from strings.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.2%{?dist}
Summary:        Helper to remove ANSI color escape codes from strings

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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Aug 26 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0-0.1.20200826git5a71ef0
- Initial package

