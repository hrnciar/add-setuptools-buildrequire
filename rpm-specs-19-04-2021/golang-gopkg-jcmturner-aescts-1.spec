# Generated by go2rpm 1
%bcond_without check

# https://github.com/jcmturner/aescts
%global goipath         gopkg.in/jcmturner/aescts.v1
%global forgeurl        https://github.com/jcmturner/aescts
Version:                1.0.1

%gometa

%global common_description %{expand:
AES CBC Ciphertext Stealing mode for Go.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        3%{?dist}
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
%gocheck
%endif

%gopkgfiles

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Feb 20 20:42:20 EST 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.1-1
- Initial package
