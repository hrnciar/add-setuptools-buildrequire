# Generated by go2rpm
%bcond_without check

# https://github.com/milochristiansen/lua
%global goipath         github.com/milochristiansen/lua
Version:                1.1.7

%gometa

%global common_description %{expand:
This is a Lua 5.3 VM and compiler written in Go. This is intended to allow easy
embedding into Go programs, with minimal fuss and bother.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        6%{?dist}
Summary:        Lua 5.3 VM and compiler written in Go

# Upstream license specification: Zlib
License:        zlib
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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.7-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 02 18:54:00 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.1.7-1
- Release 1.1.7

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Oct 23 2017 Ben Rosser <rosser.bjr@gmail.com> - 1.1.4-1
- Updated to latest upstream release (#1493534).
- Updated golang spec with new changes from gofed.

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Apr 18 2017 Ben Rosser <rosser.bjr@gmail.com> - 1.1.3-1
- Update to latest upstream release, fixing 32-bit unit test failures.
- Add new development provides for supermeta and testhelp go subpackages.
- Add new gotest command for supermeta tests.
- Re-add commit and shortcommit global macros to header for gofed.

* Wed Apr 05 2017 Ben Rosser <rosser.bjr@gmail.com> - 1.1.1-1
- Updated to latest upstream release.
- Changed Source0 to use project prefix.
- Remove vendored go library from Provides section.
- Cleaned up setup macro in prep section.
- Removed some empty/redundant template parts of the spec file and cleaned GOPATH definition.
- General spec cleanup; removed dist tag from changelog section and removed leading article from summary.

* Fri Dec 30 2016 Ben Rosser <rosser.bjr@gmail.com> - 1.0.2-1
- First package for Fedora
