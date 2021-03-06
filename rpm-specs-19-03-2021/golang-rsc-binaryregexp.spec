# Generated by go2rpm 1
%bcond_without check

# https://github.com/rsc/binaryregexp
%global goipath         rsc.io/binaryregexp
%global forgeurl        https://github.com/rsc/binaryregexp
Version:                0.2.0

%gometa

%global common_description %{expand:
Go regexp for binary/latin-1 data.}

%global golicenses      LICENSE
Name:           %{goname}
Release:        4%{?dist}
Summary:        Go regexp for binary/latin-1 data

# Upstream license specification: BSD-3-Clause
License:        BSD
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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Dec 28 17:46:59 CET 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.2.0-1
- Initial package
