# Generated by go2rpm
%ifnarch %{ix86} %{arm}
%bcond_without check
%endif

# https://github.com/uber-go/tally
%global goipath         github.com/uber-go/tally
Version:                3.3.17

%gometa

%global common_description %{expand:
Tally provides a common interface for emitting metrics, while letting you not
worry about the velocity of metrics emission.

By default it buffers counters, gauges and histograms at a specified interval
but does not buffer timer values. This is primarily so timer values can have all
their values sampled if desired and if not they can be sampled as summaries or
histograms independently by a reporter.}

%global golicenses      LICENSE
%global godocs          example README.md example

Name:           %{goname}
Release:        2%{?dist}
Summary:        Go metrics interface with fast buffered metrics and third party reporters

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/cactus/go-statsd-client/statsd)
BuildRequires:  golang(github.com/m3db/prometheus_client_golang/prometheus)
BuildRequires:  golang(github.com/m3db/prometheus_client_golang/prometheus/promhttp)
BuildRequires:  golang(github.com/pkg/errors)
BuildRequires:  golang(go.uber.org/atomic)
BuildRequires:  golang(gopkg.in/validator.v2)
BuildRequires:  golang(gopkg.in/yaml.v2)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/m3db/prometheus_client_model/go)
BuildRequires:  golang(github.com/stretchr/testify/assert)
BuildRequires:  golang(github.com/stretchr/testify/require)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep
rm -rf thirdparty
# https://github.com/uber-go/tally/issues/78
sed -i "s|github.com/m3db/prometheus_client_model/prometheus|github.com/m3db/prometheus_client_golang/prometheus|" $(find . -iname "*.go" -type f)

%install
%gopkginstall

%if %{with check}
%check
%gocheck -t m3 -t prometheus
%endif

%gopkgfiles

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 03 21:16:42 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 3.3.17-1
- Update to 3.3.17

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon May 06 15:39:53 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 3.3.8-1
- Initial package
