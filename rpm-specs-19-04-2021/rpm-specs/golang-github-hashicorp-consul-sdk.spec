# Generated by go2rpm
%bcond_without check

# https://github.com/hashicorp/consul/sdk
%global goipath         github.com/hashicorp/consul
Version:                0.7.0
%global tag             sdk/v0.7.0
%global distprefix      %{nil}

%gometa

%global goname          %{goname}-sdk
%global godevelname     %{goname}-devel

%global common_description %{expand:
Consul is a tool for service discovery and configuration. Consul is distributed,
highly available, and extremely scalable.

Consul provides several key features:
 - Service Discovery - Consul makes it simple for services to register
   themselves and to discover other services via a DNS or HTTP interface.
   External services such as SaaS providers can be registered as well.
 - Health Checking - Health Checking enables Consul to quickly alert operators
   about any issues in a cluster. The integration with service discovery
   prevents routing traffic to unhealthy hosts and enables service level circuit
   breakers.
 - Key/Value Storage - A flexible key/value store enables storing dynamic
   configuration, feature flagging, coordination, leader election and more. The
   simple HTTP API makes it easy to use anywhere.
 - Multi-Datacenter - Consul is built to be datacenter aware, and can support
   any number of regions without complex configuration.
 - Service Segmentation - Consul Connect enables secure service-to-service
   communication with automatic TLS encryption and identity-based
   authorization.}

%global golicenses      LICENSE NOTICE.md
%global godocs          INTERNALS.md README.md CHANGELOG.md README-sdk.md

%global gosupfiles testutil

Name:           %{goname}
Release:        2%{?dist}
Summary:        Solution to connect and configure applications across dynamic, distributed infrastructure

# Upstream license specification: MPL-2.0
License:        MPLv2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/hashicorp/go-cleanhttp)
BuildRequires:  golang(github.com/hashicorp/go-hclog)
BuildRequires:  golang(github.com/hashicorp/go-uuid)
BuildRequires:  golang(github.com/mitchellh/go-testing-interface)
BuildRequires:  golang(github.com/pkg/errors)
BuildRequires:  golang(golang.org/x/sys/unix)

%description
%{common_description}

%gopkg

%prep
%goprep
find ./* -maxdepth 0 -type d -not -name "sdk" -and -not -name "_build" -exec rm -rf "{}" \;
rm -rf ./*.go
mv sdk/README.md README-sdk.md

%install
%gopkginstall

%if %{with check}
%check
%gocheck -d sdk/freeport
%endif

%gopkgfiles

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 18:48:55 CEST 2020 Robert-Andr?? Mauchin <zebob.m@gmail.com> - 0.7.0-1
- Update to 0.7.0
- Close: rhbz#1862398

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Robert-Andr?? Mauchin <zebob.m@gmail.com> - 0.5.0-1
- Update to 0.5.0

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Apr 22 18:15:18 CEST 2019 Robert-Andr?? Mauchin <zebob.m@gmail.com> - 0.1.0-1
- Initial package
