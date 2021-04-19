# Generated by go2rpm
%bcond_without check

# https://github.com/revel/config
%global goipath         github.com/revel/config
Version:                1.0.0

%gometa

%global common_description %{expand:
This package implements a basic configuration file parser language which
provides a structure similar to what you would find on Microsoft Windows INI
files.}

%global godocs          README.md Doc

Name:           %{goname}
Release:        2%{?dist}
Summary:        Configuration file parser for INI format

# https://github.com/revel/config/issues/13
License:        MPLv2.0
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

* Sat Aug 01 21:29:44 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.0.0-1
- Update to 1.0.0

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May 01 18:47:06 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.21.0-1
- Initial package
