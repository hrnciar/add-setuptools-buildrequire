# Generated by go2rpm
%bcond_without check

# https://github.com/kubernetes/component-base
%global goipath         k8s.io/component-base
%global forgeurl        https://github.com/kubernetes/component-base
Version:                1.18.9
%global tag             kubernetes-1.18.9
%global distprefix      %{nil}

%gometa

%global common_description %{expand:
Shared code for Kubernetes core components.}

%global golicenses      LICENSE
%global godocs          CONTRIBUTING.md code-of-conduct.md README.md

Name:           %{goname}
Release:        2%{?dist}
Summary:        Shared code for Kubernetes core components

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}
# Backport from 1.19, drop wnen packaging it
Patch0:         https://github.com/kubernetes/component-base/commit/d9afff89f5d31dd46bf87ea83816a42b0e31deef.patch#/0001-backport-from-1.19.patch

BuildRequires:  golang(github.com/blang/semver)
BuildRequires:  golang(github.com/google/go-cmp/cmp)
BuildRequires:  golang(github.com/prometheus/client_golang/prometheus)
BuildRequires:  golang(github.com/prometheus/client_golang/prometheus/promhttp)
BuildRequires:  golang(github.com/prometheus/client_golang/prometheus/testutil)
BuildRequires:  golang(github.com/prometheus/client_model/go)
BuildRequires:  golang(github.com/prometheus/common/expfmt)
BuildRequires:  golang(github.com/prometheus/common/model)
BuildRequires:  golang(github.com/prometheus/procfs)
BuildRequires:  golang(github.com/spf13/pflag)
BuildRequires:  golang(k8s.io/apimachinery/pkg/api/apitesting/naming)
BuildRequires:  golang(k8s.io/apimachinery/pkg/api/equality)
BuildRequires:  golang(k8s.io/apimachinery/pkg/apis/meta/v1)
BuildRequires:  golang(k8s.io/apimachinery/pkg/conversion)
BuildRequires:  golang(k8s.io/apimachinery/pkg/runtime)
BuildRequires:  golang(k8s.io/apimachinery/pkg/runtime/schema)
BuildRequires:  golang(k8s.io/apimachinery/pkg/runtime/serializer)
BuildRequires:  golang(k8s.io/apimachinery/pkg/util/errors)
BuildRequires:  golang(k8s.io/apimachinery/pkg/util/naming)
BuildRequires:  golang(k8s.io/apimachinery/pkg/util/sets)
BuildRequires:  golang(k8s.io/apimachinery/pkg/util/validation/field)
BuildRequires:  golang(k8s.io/apimachinery/pkg/util/wait)
BuildRequires:  golang(k8s.io/apimachinery/pkg/version)
BuildRequires:  golang(k8s.io/client-go/tools/leaderelection)
BuildRequires:  golang(k8s.io/client-go/tools/metrics)
BuildRequires:  golang(k8s.io/client-go/util/flowcontrol)
BuildRequires:  golang(k8s.io/client-go/util/workqueue)
BuildRequires:  golang(k8s.io/klog/v2)
BuildRequires:  golang(k8s.io/utils/pointer)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/stretchr/testify/assert)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep
sed -i "s|k8s.io/klog|k8s.io/klog/v2|" $(find . -name "*.go")
%patch0 -p1

%install
%gopkginstall

%if %{with check}
%check
%gocheck -d cli/flag -d cli/globalflag
%endif

%gopkgfiles

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Sep 30 15:30:14 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.18.9-1
- Update to 1.18.9

* Fri Aug 21 23:15:26 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.18.3-3
- Backport logs/logreduction/ from 1.19 for compatibility

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 15 15:32:16 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.18.3-1
- Update to 1.18.3

* Thu Feb 06 00:25:17 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.17.2-1
- Update to 1.17.2

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jul 06 16:44:44 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.15.0-1
- Release 1.15.0

* Mon May 13 14:53:36 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.14.2-1.beta.0
- Initial package
