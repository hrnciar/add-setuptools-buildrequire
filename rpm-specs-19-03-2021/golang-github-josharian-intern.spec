# Generated by go2rpm 1
%bcond_without check

# https://github.com/josharian/intern
%global goipath         github.com/josharian/intern
Version:                1.0.0

%gometa

%global common_description %{expand:
Intern Go strings.}

%global golicenses      license.md
%global godocs          README.md

Name:           %{goname}
Release:        2%{?dist}
Summary:        Intern Go strings

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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 17:51:45 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.0.0-1
- Initial package