# Generated by go2rpm
%bcond_without check

# https://github.com/deckarep/golang-set
%global goipath         github.com/deckarep/golang-set
Version:                1.7.1

%gometa

%global common_description %{expand:
Package Mapset implements a simple and generic set collection. Items stored
within it are unordered and unique. It supports typical set operations:
membership testing, intersection, union, difference, symmetric difference and
cloning.

Package Mapset provides two implementations of the Set interface. The default
implementation is safe for concurrent access, but a non-thread-safe
implementation is also provided for programs that can benefit from the slight
speed improvement and that can enforce mutual exclusion through other means.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        5%{?dist}
Summary:        Simple set type for the Go language

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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon May 06 20:30:02 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.7.1-1
- Initial package
