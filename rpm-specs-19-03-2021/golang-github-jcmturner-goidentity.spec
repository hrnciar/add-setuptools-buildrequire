# Generated by go2rpm 1
%bcond_without check

# https://github.com/jcmturner/goidentity
%global goipath         github.com/jcmturner/goidentity
Version:                6.0.1

%gometa

%global common_description %{expand:
Standard interface for holding authenticated identities and their attributes.}

%global golicenses      LICENSE
%global godocs          v6/README.md

Name:           %{goname}
Release:        2%{?dist}
Summary:        Standard interface for holding authenticated identities and their attributes

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
sed -i 's|github.com/jcmturner/goidentity|github.com/jcmturner/goidentity/v6|' $(find .  -maxdepth 1 -iname "*go" -type f)
%gocheck
%endif

%gopkgfiles

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 22:17:36 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 6.0.1-1
- Initial package
