# Generated by go2rpm 1
%bcond_without check

# https://github.com/viant/assertly
%global goipath         github.com/viant/assertly
Version:                0.9.0

%gometa

%global common_description %{expand:
Arbitrary datastructure validation.}

%global golicenses      LICENSE NOTICE
%global godocs          CHANGELOG.md README.md

Name:           %{goname}
Release:        2%{?dist}
Summary:        Arbitrary datastructure validation

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/viant/toolbox)
BuildRequires:  golang(github.com/viant/toolbox/data)

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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 15:49:54 CET 2021 Robert-André Mauchin <zebob.m@gmail.com> - 0.9.0-1
- Update to 0.9.0

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 03 16:37:47 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.5.4-1
- Initial package
