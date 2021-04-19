# Generated by go2rpm 1
%bcond_without check

# https://github.com/zclconf/go-cty
%global goipath         github.com/zclconf/go-cty
Version:                1.7.1

%gometa

%global common_description %{expand:
A type system for dynamic values in Go applications.}

%global golicenses      LICENSE
%global godocs          docs README.md CHANGELOG.md

Name:           %{goname}
Release:        2%{?dist}
Summary:        A type system for dynamic values in Go applications

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}
# Fix an incorrect test
Patch0:         https://github.com/zclconf/go-cty/commit/251ac0b66ee75102f9e2dd88a1ae1743d3dd421f.patch#/0001-Fix-an-incorrect-test.patch

BuildRequires:  golang(github.com/apparentlymart/go-textseg/v12/textseg)
BuildRequires:  golang(github.com/vmihailenco/msgpack/v4)
BuildRequires:  golang(github.com/vmihailenco/msgpack/v4/codes)
BuildRequires:  golang(golang.org/x/text/unicode/norm)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/google/go-cmp/cmp)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep
%patch0 -p1

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 16:48:10 CET 2021 Robert-André Mauchin <zebob.m@gmail.com> - 1.7.1-1
- Update to 1.7.1

* Tue Sep 08 18:05:43 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.6.1-1
- Initial package
