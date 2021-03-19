# Generated by go2rpm 1
%bcond_without check

# https://github.com/logrusorgru/aurora
%global goipath         github.com/logrusorgru/aurora
Version:                3.0.0

%gometa

%global goaltipaths     github.com/logrusorgru/aurora/v3

%global common_description %{expand:
Golang ultimate ANSI-colors that supports Printf/Sprintf methods.}

%global golicenses      LICENSE
%global godocs          README.md CHANGELOG.md AUTHORS.md

Name:           %{goname}
Release:        2%{?dist}
Summary:        Golang ultimate ANSI-colors that supports Printf/Sprintf methods

License:        Unlicense
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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 15:12:11 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 3.0.0-1
- Update to 3.0.0

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Feb 28 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.0-1
- Initial package for Fedora