# Generated by go2rpm 1
%bcond_without check

# https://github.com/jcmturner/goidentity
%global goipath         gopkg.in/jcmturner/goidentity.v3
%global forgeurl        https://github.com/jcmturner/goidentity
Version:                3.0.0

%gometa

%global common_description %{expand:
Standard interface to holding authenticated identities and their attributes.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        2%{?dist}
Summary:        Standard interface to holding authenticated identities and their attributes

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/hashicorp/go-uuid)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/stretchr/testify/assert)
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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Aug 02 18:52:25 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 3.0.0-1
- Initial package
