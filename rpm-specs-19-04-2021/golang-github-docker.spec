# Generated by go2rpm
%bcond_without check
%bcond_with bootstrap
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^golang\\(github.com/Microsoft/hcsshim/cmd/containerd-shim-runhcs-v1/options\\)$

%if %{with bootstrap}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^golang\\(.*\\)$
%endif

# https://github.com/docker/docker
%global goipath         github.com/docker/docker
%global forgeurl        https://github.com/moby/moby
Version:                20.10.5

%gometa

%global goaltipaths    github.com/moby/moby

%global common_description %{expand:
Moby is an open-source project created by Docker to enable and accelerate
software containerization.

It provides a "Lego set" of toolkit components, the framework for assembling
them into custom container-based systems, and a place for all container
enthusiasts and professionals to experiment and exchange ideas. Components
include container build tools, a container registry, orchestration tools, a
runtime and more, and these can be used as building blocks in conjunction with
other tools and projects.}

%global golicenses      LICENSE NOTICE
%global godocs          docs AUTHORS CHANGELOG.md CONTRIBUTING.md README.md\\\
                        ROADMAP.md TESTING.md VENDORING.md

%if %{with bootstrap}
%global gosupfiles      ${vendor[@]}
%endif

Name:           %{goname}
Release:        1%{?dist}
Summary:        Collaborative project for the container ecosystem

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}
Patch0:         https://github.com/moby/moby/pull/42094.patch#/0001-skip-test-require-root.patch

