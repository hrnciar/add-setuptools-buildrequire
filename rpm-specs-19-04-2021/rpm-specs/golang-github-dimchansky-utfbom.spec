# Generated by go2rpm
%bcond_without check

# https://github.com/dimchansky/utfbom
%global goipath         github.com/dimchansky/utfbom
Version:                1.1.1

%gometa

%global common_description %{expand:
The package utfbom implements the detection of the BOM (Unicode Byte Order
Mark) and removing as necessary. It can also return the encoding detected
by the BOM.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        2%{?dist}
Summary:        Detection of the BOM and removing as necessary

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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Dec 18 08:43:06 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.1.1-1
- Update to 1.1.1
- Close: rhbz#1895557

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Apr 29 19:39:30 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.1.0-2
- Update to new macros

* Sun Mar 10 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.1.0-1
- Release 1.1.0

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.git6c6132f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.git6c6132f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Mar 26 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20180416git6c6132f
- First package for Fedora
