# Generated by go2rpm
%bcond_without check

# https://github.com/skarademir/naturalsort
%global goipath         github.com/skarademir/naturalsort
%global commit          69a5d87bef620f77ee8508db30c846b3b84b111e

%gometa

%global common_description %{expand:
A simple natural string sorter for Go.}

%global golicenses      LICENSE.md
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.16%{?dist}
Summary:        Simple natural sorter for Go Strings

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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 24 15:58:44 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.12.20190524git69a5d87
- Bump to commit 69a5d87bef620f77ee8508db30c846b3b84b111e

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.11.gitf5bc184
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.10.gitf5bc184
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9.gitf5bc184
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8.gitf5bc184
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7.gitf5bc184
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6.gitf5bc184
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.5.gitf5bc184
- https://fedoraproject.org/wiki/Changes/golang1.7

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.4.gitf5bc184
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.gitf5bc184
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Aug 10 2015 Fridolin Pokorny <fpokorny@redhat.com> - 0-0.2.gitf5bc184
- Update spec file to spec-2.0
  resolves: #1250506

* Sat Apr 18 2015 jchaloup <jchaloup@redhat.com> - 0-0.1.gitf5bc184
- First package for Fedora
  resolves: #1214878
