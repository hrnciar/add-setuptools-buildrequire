# Generated by go2rpm 1
%bcond_without check

# https://github.com/jcmturner/aescts
%global goipath         github.com/jcmturner/aescts
Version:                2.0.0

%gometa

%global common_description %{expand:
AES CBC Ciphertext Stealing mode for Go.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        2%{?dist}
Summary:        AES CBC Ciphertext Stealing mode for Go

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

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
sed -i 's|github.com/jcmturner/aescts|github.com/jcmturner/aescts/v2|' $(find . -maxdepth 1 -iname "*go" -type f)
%gocheck
%endif

%gopkgfiles

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 22:11:00 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 2.0.0-1
- Initial package
