# Generated by go2rpm
%bcond_without check

# https://github.com/fullsailor/pkcs7
%global goipath         github.com/fullsailor/pkcs7
%global commit          d7302db945fa6ea264fb79d8e13e931ea514a602

%gometa

%global common_description %{expand:
Package pkcs7 implements parsing and generation of some PKCS#7 structures.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.8%{?dist}
Summary:        Go library for a subset of PKCS#7/cryptographic message syntax

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}
# Fix FTBFS depending ondeprecated DSA
Patch0:         0001-Remove-the-EC2-test.patch

%if %{with check}
# Tests
BuildRequires:  openssl
%endif

%description
%{common_description}

%gopkg

%prep
%goprep
%patch0 -p1

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

* Tue Apr 30 01:03:11 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.4.20190430gitd7302db
- Bump to commit d7302db945fa6ea264fb79d8e13e931ea514a602

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.20180223git1d50025
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.20180223git1d50025
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 14 2018 Ed Marshall <esm@logic.net> - 0-0.1.20180223git1d50025
- Update to latest git commit to fix FTBFS.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.20170613gita009d8d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Oct 03 2017 Ed Marshall <esm@logic.net> - 0-0.1.20170613gita009d8d
- First package for Fedora
