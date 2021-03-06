# Generated by go2rpm
%bcond_with check

# https://github.com/m3db/prometheus_client_golang
%global goipath         github.com/m3db/prometheus_client_golang
Version:                0.9.0
%global commit          82f5ff156b29e276022b1a958f7d385870fb9814

%gometa

%global common_description %{expand:
This is the Go client library for Prometheus. It has two separate parts, one for
instrumenting application code, and one for creating clients that talk to the
Prometheus HTTP API.}

%global golicenses      LICENSE NOTICE
%global godocs          examples CHANGELOG.md CONTRIBUTING.md\\\
                        MAINTAINERS.md README.md

Name:           %{goname}
Release:        6.pre1%{?dist}
Summary:        Prometheus instrumentation library for Go applications

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/beorn7/perks/quantile)
BuildRequires:  golang(github.com/golang/protobuf/proto)
BuildRequires:  golang(github.com/m3db/prometheus_client_model/go)
BuildRequires:  golang(github.com/prometheus/common/expfmt)
BuildRequires:  golang(github.com/prometheus/common/model)
BuildRequires:  golang(github.com/prometheus/procfs)
BuildRequires:  golang(golang.org/x/net/context)

%description
%{common_description}

%gopkg

%prep
%goprep
find . -name "*.go" -exec sed -i "s|github.com/prometheus/client_golang|github.com/m3db/prometheus_client_golang|" "{}" +;
find . -name "*.go" -exec sed -i "s|github.com/prometheus/client_model|github.com/m3db/prometheus_client_model|" "{}" +;

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-6.pre1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-5.pre1
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-4.pre1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-3.pre1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-2.pre1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon May 06 16:24:01 CEST 2019 Robert-Andr?? Mauchin <zebob.m@gmail.com> - 0.9.0-1.pre1.20190628git82f5ff1
- Initial package
