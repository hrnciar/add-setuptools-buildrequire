# Generated by go2rpm
# Needs network
%bcond_with check

# https://github.com/hashicorp/consul/api
%global goipath         github.com/hashicorp/consul
Version:                1.9.1
%global distprefix      %{nil}

%gometa

%global goname          %{goname}-api
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
%global godocs          INTERNALS.md README.md CHANGELOG.md README-api.md

Name:           %{goname}
Release:        3%{?dist}
Summary:        Solution to connect and configure applications across dynamic, distributed infrastructure

# Upstream license specification: MPL-2.0
License:        MPLv2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/hashicorp/go-cleanhttp)
BuildRequires:  golang(github.com/hashicorp/go-hclog)
BuildRequires:  golang(github.com/hashicorp/go-rootcerts)
BuildRequires:  golang(github.com/hashicorp/serf/coordinate)
BuildRequires:  golang(github.com/mitchellh/mapstructure)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/hashicorp/consul/sdk/testutil)
BuildRequires:  golang(github.com/hashicorp/consul/sdk/testutil/retry)
BuildRequires:  golang(github.com/hashicorp/go-uuid)
BuildRequires:  golang(github.com/hashicorp/serf/coordinate)
BuildRequires:  golang(github.com/hashicorp/serf/serf)
BuildRequires:  golang(github.com/stretchr/testify/assert)
BuildRequires:  golang(github.com/stretchr/testify/require)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep
find ./* -maxdepth 0 -type d -not -name "api" -and -not -name "_build" -exec rm -rf "{}" \;
rm -rf ./*.go
mv api/README.md README-api.md

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Dec 19 13:02:56 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.9.1-2
- Fix error in package name

* Sat Dec 19 13:02:56 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.9.1-1
- Update to 1.9.1
- Close: rhbz#1862397

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.5.0-1
- Update to 1.5.0

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Apr 19 16:57:04 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.0.1-1
- Initial package
