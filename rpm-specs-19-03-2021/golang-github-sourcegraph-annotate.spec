# Generated by go2rpm
%bcond_without check

# https://github.com/sourcegraph/annotate
%global goipath         github.com/sourcegraph/annotate
%global commit          f4cad6c6324d3f584e1743d8b3e0e017a5f3a636

%gometa

%global common_description %{expand:
A Go package for applying multiple sets of annotations to a region of text.}

%global golicenses      LICENSE
%global godocs          README.md benchmark.txt

Name:           %{goname}
Version:        0
Release:        0.8%{?dist}
Summary:        Go package for applying multiple sets of annotations to a region of text

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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 24 19:30:34 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.4.20180418gitf4cad6c
- Update to new macros

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.gitf4cad6c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.gitf4cad6c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Mar 24 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20180418gitf4cad6c
- First package for Fedora
