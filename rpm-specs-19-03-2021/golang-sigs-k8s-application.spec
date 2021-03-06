# Generated by go2rpm 1
%bcond_without check

# https://github.com/kubernetes-sigs/application
%global goipath         sigs.k8s.io/application
%global forgeurl        https://github.com/kubernetes-sigs/application
Version:                0.8.3

%gometa

%global common_description %{expand:
Application metadata descriptor CRD.}

%global golicenses      LICENSE LICENSE_TEMPLATE
%global godocs          docs CONTRIBUTING.md README.md code-of-conduct.md

Name:           %{goname}
Release:        2%{?dist}
Summary:        Application metadata descriptor CRD

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/go-logr/logr)
BuildRequires:  golang(github.com/pkg/errors)
BuildRequires:  golang(k8s.io/api/apps/v1)
BuildRequires:  golang(k8s.io/api/batch/v1)
BuildRequires:  golang(k8s.io/api/core/v1)
BuildRequires:  golang(k8s.io/api/policy/v1beta1)
BuildRequires:  golang(k8s.io/apiextensions-apiserver/pkg/apis/apiextensions/v1beta1)
BuildRequires:  golang(k8s.io/apiextensions-apiserver/pkg/client/clientset/clientset)
BuildRequires:  golang(k8s.io/apimachinery/pkg/api/equality)
BuildRequires:  golang(k8s.io/apimachinery/pkg/api/errors)
BuildRequires:  golang(k8s.io/apimachinery/pkg/api/meta)
BuildRequires:  golang(k8s.io/apimachinery/pkg/apis/meta/v1)
BuildRequires:  golang(k8s.io/apimachinery/pkg/apis/meta/v1/unstructured)
BuildRequires:  golang(k8s.io/apimachinery/pkg/runtime)
BuildRequires:  golang(k8s.io/apimachinery/pkg/runtime/schema)
BuildRequires:  golang(k8s.io/apimachinery/pkg/types)
BuildRequires:  golang(k8s.io/apimachinery/pkg/util/errors)
BuildRequires:  golang(k8s.io/apimachinery/pkg/util/json)
BuildRequires:  golang(k8s.io/apimachinery/pkg/util/wait)
BuildRequires:  golang(k8s.io/apimachinery/pkg/util/yaml)
BuildRequires:  golang(k8s.io/client-go/kubernetes/scheme)
BuildRequires:  golang(k8s.io/client-go/plugin/pkg/client/auth/gcp)
BuildRequires:  golang(k8s.io/client-go/util/retry)
BuildRequires:  golang(sigs.k8s.io/controller-runtime)
BuildRequires:  golang(sigs.k8s.io/controller-runtime/pkg/client)
BuildRequires:  golang(sigs.k8s.io/controller-runtime/pkg/log/zap)
BuildRequires:  golang(sigs.k8s.io/controller-runtime/pkg/scheme)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/google/uuid)
BuildRequires:  golang(github.com/onsi/ginkgo)
BuildRequires:  golang(github.com/onsi/gomega)
BuildRequires:  golang(k8s.io/apimachinery/pkg/api/resource)
BuildRequires:  golang(k8s.io/apimachinery/pkg/util/intstr)
BuildRequires:  golang(k8s.io/client-go/rest)
BuildRequires:  golang(sigs.k8s.io/controller-runtime/pkg/controller)
BuildRequires:  golang(sigs.k8s.io/controller-runtime/pkg/envtest)
BuildRequires:  golang(sigs.k8s.io/controller-runtime/pkg/handler)
BuildRequires:  golang(sigs.k8s.io/controller-runtime/pkg/log)
BuildRequires:  golang(sigs.k8s.io/controller-runtime/pkg/manager)
BuildRequires:  golang(sigs.k8s.io/controller-runtime/pkg/reconcile)
BuildRequires:  golang(sigs.k8s.io/controller-runtime/pkg/source)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep

%build
%gobuild -o %{gobuilddir}/bin/application %{goipath}

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
# needs /usr/local/kubebuilder/bin/etcd
%gocheck -d api/v1beta1 -d controllers
%endif

%files
%license LICENSE LICENSE_TEMPLATE
%doc docs CONTRIBUTING.md README.md code-of-conduct.md hack/boilerplate.go.txt
%{_bindir}/*

%gopkgfiles

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 17 10:29:21 CEST 2020 Robert-Andr?? Mauchin <zebob.m@gmail.com> - 0.8.3-1
- Initial package
