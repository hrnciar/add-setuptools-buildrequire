# Generated by go2rpm
%ifnarch %{ix86} %{arm} s390x
%bcond_without check
%endif
%bcond_with bootstrap

# https://github.com/google/certificate-transparency-go
%global goipath         github.com/google/certificate-transparency-go
Version:                1.1.1

%gometa

%global goipaths0       github.com/google/certificate-transparency-go
%global goipathsex0     github.com/google/certificate-transparency-go/trillian github.com/google/certificate-transparency-go/submission github.com/google/certificate-transparency-go/ctutil github.com/google/certificate-transparency-go/scanner github.com/google/certificate-transparency-go/client/ctclient

%if %{without bootstrap}
%global goipaths1       github.com/google/certificate-transparency-go/trillian github.com/google/certificate-transparency-go/submission github.com/google/certificate-transparency-go/ctutil github.com/google/certificate-transparency-go/scanner github.com/google/certificate-transparency-go/client/ctclient
%endif

%global common_description %{expand:
Package Ct holds core types and utilities for Certificate Transparency.}

%global golicenses      LICENSE
%global godocs          AUTHORS CONTRIBUTING.md CHANGELOG.md CONTRIBUTORS\\\
                        README.md examples

Name:           %{goname}
Release:        2%{?dist}
Summary:        Auditing for TLS certificates, Go code

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/golang/glog)
BuildRequires:  golang(github.com/golang/mock/gomock)
BuildRequires:  golang(github.com/golang/protobuf/proto)
BuildRequires:  golang(github.com/golang/protobuf/ptypes)
BuildRequires:  golang(github.com/golang/protobuf/ptypes/any)
BuildRequires:  golang(github.com/golang/protobuf/ptypes/timestamp)
%if %{without bootstrap}
BuildRequires:  golang(github.com/google/trillian)
BuildRequires:  golang(github.com/google/trillian/client)
BuildRequires:  golang(github.com/google/trillian/client/backoff)
BuildRequires:  golang(github.com/google/trillian/crypto)
BuildRequires:  golang(github.com/google/trillian/crypto/keys)
BuildRequires:  golang(github.com/google/trillian/crypto/keys/der)
BuildRequires:  golang(github.com/google/trillian/crypto/keys/der/proto)
BuildRequires:  golang(github.com/google/trillian/crypto/keys/pem)
BuildRequires:  golang(github.com/google/trillian/crypto/keys/pem/proto)
BuildRequires:  golang(github.com/google/trillian/crypto/keys/pkcs11/proto)
BuildRequires:  golang(github.com/google/trillian/crypto/keyspb)
BuildRequires:  golang(github.com/google/trillian/merkle)
BuildRequires:  golang(github.com/google/trillian/merkle/rfc6962)
BuildRequires:  golang(github.com/google/trillian/monitoring)
BuildRequires:  golang(github.com/google/trillian/monitoring/opencensus)
BuildRequires:  golang(github.com/google/trillian/monitoring/prometheus)
BuildRequires:  golang(github.com/google/trillian/storage/testonly)
BuildRequires:  golang(github.com/google/trillian/testonly/integration)
BuildRequires:  golang(github.com/google/trillian/types)
BuildRequires:  golang(github.com/google/trillian/util)
BuildRequires:  golang(github.com/google/trillian/util/clock)
BuildRequires:  golang(github.com/google/trillian/util/election2)
BuildRequires:  golang(github.com/google/trillian/util/election2/etcd)
BuildRequires:  golang(github.com/google/trillian/util/etcd)
%endif
BuildRequires:  golang(github.com/juju/ratelimit)
BuildRequires:  golang(github.com/kylelemons/godebug/pretty)
BuildRequires:  golang(github.com/prometheus/client_golang/prometheus/promhttp)
BuildRequires:  golang(github.com/rs/cors)
BuildRequires:  golang(github.com/sergi/go-diff/diffmatchpatch)
BuildRequires:  golang(github.com/tomasen/realip)
BuildRequires:  golang(go.etcd.io/etcd/clientv3)
BuildRequires:  golang(go.etcd.io/etcd/clientv3/naming)
BuildRequires:  golang(golang.org/x/crypto/cryptobyte)
BuildRequires:  golang(golang.org/x/crypto/cryptobyte/asn1)
BuildRequires:  golang(golang.org/x/crypto/ed25519)
BuildRequires:  golang(golang.org/x/net/context/ctxhttp)
BuildRequires:  golang(google.golang.org/genproto/protobuf/field_mask)
BuildRequires:  golang(google.golang.org/grpc)
BuildRequires:  golang(google.golang.org/grpc/balancer/roundrobin)
BuildRequires:  golang(google.golang.org/grpc/codes)
# BuildRequires:  golang(google.golang.org/grpc/naming)
BuildRequires:  golang(google.golang.org/grpc/resolver)
BuildRequires:  golang(google.golang.org/grpc/resolver/manual)
BuildRequires:  golang(google.golang.org/grpc/status)
BuildRequires:  golang(google.golang.org/protobuf/encoding/prototext)
BuildRequires:  golang(google.golang.org/protobuf/proto)
BuildRequires:  golang(google.golang.org/protobuf/reflect/protoreflect)
BuildRequires:  golang(google.golang.org/protobuf/runtime/protoimpl)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/google/go-cmp/cmp)
BuildRequires:  golang(github.com/google/go-cmp/cmp/cmpopts)
%if %{without bootstrap}
BuildRequires:  golang(github.com/google/trillian/crypto/keys/testonly)
BuildRequires:  golang(github.com/google/trillian/storage/testdb)
%endif
BuildRequires:  golang(github.com/mohae/deepcopy)
BuildRequires:  golang(google.golang.org/protobuf/types/known/anypb)
BuildRequires:  golang(google.golang.org/protobuf/types/known/timestamppb)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep
# Needs google.golang.org/grpc/naming, which has been deleted in latest version
rm -rf trillian/ctfe/ct_server

%install
%gopkginstall

%if %{without bootstrap}
%if %{with check}
%check
%gocheck
%endif
%endif

%gopkgfiles

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Dec 19 00:36:22 CET 2020 Robert-Andr?? Mauchin <zebob.m@gmail.com> - 1.1.1-1
- Update to 1.1.1
- Close: rhbz#1772690

* Mon Aug 10 01:20:11 CEST 2020 Robert-Andr?? Mauchin <zebob.m@gmail.com> - 1.1.0-1.20200810gitf292cdd
- Update to 1.1.0, commit f292cdd7af64abdc38183b65000a8530ce043910

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.21-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.21-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.21-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 07 00:09:15 CEST 2019 Robert-Andr?? Mauchin <zebob.m@gmail.com> - 1.0.21-1
- Initial package
