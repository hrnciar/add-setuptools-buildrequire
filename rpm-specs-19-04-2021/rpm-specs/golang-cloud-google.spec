# Generated by go2rpm
%bcond_without check
%bcond_with bootstrap

# https://github.com/GoogleCloudPlatform/google-cloud-go
%global goipath         cloud.google.com/go
%global forgeurl        https://github.com/GoogleCloudPlatform/google-cloud-go
Version:                0.75.0

%gometa

%if %{without bootstrap}
%global goipaths0       cloud.google.com/go
%global goipathsex0     cloud.google.com/go/compute
%endif

%global goipaths1       cloud.google.com/go/compute

%global common_description %{expand:
Go packages for Google Cloud Platform services.}

%global golicenses      LICENSE
%global godocs          AUTHORS CODE_OF_CONDUCT.md CONTRIBUTING.md CONTRIBUTORS RELEASING.md old-news.md CHANGES.md README.md

Name:           %{goname}
Release:        2%{?dist}
Summary:        Google Cloud client libraries for Go

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

%if %{without bootstrap}
BuildRequires:  golang(github.com/golang/mock/gomock)
BuildRequires:  golang(github.com/golang/protobuf/proto)
BuildRequires:  golang(github.com/golang/protobuf/ptypes)
BuildRequires:  golang(github.com/golang/protobuf/ptypes/any)
BuildRequires:  golang(github.com/golang/protobuf/ptypes/duration)
BuildRequires:  golang(github.com/golang/protobuf/ptypes/empty)
BuildRequires:  golang(github.com/golang/protobuf/ptypes/struct)
BuildRequires:  golang(github.com/golang/protobuf/ptypes/timestamp)
BuildRequires:  golang(github.com/golang/protobuf/ptypes/wrappers)
BuildRequires:  golang(github.com/google/btree)
BuildRequires:  golang(github.com/google/go-cmp/cmp)
BuildRequires:  golang(github.com/google/go-cmp/cmp/cmpopts)
BuildRequires:  golang(github.com/google/go-github/v33/github)
BuildRequires:  golang(github.com/google/martian/v3)
BuildRequires:  golang(github.com/google/martian/v3/fifo)
BuildRequires:  golang(github.com/google/martian/v3/httpspec)
BuildRequires:  golang(github.com/google/martian/v3/martianhttp)
BuildRequires:  golang(github.com/google/martian/v3/martianlog)
BuildRequires:  golang(github.com/google/martian/v3/mitm)
BuildRequires:  golang(github.com/google/pprof/profile)
BuildRequires:  golang(github.com/google/uuid)
BuildRequires:  golang(github.com/googleapis/gax-go/v2)
BuildRequires:  golang(github.com/shurcooL/githubv4)
BuildRequires:  golang(go.opencensus.io/plugin/ocgrpc)
BuildRequires:  golang(go.opencensus.io/stats)
BuildRequires:  golang(go.opencensus.io/stats/view)
BuildRequires:  golang(go.opencensus.io/tag)
BuildRequires:  golang(go.opencensus.io/trace)
BuildRequires:  golang(golang.org/x/net/context)
BuildRequires:  golang(golang.org/x/oauth2)
BuildRequires:  golang(golang.org/x/oauth2/google)
BuildRequires:  golang(golang.org/x/oauth2/jwt)
BuildRequires:  golang(golang.org/x/sync/errgroup)
BuildRequires:  golang(golang.org/x/sync/semaphore)
BuildRequires:  golang(golang.org/x/text/language)
BuildRequires:  golang(golang.org/x/time/rate)
BuildRequires:  golang(golang.org/x/tools/go/packages)
BuildRequires:  golang(golang.org/x/xerrors)
BuildRequires:  golang(google.golang.org/api/bigquery/v2)
BuildRequires:  golang(google.golang.org/api/clouddebugger/v2)
BuildRequires:  golang(google.golang.org/api/cloudresourcemanager/v1)
BuildRequires:  golang(google.golang.org/api/compute/v1)
BuildRequires:  golang(google.golang.org/api/container/v1)
BuildRequires:  golang(google.golang.org/api/googleapi)
BuildRequires:  golang(google.golang.org/api/iterator)
BuildRequires:  golang(google.golang.org/api/option)
BuildRequires:  golang(google.golang.org/api/option/internaloption)
BuildRequires:  golang(google.golang.org/api/storage/v1)
BuildRequires:  golang(google.golang.org/api/support/bundler)
BuildRequires:  golang(google.golang.org/api/translate/v2)
BuildRequires:  golang(google.golang.org/api/transport)
BuildRequires:  golang(google.golang.org/api/transport/grpc)
BuildRequires:  golang(google.golang.org/api/transport/http)
BuildRequires:  golang(google.golang.org/genproto/googleapis/analytics/admin/v1alpha)
BuildRequires:  golang(google.golang.org/genproto/googleapis/analytics/data/v1alpha)
BuildRequires:  golang(google.golang.org/genproto/googleapis/api/httpbody)
BuildRequires:  golang(google.golang.org/genproto/googleapis/api/label)
BuildRequires:  golang(google.golang.org/genproto/googleapis/api/metric)
BuildRequires:  golang(google.golang.org/genproto/googleapis/api/monitoredres)
BuildRequires:  golang(google.golang.org/genproto/googleapis/appengine/logging/v1)
BuildRequires:  golang(google.golang.org/genproto/googleapis/area120/tables/v1alpha1)
BuildRequires:  golang(google.golang.org/genproto/googleapis/bigtable/admin/v2)
BuildRequires:  golang(google.golang.org/genproto/googleapis/bigtable/v2)
BuildRequires:  golang(google.golang.org/genproto/googleapis/cloud/accessapproval/v1)
BuildRequires:  golang(google.golang.org/genproto/googleapis/cloud/asset/v1)
BuildRequires:  golang(google.golang.org/genproto/googleapis/cloud/asset/v1p2beta1)
BuildRequires:  golang(google.golang.org/genproto/googleapis/cloud/asset/v1p5beta1)
BuildRequires:  golang(google.golang.org/genproto/googleapis/cloud/assuredworkloads/v1beta1)
BuildRequires:  golang(google.golang.org/genproto/googleapis/cloud/audit)
BuildRequires:  golang(google.golang.org/genproto/googleapis/cloud/automl/v1)
BuildRequires:  golang(google.golang.org/genproto/googleapis/cloud/automl/v1beta1)
BuildRequires:  golang(google.golang.org/genproto/googleapis/cloud/bigquery/connection/v1)
BuildRequires:  golang(google.golang.org/genproto/googleapis/cloud/bigquery/connection/v1beta1)
BuildRequires:  golang(google.golang.org/genproto/googleapis/cloud/bigquery/datatransfer/v1)
BuildRequires:  golang(google.golang.org/genproto/googleapis/cloud/bigquery/reservation/v1)
BuildRequires:  golang(google.golang.org/genproto/googleapis/cloud/bigquery/reservation/v1beta1)
BuildRequires:  golang(google.golang.org/genproto/googleapis/cloud/bigquery/storage/v1)
BuildRequires:  golang(google.golang.org/genproto/googleapis/cloud/bigquery/storage/v1alpha2)
BuildRequires:  golang(google.golang.org/genproto/googleapis/cloud/bigquery/storage/v1beta1)
BuildRequires:  golang(google.golang.org/genproto/googleapis/cloud/bigquery/storage/v1beta2)
BuildRequires:  golang(google.golang.org/genproto/googleapis/cloud/billing/budgets/v1)
BuildRequires:  golang(google.golang.org/genproto/googleapis/cloud/billing/budgets/v1beta1)
BuildRequires:  golang(google.golang.org/genproto/googleapis/cloud/billing/v1)
BuildRequires:  golang(google.golang.org/genproto/googleapis/cloud/channel/v1)
BuildRequires:  golang(google.golang.org/genproto/googleapis/cloud/datacatalog/v1)
BuildRequires:  golang(google.golang.org/genproto/googleapis/cloud/datacatalog/v1beta1)
BuildRequires:  golang(google.golang.org/genproto/googleapis/cloud/dataproc/v1)
BuildRequires:  golang(google.golang.org/genproto/googleapis/cloud/dataproc/v1beta2)
BuildRequires:  golang(google.golang.org/genproto/googleapis/cloud/dialogflow/cx/v3beta1)
BuildRequires:  golang(google.golang.org/genproto/googleapis/cloud/dialogflow/v2)
BuildRequires:  golang(google.golang.org/genproto/googleapis/cloud/functions/v1)
BuildRequires:  golang(google.golang.org/genproto/googleapis/cloud/gaming/v1)
BuildRequires:  golang(google.golang.org/genproto/googleapis/cloud/gaming/v1beta)
BuildRequires:  golang(google.golang.org/genproto/googleapis/cloud/iot/v1)
BuildRequires:  golang(google.golang.org/genproto/googleapis/cloud/kms/v1)
BuildRequires:  golang(google.golang.org/genproto/googleapis/cloud/language/v1)
BuildRequires:  golang(google.golang.org/genproto/googleapis/cloud/language/v1beta2)
BuildRequires:  golang(google.golang.org/genproto/googleapis/cloud/managedidentities/v1)
BuildRequires:  golang(google.golang.org/genproto/googleapis/cloud/memcache/v1beta2)
BuildRequires:  golang(google.golang.org/genproto/googleapis/cloud/notebooks/v1beta1)
BuildRequires:  golang(google.golang.org/genproto/googleapis/cloud/osconfig/agentendpoint/v1)
BuildRequires:  golang(google.golang.org/genproto/googleapis/cloud/osconfig/agentendpoint/v1beta)
BuildRequires:  golang(google.golang.org/genproto/googleapis/cloud/osconfig/v1)
BuildRequires:  golang(google.golang.org/genproto/googleapis/cloud/osconfig/v1beta)
BuildRequires:  golang(google.golang.org/genproto/googleapis/cloud/oslogin/common)
BuildRequires:  golang(google.golang.org/genproto/googleapis/cloud/oslogin/v1)
BuildRequires:  golang(google.golang.org/genproto/googleapis/cloud/oslogin/v1beta)
BuildRequires:  golang(google.golang.org/genproto/googleapis/cloud/phishingprotection/v1beta1)
BuildRequires:  golang(google.golang.org/genproto/googleapis/cloud/policytroubleshooter/v1)
BuildRequires:  golang(google.golang.org/genproto/googleapis/cloud/pubsublite/v1)
BuildRequires:  golang(google.golang.org/genproto/googleapis/cloud/recaptchaenterprise/v1)
BuildRequires:  golang(google.golang.org/genproto/googleapis/cloud/recaptchaenterprise/v1beta1)
BuildRequires:  golang(google.golang.org/genproto/googleapis/cloud/recommender/v1)
BuildRequires:  golang(google.golang.org/genproto/googleapis/cloud/recommender/v1beta1)
BuildRequires:  golang(google.golang.org/genproto/googleapis/cloud/redis/v1)
BuildRequires:  golang(google.golang.org/genproto/googleapis/cloud/redis/v1beta1)
BuildRequires:  golang(google.golang.org/genproto/googleapis/cloud/retail/v2)
BuildRequires:  golang(google.golang.org/genproto/googleapis/cloud/scheduler/v1)
BuildRequires:  golang(google.golang.org/genproto/googleapis/cloud/scheduler/v1beta1)
BuildRequires:  golang(google.golang.org/genproto/googleapis/cloud/secretmanager/v1)
BuildRequires:  golang(google.golang.org/genproto/googleapis/cloud/secretmanager/v1beta1)
BuildRequires:  golang(google.golang.org/genproto/googleapis/cloud/security/privateca/v1beta1)
BuildRequires:  golang(google.golang.org/genproto/googleapis/cloud/securitycenter/settings/v1beta1)
BuildRequires:  golang(google.golang.org/genproto/googleapis/cloud/securitycenter/v1)
BuildRequires:  golang(google.golang.org/genproto/googleapis/cloud/securitycenter/v1beta1)
BuildRequires:  golang(google.golang.org/genproto/googleapis/cloud/securitycenter/v1p1beta1)
BuildRequires:  golang(google.golang.org/genproto/googleapis/cloud/servicedirectory/v1)
BuildRequires:  golang(google.golang.org/genproto/googleapis/cloud/servicedirectory/v1beta1)
BuildRequires:  golang(google.golang.org/genproto/googleapis/cloud/speech/v1)
BuildRequires:  golang(google.golang.org/genproto/googleapis/cloud/speech/v1p1beta1)
BuildRequires:  golang(google.golang.org/genproto/googleapis/cloud/talent/v4)
BuildRequires:  golang(google.golang.org/genproto/googleapis/cloud/talent/v4beta1)
BuildRequires:  golang(google.golang.org/genproto/googleapis/cloud/tasks/v2)
BuildRequires:  golang(google.golang.org/genproto/googleapis/cloud/tasks/v2beta2)
BuildRequires:  golang(google.golang.org/genproto/googleapis/cloud/tasks/v2beta3)
BuildRequires:  golang(google.golang.org/genproto/googleapis/cloud/texttospeech/v1)
BuildRequires:  golang(google.golang.org/genproto/googleapis/cloud/translate/v3)
BuildRequires:  golang(google.golang.org/genproto/googleapis/cloud/video/transcoder/v1beta1)
BuildRequires:  golang(google.golang.org/genproto/googleapis/cloud/videointelligence/v1)
BuildRequires:  golang(google.golang.org/genproto/googleapis/cloud/videointelligence/v1beta2)
BuildRequires:  golang(google.golang.org/genproto/googleapis/cloud/vision/v1)
BuildRequires:  golang(google.golang.org/genproto/googleapis/cloud/vision/v1p1beta1)
BuildRequires:  golang(google.golang.org/genproto/googleapis/cloud/webrisk/v1)
BuildRequires:  golang(google.golang.org/genproto/googleapis/cloud/webrisk/v1beta1)
BuildRequires:  golang(google.golang.org/genproto/googleapis/cloud/websecurityscanner/v1)
BuildRequires:  golang(google.golang.org/genproto/googleapis/cloud/workflows/executions/v1beta)
BuildRequires:  golang(google.golang.org/genproto/googleapis/cloud/workflows/v1beta)
BuildRequires:  golang(google.golang.org/genproto/googleapis/container/v1)
BuildRequires:  golang(google.golang.org/genproto/googleapis/datastore/admin/v1)
BuildRequires:  golang(google.golang.org/genproto/googleapis/datastore/v1)
BuildRequires:  golang(google.golang.org/genproto/googleapis/devtools/artifactregistry/v1beta2)
BuildRequires:  golang(google.golang.org/genproto/googleapis/devtools/cloudbuild/v1)
BuildRequires:  golang(google.golang.org/genproto/googleapis/devtools/clouddebugger/v2)
BuildRequires:  golang(google.golang.org/genproto/googleapis/devtools/clouderrorreporting/v1beta1)
BuildRequires:  golang(google.golang.org/genproto/googleapis/devtools/cloudprofiler/v2)
BuildRequires:  golang(google.golang.org/genproto/googleapis/devtools/cloudtrace/v1)
BuildRequires:  golang(google.golang.org/genproto/googleapis/devtools/cloudtrace/v2)
BuildRequires:  golang(google.golang.org/genproto/googleapis/devtools/containeranalysis/v1)
BuildRequires:  golang(google.golang.org/genproto/googleapis/devtools/containeranalysis/v1beta1)
BuildRequires:  golang(google.golang.org/genproto/googleapis/devtools/containeranalysis/v1beta1/grafeas)
BuildRequires:  golang(google.golang.org/genproto/googleapis/firestore/admin/v1)
BuildRequires:  golang(google.golang.org/genproto/googleapis/firestore/v1)
BuildRequires:  golang(google.golang.org/genproto/googleapis/firestore/v1beta1)
BuildRequires:  golang(google.golang.org/genproto/googleapis/grafeas/v1)
BuildRequires:  golang(google.golang.org/genproto/googleapis/iam/admin/v1)
BuildRequires:  golang(google.golang.org/genproto/googleapis/iam/credentials/v1)
BuildRequires:  golang(google.golang.org/genproto/googleapis/iam/v1)
BuildRequires:  golang(google.golang.org/genproto/googleapis/logging/type)
BuildRequires:  golang(google.golang.org/genproto/googleapis/logging/v2)
BuildRequires:  golang(google.golang.org/genproto/googleapis/longrunning)
BuildRequires:  golang(google.golang.org/genproto/googleapis/monitoring/dashboard/v1)
BuildRequires:  golang(google.golang.org/genproto/googleapis/monitoring/v3)
BuildRequires:  golang(google.golang.org/genproto/googleapis/privacy/dlp/v2)
BuildRequires:  golang(google.golang.org/genproto/googleapis/pubsub/v1)
BuildRequires:  golang(google.golang.org/genproto/googleapis/rpc/code)
BuildRequires:  golang(google.golang.org/genproto/googleapis/rpc/errdetails)
BuildRequires:  golang(google.golang.org/genproto/googleapis/rpc/status)
BuildRequires:  golang(google.golang.org/genproto/googleapis/spanner/admin/database/v1)
BuildRequires:  golang(google.golang.org/genproto/googleapis/spanner/admin/instance/v1)
BuildRequires:  golang(google.golang.org/genproto/googleapis/spanner/v1)
BuildRequires:  golang(google.golang.org/genproto/googleapis/type/expr)
BuildRequires:  golang(google.golang.org/genproto/googleapis/type/latlng)
BuildRequires:  golang(google.golang.org/genproto/protobuf/field_mask)
BuildRequires:  golang(google.golang.org/grpc)
BuildRequires:  golang(google.golang.org/grpc/codes)
BuildRequires:  golang(google.golang.org/grpc/credentials)
BuildRequires:  golang(google.golang.org/grpc/keepalive)
BuildRequires:  golang(google.golang.org/grpc/metadata)
BuildRequires:  golang(google.golang.org/grpc/status)
BuildRequires:  golang(google.golang.org/protobuf/proto)
BuildRequires:  golang(google.golang.org/protobuf/types/known/structpb)
BuildRequires:  golang(gopkg.in/src-d/go-git.v4)
BuildRequires:  golang(gopkg.in/yaml.v2)
BuildRequires:  golang(rsc.io/binaryregexp)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/golang/protobuf/jsonpb)
BuildRequires:  golang(google.golang.org/api/iterator/testing)
BuildRequires:  golang(google.golang.org/api/logging/v2)
BuildRequires:  golang(google.golang.org/grpc/peer)
BuildRequires:  golang(google.golang.org/protobuf/types/known/timestamppb)
%endif
%endif

