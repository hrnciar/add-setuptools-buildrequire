# Generated by go2rpm 1.2
%bcond_without check

# https://github.com/hugelgupf/socketpair
%global goipath         github.com/hugelgupf/socketpair
%global commit          05d35a94e71444d53460c2b34dfb3dc87c99d0bd

%gometa

%global common_description %{expand:
socketpair is a Go library that provides bidirectionally connected net.Conns,
net.PacketConns made from socketpair(2) as well as bidirectionally connected
net.TCPConns.

socketpair is currently mostly used in testing Go protocol libraries.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.2%{?dist}
Summary:        Go library that provides bidirectionally connected Conns

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
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Nov  6 2020 Davide Cavalca <dcavalca@fedoraproject.org> - 0-0.1.20201106git05d35a9
- Initial package
