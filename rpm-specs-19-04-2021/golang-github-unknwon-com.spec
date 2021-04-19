# Generated by go2rpm
%bcond_without check

# https://github.com/unknwon/com
%global goipath         github.com/unknwon/com
Version:                1.0.1

%gometa

%global goaltipaths     github.com/Unknwon/com

%global common_description %{expand:
This is an open source project for commonly used functions for the Go
programming language.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
# Upstream published v1.0.0 after v2
Epoch:          1
Release:        2%{?dist}
Summary:        Commonly used functions for the Go programming language

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}
# Disable tests requiring network
Patch0:         no-internet-access.patch
# Go 1.15: https://github.com/unknwon/com/issues/28
Patch1:         0001-Convert-int-to-string-using-rune.patch

%if %{with check}
# Tests
BuildRequires:  golang(github.com/smartystreets/goconvey/convey)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep
%patch0 -p1
%patch1 -p1

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 17:42:28 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1:1.0.1-1
- Update to 1.0.1

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 24 17:14:07 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 2-3
- Update to new macros

* Wed Mar 20 2019 Nathan Scott <nathans@redhat.com> - 2-2
- Update BuildRequires line to use the golang()-style.

* Sun Mar 17 2019 Nathan Scott <nathans@redhat.com> - 2-1
- First package for Fedora