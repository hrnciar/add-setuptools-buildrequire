# Generated by go2rpm
%bcond_without check

# https://github.com/duosecurity/duo_api_golang
%global goipath         github.com/duosecurity/duo_api_golang
%global commit          0e07e9f869e36b7128308dccfce1b038db0e1712

%gometa

%global common_description %{expand:
The Auth API is a low-level, RESTful API for adding strong two-factor
authentication to your website or application.

This module's API client implementation is complete; corresponding methods are
exported for all available endpoints.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.13%{?dist}
Summary:        Go language bindings for the Duo APIs (both auth and admin)

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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Jan 09 17:09:25 CET 2021 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.12.20210109git0e07e9f
- Bump to commit 0e07e9f869e36b7128308dccfce1b038db0e1712

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jul 26 15:19:26 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.10.20200726git982114f
- Bump to commit 982114f7995f2fbee17bca19b206fa03e4cc4a12

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 09 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0-0.7.20190626git6c680f7
- Add Obsoletes for old names

* Tue Apr 30 00:44:42 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.6.20190626git6c680f7
- Bump to commit 6c680f768e746ca8563c19035adfd94a4a4101f1

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5.20160627git2b2d787
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4.20160627git2b2d787
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 14 2018 Ed Marshall <esm@logic.net> - 0-0.3.20160627git2b2d787
- Add patch to fix FTBFS with Go 1.10.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.20160627git2b2d787
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Oct 04 2017 Ed Marshall <esm@logic.net> - 0-0.1.20160627git2b2d787
- First package for Fedora