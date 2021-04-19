# Generated by go2rpm 1.3
%bcond_without check
%bcond_with bootstrap

# https://github.com/containerd/stargz-snapshotter
%global goipath         github.com/containerd/stargz-snapshotter
Version:                0.4.1

%gometa

%if %{without bootstrap}
%global goipaths0       github.com/containerd/stargz-snapshotter
%global goipathsex0     github.com/containerd/stargz-snapshotter/estargz
%endif

%global goipaths1       github.com/containerd/stargz-snapshotter/estargz


%global common_description %{expand:
Fast docker image distribution plugin for containerd, based on CRFS/stargz.}

%global golicenses      NOTICE.md LICENSE
%global godocs          docs README.md

Name:           %{goname}
Release:        3%{?dist}
Summary:        Fast docker image distribution plugin for containerd, based on CRFS/stargz

# Upstream license specification: Apache-2.0
# NOTICE.md mentions BSD-licensed code.
License:        ASL 2.0 and BSD
URL:            %{gourl}
Source0:        %{gosource}
Patch0:         0001-Adapt-to-containerd-1.5.0-beta.patch

BuildRequires:  golang(github.com/opencontainers/go-digest)
BuildRequires:  golang(github.com/pkg/errors)
BuildRequires:  golang(golang.org/x/sync/errgroup)
%if %{without bootstrap}
BuildRequires:  golang(github.com/BurntSushi/toml)
BuildRequires:  golang(github.com/containerd/console)
BuildRequires:  golang(github.com/containerd/containerd)
BuildRequires:  golang(github.com/containerd/containerd/api/services/snapshots/v1)
BuildRequires:  golang(github.com/containerd/containerd/cio)
BuildRequires:  golang(github.com/containerd/containerd/cmd/ctr/app)
BuildRequires:  golang(github.com/containerd/containerd/cmd/ctr/commands)
BuildRequires:  golang(github.com/containerd/containerd/cmd/ctr/commands/content)
BuildRequires:  golang(github.com/containerd/containerd/cmd/ctr/commands/tasks)
BuildRequires:  golang(github.com/containerd/containerd/containers)
BuildRequires:  golang(github.com/containerd/containerd/content)
BuildRequires:  golang(github.com/containerd/containerd/content/local)
BuildRequires:  golang(github.com/containerd/containerd/contrib/snapshotservice)
BuildRequires:  golang(github.com/containerd/containerd/errdefs)
BuildRequires:  golang(github.com/containerd/containerd/images)
BuildRequires:  golang(github.com/containerd/containerd/images/archive)
BuildRequires:  golang(github.com/containerd/containerd/images/converter)
BuildRequires:  golang(github.com/containerd/containerd/images/converter/uncompress)
BuildRequires:  golang(github.com/containerd/containerd/labels)
BuildRequires:  golang(github.com/containerd/containerd/log)
BuildRequires:  golang(github.com/containerd/containerd/mount)
BuildRequires:  golang(github.com/containerd/containerd/oci)
BuildRequires:  golang(github.com/containerd/containerd/pkg/netns)
BuildRequires:  golang(github.com/containerd/containerd/pkg/seed)
BuildRequires:  golang(github.com/containerd/containerd/platforms)
BuildRequires:  golang(github.com/containerd/containerd/reference)
BuildRequires:  golang(github.com/containerd/containerd/remotes/docker)
BuildRequires:  golang(github.com/containerd/containerd/snapshots)
BuildRequires:  golang(github.com/containerd/containerd/snapshots/storage)
BuildRequires:  golang(github.com/containerd/continuity/fs)
BuildRequires:  golang(github.com/containerd/go-cni)
BuildRequires:  golang(github.com/docker/cli/cli/config)
BuildRequires:  golang(github.com/docker/cli/cli/config/configfile)
BuildRequires:  golang(github.com/golang/groupcache/lru)
BuildRequires:  golang(github.com/hanwen/go-fuse/v2/fs)
BuildRequires:  golang(github.com/hanwen/go-fuse/v2/fuse)
BuildRequires:  golang(github.com/hashicorp/go-multierror)
BuildRequires:  golang(github.com/moby/sys/mountinfo)
BuildRequires:  golang(github.com/opencontainers/image-spec/identity)
BuildRequires:  golang(github.com/opencontainers/image-spec/specs-go/v1)
BuildRequires:  golang(github.com/opencontainers/runtime-spec/specs-go)
BuildRequires:  golang(github.com/rs/xid)
BuildRequires:  golang(github.com/sirupsen/logrus)
BuildRequires:  golang(github.com/urfave/cli)
BuildRequires:  golang(golang.org/x/sync/semaphore)
BuildRequires:  golang(golang.org/x/sync/singleflight)
BuildRequires:  golang(golang.org/x/sys/unix)
BuildRequires:  golang(google.golang.org/grpc)
BuildRequires:  golang(k8s.io/api/core/v1)
BuildRequires:  golang(k8s.io/apimachinery/pkg/apis/meta/v1)
BuildRequires:  golang(k8s.io/apimachinery/pkg/runtime)
BuildRequires:  golang(k8s.io/apimachinery/pkg/util/runtime)
BuildRequires:  golang(k8s.io/apimachinery/pkg/util/wait)
BuildRequires:  golang(k8s.io/apimachinery/pkg/watch)
BuildRequires:  golang(k8s.io/client-go/kubernetes)
BuildRequires:  golang(k8s.io/client-go/tools/cache)
BuildRequires:  golang(k8s.io/client-go/tools/clientcmd)
BuildRequires:  golang(k8s.io/client-go/util/workqueue)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/containerd/containerd/pkg/testutil)
BuildRequires:  golang(github.com/containerd/containerd/snapshots/testsuite)
%endif
%endif

%if %{without bootstrap}
%global godevelheader %{expand:
# Add dependency to devel package
Requires: golang(github.com/containerd/stargz-snapshotter/estargz)
}
%endif

%description
%{common_description}

%gopkg

%prep
%goprep
%autopatch -p1

%if %{without bootstrap}
%build
for cmd in cmd/* ; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done
%endif

%install
%gopkginstall
%if %{without bootstrap}
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
%endif

%if %{without bootstrap}
%if %{with check}
%check
%gocheck -d nativeconverter/estargz
%endif
%endif

%if %{without bootstrap}
%files
%license NOTICE.md LICENSE
%doc docs README.md
%{_bindir}/*
%endif

%gopkgfiles

%changelog
* Fri Mar 19 2021 Olivier Lemasle <o.lemasle@gmail.com> - 0.4.1-3
- Fix dependency

* Fri Mar 19 2021 Olivier Lemasle <o.lemasle@gmail.com> - 0.4.1-2
- Fix BuildRequires: add golang(github.com/containerd/stargz-snapshotter/estargz)

* Wed Mar 10 2021 Olivier Lemasle <o.lemasle@gmail.com> - 0.4.1-1
- Update to latest upstream 0.4.1

* Fri Jan 29 2021 Olivier Lemasle <o.lemasle@gmail.com> - 0.3.0-2
- Unbootstrap

* Wed Jan 27 22:19:10 CET 2021 Olivier Lemasle <o.lemasle@gmail.com> - 0.3.0-1
- Initial package (bootstrap)

