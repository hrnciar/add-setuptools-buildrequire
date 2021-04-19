# Generated by go2rpm
%bcond_without check

# https://github.com/grpc-ecosystem/go-grpc-middleware
%global goipath         github.com/grpc-ecosystem/go-grpc-middleware
Version:                1.2.2

%gometa

%global common_description %{expand:
gRPC Go recently acquired support for Interceptors, i.e. middleware that is
executed either on the gRPC Server before the request is passed onto the user's
application logic, or on the gRPC client either around the user call. It is a
perfect way to implement common patterns: auth, logging, message, validation,
retries or monitoring.

These are generic building blocks that make it easy to build multiple
microservices easily. The purpose of this repository is to act as a go-to point
for such reusable functionality. It contains some of them itself, but also will
link to useful external repos.}

%global golicenses      LICENSE
%global godocs          CONTRIBUTING.md DOC.md README.md

Name:           %{goname}
Release:        2%{?dist}
Summary:        Golang gRPC Middlewares: interceptor chaining, auth, logging, retries and more
# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/go-kit/kit/log)
BuildRequires:  golang(github.com/go-kit/kit/log/level)
BuildRequires:  golang(github.com/gogo/protobuf/gogoproto)
BuildRequires:  golang(github.com/golang/protobuf/jsonpb)
BuildRequires:  golang(github.com/golang/protobuf/proto)
BuildRequires:  golang(github.com/golang/protobuf/ptypes/timestamp)
BuildRequires:  golang(github.com/opentracing/opentracing-go)
BuildRequires:  golang(github.com/opentracing/opentracing-go/ext)
BuildRequires:  golang(github.com/opentracing/opentracing-go/log)
BuildRequires:  golang(github.com/sirupsen/logrus)
BuildRequires:  golang(github.com/stretchr/testify/require)
BuildRequires:  golang(github.com/stretchr/testify/suite)
BuildRequires:  golang(go.uber.org/zap)
BuildRequires:  golang(go.uber.org/zap/zapcore)
BuildRequires:  golang(golang.org/x/net/trace)
BuildRequires:  golang(google.golang.org/grpc)
BuildRequires:  golang(google.golang.org/grpc/codes)
BuildRequires:  golang(google.golang.org/grpc/credentials)
BuildRequires:  golang(google.golang.org/grpc/grpclog)
BuildRequires:  golang(google.golang.org/grpc/metadata)
BuildRequires:  golang(google.golang.org/grpc/peer)
BuildRequires:  golang(google.golang.org/grpc/status)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/stretchr/testify/assert)
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
%gocheck -d auth -t logging
%endif

%gopkgfiles

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 17 15:48:18 CET 2021 Robert-André Mauchin <zebob.m@gmail.com> - 1.2.2-1
- Update to 1.2.2

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 17:55:55 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.2.0-1
- Update to 1.2.0

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Apr 26 21:06:10 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.0.0-2
- Update to new macros

* Thu Mar 14 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.0.0-1
- First package for Fedora
