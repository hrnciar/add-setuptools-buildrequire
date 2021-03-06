# Generated by go2rpm 1.3
%bcond_without check

# https://github.com/google/cel-go
%global goipath         github.com/google/cel-go
Version:                0.7.0

%gometa

%global common_description %{expand:
The Common Expression Language (CEL) is a non-Turing complete language designed
for simplicity, speed, safety, and portability. CEL's C-like syntax looks nearly
identical to equivalent expressions in C++, Go, Java, and TypeScript.}

%global golicenses      LICENSE
%global godocs          examples CODE_OF_CONDUCT.md CONTRIBUTING.md

Name:           %{goname}
Release:        2%{?dist}
Summary:        Fast, portable, non-Turing complete expression evaluation

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/antlr/antlr4/runtime/Go/antlr)
BuildRequires:  golang(github.com/golang/glog)
BuildRequires:  golang(github.com/golang/protobuf/proto)
BuildRequires:  golang(github.com/golang/protobuf/ptypes/any)
BuildRequires:  golang(github.com/golang/protobuf/ptypes/duration)
BuildRequires:  golang(github.com/golang/protobuf/ptypes/struct)
BuildRequires:  golang(github.com/golang/protobuf/ptypes/timestamp)
BuildRequires:  golang(github.com/golang/protobuf/ptypes/wrappers)
BuildRequires:  golang(github.com/google/cel-spec/proto/test/v1/proto2/test_all_types)
BuildRequires:  golang(github.com/google/cel-spec/proto/test/v1/proto3/test_all_types)
BuildRequires:  golang(github.com/google/cel-spec/tools/celrpc)
BuildRequires:  golang(github.com/stoewer/go-strcase)
BuildRequires:  golang(golang.org/x/text/width)
BuildRequires:  golang(google.golang.org/genproto/googleapis/api/expr/conformance/v1alpha1)
BuildRequires:  golang(google.golang.org/genproto/googleapis/api/expr/v1alpha1)
BuildRequires:  golang(google.golang.org/genproto/googleapis/rpc/context/attribute_context)
BuildRequires:  golang(google.golang.org/genproto/googleapis/rpc/status)
BuildRequires:  golang(google.golang.org/grpc/codes)
BuildRequires:  golang(google.golang.org/grpc/status)
BuildRequires:  golang(google.golang.org/protobuf/encoding/protojson)
BuildRequires:  golang(google.golang.org/protobuf/encoding/prototext)
BuildRequires:  golang(google.golang.org/protobuf/proto)
BuildRequires:  golang(google.golang.org/protobuf/reflect/protodesc)
BuildRequires:  golang(google.golang.org/protobuf/reflect/protoreflect)
BuildRequires:  golang(google.golang.org/protobuf/reflect/protoregistry)
BuildRequires:  golang(google.golang.org/protobuf/runtime/protoimpl)
BuildRequires:  golang(google.golang.org/protobuf/types/descriptorpb)
BuildRequires:  golang(google.golang.org/protobuf/types/dynamicpb)
BuildRequires:  golang(google.golang.org/protobuf/types/known/anypb)
BuildRequires:  golang(google.golang.org/protobuf/types/known/durationpb)
BuildRequires:  golang(google.golang.org/protobuf/types/known/emptypb)
BuildRequires:  golang(google.golang.org/protobuf/types/known/structpb)
BuildRequires:  golang(google.golang.org/protobuf/types/known/timestamppb)
BuildRequires:  golang(google.golang.org/protobuf/types/known/wrapperspb)

%description
%{common_description}

%gopkg

%prep
%goprep

%install
%gopkginstall

%if %{with check}
%check
%gocheck -d server
%endif

%gopkgfiles

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 15 21:18:48 CET 2021 Robert-Andr?? Mauchin <zebob.m@gmail.com> - 0.7.0-1
- Update to 0.7.0

* Wed Dec 23 09:21:17 CET 2020 Robert-Andr?? Mauchin <zebob.m@gmail.com> - 0.6.0-1.20201223git4c3317a
- Initial package
