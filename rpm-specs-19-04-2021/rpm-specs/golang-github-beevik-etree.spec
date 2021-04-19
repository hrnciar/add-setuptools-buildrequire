# Generated by go2rpm 1
%bcond_without check

# https://github.com/beevik/etree
%global goipath         github.com/beevik/etree
Version:                1.1.0
%global tag             v1.1.0

%gometa

%global common_description %{expand:
Parse and generate XML easily in go.}

%global golicenses      LICENSE
%global godocs          README.md RELEASE_NOTES.md CONTRIBUTORS

Name:           %{goname}
Release:        3%{?dist}
Summary:        Parse and generate XML easily in go

# Upstream license specification: BSD-2-Clause
License:        BSD
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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Feb 07 16:34:05 CET 2020 Andreas Gerstmayr <agerstmayr@redhat.com> - 1.1.0-1
- Initial package
