# Generated by go2rpm 1
# Needs network to fetch glide data
%bcond_with check

# https://github.com/lyft/protoc-gen-star
%global goipath         github.com/lyft/protoc-gen-star
Version:                0.5.2

%gometa

%global common_description %{expand:
Protoc plugin library for efficient proto-based code generation.}

%global golicenses      LICENSE
%global godocs          CODE_OF_CONDUCT.md README.md

Name:           %{goname}
Release:        2%{?dist}
Summary:        Protoc plugin library for efficient proto-based code generation

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/golang/protobuf/proto)
BuildRequires:  golang(github.com/golang/protobuf/protoc-gen-go/descriptor)
BuildRequires:  golang(github.com/golang/protobuf/protoc-gen-go/plugin)
BuildRequires:  golang(github.com/spf13/afero)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/golang/protobuf/descriptor)
BuildRequires:  golang(github.com/golang/protobuf/ptypes/any)
BuildRequires:  golang(github.com/stretchr/testify/assert)
BuildRequires:  golang(github.com/stretchr/testify/require)
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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 18 16:38:50 CET 2021 Robert-André Mauchin <zebob.m@gmail.com> - 0.5.2-1
- Update to 0.5.2

* Thu Sep 03 20:26:19 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.5.1-1
- Initial package