%description
%{common_description}

%gopkg

%prep
%goprep

%install
%gopkginstall

%if %{without bootstrap}
%if %{with check}
%check
# kms/apiv1, containeranalysis/apiv1: Needs "credentials"
# spanner/spansql: https://github.com/googleapis/google-cloud-go/issues/1729
%gocheck -d kms/apiv1 \
         -d containeranalysis/apiv1 \
         -d grafeas/apiv1 \
         -d storage \
         -d datastore \
         -d firestore \
         -d internal/godocfx \
         -d internal/uid \
         -d pubsub \
         -t spanner \
         -d pubsublite/internal/wire
%endif
%endif

%gopkgfiles

%changelog
* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.75.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 14 21:22:26 CET 2021 Robert-Andr?? Mauchin <zebob.m@gmail.com> - 0.75.0-1
- Update to 0.75.0
- Close: rhbz#1915169

* Sun Dec 27 12:58:42 CET 2020 Robert-Andr?? Mauchin <zebob.m@gmail.com> - 0.74.0-1
- Update to 0.74.0
- Close: rhbz#1906846

* Fri Sep 04 20:06:46 CEST 2020 Robert-Andr?? Mauchin <zebob.m@gmail.com> - 0.73.0-1
- Update to 0.73.0
- Close: rhbz#1879310

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.52.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 16:18:11 CET 2020 Robert-Andr?? Mauchin <zebob.m@gmail.com> - 0.52.0-1
- Update to 0.52.0
- Disable profiler test until fix by upstream

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.51.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 13 17:45:56 CET 2020 Robert-Andr?? Mauchin <zebob.m@gmail.com> - 0.51.0-1
- Update to 0.51.0

