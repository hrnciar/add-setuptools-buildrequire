# Generated by go2rpm
%bcond_without check

# https://github.com/cyphar/filepath-securejoin
%global goipath         github.com/cyphar/filepath-securejoin
Version:                0.2.2

%gometa

%global common_description %{expand: An implementation of SecureJoin, a
candidate for inclusion in the Go standard library. The purpose of this function
is to be a "secure" alternative to filepath.Join, and in particular it provides
certain guarantees that are not provided by filepath.Join.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        5%{?dist}
Summary:        Proposed filepath.SecureJoin implementation

# Upstream license specification: BSD-3-Clause
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/pkg/errors)

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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat May 04 17:30:17 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.2.2-1
- Initial package
