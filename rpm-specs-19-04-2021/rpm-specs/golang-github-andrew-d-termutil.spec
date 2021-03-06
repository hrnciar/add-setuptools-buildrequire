# Generated by go2rpm 1
%bcond_without check

# https://github.com/andrew-d/go-termutil
%global goipath         github.com/andrew-d/go-termutil
%global commit          009166a695a2f516c749a26b4ac1f183d89aa336

%gometa

%global common_description %{expand:
Terminal utilities for golang.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.3%{?dist}
Summary:        Terminal utilities

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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Feb 26 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0-0.1.20200226git009166a
- Initial package for Fedora
