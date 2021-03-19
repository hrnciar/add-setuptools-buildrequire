# Generated by go2rpm
%bcond_without check
%global golang_arches x86_64 aarch64 ppc64le s390x

# https://github.com/vitessio/vitess
%global goipath         vitess.io/vitess
%global forgeurl        https://github.com/vitessio/vitess
Version:                8.0.0

%gometa

%global common_description %{expand:
Vitess is a database clustering system for horizontal scaling of MySQL through
generalized sharding.

By encapsulating shard-routing logic, Vitess allows application code and
database queries to remain agnostic to the distribution of data onto multiple
shards. With Vitess, you can even split and merge shards as your needs grow,
with an atomic cutover step that takes only a few seconds.}

%global golicenses      LICENSE
%global godocs          CODE_OF_CONDUCT.md GOVERNANCE.md\\\
                        GUIDING_PRINCIPLES.md ADOPTERS.md CONTRIBUTING.md\\\
                        README.md README-go.md

Name:           %{goname}
Release:        2%{?dist}
Summary:        Database clustering system for horizontal scaling of MySQL

# Upstream license specification: MIT and Apache-2.0
License:        MIT and ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}
# To use with newer k8s
Patch0:         0001-Add-context-to-k8s-calls.patch
# To use with newer azure-storage-blob
Patch1:         0001-Fix-for-newer-azure-storage-blob.patch
# Fix unit test error
Patch2:         https://github.com/vitessio/vitess/commit/08038850a258d6de250cf9d864d6118616f5562c.patch#/0001-Fix-unit-test-error.patch

