# Generated by go2rpm
%ifnarch ppc64le s390x
%bcond_without check
%endif

# https://gitlab.com/cznic/b
%global goipath         modernc.org/b
%global forgeurl        https://gitlab.com/cznic/b
Version:                1.0.1
%global commit          b4ae8d52903bac017fe80e6d1417cb8c77c609de
%global distprefix      %{nil}

%gometa

%global common_description %{expand:
Package b implements a B+tree.}

%global golicenses      LICENSE
%global godocs          example README.md AUTHORS CONTRIBUTORS

Name:           %{goname}
Release:        2%{?dist}
Summary:        B+tree in Go

# Upstream license specification: BSD-3-Clause
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}

%if %{with check}
# Tests
BuildRequires:  golang(modernc.org/fileutil)
BuildRequires:  golang(modernc.org/mathutil)
BuildRequires:  golang(modernc.org/strutil)
%endif

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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Dec 26 10:58:02 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.0.1-1
- Update to 1.0.1
- Close: rhbz#1900417

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun May 12 15:17:54 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.0.0-1
- Initial package