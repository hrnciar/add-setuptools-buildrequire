# Generated by go2rpm 1
%bcond_without check

# https://github.com/pkg/browser
%global goipath         github.com/pkg/browser
%global commit          0426ae3fba23d90b7f89ec6bef10e9c3ca607212

%gometa

%global common_description %{expand:
Helpers to open files, readers, and urls in a browser}

%global golicenses      LICENSE
%global godocs          examples README.md

Name:           %{goname}
Version:        0
Release:        0.5%{?dist}
Summary:        Helpers to open files, readers, and urls in a browser

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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 10 21:13:34 CET 2021 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.4.20210110git0426ae3
- Bump to commit 0426ae3fba23d90b7f89ec6bef10e9c3ca607212

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Nov 17 08:12:10 UTC 2019 Thomas Drake-Brockman <thom@sfedb.com> - 0-0.1.20191117git0a3d74b
- Initial package
