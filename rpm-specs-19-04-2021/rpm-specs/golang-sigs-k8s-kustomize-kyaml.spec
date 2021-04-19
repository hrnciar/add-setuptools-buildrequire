# Generated by go2rpm 1
%bcond_without check

# https://github.com/kubernetes-sigs/kustomize/
%global goipath         sigs.k8s.io/kustomize/kyaml
%global forgeurl        https://github.com/kubernetes-sigs/kustomize
Version:                0.10.6
%global tag             kyaml/v0.10.6
%global distprefix      %{nil}

%gometa

%global common_description %{expand:
Customization of kubernetes YAML configurations.}

%global golicenses      LICENSE_TEMPLATE

Name:           %{goname}
Release:        2%{?dist}
Summary:        Customization of kubernetes YAML configurations

# Upstream license specification: Apache-2.0
License:        ASL 2.0

URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/davecgh/go-spew/spew)
BuildRequires:  golang(github.com/go-errors/errors)
BuildRequires:  golang(github.com/go-openapi/spec)
BuildRequires:  golang(github.com/go-openapi/strfmt)
BuildRequires:  golang(github.com/go-openapi/validate)
BuildRequires:  golang(github.com/google/go-cmp/cmp)
BuildRequires:  golang(github.com/markbates/pkger)
BuildRequires:  golang(github.com/monochromegane/go-gitignore)
BuildRequires:  golang(github.com/qri-io/starlib/util)
BuildRequires:  golang(github.com/sergi/go-diff/diffmatchpatch)
BuildRequires:  golang(github.com/spf13/cobra)
BuildRequires:  golang(github.com/spf13/pflag)
BuildRequires:  golang(github.com/stretchr/testify/assert)
BuildRequires:  golang(github.com/xlab/treeprint)
BuildRequires:  golang(go.starlark.net/starlark)
BuildRequires:  golang(go.starlark.net/starlarkstruct)
BuildRequires:  golang(gopkg.in/yaml.v2)
BuildRequires:  golang(gopkg.in/yaml.v3)

%description
%{common_description}

%gopkg

%prep
%goprep
find . -mindepth 1 -maxdepth 1 -not -wholename './kyaml' -not -wholename './_build' -exec rm -rf {} +
mv kyaml/* ./

%install
%gopkginstall

%if %{with check}
%check
%gocheck -d comments \
         -d fix/fixsetters \
         -d fn/runtime/runtimeutil \
         -d fn/runtime/starlark \
         -d kio \
         -d setters2 \
         -d yaml
%endif

%gopkgfiles

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 23:46:54 CET 2021 Robert-André Mauchin <zebob.m@gmail.com> - 0.10.6-1
- Update to 0.10.6

* Tue Aug 18 04:24:00 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 3.8.1-1
- Initial package
