# Generated by go2rpm
%bcond_without check

# https://github.com/cloudfoundry/clock
%global goipath         code.cloudfoundry.org/clock
%global forgeurl        https://github.com/cloudfoundry/clock
Version:                1.0.0

%gometa

%global common_description %{expand:
This package provides a Clock interface, useful for injecting time dependencies
in tests.}

%global golicenses      LICENSE NOTICE
%global godocs          README.md

Name:           %{goname}
Release:        3%{?dist}
Summary:        Time provider & rich fake for Go

# Upstream license specification: Apache-2.0
License:        ASL 2.0
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

* Wed Jul 22 20:05:14 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.0.0-1
- Update to 1.0.0

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon May 06 21:45:50 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20190628git02e53af
- Initial package
