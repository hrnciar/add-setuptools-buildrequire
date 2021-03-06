# Generated by go2rpm
%bcond_without check

# https://github.com/kubernetes/cli-runtime
%global goipath         k8s.io/cli-runtime
%global forgeurl        https://github.com/kubernetes/cli-runtime
Version:                1.18.9
%global tag             kubernetes-1.18.9
%global distprefix      %{nil}

%gometa

%global common_description %{expand:
Set of helpers for creating kubectl commands, as well as kubectl plugins.}

%global golicenses      LICENSE
%global godocs          README.md code-of-conduct.md CONTRIBUTING.md

Name:           %{goname}
Release:        2%{?dist}
Summary:        Set of helpers for creating kubectl commands and plugins

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/evanphx/json-patch)
BuildRequires:  golang(github.com/googleapis/gnostic-0.4/openapiv2)
BuildRequires:  golang(github.com/liggitt/tabwriter)
BuildRequires:  golang(github.com/pkg/errors)
BuildRequires:  golang(github.com/spf13/cobra)
BuildRequires:  golang(github.com/spf13/pflag)
BuildRequires:  golang(golang.org/x/text/encoding/unicode)
BuildRequires:  golang(golang.org/x/text/transform)
BuildRequires:  golang(gopkg.in/yaml.v2)
BuildRequires:  golang(k8s.io/api/core/v1)
BuildRequires:  golang(k8s.io/apimachinery/pkg/api/errors)
BuildRequires:  golang(k8s.io/apimachinery/pkg/api/meta)
BuildRequires:  golang(k8s.io/apimachinery/pkg/api/validation)
BuildRequires:  golang(k8s.io/apimachinery/pkg/apis/meta/v1)
BuildRequires:  golang(k8s.io/apimachinery/pkg/apis/meta/v1/unstructured)
BuildRequires:  golang(k8s.io/apimachinery/pkg/apis/meta/v1/unstructured/unstructuredscheme)
BuildRequires:  golang(k8s.io/apimachinery/pkg/apis/meta/v1/validation)
BuildRequires:  golang(k8s.io/apimachinery/pkg/fields)
BuildRequires:  golang(k8s.io/apimachinery/pkg/labels)
BuildRequires:  golang(k8s.io/apimachinery/pkg/runtime)
BuildRequires:  golang(k8s.io/apimachinery/pkg/runtime/schema)
BuildRequires:  golang(k8s.io/apimachinery/pkg/runtime/serializer)
BuildRequires:  golang(k8s.io/apimachinery/pkg/runtime/serializer/json)
BuildRequires:  golang(k8s.io/apimachinery/pkg/types)
BuildRequires:  golang(k8s.io/apimachinery/pkg/util/duration)
BuildRequires:  golang(k8s.io/apimachinery/pkg/util/errors)
BuildRequires:  golang(k8s.io/apimachinery/pkg/util/json)
BuildRequires:  golang(k8s.io/apimachinery/pkg/util/mergepatch)
BuildRequires:  golang(k8s.io/apimachinery/pkg/util/sets)
BuildRequires:  golang(k8s.io/apimachinery/pkg/util/strategicpatch)
BuildRequires:  golang(k8s.io/apimachinery/pkg/util/validation)
BuildRequires:  golang(k8s.io/apimachinery/pkg/util/validation/field)
BuildRequires:  golang(k8s.io/apimachinery/pkg/util/yaml)
BuildRequires:  golang(k8s.io/apimachinery/pkg/watch)
BuildRequires:  golang(k8s.io/client-go/discovery)
BuildRequires:  golang(k8s.io/client-go/discovery/cached/disk)
BuildRequires:  golang(k8s.io/client-go/dynamic)
BuildRequires:  golang(k8s.io/client-go/kubernetes/scheme)
BuildRequires:  golang(k8s.io/client-go/rest)
BuildRequires:  golang(k8s.io/client-go/restmapper)
BuildRequires:  golang(k8s.io/client-go/tools/clientcmd)
BuildRequires:  golang(k8s.io/client-go/tools/clientcmd/api)
BuildRequires:  golang(k8s.io/client-go/util/homedir)
BuildRequires:  golang(k8s.io/client-go/util/jsonpath)
BuildRequires:  golang(sigs.k8s.io/kustomize/pkg/commands/build)
BuildRequires:  golang(sigs.k8s.io/kustomize/pkg/factory)
BuildRequires:  golang(sigs.k8s.io/kustomize/pkg/fs)
BuildRequires:  golang(sigs.k8s.io/kustomize/pkg/gvk)
BuildRequires:  golang(sigs.k8s.io/kustomize/pkg/ifc)
BuildRequires:  golang(sigs.k8s.io/kustomize/pkg/resmap)
BuildRequires:  golang(sigs.k8s.io/kustomize/pkg/resource)
BuildRequires:  golang(sigs.k8s.io/kustomize/pkg/transformers)
BuildRequires:  golang(sigs.k8s.io/kustomize/pkg/types)
BuildRequires:  golang(sigs.k8s.io/yaml)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/davecgh/go-spew/spew)
BuildRequires:  golang(github.com/stretchr/testify/assert)
BuildRequires:  golang(k8s.io/apimachinery/pkg/api/equality)
BuildRequires:  golang(k8s.io/apimachinery/pkg/api/meta/testrestmapper)
BuildRequires:  golang(k8s.io/apimachinery/pkg/api/resource)
BuildRequires:  golang(k8s.io/apimachinery/pkg/runtime/serializer/streaming)
BuildRequires:  golang(k8s.io/apimachinery/pkg/util/diff)
BuildRequires:  golang(k8s.io/client-go/rest/fake)
BuildRequires:  golang(k8s.io/client-go/rest/watch)
BuildRequires:  golang(k8s.io/client-go/util/testing)
BuildRequires:  golang(k8s.io/kube-openapi/pkg/util/proto/testing)
BuildRequires:  golang(sigs.k8s.io/kustomize/pkg/loader)
BuildRequires:  golang(sigs.k8s.io/kustomize/pkg/resid)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep
sed -i "s|github.com/googleapis/gnostic/OpenAPIv2|github.com/googleapis/gnostic/openapiv2|" $(find . -type f -iname "*.go")
sed -i 's|github.com/googleapis/gnostic|github.com/googleapis/gnostic-0.4|' $(find . -iname "*.go" -type f)

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

* Wed Sep 30 02:57:22 CEST 2020 Robert-Andr?? Mauchin <zebob.m@gmail.com> - 1.18.9-1
- Update to 1.18.9

* Wed Aug 19 17:56:57 CEST 2020 Robert-Andr?? Mauchin <zebob.m@gmail.com> - 1.18.3-5
- Use gnostic compat package

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 04 19:54:44 CEST 2020 Robert-Andr?? Mauchin <zebob.m@gmail.com> - 1.18.3-1
- Update to 1.18.3

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jul 07 00:55:48 CEST 2019 Robert-Andr?? Mauchin <zebob.m@gmail.com> - 1.15.0-1
- Release 1.15.0

* Mon May 20 00:14:15 CEST 2019 Robert-Andr?? Mauchin <zebob.m@gmail.com> - 1.13.7-1.beta.0
- Initial package