BuildRequires:  golang(cloud.google.com/go/storage)
BuildRequires:  golang(github.com/armon/consul-api)
BuildRequires:  golang(github.com/armon/go-metrics)
BuildRequires:  golang(github.com/aws/aws-sdk-go/aws)
BuildRequires:  golang(github.com/aws/aws-sdk-go/aws/awserr)
BuildRequires:  golang(github.com/aws/aws-sdk-go/aws/client)
BuildRequires:  golang(github.com/aws/aws-sdk-go/aws/request)
BuildRequires:  golang(github.com/aws/aws-sdk-go/aws/session)
BuildRequires:  golang(github.com/aws/aws-sdk-go/service/s3)
BuildRequires:  golang(github.com/aws/aws-sdk-go/service/s3/s3iface)
BuildRequires:  golang(github.com/aws/aws-sdk-go/service/s3/s3manager)
BuildRequires:  golang(github.com/Azure/azure-storage-blob-go/azblob)
BuildRequires:  golang(github.com/buger/jsonparser)
BuildRequires:  golang(github.com/cespare/xxhash/v2)
BuildRequires:  golang(github.com/cyberdelia/go-metrics-graphite)
BuildRequires:  golang(github.com/evanphx/json-patch)
BuildRequires:  golang(github.com/GeertJohan/go.rice)
BuildRequires:  golang(github.com/GeertJohan/go.rice/embedded)
BuildRequires:  golang(github.com/go-martini/martini)
BuildRequires:  golang(github.com/go-sql-driver/mysql)
BuildRequires:  golang(github.com/golang/glog)
BuildRequires:  golang(github.com/golang/protobuf/jsonpb)
BuildRequires:  golang(github.com/golang/protobuf/proto)
BuildRequires:  golang(github.com/golang/snappy)
BuildRequires:  golang(github.com/google/go-cmp/cmp)
BuildRequires:  golang(github.com/google/shlex)
BuildRequires:  golang(github.com/google/uuid)
BuildRequires:  golang(github.com/gorilla/websocket)
BuildRequires:  golang(github.com/grpc-ecosystem/go-grpc-middleware)
BuildRequires:  golang(github.com/grpc-ecosystem/go-grpc-prometheus)
BuildRequires:  golang(github.com/hashicorp/consul/api)
BuildRequires:  golang(github.com/hashicorp/go-msgpack/codec)
BuildRequires:  golang(github.com/howeyc/gopass)
BuildRequires:  golang(github.com/klauspost/pgzip)
BuildRequires:  golang(github.com/krishicks/yaml-patch)
BuildRequires:  golang(github.com/martini-contrib/auth)
BuildRequires:  golang(github.com/martini-contrib/gzip)
BuildRequires:  golang(github.com/martini-contrib/render)
BuildRequires:  golang(github.com/mattn/go-sqlite3)
BuildRequires:  golang(github.com/minio/minio-go/v6)
BuildRequires:  golang(github.com/montanaflynn/stats)
BuildRequires:  golang(github.com/olekukonko/tablewriter)
BuildRequires:  golang(github.com/opentracing-contrib/go-grpc)
BuildRequires:  golang(github.com/opentracing/opentracing-go)
BuildRequires:  golang(github.com/patrickmn/go-cache)
BuildRequires:  golang(github.com/pborman/uuid)
BuildRequires:  golang(github.com/pires/go-proxyproto)
BuildRequires:  golang(github.com/pkg/errors)
BuildRequires:  golang(github.com/prometheus/client_golang/prometheus)
BuildRequires:  golang(github.com/prometheus/client_golang/prometheus/promauto)
BuildRequires:  golang(github.com/prometheus/client_golang/prometheus/promhttp)
BuildRequires:  golang(github.com/prometheus/common/log)
BuildRequires:  golang(github.com/PuerkitoBio/goquery)
BuildRequires:  golang(github.com/rcrowley/go-metrics)
BuildRequires:  golang(github.com/rcrowley/go-metrics/exp)
BuildRequires:  golang(github.com/samuel/go-zookeeper/zk)
BuildRequires:  golang(github.com/sirupsen/logrus)
BuildRequires:  golang(github.com/sjmudd/stopwatch)
BuildRequires:  golang(github.com/stretchr/testify/assert)
BuildRequires:  golang(github.com/stretchr/testify/require)
BuildRequires:  golang(github.com/tchap/go-patricia/patricia)
BuildRequires:  golang(github.com/uber/jaeger-client-go)
BuildRequires:  golang(github.com/uber/jaeger-client-go/config)
BuildRequires:  golang(github.com/z-division/go-zookeeper/zk)
BuildRequires:  golang(go.etcd.io/etcd/clientv3)
BuildRequires:  golang(go.etcd.io/etcd/etcdserver/api/v3rpc/rpctypes)
BuildRequires:  golang(go.etcd.io/etcd/mvcc/mvccpb)
BuildRequires:  golang(go.etcd.io/etcd/pkg/transport)
BuildRequires:  golang(go.uber.org/ratelimit)
BuildRequires:  golang(golang.org/x/crypto/ssh/terminal)
BuildRequires:  golang(golang.org/x/net/context)
BuildRequires:  golang(golang.org/x/oauth2/google)
BuildRequires:  golang(golang.org/x/sync/errgroup)
BuildRequires:  golang(golang.org/x/text/collate)
BuildRequires:  golang(golang.org/x/text/language)
BuildRequires:  golang(golang.org/x/time/rate)
BuildRequires:  golang(google.golang.org/api/iterator)
BuildRequires:  golang(google.golang.org/api/option)
BuildRequires:  golang(google.golang.org/grpc)
BuildRequires:  golang(google.golang.org/grpc/codes)
BuildRequires:  golang(google.golang.org/grpc/credentials)
BuildRequires:  golang(google.golang.org/grpc/encoding)
BuildRequires:  golang(google.golang.org/grpc/grpclog)
BuildRequires:  golang(google.golang.org/grpc/keepalive)
BuildRequires:  golang(google.golang.org/grpc/metadata)
BuildRequires:  golang(google.golang.org/grpc/peer)
BuildRequires:  golang(google.golang.org/grpc/status)
# needed by go/trace/plugin_datadog.go
# BuildRequires:  golang(gopkg.in/DataDog/dd-trace-go.v1/ddtrace/opentracer)
# BuildRequires:  golang(gopkg.in/DataDog/dd-trace-go.v1/ddtrace/tracer)
BuildRequires:  golang(gopkg.in/gcfg.v1)
BuildRequires:  golang(gopkg.in/ldap.v2)
BuildRequires:  golang(gopkg.in/yaml.v2)
BuildRequires:  golang(k8s.io/apimachinery/pkg/api/errors)
BuildRequires:  golang(k8s.io/apimachinery/pkg/apis/meta/v1)
BuildRequires:  golang(k8s.io/apimachinery/pkg/fields)
BuildRequires:  golang(k8s.io/apimachinery/pkg/labels)
BuildRequires:  golang(k8s.io/apimachinery/pkg/runtime)
BuildRequires:  golang(k8s.io/apimachinery/pkg/runtime/schema)
BuildRequires:  golang(k8s.io/apimachinery/pkg/runtime/serializer)
BuildRequires:  golang(k8s.io/apimachinery/pkg/types)
BuildRequires:  golang(k8s.io/apimachinery/pkg/util/runtime)
BuildRequires:  golang(k8s.io/apimachinery/pkg/util/sets)
BuildRequires:  golang(k8s.io/apimachinery/pkg/watch)
BuildRequires:  golang(k8s.io/client-go/discovery)
BuildRequires:  golang(k8s.io/client-go/discovery/fake)
BuildRequires:  golang(k8s.io/client-go/kubernetes)
BuildRequires:  golang(k8s.io/client-go/rest)
BuildRequires:  golang(k8s.io/client-go/testing)
BuildRequires:  golang(k8s.io/client-go/tools/cache)
BuildRequires:  golang(k8s.io/client-go/tools/clientcmd)
BuildRequires:  golang(k8s.io/client-go/util/flowcontrol)
BuildRequires:  golang(k8s.io/client-go/util/retry)
BuildRequires:  golang(k8s.io/utils/pointer)
BuildRequires:  golang(sigs.k8s.io/yaml)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/golang/mock/gomock)
BuildRequires:  golang(github.com/magiconair/properties/assert)
BuildRequires:  golang(gotest.tools/v3/assert)
BuildRequires:  golang(k8s.io/apiextensions-apiserver/pkg/apis/apiextensions/v1beta1)
BuildRequires:  golang(k8s.io/apiextensions-apiserver/pkg/client/clientset/clientset)
BuildRequires:  golang(k8s.io/apimachinery/pkg/util/yaml)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep
%patch0 -p1
%patch1 -p1
%patch2 -p1
sed -i "s|github.com/coreos/etcd|go.etcd.io/etcd|" $(find . -iname "*.go" -type f)
sed -i "s|gotest.tools|gotest.tools/v3|" $(find . -iname "*.go" -type f)
sed -i "s|github.com/minio/minio-go|github.com/minio/minio-go/v6|" $(find . -iname "*.go" -type f)
rm -rf go/trace/plugin_datadog.go
mv go/README.md README-go.md

