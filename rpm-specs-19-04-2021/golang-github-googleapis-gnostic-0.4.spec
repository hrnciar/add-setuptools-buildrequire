# Generated by go2rpm 1
%bcond_without check

# https://github.com/googleapis/gnostic
%global goipath         github.com/googleapis/gnostic-0.4
%global forgeurl        https://github.com/googleapis/gnostic
Version:                0.4.2

%gometa

%global goname          golang-github-googleapis-gnostic-0.4
%global godevelname     golang-github-googleapis-gnostic-devel-0.4

%global common_description %{expand:
This package contains a Go command line tool which converts JSON and YAML
OpenAPI descriptions to and from equivalent Protocol Buffer representations.

Protocol Buffers provide a language-neutral, platform-neutral, extensible
mechanism for serializing structured data. gnostic's Protocol Buffer models for
the OpenAPI Specification can be used to generate code that includes data
structures with explicit fields for the elements of an OpenAPI description. This
makes it possible for developers to work with OpenAPI descriptions in type-safe
ways, which is particularly useful in strongly-typed languages like Go and
Swift.

gnostic reads OpenAPI descriptions into these generated data structures, reports
errors, resolves internal dependencies, and writes the results in a binary form
that can be used in any language that is supported by the Protocol Buffer tools.
A plugin interface simplifies integration with API tools written in a variety of
different languages, and when necessary, Protocol Buffer OpenAPI descriptions
can be reexported as JSON or YAML.

gnostic compilation code and OpenAPI Protocol Buffer models are automatically
generated from an OpenAPI JSON Schema. Source code for the generator is in the
generate-gnostic directory.}

%global golicenses      LICENSE
%global godocs          examples CONTRIBUTING.md README.md

Name:           %{goname}
Release:        2%{?dist}
Summary:        Compiler for APIs described by the OpenAPI Specification

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/docopt/docopt-go)
BuildRequires:  golang(github.com/golang/protobuf/jsonpb)
BuildRequires:  golang(github.com/golang/protobuf/proto)
BuildRequires:  golang(github.com/golang/protobuf/ptypes)
BuildRequires:  golang(github.com/golang/protobuf/ptypes/any)
BuildRequires:  golang(google.golang.org/protobuf/reflect/protoreflect)
BuildRequires:  golang(google.golang.org/protobuf/runtime/protoimpl)
BuildRequires:  golang(gopkg.in/yaml.v2)

%if %{with check}
# Tests
BuildRequires:  golang(gopkg.in/check.v1)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep
sed -i 's|github.com/googleapis/gnostic|github.com/googleapis/gnostic-0.4|' $(find . -iname "*.go" -type f)

%install
%gopkginstall

%if %{with check}
%check
%gocheck -d . \
         -d generate-gnostic \
         -d compiler \
         -d extensions \
         -d plugins \
         -d plugins/gnostic-complexity \
         -d plugins/gnostic-vocabulary \
         -d apps/petstore-builder
%endif

%gopkgfiles

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Aug 19 02:13:08 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.4.2-1
- Initial package
