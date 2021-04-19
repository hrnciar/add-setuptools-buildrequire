# Generated by go2rpm
%bcond_without check

# https://github.com/certifi/gocertifi
%global goipath         github.com/certifi/gocertifi
Version:                0.0.20200922
%global tag             2020.09.22
%global distprefix      %{nil}

%gometa

%global common_description %{expand:
This Go package contains a CA bundle that you can reference in your Go code.
This is useful for systems that do not have CA bundles that Golang can find
itself, or where a uniform set of CAs is valuable.

This is the same CA bundle that ships with the Python Requests library, and is a
Golang specific port of certifi. The CA bundle is derived from Mozilla's
canonical set.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        2%{?dist}
Summary:        Carefully curated collection of Root Certificates

License:        MPLv2.0
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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.20200922-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Dec 16 09:59:25 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.0.20200922-1
- Update to 2020.09.22
- Close: rhbz#1881939

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.20200211-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 24 21:48:25 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.0.20200211-1
- Update to 2020.02.11

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.20180118-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.20180118-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon May 06 22:12:01 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.0.20180118-1
- Initial package
