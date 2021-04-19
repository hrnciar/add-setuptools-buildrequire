# Generated by go2rpm
%bcond_without check

# https://github.com/go-errgo/errgo
%global goipath         gopkg.in/errgo.v2
%global forgeurl        https://github.com/go-errgo/errgo
Version:                2.1.0

%gometa

%global common_description %{expand:
The Errgo package provides a way to create and diagnose errors. It is compatible
with the usual Go error idioms but adds a way to wrap errors so that they record
source location information while retaining a consistent way for code to inspect
errors to find out particular problems.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        5%{?dist}
Summary:        Dependable Go errors with tracebacks

# Upstream license specification: BSD-3-Clause
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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 07 15:50:31 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 2.1.0-1
- Initial package