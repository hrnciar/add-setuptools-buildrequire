# Generated by go2rpm
# Fails on 32 bits arch
%ifnarch %{ix86} %{arm}
%bcond_without check
%endif

# https://github.com/Knetic/govaluate
%global goipath         github.com/Knetic/govaluate
Version:                3.0.0
%global commit          9aa49832a739dcd78a5542ff189fb82c3e423116

%gometa

%global common_description %{expand:
Provides support for evaluating arbitrary C-like artithmetic/string
expressions.}

%global golicenses      LICENSE
%global godocs          CONTRIBUTORS MANUAL.md README.md

Name:           %{goname}
Release:        6%{?dist}
Summary:        Arbitrary expression evaluation for golang

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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Apr 19 16:23:10 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 3.0.0-1.20190622git9aa4983
- Initial package
