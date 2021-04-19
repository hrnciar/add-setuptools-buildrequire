# Generated by go2rpm 1.3
%bcond_without check

# https://github.com/mvdan/editorconfig
%global goipath         mvdan.cc/editorconfig
%global forgeurl        https://github.com/mvdan/editorconfig
Version:                0.2.0

%gometa

%global common_description %{expand:
A small package to parse and use EditorConfig files. Currently passes all of
the official test cases.

Note that an official library exists for Go. This alternative implementation
started with a different design:
- Specialised INI parser, for full compatibility with the spec
- Ability to cache parsing files and compiling pattern matches
- Storing and querying all properties equally
- Minimising pointers and maps to store data}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        EditorConfig support in Go

# Upstream license specification: BSD-3-Clause
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}

%if %{with check}
BuildRequires:  cmake
BuildRequires:  gcc-c++
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
# cannot use %%gocheck as the test shells out to cmake which gets confused by
# the golang LDFLAGS it passes in
go test %{gotestflags}
%endif

%gopkgfiles

%changelog
* Sun Apr 04 2021 Davide Cavalca <dcavalca@fedoraproject.org> - 0.2.0-1
- Initial package