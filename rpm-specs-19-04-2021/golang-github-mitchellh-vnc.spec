# Generated by go2rpm
%bcond_without check

# https://github.com/mitchellh/go-vnc
%global goipath         github.com/mitchellh/go-vnc
%global commit          723ed9867aed0f3209a81151e52ddc61681f0b01

%gometa

%global common_description %{expand:
Go-vnc is a VNC library for Go, initially supporting VNC clients but with the
goal of eventually implementing a VNC server.

This library implements RFC 6143.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.6%{?dist}
Summary:        VNC client and server library for Go

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

Patch0:         0001-Fix-Errorf-wrong-type.patch

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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 03 00:34:08 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20190627git723ed98
- Initial package
