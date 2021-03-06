# Generated by go2rpm 1
%bcond_without check

# https://github.com/armon/go-socks5
%global goipath         github.com/armon/go-socks5
%global commit          e75332964ef517daa070d7c38a9466a0d687e0a5

%gometa

%global common_description %{expand:
This package provides the socks5 package that implements a SOCKS5 server. SOCKS
(Secure Sockets) is used to route traffic between a client and server through an
intermediate proxy layer. This can be used to bypass firewalls or NATs.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.4%{?dist}
Summary:        SOCKS5 server in Golang

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(golang.org/x/net/context)

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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 12:48:52 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20190803gite753329
- Initial package