%if %{without bootstrap}
BuildRequires:  golang(cloud.google.com/go/compute/metadata)
BuildRequires:  golang(cloud.google.com/go/logging)
BuildRequires:  golang(github.com/aws/aws-sdk-go/aws)
BuildRequires:  golang(github.com/aws/aws-sdk-go/aws/awserr)
BuildRequires:  golang(github.com/aws/aws-sdk-go/aws/credentials/endpointcreds)
BuildRequires:  golang(github.com/aws/aws-sdk-go/aws/ec2metadata)
BuildRequires:  golang(github.com/aws/aws-sdk-go/aws/request)
BuildRequires:  golang(github.com/aws/aws-sdk-go/aws/session)
BuildRequires:  golang(github.com/aws/aws-sdk-go/service/cloudwatchlogs)
BuildRequires:  golang(github.com/bsphere/le_go)
BuildRequires:  golang(github.com/BurntSushi/toml)
BuildRequires:  golang(github.com/containerd/cgroups)
BuildRequires:  golang(github.com/containerd/cgroups/stats/v1)
BuildRequires:  golang(github.com/containerd/cgroups/v2)
BuildRequires:  golang(github.com/containerd/cgroups/v2/stats)
BuildRequires:  golang(github.com/containerd/containerd)
BuildRequires:  golang(github.com/containerd/containerd/api/events)
BuildRequires:  golang(github.com/containerd/containerd/api/types)
BuildRequires:  golang(github.com/containerd/containerd/archive)
BuildRequires:  golang(github.com/containerd/containerd/cio)
BuildRequires:  golang(github.com/containerd/containerd/containers)
BuildRequires:  golang(github.com/containerd/containerd/content)
BuildRequires:  golang(github.com/containerd/containerd/content/local)
BuildRequires:  golang(github.com/containerd/containerd/contrib/nvidia)
BuildRequires:  golang(github.com/containerd/containerd/defaults)
BuildRequires:  golang(github.com/containerd/containerd/errdefs)
BuildRequires:  golang(github.com/containerd/containerd/events)
BuildRequires:  golang(github.com/containerd/containerd/gc)
BuildRequires:  golang(github.com/containerd/containerd/images)
BuildRequires:  golang(github.com/containerd/containerd/leases)
BuildRequires:  golang(github.com/containerd/containerd/log)
BuildRequires:  golang(github.com/containerd/containerd/metadata)
BuildRequires:  golang(github.com/containerd/containerd/mount)
BuildRequires:  golang(github.com/containerd/containerd/namespaces)
BuildRequires:  golang(github.com/containerd/containerd/oci)
BuildRequires:  golang(github.com/containerd/containerd/pkg/dialer)
BuildRequires:  golang(github.com/containerd/containerd/platforms)
BuildRequires:  golang(github.com/containerd/containerd/reference)
BuildRequires:  golang(github.com/containerd/containerd/remotes)
BuildRequires:  golang(github.com/containerd/containerd/remotes/docker)
BuildRequires:  golang(github.com/containerd/containerd/remotes/docker/schema1)
BuildRequires:  golang(github.com/containerd/containerd/rootfs)
BuildRequires:  golang(github.com/containerd/containerd/runtime/linux/runctypes)
BuildRequires:  golang(github.com/containerd/containerd/runtime/v1/linux)
BuildRequires:  golang(github.com/containerd/containerd/runtime/v2/runc/options)
BuildRequires:  golang(github.com/containerd/containerd/services/server/config)
BuildRequires:  golang(github.com/containerd/containerd/snapshots)
BuildRequires:  golang(github.com/containerd/containerd/sys)
BuildRequires:  golang(github.com/containerd/continuity/driver)
BuildRequires:  golang(github.com/containerd/continuity/fs)
BuildRequires:  golang(github.com/containerd/continuity/pathdriver)
BuildRequires:  golang(github.com/containerd/fifo)
BuildRequires:  golang(github.com/containerd/typeurl)
BuildRequires:  golang(github.com/coreos/go-systemd/v22/activation)
BuildRequires:  golang(github.com/coreos/go-systemd/v22/daemon)
BuildRequires:  golang(github.com/coreos/go-systemd/v22/journal)
BuildRequires:  golang(github.com/docker/distribution)
BuildRequires:  golang(github.com/docker/distribution/digestset)
BuildRequires:  golang(github.com/docker/distribution/manifest/manifestlist)
BuildRequires:  golang(github.com/docker/distribution/manifest/ocischema)
BuildRequires:  golang(github.com/docker/distribution/manifest/schema1)
BuildRequires:  golang(github.com/docker/distribution/manifest/schema2)
BuildRequires:  golang(github.com/docker/distribution/reference)
BuildRequires:  golang(github.com/docker/distribution/registry/api/errcode)
BuildRequires:  golang(github.com/docker/distribution/registry/api/v2)
BuildRequires:  golang(github.com/docker/distribution/registry/client)
BuildRequires:  golang(github.com/docker/distribution/registry/client/auth)
BuildRequires:  golang(github.com/docker/distribution/registry/client/auth/challenge)
BuildRequires:  golang(github.com/docker/distribution/registry/client/transport)
BuildRequires:  golang(github.com/docker/go-connections/nat)
BuildRequires:  golang(github.com/docker/go-connections/sockets)
BuildRequires:  golang(github.com/docker/go-connections/tlsconfig)
BuildRequires:  golang(github.com/docker/go-metrics)
BuildRequires:  golang(github.com/docker/go-units)
BuildRequires:  golang(github.com/docker/libkv)
BuildRequires:  golang(github.com/docker/libkv/store)
BuildRequires:  golang(github.com/docker/libkv/store/consul)
BuildRequires:  golang(github.com/docker/libkv/store/etcd)
BuildRequires:  golang(github.com/docker/libkv/store/zookeeper)
BuildRequires:  golang(github.com/docker/libnetwork)
BuildRequires:  golang(github.com/docker/libnetwork/cluster)
BuildRequires:  golang(github.com/docker/libnetwork/config)
BuildRequires:  golang(github.com/docker/libnetwork/datastore)
BuildRequires:  golang(github.com/docker/libnetwork/driverapi)
BuildRequires:  golang(github.com/docker/libnetwork/drivers/bridge)
BuildRequires:  golang(github.com/docker/libnetwork/ipamapi)
BuildRequires:  golang(github.com/docker/libnetwork/ipamutils)
BuildRequires:  golang(github.com/docker/libnetwork/netlabel)
BuildRequires:  golang(github.com/docker/libnetwork/netutils)
BuildRequires:  golang(github.com/docker/libnetwork/networkdb)
BuildRequires:  golang(github.com/docker/libnetwork/options)
BuildRequires:  golang(github.com/docker/libnetwork/portallocator)
BuildRequires:  golang(github.com/docker/libnetwork/resolvconf)
BuildRequires:  golang(github.com/docker/libnetwork/types)
BuildRequires:  golang(github.com/docker/libtrust)
BuildRequires:  golang(github.com/docker/swarmkit/agent)
BuildRequires:  golang(github.com/docker/swarmkit/agent/exec)
BuildRequires:  golang(github.com/docker/swarmkit/api)
BuildRequires:  golang(github.com/docker/swarmkit/api/genericresource)
BuildRequires:  golang(github.com/docker/swarmkit/api/naming)
BuildRequires:  golang(github.com/docker/swarmkit/ca)
BuildRequires:  golang(github.com/docker/swarmkit/log)
BuildRequires:  golang(github.com/docker/swarmkit/manager/allocator/cnmallocator)
BuildRequires:  golang(github.com/docker/swarmkit/manager/encryption)
BuildRequires:  golang(github.com/docker/swarmkit/node)
BuildRequires:  golang(github.com/docker/swarmkit/template)
BuildRequires:  golang(github.com/fluent/fluent-logger-golang/fluent)
BuildRequires:  golang(github.com/fsnotify/fsnotify)
BuildRequires:  golang(github.com/gogo/protobuf/proto)
BuildRequires:  golang(github.com/gogo/protobuf/sortkeys)
BuildRequires:  golang(github.com/gogo/protobuf/types)
BuildRequires:  golang(github.com/golang/gddo/httputil)
BuildRequires:  golang(github.com/google/uuid)
BuildRequires:  golang(github.com/gorilla/mux)
BuildRequires:  golang(github.com/Graylog2/go-gelf/gelf)
BuildRequires:  golang(github.com/hashicorp/go-immutable-radix)
BuildRequires:  golang(github.com/hashicorp/go-memdb)
BuildRequires:  golang(github.com/imdario/mergo)
BuildRequires:  golang(github.com/mistifyio/go-zfs)
BuildRequires:  golang(github.com/moby/buildkit/api/services/control)
BuildRequires:  golang(github.com/moby/buildkit/cache)
BuildRequires:  golang(github.com/moby/buildkit/cache/metadata)
BuildRequires:  golang(github.com/moby/buildkit/cache/remotecache)
BuildRequires:  golang(github.com/moby/buildkit/cache/remotecache/inline)
BuildRequires:  golang(github.com/moby/buildkit/cache/remotecache/local)
BuildRequires:  golang(github.com/moby/buildkit/cache/remotecache/registry)
BuildRequires:  golang(github.com/moby/buildkit/cache/remotecache/v1)
BuildRequires:  golang(github.com/moby/buildkit/client)
BuildRequires:  golang(github.com/moby/buildkit/client/llb)
BuildRequires:  golang(github.com/moby/buildkit/cmd/buildkitd/config)
BuildRequires:  golang(github.com/moby/buildkit/control)
BuildRequires:  golang(github.com/moby/buildkit/executor)
BuildRequires:  golang(github.com/moby/buildkit/executor/oci)
BuildRequires:  golang(github.com/moby/buildkit/executor/runcexecutor)
BuildRequires:  golang(github.com/moby/buildkit/exporter)
BuildRequires:  golang(github.com/moby/buildkit/exporter/containerimage/exptypes)
BuildRequires:  golang(github.com/moby/buildkit/exporter/local)
BuildRequires:  golang(github.com/moby/buildkit/exporter/tar)
BuildRequires:  golang(github.com/moby/buildkit/frontend)
BuildRequires:  golang(github.com/moby/buildkit/frontend/dockerfile/builder)
BuildRequires:  golang(github.com/moby/buildkit/frontend/dockerfile/dockerignore)
BuildRequires:  golang(github.com/moby/buildkit/frontend/dockerfile/instructions)
BuildRequires:  golang(github.com/moby/buildkit/frontend/dockerfile/parser)
BuildRequires:  golang(github.com/moby/buildkit/frontend/dockerfile/shell)
BuildRequires:  golang(github.com/moby/buildkit/frontend/gateway)
BuildRequires:  golang(github.com/moby/buildkit/frontend/gateway/forwarder)
BuildRequires:  golang(github.com/moby/buildkit/identity)
BuildRequires:  golang(github.com/moby/buildkit/session)
BuildRequires:  golang(github.com/moby/buildkit/snapshot)
BuildRequires:  golang(github.com/moby/buildkit/snapshot/containerd)
BuildRequires:  golang(github.com/moby/buildkit/solver)
BuildRequires:  golang(github.com/moby/buildkit/solver/bboltcachestorage)
BuildRequires:  golang(github.com/moby/buildkit/solver/llbsolver/mounts)
BuildRequires:  golang(github.com/moby/buildkit/solver/llbsolver/ops)
BuildRequires:  golang(github.com/moby/buildkit/solver/pb)
BuildRequires:  golang(github.com/moby/buildkit/source)
BuildRequires:  golang(github.com/moby/buildkit/source/git)
BuildRequires:  golang(github.com/moby/buildkit/source/http)
BuildRequires:  golang(github.com/moby/buildkit/source/local)
BuildRequires:  golang(github.com/moby/buildkit/util/apicaps)
BuildRequires:  golang(github.com/moby/buildkit/util/archutil)
BuildRequires:  golang(github.com/moby/buildkit/util/compression)
BuildRequires:  golang(github.com/moby/buildkit/util/contentutil)
BuildRequires:  golang(github.com/moby/buildkit/util/entitlements)
BuildRequires:  golang(github.com/moby/buildkit/util/flightcontrol)
BuildRequires:  golang(github.com/moby/buildkit/util/imageutil)
BuildRequires:  golang(github.com/moby/buildkit/util/leaseutil)
BuildRequires:  golang(github.com/moby/buildkit/util/network)
BuildRequires:  golang(github.com/moby/buildkit/util/progress)
BuildRequires:  golang(github.com/moby/buildkit/util/resolver)
BuildRequires:  golang(github.com/moby/buildkit/util/system)
BuildRequires:  golang(github.com/moby/buildkit/util/tracing)
BuildRequires:  golang(github.com/moby/buildkit/worker)
BuildRequires:  golang(github.com/moby/locker)
BuildRequires:  golang(github.com/moby/sys/mount)
BuildRequires:  golang(github.com/moby/sys/mountinfo)
BuildRequires:  golang(github.com/moby/sys/symlink)
BuildRequires:  golang(github.com/moby/term)
BuildRequires:  golang(github.com/morikuni/aec)
BuildRequires:  golang(github.com/opencontainers/go-digest)
BuildRequires:  golang(github.com/opencontainers/image-spec/identity)
BuildRequires:  golang(github.com/opencontainers/image-spec/specs-go/v1)
BuildRequires:  golang(github.com/opencontainers/runc/libcontainer/apparmor)
BuildRequires:  golang(github.com/opencontainers/runc/libcontainer/cgroups)
BuildRequires:  golang(github.com/opencontainers/runc/libcontainer/configs)
BuildRequires:  golang(github.com/opencontainers/runc/libcontainer/devices)
BuildRequires:  golang(github.com/opencontainers/runc/libcontainer/user)
BuildRequires:  golang(github.com/opencontainers/runtime-spec/specs-go)
BuildRequires:  golang(github.com/opencontainers/selinux/go-selinux)
BuildRequires:  golang(github.com/opencontainers/selinux/go-selinux/label)
BuildRequires:  golang(github.com/pkg/errors)
BuildRequires:  golang(github.com/prometheus/client_golang/prometheus)
BuildRequires:  golang(github.com/RackSec/srslog)
BuildRequires:  golang(github.com/sirupsen/logrus)
BuildRequires:  golang(github.com/spf13/cobra)
BuildRequires:  golang(github.com/spf13/pflag)
BuildRequires:  golang(github.com/syndtr/gocapability/capability)
BuildRequires:  golang(github.com/tchap/go-patricia/patricia)
BuildRequires:  golang(github.com/tonistiigi/fsutil)
BuildRequires:  golang(github.com/vbatts/tar-split/tar/asm)
BuildRequires:  golang(github.com/vbatts/tar-split/tar/storage)
BuildRequires:  golang(github.com/vishvananda/netlink)
BuildRequires:  golang(go.etcd.io/bbolt)
BuildRequires:  golang(golang.org/x/net/http2)
BuildRequires:  golang(golang.org/x/net/websocket)
BuildRequires:  golang(golang.org/x/sync/errgroup)
BuildRequires:  golang(golang.org/x/sync/semaphore)
BuildRequires:  golang(golang.org/x/sync/syncmap)
BuildRequires:  golang(golang.org/x/sys/execabs)
BuildRequires:  golang(golang.org/x/sys/unix)
BuildRequires:  golang(golang.org/x/time/rate)
BuildRequires:  golang(google.golang.org/genproto/googleapis/api/monitoredres)
BuildRequires:  golang(google.golang.org/grpc)
BuildRequires:  golang(google.golang.org/grpc/backoff)
BuildRequires:  golang(google.golang.org/grpc/codes)
BuildRequires:  golang(google.golang.org/grpc/metadata)
BuildRequires:  golang(google.golang.org/grpc/status)
BuildRequires:  golang(gotest.tools/v3/assert)
BuildRequires:  golang(gotest.tools/v3/assert/cmp)
BuildRequires:  golang(gotest.tools/v3/fs)
BuildRequires:  golang(gotest.tools/v3/icmd)
BuildRequires:  golang(gotest.tools/v3/poll)
BuildRequires:  golang(gotest.tools/v3/skip)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/gogo/protobuf/io)
BuildRequires:  golang(github.com/google/go-cmp/cmp)
BuildRequires:  golang(github.com/google/go-cmp/cmp/cmpopts)
BuildRequires:  golang(gotest.tools/v3/env)
%endif
%endif
BuildRequires:  git-core
BuildRequires:  pkgconfig(libseccomp)

