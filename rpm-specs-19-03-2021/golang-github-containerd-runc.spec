# Generated by go2rpm
%bcond_without check

# https://github.com/containerd/go-runc
%global goipath         github.com/containerd/go-runc
%global commit          16b287bc67d069a60fa48db15f330b790b74365b

%gometa

%global common_description %{expand:
This is a package for consuming the runc binary in your Go applications. It
tries to expose all the settings and features of the runc CLI.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.7%{?dist}
Summary:        Runc bindings for Go

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/containerd/console)
BuildRequires:  golang(github.com/opencontainers/runtime-spec/specs-go)
BuildRequires:  golang(github.com/pkg/errors)
BuildRequires:  golang(github.com/sirupsen/logrus)
BuildRequires:  golang(golang.org/x/sys/unix)

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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Jan 09 14:58:12 CET 2021 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.6.20210109git16b287b
- Bump to commit 16b287bc67d069a60fa48db15f330b790b74365b

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 25 16:48:23 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.4.20200725git23d84c5
- Bump to commit 23d84c510c41ee9eaeab57ec6caad8bb81686265

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May 01 17:15:44 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20190626git7d11b49
- Initial package
