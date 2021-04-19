# Generated by go2rpm
%bcond_without check
%bcond_with bootstrap

# https://github.com/uber/jaeger-lib
%global goipath         github.com/uber/jaeger-lib
Version:                2.4.0

%gometa

%global goipaths0       github.com/uber/jaeger-lib
%global goipathsex0     github.com/uber/jaeger-lib/metrics/go-kit github.com/uber/jaeger-lib/client/log/go-kit

%if %{without bootstrap}
%global goipaths1       github.com/uber/jaeger-lib/metrics/go-kit github.com/uber/jaeger-lib/client/log/go-kit
%endif

%global goaltipaths     github.com/jaegertracing/jaeger-lib

%global common_description %{expand:
A collection of shared infrastructure libraries used by different components of
Jaeger backend and jaeger-client-go. This library is not intended to be used
standalone, and provides no guarantees of backwards compatibility.}

%global golicenses      LICENSE
%global godocs          CHANGELOG.md CONTRIBUTING.md README.md

Name:           %{goname}
Release:        2%{?dist}
Summary:        Collection of shared infrastructure libraries used by Jaeger

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

%if %{without bootstrap}
BuildRequires:  golang(github.com/go-kit/kit/log)
BuildRequires:  golang(github.com/go-kit/kit/log/level)
BuildRequires:  golang(github.com/go-kit/kit/metrics)
BuildRequires:  golang(github.com/go-kit/kit/metrics/expvar)
BuildRequires:  golang(github.com/go-kit/kit/metrics/influx)
%endif
BuildRequires:  golang(github.com/HdrHistogram/hdrhistogram-go)
BuildRequires:  golang(github.com/prometheus/client_golang/prometheus)
BuildRequires:  golang(github.com/stretchr/testify/assert)
BuildRequires:  golang(github.com/uber-go/tally)

%if %{with check}
# Tests
%if %{without bootstrap}
BuildRequires:  golang(github.com/go-kit/kit/metrics/generic)
BuildRequires:  golang(github.com/influxdata/influxdb1-client/v2)
%endif
BuildRequires:  golang(github.com/stretchr/testify/require)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep

%install
%gopkginstall

%if %{with check}
%check
%gocheck -t metrics/go-kit -t client/log/go-kit -d metrics/expvar
%endif

%gopkgfiles

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Dec 23 08:49:54 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 2.4.0-1
- Update to 2.4.0
- Close: rhbz#1882234

* Mon Aug 03 20:42:52 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 2.2.0-1
- Update to 2.2.0

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon May 06 15:18:13 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 2.0.0-1
- Initial package
