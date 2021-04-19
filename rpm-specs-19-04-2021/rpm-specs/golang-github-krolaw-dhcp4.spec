# Generated by go2rpm
%bcond_without check

# https://github.com/krolaw/dhcp4
%global goipath         github.com/krolaw/dhcp4
%global commit          a50d88189771b462f903e77995cd0f4d186fbea7

%gometa

%global common_description %{expand:
IPv4 DHCP library for parsing and creating DHCP packets, along with basic DHCP
server functionality.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.8%{?dist}
Summary:        DHCP4 library written in Go

# Upstream license specification: BSD-3-Clause
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(golang.org/x/net/ipv4)

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

* Sun Jan 10 11:41:20 CET 2021 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.7.20210110gita50d881
- Bump to commit a50d88189771b462f903e77995cd0f4d186fbea7

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May 29 17:29:17 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.2.20190325git7cead47
- Update to new macros

* Thu Nov 15 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20190325git7cead47
- First package for Fedora