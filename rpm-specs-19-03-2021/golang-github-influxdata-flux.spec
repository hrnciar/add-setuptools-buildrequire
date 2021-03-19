# Generated by go2rpm
# Need main flux library
%bcond_with check

# https://github.com/influxdata/flux
%global goipath         github.com/influxdata/flux
Version:                0.100.1

%gometa

%global common_description %{expand:
Flux is a lightweight scripting language for querying databases (like influxdb)
and working with data. it's part of influxdb 1.7 and 2.0, but can be run
independently of those.}

%global golicenses      LICENSE
%global godocs          docs examples CONTRIBUTING.md README.md

%global gosupfiles      "${flux[@]}" stdlib/testing/testdata/* stdlib/pandas_tests/testdata/* stdlib/strings/testdata/*

Name:           %{goname}
Release:        2%{?dist}
Summary:        Lightweight scripting language for querying databases

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(cloud.google.com/go/bigtable)
BuildRequires:  golang(cloud.google.com/go/civil)
BuildRequires:  golang(github.com/andreyvit/diff)
BuildRequires:  golang(github.com/apache/arrow/go/arrow)
BuildRequires:  golang(github.com/apache/arrow/go/arrow/array)
BuildRequires:  golang(github.com/apache/arrow/go/arrow/bitutil)
BuildRequires:  golang(github.com/apache/arrow/go/arrow/math)
BuildRequires:  golang(github.com/apache/arrow/go/arrow/memory)
BuildRequires:  golang(github.com/Azure/go-autorest/autorest/adal)
BuildRequires:  golang(github.com/Azure/go-autorest/autorest/azure)
BuildRequires:  golang(github.com/Azure/go-autorest/autorest/azure/auth)
BuildRequires:  golang(github.com/benbjohnson/immutable)
# BuildRequires:  golang(github.com/benbjohnson/tmpl)
BuildRequires:  golang(github.com/bonitoo-io/go-sql-bigquery)
BuildRequires:  golang(github.com/c-bata/go-prompt)
BuildRequires:  golang(github.com/cespare/xxhash)
BuildRequires:  golang(github.com/dave/jennifer/jen)
BuildRequires:  golang(github.com/denisenkom/go-mssqldb)
BuildRequires:  golang(github.com/eclipse/paho.mqtt.golang)
BuildRequires:  golang(github.com/go-sql-driver/mysql)
BuildRequires:  golang(github.com/gofrs/uuid)
BuildRequires:  golang(github.com/golang/geo/r1)
BuildRequires:  golang(github.com/golang/geo/s1)
BuildRequires:  golang(github.com/golang/geo/s2)
BuildRequires:  golang(github.com/google/flatbuffers/go)
BuildRequires:  golang(github.com/google/go-cmp/cmp)
BuildRequires:  golang(github.com/google/go-cmp/cmp/cmpopts)
# BuildRequires:  golang(github.com/goreleaser/goreleaser)
# BuildRequires:  golang(github.com/influxdata/changelog)
BuildRequires:  golang(github.com/influxdata/line-protocol)
BuildRequires:  golang(github.com/influxdata/promql/v2)
BuildRequires:  golang(github.com/influxdata/promql/v2/pkg/labels)
BuildRequires:  golang(github.com/influxdata/tdigest)
BuildRequires:  golang(github.com/lib/pq)
BuildRequires:  golang(github.com/mattn/go-sqlite3)
BuildRequires:  golang(github.com/matttproud/golang_protobuf_extensions/pbutil)
BuildRequires:  golang(github.com/opentracing/opentracing-go)
BuildRequires:  golang(github.com/opentracing/opentracing-go/log)
BuildRequires:  golang(github.com/pkg/errors)
BuildRequires:  golang(github.com/prometheus/client_model/go)
BuildRequires:  golang(github.com/prometheus/common/expfmt)
BuildRequires:  golang(github.com/prometheus/common/model)
BuildRequires:  golang(github.com/SAP/go-hdb/driver)
BuildRequires:  golang(github.com/segmentio/kafka-go)
BuildRequires:  golang(github.com/snowflakedb/gosnowflake)
BuildRequires:  golang(github.com/spf13/cobra)
BuildRequires:  golang(github.com/uber/athenadriver/go)
BuildRequires:  golang(go.uber.org/zap)
BuildRequires:  golang(go.uber.org/zap/zapcore)
BuildRequires:  golang(go.uber.org/zap/zaptest)
BuildRequires:  golang(golang.org/x/net/context)
BuildRequires:  golang(golang.org/x/tools/go/callgraph)
BuildRequires:  golang(golang.org/x/tools/go/callgraph/rta)
BuildRequires:  golang(golang.org/x/tools/go/packages)
BuildRequires:  golang(golang.org/x/tools/go/ssa)
BuildRequires:  golang(golang.org/x/tools/go/ssa/ssautil)
BuildRequires:  golang(gonum.org/v1/gonum/floats)
BuildRequires:  golang(google.golang.org/api/option)
# BuildRequires:  golang(honnef.co/go/tools/cmd/staticcheck)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/DATA-DOG/go-sqlmock)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep
rm -rf internal/tools
mapfile -t flux <<< $(find . -iname "*.flux" -type f)

%install
%gopkginstall

%if %{with check}
%check
%gocheck -t stdlib \
         -d execute
%endif

%gopkgfiles

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.100.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 17 17:39:17 CET 2021 Robert-André Mauchin <zebob.m@gmail.com> - 0.100.1-1
- Update to 0.100.1
- Close: rhbz#1915150

* Fri Jan  8 10:03:04 CET 2021 Robert-André Mauchin <zebob.m@gmail.com> - 0.100.0-1
- Update to 0.100.0
- Close: rhbz#1913992

* Sun Dec 20 09:27:36 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.99.0-1
- Update to 0.99.0
- Close: rhbz#1877615

* Tue Sep 08 18:43:39 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.83.1-1
- Update to 0.83.1

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.65.0-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.65.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Apr 04 21:27:23 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.65.0-1
- Update to 0.65.0

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.37.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 05 16:55:33 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.37.2-3
- Force inclusion of stdlib/strings/testdata/

* Mon Aug 05 16:55:33 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.37.2-2
- Force inclusion of stdlib/pandas_tests/testdata

* Mon Aug 05 15:32:29 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.37.2-1
- Release 0.37.2

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.28.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 24 22:46:25 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.28.0-1
- Initial package