# Generated by go2rpm
%bcond_without check

# https://github.com/kubernetes/cloud-provider
%global goipath         k8s.io/cloud-provider
%global forgeurl        https://github.com/kubernetes/cloud-provider
Version:                1.18.9
%global tag             kubernetes-1.18.9
%global distprefix      %{nil}

%gometa

%global common_description %{expand:
Cloud-provider defines the shared interfaces which Kubernetes cloud providers
implement. These interfaces allow various controllers to integrate with any
cloud provider in a pluggable fashion. Also serves as an issue tracker for SIG
Cloud Provider.}

%global golicenses      LICENSE
%global godocs          README.md code-of-conduct.md CONTRIBUTING.md

Name:           %{goname}
Release:        2%{?dist}
Summary:        Shared interfaces which Kubernetes cloud providers implement

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(k8s.io/api/core/v1)
BuildRequires:  golang(k8s.io/apimachinery/pkg/api/equality)
BuildRequires:  golang(k8s.io/apimachinery/pkg/api/resource)
BuildRequires:  golang(k8s.io/apimachinery/pkg/apis/meta/v1)
BuildRequires:  golang(k8s.io/apimachinery/pkg/types)
BuildRequires:  golang(k8s.io/apimachinery/pkg/util/runtime)
BuildRequires:  golang(k8s.io/apimachinery/pkg/util/sets)
BuildRequires:  golang(k8s.io/apimachinery/pkg/util/strategicpatch)
BuildRequires:  golang(k8s.io/apimachinery/pkg/util/wait)
BuildRequires:  golang(k8s.io/client-go/informers)
BuildRequires:  golang(k8s.io/client-go/kubernetes)
BuildRequires:  golang(k8s.io/client-go/kubernetes/typed/core/v1)
BuildRequires:  golang(k8s.io/client-go/rest)
BuildRequires:  golang(k8s.io/client-go/util/retry)
BuildRequires:  golang(k8s.io/klog/v2)
BuildRequires:  golang(k8s.io/utils/net)

%if %{with check}
# Tests
BuildRequires:  golang(k8s.io/client-go/kubernetes/fake)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep
sed -i 's|k8s.io/klog|k8s.io/klog/v2|' $(find . -name "*.go" -type f)

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Sep 30 12:37:25 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.18.9-1
- Update to 1.18.9

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 04 21:13:24 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.18.3-1
- Update to 1.18.3

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.0-3.beta.0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.0-2.beta.0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jul 07 00:55:48 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.15.0-1
- Release 1.15.0

* Mon May 20 00:43:21 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.13.7-1.beta.0
- Initial package