* Sat Dec 28 22:05:56 CET 2019 Robert-Andr?? Mauchin <zebob.m@gmail.com> - 0.50.0-2
- Bootstrap storage

* Sat Dec 28 15:36:09 CET 2019 Robert-Andr?? Mauchin <zebob.m@gmail.com> - 0.50.0-1
- Update to 0.50.0

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.37.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 05 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.37.4-2
- Add Obsoletes for old name

* Tue Apr 23 09:48:52 CEST 2019 Robert-Andr?? Mauchin <zebob.m@gmail.com> - 0.37.4-1
- Release 0.37.4

* Sat Mar 09 2019 Robert-Andr?? Mauchin <zebob.m@gmail.com> - 0.36.0-4
- Unbootstrap

* Mon Feb 25 2019 Robert-Andr?? Mauchin <zebob.m@gmail.com> - 0.36.0-3
- Bootstrap 2

* Mon Feb 25 2019 Robert-Andr?? Mauchin <zebob.m@gmail.com> - 0.36.0-2
- Bootstrap

* Mon Feb 25 2019 Robert-Andr?? Mauchin <zebob.m@gmail.com> - 0.36.0-1
- Update to release v0.36.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.31.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Oct 25 2018 Robert-Andr?? Mauchin <zebob.m@gmail.com> - 0.31.0-1
- Update to release v0.31.0

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 0.21.0-3
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it???s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed May 09 2018 Jan Chaloupka <jchaloup@redhat.com> - 0.21.0-1
- Update to v0.21.0
  Change import path prefix to cloud.google.com/go
  resolves: #1558755

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.14.git872c736
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.13.git872c736
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.12.git872c736
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.11.git872c736
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Dec 16 2016 Jan Chaloupka <jchaloup@redhat.com> - 0-0.10.git872c736
- Bump to upstream 872c736f496c2ba12786bedbb8325576bbdb33cf
  related: #1246239

* Thu Dec 15 2016 Jan Chaloupka <jchaloup@redhat.com> - 0-0.9.git2400193
- Polish the spec file
  related: #1246239

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.8.git2400193
- https://fedoraproject.org/wiki/Changes/golang1.7

* Sun Mar 06 2016 jchaloup <jchaloup@redhat.com> - 0-0.7.git2400193
- Bump to upstream 2400193c85c3561d13880d34e0e10c4315bb02af
  related: #1246239

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.6.git95c332f
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5.git95c332f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Aug 20 2015 jchaloup <jchaloup@redhat.com> - 0-0.4.git95c332f
- Update spec file to spec-2.0
  related: #1246239

* Thu Jul 23 2015 jchaloup <jchaloup@redhat.com> - 0-0.3.git95c332f
- Bump to upstream 95c332f94e6766fa122231c0a95ddf15ac26bf70
  resolves: #1246239

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.2.git2e43671
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jan 22 2015 jchaloup <jchaloup@redhat.com> - 0-0.1.git1c3fdc5
- First package for Fedora
  resolves: #1185281

