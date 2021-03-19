# Generated by go2rpm
%bcond_without check

# https://github.com/Rican7/retry
%global goipath         github.com/Rican7/retry
Version:                0.1.0
%global commit          272ad122d6e5ce1be757544007cf8bcd1c9c9ab0

%gometa

%global common_description %{expand:
A simple, stateless, functional mechanism to perform actions repetitively until
successful.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        6%{?dist}
Summary:        Simple, stateless, functional mechanism to perform actions repetitively

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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 17 20:25:15 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.1.0-2.20190306git272ad12
- Update to new macros

* Mon Oct 29 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.1.0-1.20190306git272ad12
- First package for Fedora