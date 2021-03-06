# Generated by go2rpm
%bcond_without check

# https://github.com/GoogleCloudPlatform/k8s-cloud-provider
%global goipath         github.com/GoogleCloudPlatform/k8s-cloud-provider
Version:                1.13.0
%global tag             1.13.0

%gometa

%global common_description %{expand:
Support code for implementing a Kubernetes cloud provider for Google Cloud
Platform.}

%global golicenses      LICENSE
%global godocs          CONTRIBUTING.md README.md

Name:           %{goname}
Release:        3%{?dist}
Summary:        Support code for implementing a Kubernetes cloud provider for GCP

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(google.golang.org/api/compute/v0.alpha)
BuildRequires:  golang(google.golang.org/api/compute/v0.beta)
BuildRequires:  golang(google.golang.org/api/compute/v1)
BuildRequires:  golang(google.golang.org/api/googleapi)
BuildRequires:  golang(k8s.io/klog/v2)

%if %{with check}
# Tests
BuildRequires:  golang(golang.org/x/oauth2/google)
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
%gocheck
%endif

%gopkgfiles

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 15:16:17 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.13.0-1
- Update to 1.13.0

* Sun Apr 12 20:23:24 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.12.0-1
- Update to 1.12.0

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Aug 04 18:28:41 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.9.0-1
- Release 1.9.0 (#1733766)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 08 20:04:10 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.6.0-1
- Initial package
