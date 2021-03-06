# Generated by go2rpm 1
%bcond_without check

# https://github.com/dennwc/base
%global goipath         github.com/dennwc/base
Version:                1.0.0

%gometa

%global common_description %{expand:
Common Go interfaces.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        3%{?dist}
Summary:        Common Go interfaces

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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Apr 07 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.0-1
- Initial package

