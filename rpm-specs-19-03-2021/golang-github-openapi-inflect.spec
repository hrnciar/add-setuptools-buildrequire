# Generated by go2rpm 1.2
%bcond_without check

# https://github.com/go-openapi/inflect
%global goipath         github.com/go-openapi/inflect
Version:                0.19.0

%gometa

%global common_description %{expand:
This is a Go library to perform word transformations like pluralization,
singularization, etc. It is a fork of https://bitbucket.org/pkg/inflect.}

%global golicenses      LICENCE
%global godocs          README

Name:           %{goname}
Release:        2%{?dist}
Summary:        Go library to perform word transformations

License:        MIT
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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.19.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Nov 08 2020 Davide Cavalca <dcavalca@fedoraproject.org> - 0.19.0-1
- Initial package