%description
%{common_description}

%gopkg

%prep
%if %{with bootstrap}
%goprep -k
%else
%goprep
%endif
%autopatch -p1

# %%build
# for cmd in cmd/* ; do
#   %%gobuild -o %%{gobuilddir}/bin/$(basename $cmd) %%{goipath}/$cmd
# done

%install
%if %{with bootstrap}
mapfile -t vendor <<< $(find vendor -type f)
%endif
%gopkginstall
# install -m 0755 -vd                     %%{buildroot}%%{_bindir}
# install -m 0755 -vp %%{gobuilddir}/bin/* %%{buildroot}%%{_bindir}/

%if %{with check}
%check
%gocheck -t daemon \
         -d distribution \
         -t cmd/dockerd \
         -d integration/network \
         -d pkg/authorization \
         -d pkg/chrootarchive \
         -d plugin \
         -d pkg/mount \
         -d pkg/signal \
         -d pkg/fileutils \
         -d pkg/system
%endif

# %%files
# %%license LICENSE NOTICE
# %%doc docs AUTHORS CHANGELOG.md CONTRIBUTING.md README.md ROADMAP.md TESTING.md
# %%doc VENDORING.md
# %%{_bindir}/*

%gopkgfiles

%changelog
* Sun Mar 07 2021 Olivier Lemasle <o.lemasle@gmail.com> - 20.10.5-1
- Update to 20.10.5

