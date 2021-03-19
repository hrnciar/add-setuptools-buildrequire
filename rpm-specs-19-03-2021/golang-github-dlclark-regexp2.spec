# Generated by go2rpm
%bcond_without check

# https://github.com/dlclark/regexp2
%global goipath         github.com/dlclark/regexp2
Version:                1.4.0

%gometa

%global common_description %{expand:
Regexp2 is a feature-rich RegExp engine for Go. It doesn't have constant time
guarantees like the built-in regexp package, but it allows backtracking and is
compatible with Perl5 and .NET. You'll likely be better off with the RE2 engine
from the regexp package and should only use this if you need to write very
complex patterns or require compatibility with .NET.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        2%{?dist}
Summary:        Regex engine for Go based on the .NET engine

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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Jan  2 18:47:28 CET 2021 Robert-André Mauchin <zebob.m@gmail.com> - 1.4.0-1
- Update to 1.4.0
- Close: rhbz#1886267

* Tue Aug 25 2020 Athos Ribeiro <athoscr@fedoraproject.org> - 1.2.1-1
- Update to latest version
- Remove patch applied upstream

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Aug 18 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.2.0-1
- Update to latest version

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 24 19:07:42 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.1.6-5
- Update to new macros

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Oct 11 2017 Athos Ribeiro <athoscr@fedoraproject.org> - 1.1.6-1
- First package for Fedora