%build
for cmd in $(find go/cmd/* -maxdepth 0 -type d); do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
%gocheck -t go/cmd \
         -d go/mysql \
         -d go/mysql/endtoend \
         -d go/sqltypes \
         -d go/vt/hook \
         -d go/vt/mysqlctl \
         -d go/vt/srvtopo \
         -t go/vt/topo \
         -d go/vt/vtctld \
         -d go/vt/vtgate/evalengine \
         -d go/vt/vtqueryserver \
         -d go/vt/vttablet/endtoend \
         -t go/vt/vttablet/tabletmanager \
         -t go/vt/vttablet/tabletserver \
         -t go/vt/vttablet/worker \
         -d go/vt/withddl \
         -t go/vt/worker \
         -d go/vt/workflow/reshardingworkflowgen \
         -d go/vt/wrangler \
         -d go/vt/wrangler/testlib \
         -d go/vt/zkctl \
         -d go/json2 \
         -t go/test/endtoend
%endif

%files
%license LICENSE
%doc CODE_OF_CONDUCT.md GOVERNANCE.md GUIDING_PRINCIPLES.md
%doc ADOPTERS.md CONTRIBUTING.md README.md README-go.md
%{_bindir}/*

%gopkgfiles

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Dec 26 13:28:45 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 8.0.0-1
- Update to 8.0.0
- Close: rhbz#1742264

* Thu Oct 01 11:57:17 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 7.0.2-1
- Update to 7.0.2

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.1-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Apr 08 2020 Robert-André Mauchin <zebob.m@gmail.com> - 5.0.1-1
- Update to 5.0.1

* Mon Feb 17 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 3.0-4
- Rebuilt for GHSA-jf24-p9p9-4rjh

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 16 00:30:49 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 3.0-1.20190701git948c251
- Initial package