* Sun Jan 31 2021 Olivier Lemasle <o.lemasle@gmail.com> - 20.10.2-3
- Fix license (ASL 2.0 only)

* Fri Jan 29 2021 Olivier Lemasle <o.lemasle@gmail.com> - 20.10.2-2
- Unbootstrap

* Thu Jan 28 2021 Olivier Lemasle <o.lemasle@gmail.com> - 20.10.2-1
- Update to 20.10.2 - Bootstrap

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 19.03.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Aug 23 02:25:48 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 19.03.13-1
- Update to 19.03.13

* Sun Aug 23 02:25:48 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 19.03.12-3
- Fix FTBFS

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 19.03.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 25 22:11:51 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 19.03.12-1
- Update to 19.03.12

* Wed Apr 01 2020 Olivier Lemasle <o.lemasle@gmail.com> - 19.03.5-4
- Unbootstrap

* Wed Apr 01 2020 Olivier Lemasle <o.lemasle@gmail.com> - 19.03.5-3
- Make it compatible with Go 1.14

* Wed Apr 01 2020 Olivier Lemasle <o.lemasle@gmail.com> - 19.03.5-2
- Bootstrap

* Thu Jan 30 00:42:22 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 19.03.5-1
- Update to 19.03.5
- Patch test to work with Go 1.14

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 19.03.0-2.rc3.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 19.03.0-2.rc3.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jul 06 15:03:03 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 19.03.0-2.rc3
- Remove Windows only dependency

* Sat Jul 06 13:58:06 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 19.03.0-1.rc3
- Release 19.03.0-rc3

* Thu Jul 04 19:22:49 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 18.09.7-1
- Release 18.09.7

* Sat May 04 20:50:08 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 17.03.2-1.ce.20190504git619df5a
- Initial package
